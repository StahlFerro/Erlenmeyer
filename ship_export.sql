--
-- File generated with SQLiteStudio v3.1.1 on Tue Nov 20 23:15:01 2018
--
-- Text encoding used: UTF-8
--
-- This sql file is generated to assist on migrating data from the old sqlite database (app.db) to the new postgres
-- database (imvr_data)

BEGIN TRANSACTION;

-- Table: ship
CREATE TABLE IF NOT EXISTS ship (
    id          INTEGER      NOT NULL,
    name        VARCHAR (40),
    code        VARCHAR (5),
    speed       FLOAT,
    launch_date DATE,
    capacity    INTEGER,
    engine_id   INTEGER,
    PRIMARY KEY (
        id
    )
);

INSERT INTO ship (
                     id,
                     name,
                     code,
                     speed,
                     launch_date,
                     capacity,
                     engine_id
                 )
                 VALUES (
                     1,
                     'USS Enterprise',
                     'CV-6',
                     40,
                     '1961-01-01',
                     40,
                     NULL
                 );

INSERT INTO ship (
                     id,
                     name,
                     code,
                     speed,
                     launch_date,
                     capacity,
                     engine_id
                 )
                 VALUES (
                     2,
                     'Queen Star 3',
                     '9VBQ5',
                     65,
                     '2016-10-28',
                     60,
                     NULL
                 );

INSERT INTO ship (
                     id,
                     name,
                     code,
                     speed,
                     launch_date,
                     capacity,
                     engine_id
                 )
                 VALUES (
                     3,
                     'Pegasus V',
                     'P5STE',
                     31,
                     '2013-05-12',
                     12,
                     NULL
                 );


---- Index: ix_ship_code
--CREATE INDEX ix_ship_code ON ship (
--    code
--);
--
--
---- Index: ix_ship_name
--CREATE INDEX ix_ship_name ON ship (
--    name
--);


COMMIT TRANSACTION;
--PRAGMA foreign_keys = on;
