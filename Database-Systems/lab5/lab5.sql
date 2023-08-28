--create database Lab5

use Lab5


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

INSERT INTO Customers
VALUES ('4' , 'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway')



SELECT DISTINCT City FROM Customers

SELECT *
FROM Customers
WHERE Country='Mexico'

SELECT * FROM Customers 
WHERE CustomerID=1


SELECT *
FROM Customers
WHERE Country='Germany' AND City='Berlin'


SELECT *
FROM Customers
WHERE City='Berlin' OR City='München'


SELECT *
FROM Customers
WHERE Country='Germany'AND (City='Berlin' OR City='München')


SELECT *
FROM Customers
ORDER BY Country


SELECT *
FROM Customers
ORDER BY Country DESC

SELECT *
FROM Customers
ORDER BY Country,CustomerName



SELECT *
FROM Customers
WHERE CustomerID <= 2

SELECT TOP 2 *
FROM Customers


SELECT TOP 50 PERCENT *
FROM Customers
