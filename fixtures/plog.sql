-- Table to store squid access logs

CREATE TABLE statistics_plog (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    proxy_host           VARCHAR(30),
    timestamp            DECIMAL(15,3),
    date_day             DATE,                  -- set by trigger
    date_time            TIME,                  -- set by trigger
    response_time        INTEGER,
    client_ip            CHAR(15),
    squid_status         VARCHAR(30),
    http_status          VARCHAR(10),
    reply_size           INTEGER,
    request_method       VARCHAR(15),
    url                  VARCHAR(200),
    domain               VARCHAR(50),
    username             VARCHAR(30),
    squid_connect        VARCHAR(20),
    server_ip            CHAR(15),
    mime_type            VARCHAR(50)
) ENGINE=MYISAM;

-- trigger that extracts the date value from the timestamp column
-- and stores it in the date_day and date_time columns
-- this allows fast calculation of per-day aggregate values
DELIMITER //
CREATE TRIGGER extract_date_bi BEFORE INSERT ON statistics_plog FOR EACH ROW
BEGIN
    SET NEW.date_day  = DATE(FROM_UNIXTIME(NEW.timestamp));
    SET NEW.date_time = TIME(FROM_UNIXTIME(NEW.timestamp));
END; //

CREATE TABLE deny_log (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    proxy_host           VARCHAR(30),
    date_day             DATE,
    date_time            TIME,
    category             VARCHAR(40),
    client_ip            CHAR(15),
    url                  VARCHAR(200),
    domain               VARCHAR(50),
    username             VARCHAR(30)
) ENGINE=MYISAM;
