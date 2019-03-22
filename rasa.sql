#$ createdb -U postgres rasa_prueba <--Crear la base de datos-->
#$ psql rasa_prueba postgres <--Entrar en postgres-->

create table increment(colname serial);

create table answers(id serial primary key, contenido text);

insert into answers(contenido) values ('Primera respuesta');
insert into answers(contenido) values ('Segunda respuesta');
insert into answers(contenido) values ('Tercera respuesta');
insert into answers(contenido) values ('Cuarta respuesta');

create table incidencias(hnc text primary key, contenido text);

insert into answers(hnc, contenido) values ('ES-123456','Esta es la incidencia ES-123456');
insert into answers(hnc, contenido) values ('ES-369258','Esta es la incidencia ES-369258');
insert into answers(hnc, contenido) values ('ES-999999','Esta es la incidencia ES-999999');
insert into answers(hnc, contenido) values ('FR-111111','Esta es la incidencia FR-111111');
insert into answers(hnc, contenido) values ('FR-258147','Esta es la incidencia FR-258147');
insert into answers(hnc, contenido) values ('FR-111999','Esta es la incidencia FR-111999');