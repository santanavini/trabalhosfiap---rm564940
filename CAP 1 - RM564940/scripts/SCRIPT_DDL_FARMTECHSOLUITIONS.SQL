-- Gerado por Oracle SQL Developer Data Modeler 21.4.2.059.0838
--   em:        2025-04-18 00:12:06 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE culturas CASCADE CONSTRAINTS;

DROP TABLE fazendas CASCADE CONSTRAINTS;

DROP TABLE leituras CASCADE CONSTRAINTS;

DROP TABLE sensores CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE culturas (
    id_cultura          INTEGER NOT NULL,
    name_cultura        VARCHAR2(50) NOT NULL,
    fazendas_id_fazenda INTEGER NOT NULL
);

ALTER TABLE culturas ADD CONSTRAINT cultura_pk PRIMARY KEY ( id_cultura );

ALTER TABLE culturas ADD CONSTRAINT un_culturas_name_ UNIQUE ( name_cultura );

CREATE TABLE fazendas (
    id_fazenda   INTEGER NOT NULL,
    name_fazenda VARCHAR2(50) NOT NULL
);

ALTER TABLE fazendas ADD CONSTRAINT fazendas_pk PRIMARY KEY ( id_fazenda );

ALTER TABLE fazendas ADD CONSTRAINT un_fazendas_name UNIQUE ( name_fazenda );

CREATE TABLE leituras (
    id_leitura         INTEGER NOT NULL,
    data_leitura       DATE NOT NULL,
    sensores_id_sensor INTEGER NOT NULL,
    valor_lido         NUMBER(10, 2) NOT NULL
);

ALTER TABLE leituras ADD CONSTRAINT leituras_pk PRIMARY KEY ( id_leitura );

CREATE TABLE sensores (
    id_sensor           INTEGER NOT NULL,
    name_sensor         VARCHAR2(50) NOT NULL,
    local_sensor        VARCHAR2(50) NOT NULL,
    culturas_id_cultura INTEGER NOT NULL
);

ALTER TABLE sensores ADD CONSTRAINT sensores_pk PRIMARY KEY ( id_sensor );

ALTER TABLE sensores ADD CONSTRAINT un_sensores_name UNIQUE ( name_sensor );

ALTER TABLE culturas
    ADD CONSTRAINT culturas_fazendas_fk FOREIGN KEY ( fazendas_id_fazenda )
        REFERENCES fazendas ( id_fazenda );

ALTER TABLE leituras
    ADD CONSTRAINT leituras_sensores_fk FOREIGN KEY ( sensores_id_sensor )
        REFERENCES sensores ( id_sensor );

ALTER TABLE sensores
    ADD CONSTRAINT sensores_culturas_fk FOREIGN KEY ( culturas_id_cultura )
        REFERENCES culturas ( id_cultura );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             0
-- ALTER TABLE                             10
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
