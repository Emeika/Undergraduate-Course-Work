--create database Lab4B

use lab4B

CREATE TABLE StudentDetails (
	ID varchar(255) Primary Key,
	Name varchar(255),
	Course varchar(255)
	
)


insert into	StudentDetails
values('1041' , 'Sara' , 'Java'),
('1204' , 'Aryan' , 'C++'),
('1043' , 'Sameer' , 'Python'),
('1032' , 'Abhijeet' , 'Oracle')


CREATE TABLE StudentMarks(
	ID varchar(255) Primary key,
	Marks int
	FOREIGN KEY (ID) REFERENCES StudentDetails(ID)
)

Insert into StudentMarks
values('1041' , 65),
('1204' , 55),
('1043' , 73),
('1032' , 62)



select * from StudentDetails
select * from StudentMarks
