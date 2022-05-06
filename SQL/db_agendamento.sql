-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE DATABASE `db_agendamento`;
USE `db_agendamento` ;

-- -----------------------------------------------------
-- Table `Cliente`
-- -----------------------------------------------------
CREATE TABLE `Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `rg` VARCHAR(8) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `telefone` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`idCliente`));


-- -----------------------------------------------------
-- Table `Categoria`
-- -----------------------------------------------------
CREATE TABLE `Categoria` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `descricao_categoria` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idCategoria`));


-- -----------------------------------------------------
-- Table `Servico`
-- -----------------------------------------------------
CREATE TABLE `Servico` (
  `idServico` INT NOT NULL AUTO_INCREMENT,
  `descricao_servico` VARCHAR(50) NOT NULL,
  `valor` DOUBLE NOT NULL,
  `categoria_fk` INT,
  PRIMARY KEY (`idServico`),
  CONSTRAINT `fk_Servico_Categoria2`
    FOREIGN KEY (`categoria_fk`)
    REFERENCES `Categoria` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table `Agendamento`
-- -----------------------------------------------------
CREATE TABLE `Agendamento` (
  `idAgendamento` INT NOT NULL AUTO_INCREMENT,
  `data` DATE NOT NULL,
  `hora_inicio` TIME NOT NULL,
  `hora_fim` TIME NOT NULL,
  `cliente_fk` INT,
  `servico_fk` INT,
  PRIMARY KEY (`idAgendamento`),
  CONSTRAINT `fk_Agendamento_Cliente1`
    FOREIGN KEY (`cliente_fk`)
    REFERENCES `Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Agendamento_Servico1`
    FOREIGN KEY (`servico_fk`)
    REFERENCES `Servico` (`idServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);