--create database lab7

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

SELECT AVG(Price) AS PriceAverage FROM Product

SELECT ProductName, Price
FROM Product
WHERE Price>(SELECT AVG(Price) FROM Product)

SELECT COUNT(ProductId) FROM Product

SELECT COUNT(*) FROM Product

SELECT COUNT(DISTINCT SupplierID) FROM Product

create table ord(
	OrderID  int,
	CustomerID int,
	EmployeeID int,
	OrderDate date,
	ShipperID int
)

insert into ord
values (10248, 90, 5, '7-4-1996', 3),
(10249, 7, 6, '7-5-1996', 1),
(10250, 34, 4, '7-8-1996', 2),
(10251, 84, 3, '7-9-1996', 1),
(10252, 7, 4, '7-10-1996', 2)

insert into ord
values(10248, 90, 5, '1996-07-04', 3),
(10249, 81, 6, '1996-07-05', 1),
(10250, 34, 4, '1996-07-08', 2)


SELECT COUNT(CustomerID) AS OrdersFromCustomerID7
FROM ord WHERE CustomerID=7

SELECT COUNT(*) AS NumberOfOrders FROM ord

SELECT COUNT(DISTINCT CustomerID) AS NumberOfCustomers FROM ord

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
('4' , 'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway')



SELECT TOP 1 CustomerName FROM Customers
ORDER BY CustomerName ASC

SELECT TOP 1 CustomerName FROM Customers
ORDER BY CustomerName DESC

SELECT MAX(PostalCode) FROM Customers

SELECT MAX(Price) AS HighestPrice FROM
Product;

SELECT MIN(Price) FROM Product

SELECT SUM(Price) FROM Product

CREATE TABLE OrderDetails (
	OrderDetailID int,
	OrderID int,
	ProductID int,
	Quantity int
)

insert into OrderDetails
values(1, 10248, 11, 12),
(2, 10248, 42, 10),
(3, 10248, 72, 5),
(4, 10249, 14, 9),
(5, 10249, 51, 40)



SELECT SUM(Quantity) AS TotalItemsOrdered FROM
OrderDetails


create table Shippers(
	ShipperID int ,
	ShipperName varchar(255),
	Phone varchar(255)
)

insert into  Shippers
values (1, 'Speedy Express', '(503) 555-9831'),
(2, 'United Package', '(503) 555-3199'),
(3, 'Federal Shipping', '(503) 555-9931')


create table Employees
(	EmployeeID int,
	LastName varchar(255),
	FirstName varchar(255),
	BirthDate date,
	Photo varchar(255),
	Notes varchar(255)
)

insert into Employees
values( 1, 'Davolio', 'Nancy', '1968-12-08', 'EmpID1.pic', 'Education includes a BA....'),
(2, 'Fuller', 'Andrew', '1952-02-19', 'EmpID2.pic', 'Andrew received his BTS....'),
(3, 'Leverling', 'Janet', '1963-08-30', 'EmpID3.pic', 'Janet has a BSdegree....')



SELECT Shippers.ShipperName, COUNT(ord.OrderID) AS NumberOfOrders
FROM ord LEFT JOIN Shippers
ON
ord.ShipperID=Shippers.ShipperID 
GROUP BY ShipperName

SELECT Shippers.ShipperName,
Employees.LastName, COUNT(ord.OrderID)
AS NumberOfOrders
FROM ((ord INNER JOIN Shippers ON ord.ShipperID=Shippers.ShipperID)
INNER JOIN Employees
ON ord.EmployeeID=Employees.EmployeeID)
GROUP BY ShipperName,LastName


SELECT Employees.LastName, COUNT(ord.OrderID) AS NumberOfOrders
FROM (ord INNER JOIN Employees
ON
ord.EmployeeID=Employees.EmployeeID) GROUP BY LastName
HAVING COUNT(ord.OrderID) > 10



SELECT Employees.LastName,
COUNT(ord.OrderID) AS NumberOfOrders FROM
ord INNER JOIN Employees
ON
ord.EmployeeID=Employees.EmployeeID
WHERE LastName='Davolio' OR
LastName='Fuller' GROUP BY LastName
HAVING COUNT(ord.OrderID)
> 25;