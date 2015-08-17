BEGIN;
CREATE TABLE `License_license` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `client` varchar(64) NOT NULL,
    `province` varchar(64) NOT NULL,
    `lic_a` varchar(64) NOT NULL,
    `lic_b` varchar(64) NOT NULL,
    `exp_lic` date NOT NULL
);
COMMIT;
