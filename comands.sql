CREATE TABLE cliente (
	dni int PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150),
	telefono VARCHAR (10)
);

CREATE TABLE servicio (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	descripcion VARCHAR (250),
	telefono VARCHAR (10),
	web VARCHAR (150)
);

CREATE TABLE subscripcion (
	id serial PRIMARY KEY,
	cuota int NOT NULL,
	fk_cliente integer,
	CONSTRAINT cliente_frkey FOREIGN KEY (fk_cliente) REFERENCES cliente (dni),
	fk_servicio integer,
	CONSTRAINT serv_frkey FOREIGN KEY (fk_servicio) REFERENCES servicio (id)
);


createCliente(dni: 1234567, firstName: "Gabriel", lastName: "Casares"
	telefono: "3442561142", email: "test@test.com") {
		cliente {
			dni
			firstName
		}
}

createServicio(name: "Netflix", descripcion: "Hola mundo") {
	servicio {
		id
		name
	}
}

createSubscripcion(idCliente: 1234567, idServicio: 1, cuota: 12345) {
	subscripcion {
		cliente {
			firstName
		}
		servicio {
			name
		}
		cuota
	}
}