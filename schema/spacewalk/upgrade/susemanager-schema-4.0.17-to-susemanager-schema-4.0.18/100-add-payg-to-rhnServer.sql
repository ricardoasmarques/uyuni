ALTER TABLE rhnServer
    ADD COLUMN IF NOT EXISTS payg CHAR(1)
       DEFAULT ('N') NOT NULL;
