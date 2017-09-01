-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: aron
-- ------------------------------------------------------
-- Server version	5.6.28-0ubuntu0.15.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Configurazione_exportconfig`
--

DROP TABLE IF EXISTS `Configurazione_exportconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Configurazione_exportconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Configurazione_exportconfig`
--

LOCK TABLES `Configurazione_exportconfig` WRITE;
/*!40000 ALTER TABLE `Configurazione_exportconfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `Configurazione_exportconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Configurazione_importconfig`
--

DROP TABLE IF EXISTS `Configurazione_importconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Configurazione_importconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filename` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Configurazione_importconfig`
--

LOCK TABLES `Configurazione_importconfig` WRITE;
/*!40000 ALTER TABLE `Configurazione_importconfig` DISABLE KEYS */;
/*!40000 ALTER TABLE `Configurazione_importconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DashBoard_dashboard`
--

DROP TABLE IF EXISTS `DashBoard_dashboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DashBoard_dashboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wan_image` varchar(16) NOT NULL,
  `lan1_image` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DashBoard_dashboard`
--

LOCK TABLES `DashBoard_dashboard` WRITE;
/*!40000 ALTER TABLE `DashBoard_dashboard` DISABLE KEYS */;
INSERT INTO `DashBoard_dashboard` VALUES ('1', 'CHANGE_ETH0', 'CHANGE_ETH1');
/*!40000 ALTER TABLE `DashBoard_dashboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DashBoard_top`
--

DROP TABLE IF EXISTS `DashBoard_top`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DashBoard_top` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `top` char(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DashBoard_top`
--

LOCK TABLES `DashBoard_top` WRITE;
/*!40000 ALTER TABLE `DashBoard_top` DISABLE KEYS */;
/*!40000 ALTER TABLE `DashBoard_top` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `License_license`
--

DROP TABLE IF EXISTS `License_license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `License_license` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client` varchar(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  `province` varchar(64) NOT NULL,
  `req` varchar(128) NOT NULL,
  `lic` varchar(128) NOT NULL,
  `exp_lic` varchar(128) NOT NULL,
  `qty_dev` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `License_license`
--

LOCK TABLES `License_license` WRITE;
/*!40000 ALTER TABLE `License_license` DISABLE KEYS */;
/*!40000 ALTER TABLE `License_license` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_apply`
--

DROP TABLE IF EXISTS `Network_apply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_apply` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_import` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_apply`
--

LOCK TABLES `Network_apply` WRITE;
/*!40000 ALTER TABLE `Network_apply` DISABLE KEYS */;
/*!40000 ALTER TABLE `Network_apply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_choices`
--

DROP TABLE IF EXISTS `Network_choices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_choices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_choices`
--

LOCK TABLES `Network_choices` WRITE;
/*!40000 ALTER TABLE `Network_choices` DISABLE KEYS */;
/*!40000 ALTER TABLE `Network_choices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_dhcptable`
--

DROP TABLE IF EXISTS `Network_dhcptable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_dhcptable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `mac` varchar(17) NOT NULL,
  `ip` char(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `mac` (`mac`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_dhcptable`
--

LOCK TABLES `Network_dhcptable` WRITE;
/*!40000 ALTER TABLE `Network_dhcptable` DISABLE KEYS */;
/*!40000 ALTER TABLE `Network_dhcptable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_lan`
--

DROP TABLE IF EXISTS `Network_lan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_lan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eth_ip_lan` varchar(16) NOT NULL,
  `ip_lan` char(39) NOT NULL,
  `mask_lan` varchar(17) NOT NULL,
  `dhcp` tinyint(1) NOT NULL,
  `ip_start` char(39) NOT NULL,
  `ip_end` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `eth_ip_lan` (`eth_ip_lan`),
  UNIQUE KEY `ip_lan` (`ip_lan`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_lan`
--

LOCK TABLES `Network_lan` WRITE;
/*!40000 ALTER TABLE `Network_lan` DISABLE KEYS */;
INSERT INTO `Network_lan` VALUES (1,'CHANGE_ETH1','192.168.50.1','255.255.255.0',1,'192.168.50.2','192.168.50.254');
/*!40000 ALTER TABLE `Network_lan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_mac`
--

DROP TABLE IF EXISTS `Network_mac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_mac` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mac` varchar(17) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mac` (`mac`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_mac`
--

LOCK TABLES `Network_mac` WRITE;
/*!40000 ALTER TABLE `Network_mac` DISABLE KEYS */;
/*!40000 ALTER TABLE `Network_mac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_management`
--

DROP TABLE IF EXISTS `Network_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_management` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mac` varchar(17) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mac` (`mac`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_management`
--

LOCK TABLES `Network_management` WRITE;
/*!40000 ALTER TABLE `Network_management` DISABLE KEYS */;
INSERT INTO `Network_management` VALUES (1,'CHANGEMAC');
/*!40000 ALTER TABLE `Network_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_wan`
--

DROP TABLE IF EXISTS `Network_wan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_wan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eth_ip_wan` varchar(16) NOT NULL,
  `ip_wan` char(39) NOT NULL,
  `mask_wan` varchar(17) NOT NULL,
  `gateway` char(39) NOT NULL,
  `dns1` char(39) NOT NULL,
  `dns2` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `eth_ip_wan` (`eth_ip_wan`),
  UNIQUE KEY `ip_wan` (`ip_wan`),
  UNIQUE KEY `mask_wan` (`mask_wan`),
  UNIQUE KEY `gateway` (`gateway`),
  UNIQUE KEY `dns1` (`dns1`),
  UNIQUE KEY `dns2` (`dns2`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_wan`
--

LOCK TABLES `Network_wan` WRITE;
/*!40000 ALTER TABLE `Network_wan` DISABLE KEYS */;
INSERT INTO `Network_wan` VALUES (1,'CHANGE_ETH0','0.0.0.0','0.0.0.0','0.0.0.0','8.8.8.8','8.8.4.4');
/*!40000 ALTER TABLE `Network_wan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_blacklist`
--

DROP TABLE IF EXISTS `Proxy_blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_blacklist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_blacklist`
--

LOCK TABLES `Proxy_blacklist` WRITE;
/*!40000 ALTER TABLE `Proxy_blacklist` DISABLE KEYS */;
/*!40000 ALTER TABLE `Proxy_blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_classi`
--

DROP TABLE IF EXISTS `Proxy_classi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_classi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classi` varchar(20) NOT NULL,
  `internet` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `classi` (`classi`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_classi`
--

LOCK TABLES `Proxy_classi` WRITE;
/*!40000 ALTER TABLE `Proxy_classi` DISABLE KEYS */;
INSERT INTO `Proxy_classi` VALUES (1,'LAN',0);
/*!40000 ALTER TABLE `Proxy_classi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_https`
--

DROP TABLE IF EXISTS `Proxy_https`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_https` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `https` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_https`
--

LOCK TABLES `Proxy_https` WRITE;
/*!40000 ALTER TABLE `Proxy_https` DISABLE KEYS */;
INSERT INTO `Proxy_https` VALUES (1,0);
/*!40000 ALTER TABLE `Proxy_https` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_mac`
--

DROP TABLE IF EXISTS `Proxy_mac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_mac` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classi_id` int(11) NOT NULL,
  `name` varchar(64) DEFAULT NULL,
  `mac` varchar(17) NOT NULL,
  `internet` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mac` (`mac`),
  KEY `Proxy_mac_33b99cda` (`classi_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_mac`
--

LOCK TABLES `Proxy_mac` WRITE;
/*!40000 ALTER TABLE `Proxy_mac` DISABLE KEYS */;
/*!40000 ALTER TABLE `Proxy_mac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_newdevices`
--

DROP TABLE IF EXISTS `Proxy_newdevices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_newdevices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_import` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_newdevices`
--

LOCK TABLES `Proxy_newdevices` WRITE;
/*!40000 ALTER TABLE `Proxy_newdevices` DISABLE KEYS */;
/*!40000 ALTER TABLE `Proxy_newdevices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_professori`
--

DROP TABLE IF EXISTS `Proxy_professori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_professori` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `professori_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Proxy_professori_8a5ea53a` (`professori_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_professori`
--

LOCK TABLES `Proxy_professori` WRITE;
/*!40000 ALTER TABLE `Proxy_professori` DISABLE KEYS */;
/*!40000 ALTER TABLE `Proxy_professori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Proxy_professori_classi`
--

DROP TABLE IF EXISTS `Proxy_professori_classi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Proxy_professori_classi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `professori_id` int(11) NOT NULL,
  `classi_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `professori_id` (`professori_id`,`classi_id`),
  KEY `Proxy_professori_classi_8a5ea53a` (`professori_id`),
  KEY `Proxy_professori_classi_33b99cda` (`classi_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Proxy_professori_classi`
--

LOCK TABLES `Proxy_professori_classi` WRITE;
/*!40000 ALTER TABLE `Proxy_professori_classi` DISABLE KEYS */;
/*!40000 ALTER TABLE `Proxy_professori_classi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Routing_routing`
--

DROP TABLE IF EXISTS `Routing_routing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Routing_routing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mode` varchar(48) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Routing_routing`
--

LOCK TABLES `Routing_routing` WRITE;
/*!40000 ALTER TABLE `Routing_routing` DISABLE KEYS */;
INSERT INTO `Routing_routing` VALUES (1,'8idzJSIxoDH6RH0G4uuLGa5HKl7UB7q+yofylSaOkVA=');
/*!40000 ALTER TABLE `Routing_routing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aron_logs`
--

DROP TABLE IF EXISTS `aron_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aron_logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_since_epoch` datetime DEFAULT NULL,
  `time_response` int(11) DEFAULT NULL,
  `ip_client` char(15) DEFAULT NULL,
  `ip_server` char(15) DEFAULT NULL,
  `http_status_code` varchar(10) DEFAULT NULL,
  `http_reply_size` int(11) DEFAULT NULL,
  `http_method` varchar(20) DEFAULT NULL,
  `http_url` text,
  `http_username` varchar(20) DEFAULT NULL,
  `http_mime_type` varchar(50) DEFAULT NULL,
  `squid_hier_status` varchar(20) DEFAULT NULL,
  `squid_request_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aron_logs`
--

LOCK TABLES `aron_logs` WRITE;
/*!40000 ALTER TABLE `aron_logs` DISABLE KEYS */;
/*!40000 ALTER TABLE `aron_logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`aron`@`localhost`*/ /*!50003 trigger on_cache BEFORE INSERT ON aron.aron_logs
FOR EACH ROW
BEGIN
    IF new.ip_server = '-' THEN
 SET new.ip_server = 'CACHE';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
