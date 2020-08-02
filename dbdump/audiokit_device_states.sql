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
-- Table structure for table `device_states`
--

DROP TABLE IF EXISTS `device_states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device_states` (
  `state_id` int(11) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(145) NOT NULL,
  `state_code` varchar(45) DEFAULT NULL,
  `ZONE_NAME` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device_states`
--

LOCK TABLES `device_states` WRITE;
/*!40000 ALTER TABLE `device_states` DISABLE KEYS */;
INSERT INTO `device_states` VALUES (4,'Maharashtra',NULL,'North Region'),(5,'Delhi',NULL,'North Region'),(6,'West Bengali',NULL,'North Region'),(7,'Tamil Nadu',NULL,'North Region'),(8,'Andhra Pradesh',NULL,'North Region'),(9,'Gujarat',NULL,'North Region'),(10,'Karnataka',NULL,'North Region'),(11,'Uttar Pradesh',NULL,'North Region'),(12,'Rajasthan',NULL,'North Region'),(13,'Madhya Pradesh',NULL,'North Region'),(14,'Punjab',NULL,'North Region'),(15,'Bihar',NULL,NULL),(16,'Jammu and Kashmir',NULL,'South Region'),(17,'Haryana',NULL,'South Region'),(18,'Jharkhand',NULL,'South Region'),(19,'Assam',NULL,'South Region'),(20,'Kerala',NULL,'South Region'),(21,'Chandigarh',NULL,'South Region'),(22,'Chhatisgarh',NULL,'South Region'),(23,'Orissa',NULL,'South Region'),(24,'Uttaranchal',NULL,'South Region'),(25,'Pondicherry',NULL,'South Region'),(26,'Manipur',NULL,'South Region'),(27,'Tripura',NULL,'South Region'),(28,'Mizoram',NULL,'South Region'),(29,'Meghalaya',NULL,'South Region');
/*!40000 ALTER TABLE `device_states` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02 13:53:08
