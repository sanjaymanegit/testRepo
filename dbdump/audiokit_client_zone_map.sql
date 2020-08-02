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
-- Table structure for table `client_zone_map`
--

DROP TABLE IF EXISTS `client_zone_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `client_zone_map` (
  `client_zone_map_id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `zone_id` int(11) NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_by` varchar(45) DEFAULT 'SYS',
  PRIMARY KEY (`client_zone_map_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_zone_map`
--

LOCK TABLES `client_zone_map` WRITE;
/*!40000 ALTER TABLE `client_zone_map` DISABLE KEYS */;
INSERT INTO `client_zone_map` VALUES (1,1,1,'2018-12-02 22:46:39','SYS'),(2,1,2,'2018-12-02 22:46:39','SYS'),(3,1,3,'2018-12-02 22:46:39','SYS'),(4,1,4,'2018-12-02 22:46:39','SYS'),(5,2,1,'2018-12-02 22:46:39','SYS'),(6,2,2,'2018-12-02 22:46:39','SYS'),(7,2,3,'2018-12-02 22:46:39','SYS'),(8,2,4,'2018-12-02 22:46:39','SYS'),(9,3,1,'2018-12-02 22:46:39','SYS'),(10,3,2,'2018-12-02 22:46:39','SYS'),(11,3,3,'2018-12-02 22:46:39','SYS'),(12,3,4,'2018-12-02 22:46:39','SYS'),(13,4,1,'2018-12-02 22:46:39','SYS'),(14,4,2,'2018-12-02 22:46:39','SYS'),(15,4,3,'2018-12-02 22:46:39','SYS'),(16,4,4,'2018-12-02 22:46:39','SYS');
/*!40000 ALTER TABLE `client_zone_map` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02 13:52:56
