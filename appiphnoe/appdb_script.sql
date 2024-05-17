create table orderrequests (
	id integer PRIMARY KEY autoincrement,
	firstName varchar(255) NOT NULL,
	lastName varchar(255) NOT NULL,
	phone INTEGER(20) NOT NULL,
	email varchar(255),
	createdAt datetime,
	updatedAt datetime
);

create table logins (
	id integer PRIMARY KEY autoincrement,
	username varchar(255) NOT NULL UNIQUE,
	email varchar(255) NOT NULL UNIQUE,
	password varchar(255) NOT NULL UNIQUE
);