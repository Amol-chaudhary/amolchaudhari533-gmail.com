-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.19


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema demo
--

CREATE DATABASE IF NOT EXISTS demo;
USE demo;

--
-- Definition of table `account_login`
--

DROP TABLE IF EXISTS `account_login`;
CREATE TABLE `account_login` (
  `acc` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Account_number` int(10) unsigned NOT NULL,
  `Age` int(10) unsigned NOT NULL,
  `Adhar Number` int(10) unsigned NOT NULL,
  `Account type` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `Balance` int(10) unsigned NOT NULL,
  PRIMARY KEY (`acc`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account_login`
--

/*!40000 ALTER TABLE `account_login` DISABLE KEYS */;
INSERT INTO `account_login` (`acc`,`Account_number`,`Age`,`Adhar Number`,`Account type`,`mobile`,`address`,`Email`,`password`,`name`,`Balance`) VALUES 
 (1,123,12,1234,'saving','12345','dewhwcf','abc@gmail.com','123','amol chaudhari',0),
 (2,123,12,123,'saving','123','shgqs','a@gmail.com','123','amol',0),
 (3,234,67,3456,'custome','23531','a@gmail.com','a@efg','234','ajat',1100),
 (4,345,23,567,'saving','787965','djahvsfkj gbjkgb','a@gma','345','ajay',1200);
/*!40000 ALTER TABLE `account_login` ENABLE KEYS */;


--
-- Definition of table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `roll number` int(10) unsigned NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`id`,`name`,`roll number`,`username`,`password`) VALUES 
 (1,'amol',12,'amol','amol'),
 (2,'amol chaudhari',34,'omkar','omkar'),
 (3,'gaurav',23,'gavrav','gavrav');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;


--
-- Definition of table `sample`
--

DROP TABLE IF EXISTS `sample`;
CREATE TABLE `sample` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `standard` varchar(45) NOT NULL,
  `division` varchar(45) NOT NULL,
  `batch` varchar(45) NOT NULL,
  `marks` int(123) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sample`
--

/*!40000 ALTER TABLE `sample` DISABLE KEYS */;
INSERT INTO `sample` (`id`,`name`,`standard`,`division`,`batch`,`marks`) VALUES 
 (1,'amol','TE','A','A1',17),
 (2,'ajay','BE','B','b4',45),
 (3,'onkar','TE','A','A1',45),
 (4,'omkar','BE','B','B6',78);
/*!40000 ALTER TABLE `sample` ENABLE KEYS */;


--
-- Definition of table `transcation`
--

DROP TABLE IF EXISTS `transcation`;
CREATE TABLE `transcation` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `frome` varchar(45) NOT NULL,
  `to` varchar(45) NOT NULL,
  `amount` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transcation`
--

/*!40000 ALTER TABLE `transcation` DISABLE KEYS */;
INSERT INTO `transcation` (`id`,`frome`,`to`,`amount`) VALUES 
 (1,'3','345',200),
 (2,'3','345',200),
 (3,'345','3',200),
 (4,'234','345',200),
 (5,'345','234',200);
/*!40000 ALTER TABLE `transcation` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
