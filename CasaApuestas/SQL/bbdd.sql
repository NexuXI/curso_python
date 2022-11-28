select * from productos;

INSERT INTO `curso_python`.`productos` (`id`, `nombre`, `precio`, `fecha_registro`) VALUES ('1', 'Prodcuto1', '100', '2022-10-13');

Insert into productos (nombre, precio, fecha_registro) values(
	"Producto3",
    "200",
    "2022-08-11"
);

select * from personas;

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
