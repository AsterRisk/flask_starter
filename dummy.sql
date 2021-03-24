drop database if exists info3180_project;
create database info3180_project;

use info3180_project;

drop table if exists properties;

create table properties(
    prop_id int not null AUTO_INCREMENT,
    title varchar(40) not null,
    
    no_bed int not null,
    no_bath int not null, 
    loc varchar(60) not null,
    descr varchar(255) not null,
    typ varchar(15) not null,
    price numeric(10, 2) not null,
    media_addr varchar(70),
    primary key (prop_id)
)