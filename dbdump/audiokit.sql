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
) ENGINE=InnoDB AUTO_INCREMENT=8 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=29 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `business_users`
--

DROP TABLE IF EXISTS `business_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `business_users` (
  `USER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` varchar(145) DEFAULT NULL,
  `LAST_NAME` varchar(145) DEFAULT NULL,
  `USER_LOGIN_ID` varchar(45) DEFAULT NULL,
  `USER_PWD` varchar(45) DEFAULT NULL,
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `CREATED_BY` varchar(45) NOT NULL DEFAULT 'SYS',
  `ACTIVE` varchar(1) NOT NULL DEFAULT 'Y',
  `ROLE_NAME` varchar(45) DEFAULT 'OPERATOR',
  `EMAIL_ID` varchar(45) DEFAULT NULL,
  `UPDATED_BY` varchar(45) DEFAULT NULL,
  `UPDATED_ON` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `client_dtls`
--

DROP TABLE IF EXISTS `client_dtls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `client_dtls` (
  `client_id` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(150) DEFAULT NULL,
  `is_active` varchar(1) NOT NULL DEFAULT 'Y',
  `client_desc` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=17 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `client_zons_vw`
--

DROP TABLE IF EXISTS `client_zons_vw`;
/*!50001 DROP VIEW IF EXISTS `client_zons_vw`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `client_zons_vw` AS SELECT 
 1 AS `client_zone_map_id`,
 1 AS `client_id`,
 1 AS `client_name`,
 1 AS `zone_id`,
 1 AS `zone_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `device_city`
--

DROP TABLE IF EXISTS `device_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device_city` (
  `city_id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(145) NOT NULL,
  `city_code` varchar(45) DEFAULT NULL,
  `city_pin` varchar(45) DEFAULT NULL,
  `State_name` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB AUTO_INCREMENT=342 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `device_dtls`
--

DROP TABLE IF EXISTS `device_dtls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device_dtls` (
  `DEV_ID` varchar(50) NOT NULL,
  `ADDRESS` varchar(500) DEFAULT NULL,
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `CREATED_BY` varchar(45) DEFAULT 'SYS',
  `IN_PHONE_NO_1` varchar(50) DEFAULT NULL,
  `STATE_ID` int(11) NOT NULL DEFAULT '1',
  `PANEL_ID` varchar(45) DEFAULT NULL,
  `CLIENT_ID` int(11) DEFAULT NULL,
  `IN_PHONE_NO_2` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_3` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_4` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_5` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_6` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_7` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_8` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_9` varchar(45) DEFAULT NULL,
  `IN_PHONE_NO_10` varchar(45) DEFAULT NULL,
  `CITY_ID` int(11) DEFAULT NULL,
  `ZONE_REGION_ID` int(11) DEFAULT NULL,
  `ui_update_status` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=35 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `device_status`
--

DROP TABLE IF EXISTS `device_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device_status` (
  `STATUS_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DEV_ID` varchar(50) NOT NULL,
  `CREATED_DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `STATUS` varchar(45) DEFAULT 'ACTIVE',
  PRIMARY KEY (`STATUS_ID`),
  KEY `FK_DEV_ID_idx` (`DEV_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=382445 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `device_status_list`
--

DROP TABLE IF EXISTS `device_status_list`;
/*!50001 DROP VIEW IF EXISTS `device_status_list`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `device_status_list` AS SELECT 
 1 AS `DEV_ID`,
 1 AS `CLIENT_NAME`,
 1 AS `CLIENT_ID`,
 1 AS `ZONE`,
 1 AS `STATE`,
 1 AS `CITY`,
 1 AS `ADDRESS`,
 1 AS `STATUS`,
 1 AS `STATUS_ACTUAL`,
 1 AS `L_DATE`,
 1 AS `PANEL_ID`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `device_zones_regions`
--

DROP TABLE IF EXISTS `device_zones_regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `device_zones_regions` (
  `zone_id` int(11) NOT NULL AUTO_INCREMENT,
  `zone_name` varchar(145) NOT NULL,
  `crerated_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `zone_txt` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`zone_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `role_actions_map`
--

DROP TABLE IF EXISTS `role_actions_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `role_actions_map` (
  `ROLE_ACTION_MAP_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ROLE_ID` varchar(45) DEFAULT NULL,
  `ROLE_NAME` varchar(45) DEFAULT NULL,
  `ACTION_KEY` varchar(45) DEFAULT NULL,
  `CREATED_BY` varchar(45) DEFAULT NULL,
  `CREATED_ON` datetime DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_BY` varchar(45) DEFAULT NULL,
  `UPDATED_ON` datetime DEFAULT NULL,
  `STATUS` varchar(45) DEFAULT 'enabled',
  PRIMARY KEY (`ROLE_ACTION_MAP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `role_mst`
--

DROP TABLE IF EXISTS `role_mst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `role_mst` (
  `ROLE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ROLE_NAME` varchar(145) DEFAULT NULL,
  `CREATED_BY` varchar(45) DEFAULT NULL,
  `CREATE_ON` varchar(45) DEFAULT 'now()',
  `UPDATED_BY` varchar(45) DEFAULT NULL,
  `UPDATED_ON` datetime DEFAULT NULL,
  `COMMENT` varchar(145) DEFAULT NULL,
  PRIMARY KEY (`ROLE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 ; 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `vw_ref_phones`
--

DROP TABLE IF EXISTS `vw_ref_phones`;
/*!50001 DROP VIEW IF EXISTS `vw_ref_phones`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8mb4;
/*!50001 CREATE VIEW `vw_ref_phones` AS SELECT 
 1 AS `IN_PHONE_NO`,
 1 AS `CLIENT_NAME`,
 1 AS `CLIENT_ID`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping routines for database 'audiokit'
--
/*!50003 DROP FUNCTION IF EXISTS `get_access` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `get_access`(`user_login_id` varchar(45), `action_key` varchar(45)) RETURNS varchar(15) CHARSET utf8mb4
    DETERMINISTIC
BEGIN
 DECLARE `re_val` VARCHAR(10) default "disabled";

 
 SELECT status into `re_val` FROM ROLE_ACTIONS_MAP WHERE ROLE_NAME = (SELECT ROLE_NAME FROM BUSINESS_USERS WHERE USER_LOGIN_ID =user_login_id)
and ACTION_KEY=action_key; 
 
RETURN (re_val);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `client_zons_vw`
--

/*!50001 DROP VIEW IF EXISTS `client_zons_vw`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `client_zons_vw` AS select `a`.`client_zone_map_id` AS `client_zone_map_id`,`a`.`client_id` AS `client_id`,`b`.`client_name` AS `client_name`,`a`.`zone_id` AS `zone_id`,`c`.`zone_name` AS `zone_name` from ((`client_zone_map` `a` left join `client_dtls` `b` on((`a`.`client_id` = `b`.`client_id`))) left join `device_zones_regions` `c` on((`a`.`zone_id` = `c`.`zone_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `device_status_list`
--

/*!50001 DROP VIEW IF EXISTS `device_status_list`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `device_status_list` AS select `a`.`DEV_ID` AS `DEV_ID`,`f`.`client_name` AS `CLIENT_NAME`,`f`.`client_id` AS `CLIENT_ID`,`c`.`zone_name` AS `ZONE`,`d`.`state_name` AS `STATE`,`e`.`city_name` AS `CITY`,`b`.`ADDRESS` AS `ADDRESS`,(case when (timestampdiff(HOUR,`a`.`cr_date`,now()) > 4) then '<font color="red">Offline</font>' else '<font color="blue">Online</font>' end) AS `STATUS`,(case when (timestampdiff(HOUR,`a`.`cr_date`,now()) > 4) then 'Offline' else 'Online' end) AS `STATUS_ACTUAL`,`a`.`cr_date` AS `L_DATE`,`b`.`PANEL_ID` AS `PANEL_ID` from ((((((select `device_status`.`DEV_ID` AS `DEV_ID`,max(`device_status`.`CREATED_DATE`) AS `cr_date` from `device_status` group by `device_status`.`DEV_ID` order by `device_status`.`CREATED_DATE` desc) `a` left join `device_dtls` `b` on((trim(`a`.`DEV_ID`) = trim(`b`.`DEV_ID`)))) left join `device_zones_regions` `c` on((`b`.`ZONE_REGION_ID` = `c`.`zone_id`))) left join `device_states` `d` on((`b`.`STATE_ID` = `d`.`state_id`))) left join `device_city` `e` on((`b`.`CITY_ID` = `e`.`city_id`))) left join `client_dtls` `f` on((`b`.`CLIENT_ID` = `f`.`client_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_ref_phones`
--

/*!50001 DROP VIEW IF EXISTS `vw_ref_phones`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_ref_phones` AS select distinct `a`.`IN_PHONE_NO_1` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_1` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_2` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_2` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_3` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_3` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_4` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_4` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_5` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_5` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_6` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_6` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_7` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_7` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_8` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_8` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_9` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_9` <> 'null')) union all select distinct `a`.`IN_PHONE_NO_10` AS `IN_PHONE_NO`,`b`.`client_name` AS `CLIENT_NAME`,`b`.`client_id` AS `CLIENT_ID` from (`device_dtls` `a` join `client_dtls` `b`) where ((`a`.`CLIENT_ID` = `b`.`client_id`) and (`a`.`IN_PHONE_NO_10` <> 'null')) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02 14:50:56
