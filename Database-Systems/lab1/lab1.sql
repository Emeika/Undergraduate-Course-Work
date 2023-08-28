Hafsah Shahbaz
251684784

--CREATE DATABASE LAB1;
use LAB1

create table Persons(
	PersonID int,
	LastName varchar(255),
	FirstName varchar(255),
	Address varchar(255),
	City varchar(255)
)

insert into Persons(PersonID, LastName, FirstName, Address, City)
values('1' , 'Hansen' , 'Ola' , 'Timoteivn 10' , 'Sandnes'),
('2' , 'Svendson' , 'Tove' , 'Borgvn 23' , 'Sandnes'),
('3' , 'Pettersen' , 'Kari' , 'Storgt 20' , 'Stavanger')

ALTER TABLE Persons
ADD DateOfBirth date 
ALTER TABLE Persons
ALTER COLUMN DateOfBirth year



ALTER TABLE Persons
DROP COLUMN DateOfBirth

select * from Persons