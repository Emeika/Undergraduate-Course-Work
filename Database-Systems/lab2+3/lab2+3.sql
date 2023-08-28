--CREATE DATABASE LAB2and3;

use LAB2and3
/*
CREATE TABLE PersonsNotNull (
	P_Id int NOT NULL,
	LastName varchar(255) NOT NULL,
	FirstName varchar(255),
	Address varchar(255),
	City varchar(255)
)

insert into PersonsNotNull(P_Id, LastName, FirstName, Address, City)
values('1' , 'Hansen' , 'Ola' , 'Timoteivn 10' , 'Sandnes'),
('2' , 'Svendson' , 'Tove' , 'Borgvn 23' , 'Sandnes'),
('3' , 'Pettersen' , 'Kari' , 'Storgt 20' , 'Stavanger')

-- create a UNIQUE constraint on the "P_Id" column
ALTER TABLE PersonsNotNull
ADD UNIQUE (P_Id)

--  UNIQUE constraint on multiple columns
ALTER TABLE PersonsNotNull
ADD CONSTRAINT uc_PersonID UNIQUE (P_Id,LastName)


--To DROP a UNIQUE ConstrainT
ALTER TABLE PersonsNotNull
DROP CONSTRAINT uc_PersonID

--SQL PRIMARY KEY Constraint on ALTER TABLE
ALTER TABLE PersonsNotNull
ADD PRIMARY KEY (P_Id)

-- defining a PRIMARY KEY constraint on multiple columns,
ALTER TABLE Persons
ADD CONSTRAINT pk_PersonID PRIMARY KEY (P_Id,LastName)


--To drop a PRIMARY KEY constraint
ALTER TABLE Persons
DROP CONSTRAINT pk_PersonID



CREATE TABLE Orders
(
	O_Id int NOT NULL, 
	OrderNo int NOT NULL,
	P_Id int,
	PRIMARY KEY (O_Id),
	FOREIGN KEY (P_Id) REFERENCES PersonsNotNull(P_Id)
)


insert into Orders(O_Id, OrderNo, P_Id)
values('1' , '77895' , '3'),
('2' , '44678' , '3'),
('3' , '22456', '2'),
('4', '24562' , '1')



-- To create a FOREIGN KEY constraint on the "P_Id" column
ALTER TABLE Orders
ADD FOREIGN KEY (P_Id)
REFERENCES PersonsNotNull(P_Id)


-- defining a FOREIGN KEY constraint on multiple columns
ALTER TABLE Orders
ADD CONSTRAINT 
fk_PerOrders FOREIGN KEY (P_Id)
--REFERENCES To DROP a FOREIGN PersonsNotNull(P_Id) KEY Constraint



-- To drop a FOREIGN KEY constraint
ALTER TABLE Orders
DROP FOREIGN KEY fk_PerOrders

--SQL CHECK Constraint on ALTER TABLE
ALTER TABLE PersonsNotNull
ADD CHECK (P_Id>0)

--To DROP a CHECK Constraint
ALTER TABLE PersonsNotNull
DROP CONSTRAINT chk_Person

--ALTER TABLE PersonsNotNull
ALTER Access:TABLE PersonsNotNull
ALTER COLUMN City SET DEFAULT 'SANDNES'

--To DROP a DEFAULT Constraint

ALTER Access:TABLE Persons
ALTER COLUMN City DROP DEFAULT

select * from Orders
select * from PersonsNotNull

*/