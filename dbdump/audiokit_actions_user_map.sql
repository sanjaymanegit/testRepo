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
-- Table structure for table `actions_user_map`
--

DROP TABLE IF EXISTS `actions_user_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `actions_user_map` (
  `ACTION_USER_MAP_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` varchar(45) DEFAULT NULL,
  `USER_LOGIN_ID` varchar(45) DEFAULT NULL,
  `ACTION_KEY` varchar(45) DEFAULT NULL,
  `CREATED_BY` varchar(45) DEFAULT NULL,
  `CREATED_ON` datetime DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_BY` varchar(45) DEFAULT NULL,
  `UPDATED_ON` datetime DEFAULT NULL,
  `STATUS` varchar(45) DEFAULT 'enabled',
  PRIMARY KEY (`ACTION_USER_MAP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actions_user_map`
--

LOCK TABLES `actions_user_map` WRITE;
/*!40000 ALTER TABLE `actions_user_map` DISABLE KEYS */;
INSERT INTO `actions_user_map` VALUES (1,'1','SM1610','ADMIN',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(2,'22','VK_SINGH','ADMIN',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(3,'23','SURESH_12345','ADMIN',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(4,'24','ADMIN','ADMIN',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(5,'1','SM1610','BULK_UPLOAD',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(6,'22','VK_SINGH','BULK_UPLOAD',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(7,'23','SURESH_12345','BULK_UPLOAD',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(8,'24','ADMIN','BULK_UPLOAD',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(9,'1','SM1610','CHANGE_PASSWORD',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(10,'22','VK_SINGH','CHANGE_PASSWORD',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(11,'23','SURESH_12345','CHANGE_PASSWORD',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(12,'24','ADMIN','CHANGE_PASSWORD',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(13,'1','SM1610','MONITOR',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(14,'22','VK_SINGH','MONITOR',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(15,'23','SURESH_12345','MONITOR',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(16,'24','ADMIN','MONITOR',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(17,'1','SM1610','ONLINE_OFFLINE_LIST',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(18,'22','VK_SINGH','ONLINE_OFFLINE_LIST',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(19,'23','SURESH_12345','ONLINE_OFFLINE_LIST',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(20,'24','ADMIN','ONLINE_OFFLINE_LIST',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(21,'1','SM1610','REPORTS',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(22,'22','VK_SINGH','REPORTS',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(23,'23','SURESH_12345','REPORTS',NULL,'2019-06-24 13:21:12',NULL,NULL,'disabled'),(24,'24','ADMIN','REPORTS',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(25,'1','SM1610','SETUP_DEVICE',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(26,'22','VK_SINGH','SETUP_DEVICE',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(27,'23','SURESH_12345','SETUP_DEVICE',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled'),(28,'24','ADMIN','SETUP_DEVICE',NULL,'2019-06-24 13:21:12',NULL,NULL,'enabled');
/*!40000 ALTER TABLE `actions_user_map` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02 13:53:03
