create database Lab6

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
VALUES ('4' , 'Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway'),

('5' , 'Around the Horn' , 'Thomas Hardy' , '120 Hanover Sq. ' ,'London', 'WA1 1DP',  'UK')



SELECT * FROM
Customers WHERE
City LIKE 'ber%';



SELECT * FROM
Customers WHERE
City LIKE '%es%'

SELECT * FROM
Customers WHERE
City LIKE '_erlin';


SELECT * FROM
Customers WHERE
City LIKE 'L_n_on';


SELECT * FROM
Customers WHERE
City LIKE '[bsp]%';


SELECT * FROM
Customers WHERE
City LIKE '[a-c]%'


SELECT * FROM
Customers WHERE
City LIKE '[!bsp]%';

SELECT * FROM
Customers WHERE City
NOT LIKE '[bsp]%';

SELECT * FROM
Customers WHERE
City LIKE 's%';

SELECT * FROM
Customers WHERE
City LIKE '%s'

SELECT * FROM
Customers WHERE
Country LIKE '%land%'

SELECT * FROM Customers
WHERE Country NOT LIKE
'%land%';

SELECT * FROM Customers
WHERE City IN
('Paris','London')


create table Products(
	ProductId varchar(255),
	ProductName varchar(255),
	SupplierID varchar(255),
	CategoryID varchar(255),
	Unit varchar(255),
	Price float

)

insert into Products
values('1', 'Chais' , '1' , '1' , '10 boxes x 20 bags' ,18),
('2', 'Chang' , '1' , '1' , '24 - 12 oz bottles' , 19),
('3', 'Aniseed Syrup' , '1' , '2' , '12 - 550 ml bottles' , 10),
('4' , 'Chef Antons Cajun Seasoni ng' , '1' , '2' , '48 - 6 oz jars' , 22),
('5' , 'Chef Antons Gumbo Mix' , '1' , '2' , '36 boxes' , 21.35 )

SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;

SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20


SELECT * FROM Products
WHERE (Price BETWEEN 10
AND 20) AND NOT CategoryID
IN (1,2,3)


SELECT * FROM Products WHERE ProductName BETWEEN
'C' AND 'M'

SELECT * FROM Products
SELECT * FROM Customers

 
