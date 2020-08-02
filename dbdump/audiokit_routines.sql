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

-- Dump completed on 2020-08-02 13:53:09
