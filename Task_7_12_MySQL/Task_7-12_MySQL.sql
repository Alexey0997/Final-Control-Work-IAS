/*
7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”
*/

DROP DATABASE IF EXISTS Human_friends;
CREATE DATABASE Human_friends;
USE Human_friends;
ALTER DATABASE Human_friends CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

/*
8. Создать таблицы с иерархией из диаграммы в БД.
9. Заполнить низкоуровневые таблицы именами животных, командами, которые они выполняют, и датами рождения.
*/

-- Создадим таблицу Animals (Животные), которая будет включать в себя диких и домашних животных.
DROP TABLE IF EXISTS Animals;
CREATE TABLE Animals (
	id_type INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   	type_animals VARCHAR(50)
);

INSERT INTO Animals(id_type, type_animals) VALUES 
('1', 'Pets'), 
('2', 'PackAnimals');

-- Создадим таблицу Cats (Кошки) и заполним сведения о двух питомцах.
DROP TABLE IF EXISTS Cats;
CREATE TABLE Cats (
	id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT UNSIGNED NOT NULL,
   	name VARCHAR(50),
   	command TEXT,
   	birth_date DATE,
   	FOREIGN KEY (type_id) REFERENCES Animals(id_type)
);

INSERT INTO Cats (id_animal, type_id, name, command, birth_date) VALUES
('1', '1','Кузьма', 'кушать, спать', '2010-06-13'),
('2', '1', 'Сельверадо', 'гулять, голос', '2008-12-02');

-- Создадим таблицу Dogs (Собаки) и заполним сведения о двух питомцах.
DROP TABLE IF EXISTS Dogs;
CREATE TABLE Dogs (
	id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT UNSIGNED NOT NULL,
   	name VARCHAR(50),
   	command TEXT,
   	birth_date DATE,
   	FOREIGN KEY (type_id) REFERENCES Animals(id_type)
);

INSERT INTO Dogs (id_animal, type_id, name, command, birth_date) VALUES
('1', '1','Рекс', 'охранять, голос, фас', '2020-01-01'),
('2', '1', 'Шарик', 'сидеть, лежать, рядом', '2022-12-12');

-- Создадим таблицу Hamsters (Хомячки) и заполним сведения о двух питомцах.
DROP TABLE IF EXISTS Hamsters;
CREATE TABLE Hamsters (
	id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT UNSIGNED NOT NULL,
   	name VARCHAR(50),
   	command TEXT,
   	birth_date DATE,
   	FOREIGN KEY (type_id) REFERENCES Animals(id_type)
);

INSERT INTO Hamsters (id_animal, type_id, name, command, birth_date) VALUES
('1', '1', 'Начфин', 'хенде хох', '2023-02-02'),
('2', '1', 'Начпрод', 'спать, есть', '2023-03-03');

-- Создадим таблицу Horses (Лошади) и заполним сведения о двух животных.
DROP TABLE IF EXISTS Horses;
CREATE TABLE Horses (
	id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT UNSIGNED NOT NULL,
   	name VARCHAR(50),
   	command TEXT,
   	birth_date DATE,
   	FOREIGN KEY (type_id) REFERENCES Animals(id_type)
);

INSERT INTO Horses (id_animal, type_id, name, command, birth_date) VALUES
('1', '2','Сивка', 'шаг, рысь, галоп, карьер', '2019-09-09'),
('2', '2','Бурка', 'стоять, лечь, сесть, тихо, ко мне', '2020-11-11');


-- Создадим таблицу Camels (Верблюды) и заполним сведения о двух животных.
DROP TABLE IF EXISTS Camels;
CREATE TABLE Camels (
	id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT UNSIGNED NOT NULL,
   	name VARCHAR(50),
   	command TEXT,
   	birth_date DATE,
   	FOREIGN KEY (type_id) REFERENCES Animals(id_type)
);

INSERT INTO Camels (id_animal, type_id, name, command, birth_date) VALUES
('1', '2','Камиль', 'стоять, лечь, вперед', '2017-10-01'),
('2', '2','Рамиль', 'стоять, лечь, вперед', '2022-11-11');

-- Создадим таблицу Donkeys (Ослы) и заполним сведения о двух животных.
DROP TABLE IF EXISTS Donkeys;
CREATE TABLE Donkeys (
	id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	type_id INT UNSIGNED NOT NULL,
   	name VARCHAR(50),
   	command TEXT,
   	birth_date DATE,
   	FOREIGN KEY (type_id) REFERENCES Animals(id_type)
);

INSERT INTO Donkeys (id_animal, type_id, name, command, birth_date) VALUES
('1', '2','Боря', 'стоять, лечь, вперед', '2023-02-02'),
('2', '2','Миша', 'стоять, лечь, вперед', '2022-01-03');

/*
10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. 
Объединить таблицы лошади, и ослы в одну таблицу.
*/
-- Отключим режим безопасного обновления MySQL и удалим все данные из таблицы Camels (Верблюды).
SET SQL_SAFE_UPDATES = 0;
DELETE FROM Camels; 

-- Объедененим таблицы лошадей и ослов в одну таблицу
SELECT id_animal, 'Horse' AS kind_animals, type_id, name, command, birth_date
FROM Horses
UNION ALL
SELECT id_animal, 'Donkey' AS kind_animals, type_id, name, command, birth_date
FROM Donkeys;

/*
12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.

11.Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года, 
но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице.
*/

-- Создадим таблицу  AllAnimals (Все животные), в которую объединим все таблицы. 
DROP VIEW IF EXISTS AllAnimals;
CREATE VIEW AllAnimals AS SELECT id_type, type_animals, kind_animals, id_animal, name, command, birth_date 
FROM (
	SELECT ta.id_type, ta.type_animals, 'cat' AS kind_animals, c.id_animal, c.name, c.command, c.birth_date
	FROM Animals ta
	JOIN cats c ON ta.id_type = c.type_id
	
	UNION ALL
	
	SELECT ta.id_type, ta.type_animals,'dog' AS kind_animals, d.id_animal, d.name, d.command, d.birth_date 
	FROM Animals ta
	JOIN dogs d ON ta.id_type = d.type_id
	
	UNION ALL
	SELECT ta.id_type, ta.type_animals,'hamster' AS kind_animals, h.id_animal, h.name, command, h.birth_date 
	FROM Animals ta
	JOIN hamsters h ON ta.id_type = h.type_id
	
	UNION ALL
	
	SELECT ta.id_type, ta.type_animals,'horse' AS kind_animals, hor.id_animal, hor.name, hor.command, hor.birth_date 
	FROM Animals ta
	JOIN horses hor ON ta.id_type = hor.type_id
	
	UNION ALL
	
	SELECT ta.id_type, ta.type_animals,'верблюд' AS kind_animals, cam.id_animal, cam.name, cam.command, cam.birth_date 
	FROM Animals ta
	JOIN camels cam ON ta.id_type = cam.type_id
	
	UNION ALL
	
	SELECT ta.id_type, ta.type_animals, 'donkey' AS kind_animals, don.id_animal, don.name, don.command, don.birth_date 
	FROM Animals ta
	JOIN donkeys don ON ta.id_type = don.type_id
) all_animals;

SELECT * FROM AllAnimals;


DROP VIEW IF EXISTS pets;
CREATE VIEW pets AS (
SELECT 
	id_type, type_animals, kind_animals, 
	id_animal, name, command, birth_date  
FROM AllAnimals
WHERE id_type = 1
);

DROP VIEW IF EXISTS pack_animals;
CREATE VIEW pack_animals AS (
SELECT 
	id_type, type_animals, kind_animals, 
	id_animal, name, command, birth_date  
FROM AllAnimals
WHERE id_type = 2
);

-- Создадим таблицу Young_animals (Молодые животные), в которую поместим животных старше года, но младше трех.
DROP VIEW IF EXISTS Young_animals;
CREATE VIEW Young_animals AS (
SELECT 
	id_type, type_animals, kind_animals, 
	id_animal, name, command, birth_date, 
	TIMESTAMPDIFF(MONTH, birth_date, NOW()) AS age  
FROM AllAnimals
WHERE TIMESTAMPDIFF(MONTH, birth_date, NOW()) > 12 AND TIMESTAMPDIFF(MONTH, birth_date, NOW()) < 37
);

SELECT * FROM Young_animals;