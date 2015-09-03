-- MySQL dump 10.13  Distrib 5.6.25, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: aron
-- ------------------------------------------------------
-- Server version	5.6.25-0ubuntu1-log

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
-- Table structure for table `Internet_classi`
--

DROP TABLE IF EXISTS `Internet_classi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_classi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classi` varchar(20) NOT NULL,
  `internet` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `classi` (`classi`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_classi`
--

LOCK TABLES `Internet_classi` WRITE;
/*!40000 ALTER TABLE `Internet_classi` DISABLE KEYS */;
INSERT INTO `Internet_classi` VALUES (1,'autodiscover',0);
/*!40000 ALTER TABLE `Internet_classi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internet_ip`
--

DROP TABLE IF EXISTS `Internet_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classi_id` int(11) NOT NULL,
  `ip` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`),
  KEY `Internet_ip_33b99cda` (`classi_id`),
  CONSTRAINT `classi_id_refs_id_c17fe77b` FOREIGN KEY (`classi_id`) REFERENCES `Internet_classi` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_ip`
--

LOCK TABLES `Internet_ip` WRITE;
/*!40000 ALTER TABLE `Internet_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internet_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internet_mac`
--

DROP TABLE IF EXISTS `Internet_mac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_mac` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classi_id` int(11) NOT NULL,
  `mac` varchar(17) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mac` (`mac`),
  KEY `Internet_mac_33b99cda` (`classi_id`),
  CONSTRAINT `classi_id_refs_id_a9b80970` FOREIGN KEY (`classi_id`) REFERENCES `Internet_classi` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_mac`
--

LOCK TABLES `Internet_mac` WRITE;
/*!40000 ALTER TABLE `Internet_mac` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internet_mac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internet_newdevices`
--

DROP TABLE IF EXISTS `Internet_newdevices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_newdevices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_import` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_newdevices`
--

LOCK TABLES `Internet_newdevices` WRITE;
/*!40000 ALTER TABLE `Internet_newdevices` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internet_newdevices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internet_professori`
--

DROP TABLE IF EXISTS `Internet_professori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_professori` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `professori_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Internet_professori_8a5ea53a` (`professori_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_professori`
--

LOCK TABLES `Internet_professori` WRITE;
/*!40000 ALTER TABLE `Internet_professori` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internet_professori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internet_professori_classi`
--

DROP TABLE IF EXISTS `Internet_professori_classi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_professori_classi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `professori_id` int(11) NOT NULL,
  `classi_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `professori_id` (`professori_id`,`classi_id`),
  KEY `Internet_professori_classi_8a5ea53a` (`professori_id`),
  KEY `Internet_professori_classi_33b99cda` (`classi_id`),
  CONSTRAINT `classi_id_refs_id_9232fb97` FOREIGN KEY (`classi_id`) REFERENCES `Internet_classi` (`id`),
  CONSTRAINT `professori_id_refs_id_3e1ac511` FOREIGN KEY (`professori_id`) REFERENCES `Internet_professori` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_professori_classi`
--

LOCK TABLES `Internet_professori_classi` WRITE;
/*!40000 ALTER TABLE `Internet_professori_classi` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internet_professori_classi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internet_webcontentfilter`
--

DROP TABLE IF EXISTS `Internet_webcontentfilter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internet_webcontentfilter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abortion` tinyint(1) NOT NULL,
  `ads` tinyint(1) NOT NULL,
  `adult` tinyint(1) NOT NULL,
  `aggressive` tinyint(1) NOT NULL,
  `antispyware` tinyint(1) NOT NULL,
  `artnudes` tinyint(1) NOT NULL,
  `astrology` tinyint(1) NOT NULL,
  `banking` tinyint(1) NOT NULL,
  `beerliquorinfo` tinyint(1) NOT NULL,
  `beerliquorsale` tinyint(1) NOT NULL,
  `blog` tinyint(1) NOT NULL,
  `cellphones` tinyint(1) NOT NULL,
  `chat` tinyint(1) NOT NULL,
  `childcare` tinyint(1) NOT NULL,
  `cleaning` tinyint(1) NOT NULL,
  `clothing` tinyint(1) NOT NULL,
  `contraception` tinyint(1) NOT NULL,
  `culnary` tinyint(1) NOT NULL,
  `dating` tinyint(1) NOT NULL,
  `desktopsillies` tinyint(1) NOT NULL,
  `dialers` tinyint(1) NOT NULL,
  `drugs` tinyint(1) NOT NULL,
  `ecommerce` tinyint(1) NOT NULL,
  `entertainment` tinyint(1) NOT NULL,
  `filehosting` tinyint(1) NOT NULL,
  `frencheducation` tinyint(1) NOT NULL,
  `gambling` tinyint(1) NOT NULL,
  `games` tinyint(1) NOT NULL,
  `gardening` tinyint(1) NOT NULL,
  `government` tinyint(1) NOT NULL,
  `guns` tinyint(1) NOT NULL,
  `hacking` tinyint(1) NOT NULL,
  `homerepair` tinyint(1) NOT NULL,
  `hygiene` tinyint(1) NOT NULL,
  `instantmessaging` tinyint(1) NOT NULL,
  `jewelry` tinyint(1) NOT NULL,
  `jobsearch` tinyint(1) NOT NULL,
  `kidstimewasting` tinyint(1) NOT NULL,
  `mail` tinyint(1) NOT NULL,
  `marketingware` tinyint(1) NOT NULL,
  `medical` tinyint(1) NOT NULL,
  `mixed_adult` tinyint(1) NOT NULL,
  `naturism` tinyint(1) NOT NULL,
  `news` tinyint(1) NOT NULL,
  `onlineauctions` tinyint(1) NOT NULL,
  `onlinegames` tinyint(1) NOT NULL,
  `onlinepayment` tinyint(1) NOT NULL,
  `personalfinance` tinyint(1) NOT NULL,
  `pets` tinyint(1) NOT NULL,
  `phishing` tinyint(1) NOT NULL,
  `porn` tinyint(1) NOT NULL,
  `proxy` tinyint(1) NOT NULL,
  `radio` tinyint(1) NOT NULL,
  `religion` tinyint(1) NOT NULL,
  `ringtones` tinyint(1) NOT NULL,
  `searchengines` tinyint(1) NOT NULL,
  `sect` tinyint(1) NOT NULL,
  `sexuality` tinyint(1) NOT NULL,
  `sexualityeducation` tinyint(1) NOT NULL,
  `shopping` tinyint(1) NOT NULL,
  `socialnetworking` tinyint(1) NOT NULL,
  `sportnews` tinyint(1) NOT NULL,
  `sports` tinyint(1) NOT NULL,
  `spyware` tinyint(1) NOT NULL,
  `updatesites` tinyint(1) NOT NULL,
  `vacation` tinyint(1) NOT NULL,
  `violence` tinyint(1) NOT NULL,
  `virusinfected` tinyint(1) NOT NULL,
  `warez` tinyint(1) NOT NULL,
  `weather` tinyint(1) NOT NULL,
  `weapons` tinyint(1) NOT NULL,
  `webmail` tinyint(1) NOT NULL,
  `whitelist` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internet_webcontentfilter`
--

LOCK TABLES `Internet_webcontentfilter` WRITE;
/*!40000 ALTER TABLE `Internet_webcontentfilter` DISABLE KEYS */;
INSERT INTO `Internet_webcontentfilter` VALUES (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `Internet_webcontentfilter` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `License_license`
--

LOCK TABLES `License_license` WRITE;
/*!40000 ALTER TABLE `License_license` DISABLE KEYS */;
/*!40000 ALTER TABLE `License_license` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Network_ipnetwork`
--

DROP TABLE IF EXISTS `Network_ipnetwork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Network_ipnetwork` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip_wan` char(39) NOT NULL,
  `mask_wan` varchar(17) NOT NULL,
  `gateway` char(39) NOT NULL,
  `dns1` char(39) NOT NULL,
  `dns2` char(39) NOT NULL,
  `ip_lan` char(39) NOT NULL,
  `mask_lan` varchar(17) NOT NULL,
  `dhcp` tinyint(1) NOT NULL,
  `ip_start` char(39) NOT NULL,
  `ip_end` char(39) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip_wan` (`ip_wan`),
  UNIQUE KEY `mask_wan` (`mask_wan`),
  UNIQUE KEY `gateway` (`gateway`),
  UNIQUE KEY `dns1` (`dns1`),
  UNIQUE KEY `dns2` (`dns2`),
  UNIQUE KEY `ip_lan` (`ip_lan`),
  UNIQUE KEY `mask_lan` (`mask_lan`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_ipnetwork`
--

LOCK TABLES `Network_ipnetwork` WRITE;
/*!40000 ALTER TABLE `Network_ipnetwork` DISABLE KEYS */;
INSERT INTO `Network_ipnetwork` VALUES (1,'0.0.0.0','0.0.0.0','0.0.0.0','0.0.0.0','0.0.0.0','192.168.0.1','255.255.255.0',1,'192.168.0.10','192.168.0.254');
/*!40000 ALTER TABLE `Network_ipnetwork` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Network_mac`
--

LOCK TABLES `Network_mac` WRITE;
/*!40000 ALTER TABLE `Network_mac` DISABLE KEYS */;
/*!40000 ALTER TABLE `Network_mac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Posta_veximdomains`
--

DROP TABLE IF EXISTS `Posta_veximdomains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Posta_veximdomains` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(128) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  `maxmsgsize` bigint(20) NOT NULL,
  `max_accounts` int(11) NOT NULL,
  `type` varchar(5) NOT NULL,
  `avscan` tinyint(1) NOT NULL,
  `spamassassin` tinyint(1) NOT NULL,
  `mailinglists` tinyint(1) NOT NULL,
  `sa_tag` int(11) NOT NULL,
  `sa_refuse` int(11) NOT NULL,
  `maildir` varchar(128) NOT NULL,
  `uid` int(11) NOT NULL,
  `gid` int(11) NOT NULL,
  `blocklists` tinyint(1) NOT NULL,
  `complexpass` tinyint(1) NOT NULL,
  `pipe` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posta_veximdomains`
--

LOCK TABLES `Posta_veximdomains` WRITE;
/*!40000 ALTER TABLE `Posta_veximdomains` DISABLE KEYS */;
/*!40000 ALTER TABLE `Posta_veximdomains` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Posta_veximusers`
--

DROP TABLE IF EXISTS `Posta_veximusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Posta_veximusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `domain_id` int(11) NOT NULL,
  `passwd` varchar(64) NOT NULL,
  `localpart` varchar(64) NOT NULL,
  `on_avscan` tinyint(1) NOT NULL,
  `on_spamassassin` tinyint(1) NOT NULL,
  `on_forward` tinyint(1) NOT NULL,
  `forward` varchar(32) NOT NULL,
  `unseen` tinyint(1) NOT NULL,
  `on_vacation` tinyint(1) NOT NULL,
  `vacation` longtext NOT NULL,
  `maxmsgsize` bigint(20) NOT NULL,
  `quota` bigint(20) NOT NULL,
  `sa_tag` int(11) NOT NULL,
  `sa_refuse` int(11) NOT NULL,
  `on_blocklist` tinyint(1) NOT NULL,
  `on_complexpass` tinyint(1) NOT NULL,
  `on_piped` tinyint(1) NOT NULL,
  `username` varchar(64) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  `uid` int(11) NOT NULL,
  `gid` int(11) NOT NULL,
  `smtp` varchar(64) NOT NULL,
  `pop` varchar(64) NOT NULL,
  `type` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `Posta_veximusers_e8b327e7` (`domain_id`),
  CONSTRAINT `domain_id_refs_id_d87114c3` FOREIGN KEY (`domain_id`) REFERENCES `Posta_veximdomains` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Posta_veximusers`
--

LOCK TABLES `Posta_veximusers` WRITE;
/*!40000 ALTER TABLE `Posta_veximusers` DISABLE KEYS */;
/*!40000 ALTER TABLE `Posta_veximusers` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add license',7,'add_license'),(20,'Can change license',7,'change_license'),(21,'Can delete license',7,'delete_license'),(22,'Can add classi',8,'add_classi'),(23,'Can change classi',8,'change_classi'),(24,'Can delete classi',8,'delete_classi'),(25,'Can add professori',9,'add_professori'),(26,'Can change professori',9,'change_professori'),(27,'Can delete professori',9,'delete_professori'),(28,'Can add ip',10,'add_ip'),(29,'Can change ip',10,'change_ip'),(30,'Can delete ip',10,'delete_ip'),(31,'Can add mac',11,'add_mac'),(32,'Can change mac',11,'change_mac'),(33,'Can delete mac',11,'delete_mac'),(34,'Can add web content filter',12,'add_webcontentfilter'),(35,'Can change web content filter',12,'change_webcontentfilter'),(36,'Can delete web content filter',12,'delete_webcontentfilter'),(37,'Can add new devices',13,'add_newdevices'),(38,'Can change new devices',13,'change_newdevices'),(39,'Can delete new devices',13,'delete_newdevices'),(40,'Can add Dominio',14,'add_veximdomains'),(41,'Can change Dominio',14,'change_veximdomains'),(42,'Can delete Dominio',14,'delete_veximdomains'),(43,'Can add Account',15,'add_veximusers'),(44,'Can change Account',15,'change_veximusers'),(45,'Can delete Account',15,'delete_veximusers'),(46,'Can add ip network',16,'add_ipnetwork'),(47,'Can change ip network',16,'change_ipnetwork'),(48,'Can delete ip network',16,'delete_ipnetwork'),(49,'Can add MAC',17,'add_mac'),(50,'Can change MAC',17,'change_mac'),(51,'Can delete MAC',17,'delete_mac'),(52,'Can add module',18,'add_module'),(53,'Can change module',18,'change_module'),(54,'Can delete module',18,'delete_module'),(55,'Can install/uninstall modules',18,'can_configure');
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
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'md5$VC2acMCFSunF$0ecf68e03cecf77d00217d5acbfc085e','2015-08-31 15:02:50',1,'admin','','','antonio@ctime.it',1,1,'2015-08-26 11:15:06');
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
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1);
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
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(18,'frontend','module'),(8,'Internet','classi'),(10,'Internet','ip'),(11,'Internet','mac'),(13,'Internet','newdevices'),(9,'Internet','professori'),(12,'Internet','webcontentfilter'),(7,'License','license'),(16,'Network','ipnetwork'),(17,'Network','mac'),(14,'Posta','veximdomains'),(15,'Posta','veximusers'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frontend_module`
--

DROP TABLE IF EXISTS `frontend_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frontend_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(50) NOT NULL,
  `installed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `frontend_module_2dbcba41` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frontend_module`
--

LOCK TABLES `frontend_module` WRITE;
/*!40000 ALTER TABLE `frontend_module` DISABLE KEYS */;
/*!40000 ALTER TABLE `frontend_module` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-31 22:37:52
