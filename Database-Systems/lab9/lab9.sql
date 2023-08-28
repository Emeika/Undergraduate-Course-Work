--create database lab9



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


SELECT upper(CustomerName) AS
Customer, City FROM Customers

SELECT lower(CustomerName) AS
Customer, City FROM Customers

SELECT substring(City,1,4) AS
ShortCity FROM Customers

SELECT CustomerName,LEN(Address) as
LengthOfAddress FROM Customers;



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


select round(Price,1)
from Product


SELECT ProductName, Price, FORMAT(getdate(),'yyyy-mm-dd')
AS PerDate FROM Product