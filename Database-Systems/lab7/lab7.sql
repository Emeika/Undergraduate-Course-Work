create database LAB34


create table LOCATION(
	CITYID varchar(255) Primary Key,
	CITYNAME varchar(255)
)

insert into LOCATION
values ('C10' , 'Los Angeles'),
('C20' , 'Karachi'),
('C30' , 'Lahore')


create table DEPT(
	DeptNo int Primary key,
	DEPTNAME varchar(255) Not Null,
	CITYID varchar(255) FOREIGN KEY REFERENCES LOCATION(CITYID)
)

insert into DEPT
values(10 , 'Sales' , 'C10' ),
(20 , 'Finance and Administration' ,'C20'),
(30 , 'Software' , 'C30'),
(40 , 'Finance' , 'C30')


create table EMP(
	Empno varchar(255) Not Null Primary key,
	Ename varchar(255) Not Null,
	Gender char Not Null,
	Job varchar(255) Not Null,
	Mgr varchar(255),
	Salary int,
	Comm varchar(255),
	DeptNo int FOREIGN KEY REFERENCES DEPT(DeptNo)
)

Insert into EMP(Empno, Ename, Gender, Job, Mgr , Salary, Comm, DeptNo)
values ('7201' , 'Alice' , 'F' , 'Clerk' , '7202' , 30000 , ' ', 20),
('7101' , 'Bob' , 'M' , 'Salesman' , '7102' , 50000 , '10000' , 10),
('7102' , 'Chris' , 'M' , 'Manager', '7205' , 75000 , ' ' , 10),
('7202' , 'David' , 'M' , 'Manager' , '7205' , 75000 , ' ' , 20),
('7203' , 'Earl' , 'M' , 'President' ,' ' , 150000 , ' ' , 20),
('7302' ,'Gomes' , 'M' , 'Programmer' , '7205' , 50000 , ' ' , 30),
('7204' , 'Helen' , 'F' , 'Accountant' , '7202' , 50000 , ' ' , 20),
('7103' , 'Jamie' , 'F' ,'Salesman' , '7102' , 35000 , '20000' , 10),
('7205' , 'Kyle' , 'F' , 'Vice President' , '7203', 100000 , ' ' , 20)

select * from EMP

select Ename from EMP 
WHERE DeptNo = 10

select Distinct Empno, Ename , DEPTNAME
from EMP , DEPT


SELECT EMP.Empno, EMP.Ename, DEPT.DEPTNAME
FROM EMP
INNER JOIN DEPT ON EMP.DeptNo = DEPT.DeptNo

select count(*)
from EMP
where DeptNo = 20





 






