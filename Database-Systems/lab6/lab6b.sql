--create database Lab6b


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
('3' , 'Antonio Moreno Taquería' , 'Antonio Moreno' , 'Mataderos 2312' , 'México d.f', '05023' , 'Mexico'),
('4' , 'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway'),
('5' , 'Around the Horn' , 'Thomas Hardy' , '120 Hanover Sq. ' ,'London', 'WA1 1DP',  'UK')


create table Product(
	ProductId varchar(255),
	ProductName varchar(255),
	SupplierID varchar(255),
	CategoryID varchar(255),
	Unit varchar(255),
	Price float

)

insert into Product
values('1', 'Chais' , '1' , '1' , '10 boxes x 20 bags' ,18),
('2', 'Chang' , '1' , '1' , '24 - 12 oz bottles' , 19),
('3', 'Aniseed Syrup' , '1' , '2' , '12 - 550 ml bottles' , 10),
('4' , 'Chef Antons Cajun Seasoni ng' , '1' , '2' , '48 - 6 oz jars' , 22),
('5' , 'Chef Antons Gumbo Mix' , '1' , '2' , '36 boxes' , 21.35 )

create table ord(
	OrderID  int,
	CustomerID int,
	EmployeeID int,
	OrderDate date,
	ShipperID int
)

insert into ord
values (10248, 90, 5, '7-4-1996', 3),
(10249, 81, 6, '7-5-1996', 1),
(10250, 34, 4, '7-8-1996', 2),
(10251, 84, 3, '7-9-1996', 1),
(10252, 76, 4, '7-10-1996', 2)


SELECT * FROM ord
WHERE OrderDate BETWEEN '7-4-1996' AND '7-9-1996'

SELECT CustomerName AS Customer, ContactName AS [Contact Person] 
FROM Customers

SELECT CustomerName, Address+', '+City+', '+PostalCode+', '+Country
AS Address FROM Customers;

SELECT o.OrderID, o.OrderDate,
c.CustomerName 
FROM Customers AS c, ord AS o
WHERE c.CustomerName= 'Around the Horn' AND
c.CustomerID=o.CustomerID;

SELECT ord.OrderID, ord.OrderDate,
Customers.CustomerName FROM Customers, ord
WHERE Customers.CustomerName='Around the Horn' AND
Customers.CustomerID=ord.CustomerID;

CREATE TABLE Persons
(
	ID int IDENTITY(1,1) PRIMARY KEY,
	LastName varchar(255) NOT NULL,
	FirstName varchar(255),
	Address varchar(255),
	City varchar(255)
)

insert into Persons
values('Hansen' , 'Ola' , 'Timoteivn 10' , 'Sandnes'),
('Svendson' , 'Tove' , 'Borgvn 23' , 'Sandnes'),
('Pettersen' , 'Kari' , 'Storgt 20' , 'Stavanger')

INSERT INTO Persons (FirstName,LastName)
VALUES ('Lars','Monsen')

select * from Persons
