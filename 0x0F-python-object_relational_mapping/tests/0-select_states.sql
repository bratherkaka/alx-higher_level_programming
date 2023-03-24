DROP DATABASE IF EXISTS test_2;
CREATE DATABASE IF NOT EXISTS test_2;
USE test_2;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
) COLLATE = utf8_bin;
INSERT INTO states (name) VALUES ("California"), ("nevada"), ("Nevada"), ("neVAda"), ("New York");
