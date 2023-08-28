create database lab91011
create table Orders(
	OrderID  int,
	CustomerID int,
	EmployeeID int,
	OrderDate date,
	ShipperID int
)

insert into Orders
values (10248, 1, 5, '7-4-1996', 3),
(10249, 2, 6, '7-5-1996', 1),
(10250, 3, 4, '7-8-1996', 2),
(10251, 84, 3, '7-9-1996', 1),
(10252, 7, 4, '7-10-1996', 2)

insert into Orders
values(10248, 90, 5, '1996-07-04', 3),
(10249, 81, 6, '1996-07-05', 1),
(10250, 34, 4, '1996-07-08', 2)


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


SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers
ON
Orders.CustomerID=Customers.CustomerID

SELECT Customers.CustomerName, Orders.OrderID
FROM
Customers
INNER JOIN
Orders
ON
Customers.CustomerID=Orders.CustomerID 
ORDER BY Customers.CustomerName



SELECT Customers.CustomerName,
Orders.OrderID FROM Customers
LEFT JOIN Orders
ON
Customers.CustomerID=Orders.CustomerID
 ORDER BY Customers.CustomerName;

 
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


 SELECT Orders.OrderID,
Employees.FirstName
FROM Orders
RIGHT JOIN Employees
ON
Orders.EmployeeID=Employees.EmployeeID ORDER BY Orders.OrderID

SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName


create table Suppliers(
	SupplierID int not null, 
	SupplierName varchar(255), 
	ContactName varchar(255), 
	Address varchar(255), 
	City varchar(255), 
	PostalCode varchar(255), 
	Country varchar(255))
insert into Suppliers(SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country)
values (1, 'Exotic Liquid', 'CharlotteCooper','49 GilbertSt.','Londona', 'EC1 4SD', 'UK'),
		(2, 'New OrleansCajun Delights','Shelley Burke', 'P.O. Box78934','NewOrleans','70117', 'USA'),
		(3, 'GrandmaKellysHomestead','ReginaMurphy','707 OxfordRd','Ann Arbor', '48104', 'USA')

SELECT City FROM Customers UNION SELECT City FROM Suppliers ORDER BY
City;

SELECT City FROM
Customers UNION ALL SELECT City FROM
Suppliers ORDER BY
City

SELECT City, Country FROM
Customers WHERE
Country='Germany'
UNION ALL
SELECT City, Country FROM
Suppliers WHERE
Country='Germany'
ORDER BY City;