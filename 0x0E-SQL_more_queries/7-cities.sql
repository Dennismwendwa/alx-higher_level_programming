-- create database hbtn_0d_use and table cities with relationship to table states
CREATE DATABASE IF NOT EXISTS hbtn_9d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
	UNIQUE, state_id INT NOT NULL, FOREIGN KEY(state_id)
	REFERENCES states(id), name VARCHAR(256) NOT NULL);
