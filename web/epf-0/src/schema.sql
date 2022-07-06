create table users (
  username varchar(255) primary key,
  pepper char(16) not null,
  password varchar(255) not null
);
