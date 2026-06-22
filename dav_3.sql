create table hotels(
hotel_id serial primary key,
name varchar(100) not null,
city varchar(50) not null,
stars int not null check (stars between 1 and 5)
);

create table rooms (
room_id serial primary key,
hotel_id int not null,
room_number varchar(10) not null,
floor int not null, 
night_price decimal(10,2),

foreign key(hotel_id)
references hotels(hotel_id)
on delete cascade
);


create table guests(
guest_id serial primary key,
room_id int not null,
first_name varchar(50) not null,
last_name varchar(50) not null,
phone varchar(20),

foreign key (room_id)
references rooms(room_id)
on delete cascade
);


create table services(
service_id serial primary key,
room_id int not null,
service_name varchar(100) not null,
service_price decimal(10,2) not null,

foreign key (room_id)
references rooms(room_id)
on delete cascade
);




