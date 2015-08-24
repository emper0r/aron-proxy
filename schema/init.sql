BEGIN;
DROP TABLE IF EXISTS License_license;
CREATE TABLE `License_license` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `client` varchar(64) NOT NULL,
    `province` varchar(64) NOT NULL,
    `req` varchar(128) NOT NULL,
    `lic` varchar(128) NOT NULL,
    `exp_lic` varchar(128) NOT NULL);
COMMIT;
