create table gran_premio(
	id int primary key auto_increment,
	nombre varchar(45),
	distancia int,
	num_carreras int
);
create table caballos(
	id int primary key auto_increment,
	nombre varchar(45),
	fecha_nacimiento datetime,
	velocidad int,
	experiencia int,
	valor_apuesta int,
	id_carrera int, 
	FOREIGN KEY (id_carrera) REFERENCES gran_premio(id)
);
create table apostantes(
	id int primary key auto_increment,
	nombre varchar(45),
	saldo int
);
