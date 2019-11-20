TABLA_JUGUETES = """CREATE TABLE juguetes (
    juguete_id          INTEGER PRIMARY KEY,
    nombre              varchar NOT NULL,
    precio              INTEGER NOT NULL,
    edad_recomendada    INTEGER NOT NULL,
    popularidad         INTEGER NOT NULL
    );"""

TABLA_NENES = """CREATE TABLE nenes (
    nene_id         INTEGER PRIMARY KEY,
    nombre          varchar NOT NULL,
    edad            INTEGER NOT NULL,
    esta_registrado INTEGER NOT NULL,
    karma           INTEGER NOT NULL
    );"""

TABLA_DESEOS_NENE = """CREATE TABLE deseos_nene (
    deseo_nene_id   INTEGER PRIMARY KEY,
    nene_id         INTEGER NOT NULL,
    juguete_id      INTEGER NOT NULL,
    FOREIGN KEY (nene_id)
      REFERENCES nenes (nene_id),
    FOREIGN KEY (juguete_id)
      REFERENCES juguetes (juguete_id)
    );"""

TABLA_PAPAS = """CREATE TABLE papas (
    papa_id          INTEGER PRIMARY KEY,
    nene_a_su_cargo  INTEGER NOT NULL,
    FOREIGN KEY (nene_a_su_cargo)
      REFERENCES nenes (nene_id)
    );"""