#$ createdb -U postgres rasa_prueba <--Crear la base de datos-->
#$ psql rasa_prueba postgres <--Entrar en postgres-->

#pslq -U postgres(root)

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

create table hnc(hnc bigint primary key, contenido text);
insert into hnc(hnc, contenido) values (2234567891,'Incidencia hnc de avion 1');
insert into hnc(hnc, contenido) values (2234567892,'Incidencia hnc de avion 2');
insert into hnc(hnc, contenido) values (2234567893,'Incidencia hnc de avion 3');
insert into hnc(hnc, contenido) values (2234567894,'Incidencia hnc de avion 4');
insert into hnc(hnc, contenido) values (2234567895,'Incidencia hnc de avion 5');
insert into hnc(hnc, contenido) values (2234567896,'Incidencia hnc de avion 6');


create table obs(obs bigint primary key, contenido text);
insert into obs(obs, contenido) values (4234567891,'Incidencia obs de avion 7');
insert into obs(obs, contenido) values (4234567892,'Incidencia obs de avion 8');
insert into obs(obs, contenido) values (4234567893,'Incidencia obs de avion 9');
insert into obs(obs, contenido) values (4234567894,'Incidencia obs de avion 10');
insert into obs(obs, contenido) values (4234567895,'Incidencia obs de avion 11');
insert into obs(obs, contenido) values (4234567896,'Incidencia obs de avion 12');

create table erc(erc text primary key, contenido text);
insert into erc(erc, contenido) values ('CA01-00001','Incidencia erc de avion 1');
insert into erc(erc, contenido) values ('CA01-00002','Incidencia erc de avion 2');
insert into erc(erc, contenido) values ('CA01-00003','Incidencia erc de avion 3');
insert into erc(erc, contenido) values ('CA01-00004','Incidencia erc de avion 4');
insert into erc(erc, contenido) values ('CA01-00005','Incidencia erc de avion 5');
insert into erc(erc, contenido) values ('CA01-00006','Incidencia erc de avion 6');