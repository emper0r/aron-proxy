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

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'professori');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,23);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add license',7,'add_license'),(20,'Can change license',7,'change_license'),(21,'Can delete license',7,'delete_license'),(22,'Can add classi',8,'add_classi'),(23,'Can change classi',8,'change_classi'),(24,'Can delete classi',8,'delete_classi'),(25,'Can add professori',9,'add_professori'),(26,'Can change professori',9,'change_professori'),(27,'Can delete professori',9,'delete_professori'),(28,'Can add mac',10,'add_mac'),(29,'Can change mac',10,'change_mac'),(30,'Can delete mac',10,'delete_mac'),(31,'Can add new devices',11,'add_newdevices'),(32,'Can change new devices',11,'change_newdevices'),(33,'Can delete new devices',11,'delete_newdevices'),(34,'Can add blacklist',12,'add_blacklist'),(35,'Can change blacklist',12,'change_blacklist'),(36,'Can delete blacklist',12,'delete_blacklist'),(37,'Can add https',13,'add_https'),(38,'Can change https',13,'change_https'),(39,'Can delete https',13,'delete_https'),(40,'Can add choices',14,'add_choices'),(41,'Can change choices',14,'change_choices'),(42,'Can delete choices',14,'delete_choices'),(49,'Can add routing',17,'add_routing'),(50,'Can change routing',17,'change_routing'),(51,'Can delete routing',17,'delete_routing'),(52,'Can add import config',18,'add_importconfig'),(53,'Can change import config',18,'change_importconfig'),(54,'Can delete import config',18,'delete_importconfig'),(55,'Can add export config',19,'add_exportconfig'),(56,'Can change export config',19,'change_exportconfig'),(57,'Can delete export config',19,'delete_exportconfig'),(58,'Can add dash board',20,'add_dashboard'),(59,'Can change dash board',20,'change_dashboard'),(60,'Can delete dash board',20,'delete_dashboard'),(61,'Can add aron logs',21,'add_aronlogs'),(62,'Can change aron logs',21,'change_aronlogs'),(63,'Can delete aron logs',21,'delete_aronlogs'),(64,'Can add cache',22,'add_cache'),(65,'Can change cache',22,'change_cache'),(66,'Can delete cache',22,'delete_cache'),(67,'Can add lfd',23,'add_lfd'),(68,'Can change lfd',23,'change_lfd'),(69,'Can delete lfd',23,'delete_lfd'),(70,'Can add top',24,'add_top'),(71,'Can change top',24,'change_top'),(72,'Can delete top',24,'delete_top'),(73,'Can add aiuto',25,'add_aiuto'),(74,'Can change aiuto',25,'change_aiuto'),(75,'Can delete aiuto',25,'delete_aiuto'),(76,'Can add wan',26,'add_wan'),(77,'Can change wan',26,'change_wan'),(78,'Can delete wan',26,'delete_wan'),(79,'Can add lan',27,'add_lan'),(80,'Can change lan',27,'change_lan'),(81,'Can delete lan',27,'delete_lan'),(82,'Can add MAC Management',28,'add_management'),(83,'Can change MAC Management',28,'change_management'),(84,'Can delete MAC Management',28,'delete_management'),(85,'Can add apply',29,'add_apply'),(86,'Can change apply',29,'change_apply'),(87,'Can delete apply',29,'delete_apply'),(88,'Can add dhcptable',30,'add_dhcptable'),(89,'Can change dhcptable',30,'change_dhcptable'),(90,'Can delete dhcptable',30,'delete_dhcptable');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'bcrypt_sha256$$2a$12$ByxY9pv.rnyvgpbEMNMK2.0ZuWlMVmswSNnmSIAWV80azP5hhfycq','2016-03-13 19:20:17',1,'admin','','','antonio@ctime.it',1,1,'2016-03-13 19:11:40');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'license','License','license'),(8,'classi','Proxy','classi'),(9,'professori','Proxy','professori'),(10,'mac','Proxy','mac'),(11,'new devices','Proxy','newdevices'),(12,'blacklist','Proxy','blacklist'),(13,'https','Proxy','https'),(14,'choices','Network','choices'),(17,'routing','Routing','routing'),(18,'import config','Configurazione','importconfig'),(19,'export config','Configurazione','exportconfig'),(20,'dash board','DashBoard','dashboard'),(21,'aron logs','DashBoard','aronlogs'),(22,'cache','DashBoard','cache'),(23,'lfd','DashBoard','lfd'),(24,'top','DashBoard','top'),(25,'aiuto','DashBoard','aiuto'),(26,'wan','Network','wan'),(27,'lan','Network','lan'),(28,'MAC Management','Network','management'),(29,'apply','Network','apply'),(30,'dhcptable','Network','dhcptable');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-03 14:40:09
