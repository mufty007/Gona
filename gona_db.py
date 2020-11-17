import sqlite3
conn = sqlite3.connect('gona.db')


c.execute('''
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`tree`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tree` (
  `idtree` INT NOT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`idtree`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`plot`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`plot` (
  `idplot` INT NOT NULL,
  `location` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `tree_idtree` INT NOT NULL,
  PRIMARY KEY (`idplot`),
  INDEX `fk_plot_tree_idx` (`tree_idtree` ASC) VISIBLE,
  CONSTRAINT `fk_plot_tree`
    FOREIGN KEY (`tree_idtree`)
    REFERENCES `mydb`.`tree` (`idtree`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`grid`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`grid` (
  `idgrid` INT NOT NULL,
  `plot_idplot` INT NOT NULL,
  PRIMARY KEY (`idgrid`),
  INDEX `fk_grid_plot1_idx` (`plot_idplot` ASC) VISIBLE,
  CONSTRAINT `fk_grid_plot1`
    FOREIGN KEY (`plot_idplot`)
    REFERENCES `mydb`.`plot` (`idplot`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
''')
