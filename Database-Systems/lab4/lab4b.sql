--create database Lab4BB

use Lab4BB 


create table Customers(
	CustomerID varchar(255),
	CustomerName varchar(255),
	ContactName varchar(255), 
	Address varchar(255),
	City varchar(255),
	PostalCode varchar(255),
	Country varchar(255)
)

insert into Customers
values('1' , 'Alfreds Futterkiste' , 'Maria Anders' , 'Obere Str. 57' , 'Berlin', '12209' , 'Germany'),
('2' , 'Ana Trujillo Emparedado	s y helados' , 'Ana Trujillo' , 'Avda. de la Constitució n 2222' , 'México d.f', '05021' , 'Mexico'),
('3' , 'Antonio Moreno Taquería' , 'Antonio Moreno' , 'Mataderos 2312' , 'México d.f', '05023' , 'Mexico')


INSERT INTO Customers (CustomerID ,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('4' , 'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway');

INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger','Norway')


DELETE FROM Customers
WHERE CustomerName='Alfreds Futterkiste' AND ContactName='Maria Anders'

INSERT INTO Customers (CustomerID ,CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('1' , 'Alfreds Futterkiste','Maria Anders', 'Obere Str. 57' , 'Berlin', '12209' , 'Germany')

UPDATE Customers
SET ContactName='Alfred Schmidt', City='Hamburg'
WHERE CustomerName='Alfreds Futterkiste'

SELECT CustomerName,City FROM Customers
SELECT * FROM Customers