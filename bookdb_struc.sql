CREATE DATABASE  IF NOT EXISTS `bookdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bookdb`;

CREATE TABLE `books` (
  `bid` varchar(20) NOT NULL,
  `title` varchar(30) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`bid`)
)

CREATE TABLE `books_issued` (
  `bid` varchar(20) NOT NULL,
  `issuedto` varchar(30) DEFAULT NULL,
  `expiry` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bid`)
)

CREATE TABLE `event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `notice` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
)