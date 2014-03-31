SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `syslog` DEFAULT CHARACTER SET latin1 ;
USE `syslog` ;

-- -----------------------------------------------------
-- Table `syslog`.`signed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `syslog`.`signed` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `sign` VARCHAR(100) NULL DEFAULT NULL,
  `message` VARCHAR(255) NULL DEFAULT NULL,
  `signdate` DATETIME NULL DEFAULT NULL,
  `created` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `syslog`.`alert`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `syslog`.`alert` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(100) NULL DEFAULT NULL,
  `host` VARCHAR(100) NULL DEFAULT NULL,
  `alert` VARCHAR(255) NULL DEFAULT NULL,
  `status` ENUM('OK', 'CRITICAL', 'WARNING') NULL DEFAULT NULL,
  `created` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `syslog`.`exclude`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `syslog`.`exclude` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(100) NULL DEFAULT NULL,
  `exclude` VARCHAR(255) NULL DEFAULT NULL,
  `status` ENUM('DELETE', 'EXCLUDE') NULL DEFAULT NULL,
  `created` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
