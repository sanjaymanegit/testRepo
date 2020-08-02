-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: audiokit
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `action_mst`
--

DROP TABLE IF EXISTS `action_mst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `action_mst` (
  `action_id` int(11) NOT NULL AUTO_INCREMENT,
  `action_key` varchar(45) DEFAULT NULL,
  `action_name` varchar(45) DEFAULT NULL,
  `action_desc` varchar(445) DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_by` varchar(45) DEFAULT NULL,
  `updated_on` datetime DEFAULT NULL,
  PRIMARY KEY (`action_id`),
  UNIQUE KEY `action_key_UNIQUE` (`action_key`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action_mst`
--

LOCK TABLES `action_mst` WRITE;
/*!40000 ALTER TABLE `action_mst` DISABLE KEYS */;
INSERT INTO `action_mst` VALUES (1,'ONLINE_OFFLINE_LIST','online offline list','online offline list',NULL,'2019-05-14 12:28:11',NULL,'2019-05-14 12:28:11'),(2,'SETUP_DEVICE','Setup Device','delelete device data',NULL,'2019-05-14 12:30:40',NULL,NULL),(3,'ADMIN','Admin','admin tasks ',NULL,'2019-05-14 12:30:40',NULL,NULL),(4,'REPORTS','Reports details','Reports details',NULL,'2019-05-14 12:30:40',NULL,NULL),(5,'BULK_UPLOAD','Bulk Data Upload (xls)','Bulk Data Upload (xls)',NULL,'2019-05-14 12:30:40',NULL,NULL),(6,'MONITOR','Monitor Data','Monitor Data',NULL,'2019-05-14 12:30:40',NULL,NULL),(7,'CHANGE_PASSWORD','Change My Password','Here change your password.',NULL,'2019-05-15 12:18:41',NULL,NULL);
/*!40000 ALTER TABLE `action_mst` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02 13:52:54
