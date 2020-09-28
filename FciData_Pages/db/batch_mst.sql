CREATE TABLE `batch_mst` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `BATCH_ID` int(11) DEFAULT NULL,
  `BATCH_ID_DISPLAY` varchar(45) DEFAULT NULL,
  `BATCH_DATE` datetime DEFAULT NULL,
  `ACCPT_WT_KG` float DEFAULT NULL,
  `ACCPT_BAGS_CNT` int(11) DEFAULT NULL,
  `RECV_WT_KG` float DEFAULT NULL,
  `RECV_BAGS_CNT` int(11) DEFAULT NULL,
  `TL_RECVED` float DEFAULT NULL,
  `TL_ACCPTED` float DEFAULT NULL,
  `STORAGE_BAGS` int(11) DEFAULT NULL,
  `MATERIAL_TYPE` varchar(45) DEFAULT NULL,
  `STATUS` varchar(45) DEFAULT NULL,
  `WAGON_CNT` int(11) DEFAULT NULL,
  `REQUIRED_TRUCKS` int(11) DEFAULT NULL,
  `CONTRACTOR_NAME` varchar(145) DEFAULT NULL,
  `DEVICE_ID` varchar(45) DEFAULT NULL,
  `DEVICE_LOCATION_TYPE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
);
