--create database dbk_lab13

create table Program (
    ProgramID varchar(10) primary key,
    Duration int not null,
    Description varchar(255) not null
);

insert into Program (ProgramID, Duration, Description)
values('BA', 2, 'Bachelors in Arts'),
('BBA', 2, 'Bachelors in Business Administration'),
('BSCS', 4, 'Bachelors in Computer Science'),
('MBA', 2, 'Masters in Business Administration'),
('MCS', 2, 'Masters in Computer Science');

create table Student(
StdID varchar(255) not null primary key,
FirstName varchar(255) not null,
LastName varchar(255) not null,
Gender varchar(255) not null,
Program varchar(10) foreign key references Program(ProgramID),
EnrollSemester varchar(10) not null,
EnrollYear int not null
)

insert into Student(StdID, FirstName, LastName, Gender, Program, EnrollSemester, EnrollYear)
values('S001', 'Ab', 'Rehman', 'M', 'BSCS', 'Spring', 2014),
('S002', 'Alizeh', 'Irfan', 'F', 'BSCS', 'Fall', '2016'),
('S003', 'Nehal', 'Asif', 'F', 'BSCS', 'Spring', '2015'),
('S004', 'Zain', 'Qureshi', 'M', 'BSCS', 'Spring', '2015'),
('S005', 'Shozab', 'Khan', 'M', 'BSCS', 'Fall', '2014'),
('S006', 'Sohaib', 'Asghar', 'M', 'BSCS', 'Fall', '2015'),
('S007', 'Zainab', 'Ashfaq', 'F', 'BSCS', 'Fall', '2015'),
('S008', 'Ali', 'Haider', 'M', 'BSCS', 'Spring', '2016'),
('S009', 'Ijaz', 'Malik', 'M', 'BBA', 'Fall', '2014'),
('S010', 'Mujtaba', 'Ahsan', 'M', 'BBA', 'Spring', '2014'),
('S011', 'Zeeshan', 'Tariq', 'M', 'BBA', 'Fall', '2015'),
('S012', 'Ayesha', 'Abid', 'F', 'BBA', 'Spring', '2016'),
('S013', 'Fatima', 'Ijaz', 'F', 'BBA', 'Spring', '2016'),
('S014', 'Ali', 'Jaffery', 'M', 'BBA', 'Fall', '2013'),
('S015', 'Qasim', 'Abid', 'M', 'BA', 'Spring', '2015'),
('S016', 'Babak', 'Ashfaq', 'M', 'BA', 'Fall', '2016'),
('S017', 'Sakina', 'Abbas', 'F', 'BA', 'Fall', '2015'),
('S018', 'Ailia', 'Zahra', 'F', 'MBA', 'Spring', '2014'),
('S019', 'Usman', 'Ilyas', 'M', 'MBA', 'Fall', '2014'),
('S020', 'Amina', 'Hussain', 'F', 'MBA', 'Spring', '2014'),
('S021', 'Momina', 'Qureshi', 'F', 'MCS', 'Fall', '2014'),
('S022', 'Christoper', 'Emmanuelle', 'M', 'MCS', 'Spring', '2015'),
('S023', 'Ali', 'Malik', 'M', 'MCS', 'Fall', '2015')

create table Faculty (
  FacID varchar(4) not null primary key,
  FirstName varchar(20) not null,
  LastName varchar(20) not null,
  Specialization varchar(50) not null
);

insert into Faculty (FacID, FirstName, LastName, Specialization)
values ('F001', 'Sarwan', 'Abbasi', 'Human Computer Interaction'),
('F002', 'Marshal', 'Mathers', 'Artificial Intelligence'),
('F003', 'Tupac', 'Shakur', 'Algorithms'),
('F004', 'Mike', 'Shinoda', 'Pakistan History'),
('F005', 'Kanye', 'West', 'Mass Communication'),
('F006', 'Dr', 'Dre', 'English Literature'),
('F007', 'Ice', 'Cube', 'Economics'),
('F008', 'Kendrik', 'Lamar', 'Management'),
('F009', 'Rick', 'Ross', 'Marketing'),
('F010', 'Lil', 'Wayne', 'Maths'),
('F011', 'Jay', 'Z', 'Physics')

create table Courses(
CourseID varchar(255) primary key,
CourseName varchar(255) not null,
Program varchar(255) not null
)

insert into Courses
values('BUSN121', 'Micro Economics', 'BBA'),
('BUSN305', 'Corporate Governance', 'BBA'),
('BUSN322', 'Financial Management', 'BBA'),
('BUSN361', 'Ops Excellence', 'BBA'),
('BUSN460', 'Business Law', 'BBA'),
('BUSN554', 'Entrepreneurship', 'MBA'),
('BUSN565', 'Advanced Marketing Skills', 'MBA'),
('COMP111', 'Programming II', 'BSCS'),
('COMP213', 'Database Systems', 'BSCS'),
('COMP220', 'Software Engineering', 'BSCS'),
('COMP301', 'Operating Systems', 'BSCS'),
('COMP302', 'Theory of Automota', 'BSCS'),
('COMP303', 'Algorithms', 'BSCS'),
('COMP323', 'Computer Organization', 'BSCS'),
('COMP650', 'Digital Signal Processing', 'MCS'),
('COMP660', 'Advanced AI', 'MCS'),
('COMP788', 'Quantum Computing', 'MCS'),
('CSCS100', 'Intro To Computing', 'ALL'),
('ENGL101', 'Basic WritingSkills', 'ALL'),
('ENGL103', 'Advanced Writing Skills', 'ALL'),
('ENGL313', 'Sociolinguistics', 'BA'),
('ENGL315', 'Poetry I', 'BA'),
('MATHS100', 'Basic Mathematics', 'ALL'),
('MATHS103', 'Calculus', 'ALL'),
('MCOM100', 'Intro to Mass Communication', 'ALL'),
('MCOM301', 'Press Laws And Ethics', 'BA'),
('PHYS101', 'Physics I', 'ALL'),
('PHYS103', 'Physics II', 'ALL'),
('STAT101', 'Basic Statistics', 'ALL')

create table CourseSection(
CSID varchar(255) primary key,
CourseID varchar(255) foreign key references Courses(CourseID),
Semester varchar(255),
FacID varchar(4) foreign key references Faculty(FacID),
Section varchar(255) not null,
Room varchar(255) not null,
)

insert into CourseSection
values('CS001', 'COMP213', 'Spring 2017', 'F001', 'A', 'S219'),
('CS002', 'COMP213','Spring 2017', 'F003', 'B', 'S317'),
('CS003', 'COMP303', 'Spring 2017', 'F003', 'A', 'S218'),
('CS004', 'COMP303', 'Spring 2017', 'F003', 'B', 'S216'),
('CS005', 'COMP302', 'Spring 2017', 'F001', 'A', 'S417'),
('CS006', 'COMP302', 'Spring 2017', 'F003', 'B' ,'S412'),
('CS007', 'COMP111', 'Spring 2017', 'F001', 'A', 'S218'),
('CS008','COMP111', 'Spring 2017', 'F001', 'B', 'S320'),
('CS009','COMP220', 'Spring 2017', 'F001', 'A', 'S316'),
('CS010', 'COMP220', 'Spring 2017', 'F002', 'B', 'S318'),
('CS011', 'COMP301', 'Spring 2017', 'F003', 'A', 'S319'),
('CS012', 'COMP301', 'Spring 2017', 'F002', 'B', 'S316'),
('CS013', 'COMP323', 'Spring 2017', 'F002', 'A', 'S216'),
('CS014', 'COMP323', 'Spring 2017', 'F002', 'B', 'S318'),
('CS015', 'COMP788', 'Spring 2017', 'F001', 'A', 'S217'),
('CS016', 'COMP650','Spring 2017', 'F002', 'A', 'S412'),
('CS017', 'COMP660', 'Spring 2017', 'F002', 'A', 'S216'),
('CS018', 'BUSN121','Spring 2017', 'F008', 'A', 'S417'),
('CS019', 'BUSN121', 'Spring 2017', 'F009', 'B', 'S318'),
('CS020', 'BUSN322', 'Spring 2017', 'F007', 'A', 'S318'),
('CS021', 'BUSN322', 'Spring 2017', 'F009', 'B', 'S320'),
('CS022', 'BUSN361', 'Spring 2017', 'F009', 'A', 'S313'),
('CS023', 'BUSN361', 'Spring 2017', 'F009', 'B','S319'),
('CS024','BUSN460','Spring 2017', 'F007', 'A', 'S318'),
('CS025', 'BUSN460', 'Spring 2017', 'F009', 'B', 'S412'),
('CS026', 'BUSN305', 'Spring 2017', 'F007', 'A', 'S219'),
('CS027', 'BUSN305', 'Spring 2017', 'F007', 'B','S218'),
('CS028','BUSN554', 'Spring 2017', 'F008', 'A', 'S412'),
('CS029', 'BUSN565', 'Spring 2017', 'F007', 'A', 'S218'),
('CS030', 'ENGL313', 'Spring 2017', 'F006', 'A', 'S318'),
('CS031', 'ENGL313', 'Spring 2017', 'F006', 'B', 'S316'),
('CS032', 'ENGL315','Spring 2017', 'F006', 'A', 'S320'),
('CS033', 'ENGL315','Spring 2017', 'F006', 'B', 'S216'),
('CS034', 'MCOM301',' Spring 2017','F005' ,'A' ,'E319'),
('CS035', 'MCOM301', 'Spring 2017', 'F005', 'B', 'E317'),
('CS036', 'ENGL101', 'Spring 2017', 'F006', 'A' ,'E319'),
('CS037', 'ENGL101', 'Spring 2017', 'F006' ,'B' ,'E416'),
('CS038', 'ENGL103', 'Spring 2017', 'F006' ,'A' ,'E219'),
('CS039', 'MCOM100','Spring 2017', 'F005' ,'A' ,'E320'),
('CS040', 'MATHS100', 'Spring 2017', 'F010', 'A', 'S412'),
('CS041', 'MATHS100', 'Spring 2017', 'F010', 'B', 'S219'),
('CS042', 'MATHS103', 'Spring 2017', 'F010', 'A', 'S313'),
('CS043', 'STAT101', 'Spring 2017', 'F010','A' ,'S313'),
('CS044', 'STAT101', 'Spring 2017', 'F010' ,'B', 'S319'),
('CS045', 'PHYS101', 'Spring 2017', 'F011' ,'A', 'S313'),
('CS046', 'PHYS101', 'Spring 2017', 'F011' ,'B', 'S412'),
('CS047' ,'PHYS103', 'Spring 2017', 'F011' ,'A', 'S316'),
('CS048' ,'CSCS100', 'Spring 2017', 'F001' ,'A', 'S412'),
('CS049', 'CSCS100', 'Spring 2017', 'F003' ,'B', 'S316'),
('CS050', 'CSCS100', 'Spring 2017', 'F003' ,'C', 'S316'),
('CS051', 'CSCS100' ,'Spring 2017', 'F003' ,'D', 'S316'),
('CS052', 'CSCS100', 'Spring 2017', 'F003' ,'E', 'S316'),
('CS053', 'CSCS100', 'Spring 2017', 'F003' ,'F', 'S316'),
('CS054', 'COMP213', 'Fall 2017', 'F003' ,'A','S320'),
('CS055', 'COMP213', 'Fall 2017', 'F003' ,'B' ,'S216'),
('CS056', 'COMP302', 'Fall 2017', 'F001' ,'A', 'S417'),
('CS057', 'COMP302', 'Fall 2017', 'F003' ,'B', 'S412'),
('CS058', 'COMP303', 'Fall 2017', 'F001' ,'A' ,'S217'),
('CS059', 'COMP303', 'Fall 2017', 'F003', 'B', 'S218'),
('CS060', 'COMP111', 'Fall 2017', 'F001' ,'A', 'S417'),
('CS061', 'COMP111', 'Fall 2017', 'F002' ,'B' ,'S313'),
('CS062', 'COMP220', 'Fall 2017', 'F002' ,'A', 'S217'),
('CS063', 'COMP220', 'Fall 2017', 'F001' ,'B' ,'S320'),
('CS064', 'COMP301', 'Fall 2017', 'F001', 'A', 'S417'),
('CS065', 'COMP301', 'Fall 2017', 'F002' ,'B', 'S320'),
('CS066', 'COMP323', 'Fall 2017', 'F001' ,'A', 'S319'),
('CS067', 'COMP323', 'Fall 2017', 'F001', 'B', 'S319'),
('CS068', 'COMP788', 'Fall 2017', 'F003', 'A', 'S219'),
('CS069', 'COMP650', 'Fall 2017', 'F001', 'A', 'S412'),
('CS070', 'COMP660', 'Fall 2017', 'F003', 'A', 'S416'),
('CS071', 'BUSN121', 'Fall 2017', 'F008', 'A', 'S412'),
('CS072', 'BUSN121', 'Fall 2017', 'F007', 'B', 'S319'),
('CS073', 'BUSN322', 'Fall 2017', 'F007', 'A', 'S219'),
('CS074', 'BUSN322', 'Fall 2017', 'F009', 'B', 'S219'),
('CS075', 'BUSN361', 'Fall 2017', 'F009', 'A', 'S313'),
('CS076', 'BUSN361', 'Fall 2017', 'F009', 'B', 'S219'),
('CS077', 'BUSN460', 'Fall 2017', 'F008', 'A', 'S317'),
('CS078', 'BUSN460', 'Fall 2017', 'F009', 'B', 'S316'),
('CS079', 'BUSN305', 'Fall 2017', 'F009', 'A', 'S318'),
('CS080', 'BUSN305', 'Fall 2017', 'F007', 'B', 'S217'),
('CS081', 'BUSN554', 'Fall 2017', 'F007', 'A', 'S313'),
('CS082', 'BUSN565', 'Fall 2017', 'F009', 'A', 'S417'),
('CS083', 'ENGL313', 'Fall 2017', 'F006', 'A', 'S320'),
('CS084', 'ENGL313', 'Fall 2017', 'F006', 'B', 'S319'),
('CS085', 'ENGL315', 'Fall 2017', 'F006', 'A', 'S217'),
('CS086', 'ENGL315', 'Fall 2017', 'F006', 'B', 'S219'),
('CS087', 'MCOM301', 'Fall 2017', 'F005', 'A', 'E318'),
('CS088', 'MCOM301', 'Fall 2017', 'F005', 'B', 'E317'),
('CS089', 'ENGL101', 'Fall 2017', 'F006', 'A', 'E216'),
('CS090', 'ENGL101', 'Fall 2017', 'F006', 'B', 'E320'),
('CS091', 'ENGL103', 'Fall 2017', 'F006', 'A', 'E217'),
('CS092', 'MCOM100', 'Fall 2017', 'F005', 'A', 'E320'),
('CS093', 'MATHS100', 'Fall 2017', 'F010', 'A', 'S217'),
('CS094', 'MATHS100', 'Fall 2017', 'F010', 'B', 'S218'),
('CS095', 'MATHS103', 'Fall 2017', 'F010', 'A', 'S412'),
('CS096', 'STAT101', 'Fall 2017', 'F010', 'A', 'S219'),
('CS097', 'STAT101', 'Fall 2017', 'F010', 'B', 'S313'),
('CS098', 'PHYS101', 'Fall 2017', 'F011', 'A', 'S320'),
('CS099', 'PHYS101', 'Fall 2017', 'F011', 'B', 'S313'),
('CS100', 'PHYS103', 'Fall 2017', 'F011', 'A', 'S219'),
('CS101', 'CSCS100', 'Fall 2017', 'F001', 'A', 'S417'),
('CS102', 'CSCS100', 'Fall 2017', 'F002', 'B', 'S219'),
('CS103', 'CSCS100', 'Fall 2017', 'F002', 'C', 'S219'),
('CS104', 'CSCS100', 'Fall 2017', 'F002', 'D', 'S219')

create table StudentCourses
(StdID varchar(255) foreign key references Student(StdID),
CSID varchar(255) foreign key references CourseSection(CSID)
)

insert into StudentCourses
values('S001', 'CS005'),
('S001', 'CS009'),
('S001', 'CS011'),
('S001', 'CS013'),
('S001', 'CS040'),
('S001', 'CS054'),
('S001', 'CS061'),
('S001', 'CS065'),
('S001', 'CS067'),
('S001', 'CS102'),
('S002', 'CS001'),
('S002', 'CS004'),
('S002', 'CS008'),
('S002', 'CS014'),
('S002', 'CS053'),
('S002', 'CS054'),
('S002', 'CS055'),
('S002', 'CS062'),
('S002', 'CS065'),
('S002', 'CS101'),
('S003', 'CS001'),
('S003', 'CS004'),
('S003', 'CS006'),
('S003', 'CS011'),
('S003', 'CS050'),
('S003', 'CS054'),
('S003', 'CS056'),
('S003', 'CS060'),
('S003', 'CS065'),
('S003', 'CS102'),
('S004', 'CS001'),
('S004', 'CS008'),
('S004', 'CS012'),
('S004', 'CS014'),
('S004', 'CS042'),
('S004', 'CS054'),
('S004', 'CS057'),
('S004', 'CS061'),
('S004', 'CS067'),
('S004', 'CS104'),
('S005', 'CS001'),
('S005', 'CS005'),
('S005', 'CS012'),
('S005', 'CS014'),
('S005', 'CS050'),
('S005', 'CS056'),
('S005', 'CS058'),
('S005', 'CS061'),
('S005', 'CS065'),
('S005', 'CS093'),
('S006', 'CS001'),
('S006', 'CS005'),
('S006', 'CS008'),
('S006', 'CS013'),
('S006', 'CS042'),
('S006', 'CS055'),
('S006', 'CS058'),
('S006', 'CS063'),
('S006', 'CS067'),
('S006', 'CS096'),
('S007', 'CS001'),
('S007', 'CS004'),
('S007', 'CS007'),
('S007', 'CS014'),
('S007', 'CS046'),
('S007', 'CS056'),
('S007', 'CS060'),
('S007', 'CS064'),
('S007', 'CS067'),
('S007', 'CS094'),
('S008', 'CS001'),
('S008', 'CS003'),
('S008', 'CS006'),
('S008', 'CS009'),
('S008', 'CS049'),
('S008', 'CS055'),
('S008', 'CS060'),
('S008', 'CS065'),
('S008', 'CS067'),
('S008', 'CS104'),
('S009', 'CS018'),
('S009', 'CS020'),
('S009', 'CS024'),
('S009', 'CS027'),
('S009', 'CS050'),
('S009', 'CS071'),
('S009', 'CS073'),
('S009', 'CS076'),
('S009', 'CS079'),
('S009', 'CS096'),
('S010', 'CS018'),
('S010', 'CS021'),
('S010', 'CS025'),
('S010', 'CS027'),
('S010', 'CS038'),
('S010', 'CS071'),
('S010', 'CS075'),
('S010', 'CS077'),
('S010', 'CS080'),
('S010', 'CS100'),
('S011', 'CS018'),
('S011', 'CS021'),
('S011', 'CS024'),
('S011', 'CS027'),
('S011', 'CS050'),
('S011', 'CS072'),
('S011', 'CS077'),
('S011', 'CS078'),
('S011', 'CS080'),
('S011', 'CS097'),
('S012', 'CS018'),
('S012', 'CS023'),
('S012', 'CS026'),
('S012', 'CS027'),
('S012', 'CS047'),
('S012', 'CS072'),
('S012', 'CS074'),
('S012', 'CS077'),
('S012', 'CS079'),
('S012', 'CS091'),
('S013', 'CS018'),
('S013', 'CS021'),
('S013', 'CS025'),
('S013', 'CS027'),
('S013', 'CS050'),
('S013', 'CS071'),
('S013', 'CS073'),
('S013', 'CS076'),
('S013', 'CS079'),
('S013', 'CS095'),
('S014', 'CS018'),
('S014', 'CS021'),
('S014', 'CS025'),
('S014', 'CS027'),
('S014', 'CS038'),
('S014', 'CS073'),
('S014', 'CS077'),
('S014', 'CS079'),
('S014', 'CS085'),
('S014', 'CS089'),
('S015', 'CS032'),
('S015', 'CS036'),
('S015', 'CS039'),
('S015', 'CS044'),
('S015', 'CS052'),
('S015', 'CS086'),
('S015', 'CS091'),
('S015', 'CS097'),
('S015', 'CS103'),
('S015', 'CS104'),
('S016', 'CS030'),
('S016', 'CS040'),
('S016', 'CS044'),
('S016', 'CS049'),
('S016', 'CS053'),
('S016', 'CS085'),
('S016', 'CS094'),
('S016', 'CS097'),
('S016', 'CS101'),
('S016', 'CS104'),
('S017', 'CS034'),
('S017', 'CS036'),
('S017', 'CS039'),
('S017', 'CS048'),
('S017', 'CS053'),
('S017', 'CS085'),
('S017', 'CS090'),
('S017', 'CS093'),
('S017', 'CS095'),
('S017', 'CS102'),
('S018', 'CS029'),
('S018', 'CS039'),
('S018', 'CS047'),
('S018', 'CS081'),
('S018', 'CS094'),
('S018', 'CS098'),
('S019', 'CS029'),
('S019', 'CS044'),
('S019', 'CS047'),
('S019', 'CS082'),
('S019', 'CS100'),
('S019', 'CS104'),
('S020', 'CS029'),
('S020', 'CS042'),
('S020', 'CS048'),
('S020', 'CS082'),
('S020', 'CS097'),
('S020', 'CS103'),
('S021', 'CS016'),
('S021', 'CS038'),
('S021', 'CS045'),
('S021', 'CS070'),
('S021', 'CS095'),
('S021', 'CS100'),
('S022', 'CS015'),
('S022', 'CS041'),
('S022', 'CS047'),
('S022', 'CS070'),
('S022', 'CS093'),
('S022', 'CS104')

--Query_01: How many courses has 'Ab Rehman' registered for in Fall-2017
select count(*) as "Ab Rehman's Courses in Fall 2017"
from CourseSection cs
join StudentCourses sc on sc.CSID = cs.CSID
join Courses c on c.CourseID = cs.CourseID
join Student s on s.StdID = sc.StdID
where s.FirstName = 'Ab' and s.LastName = 'Rehman'
and cs.Semester = 'Fall 2017';

--Query_02: List down the courses that 'Ab Rehman' has taken till now or is currentlytaking.
select cs.CourseID, c.Coursename
from CourseSection cs
join StudentCourses sc on sc.CSID = cs.CSID
join Courses c on c.CourseID = cs.CourseID
join Student s on s.StdID = sc.StdID
where s.FirstName = 'Ab' and s.LastName = 'Rehman';

--Query_03: List down the courses that 'Ab Rehman' has taken till now (but not the ones that he is currentlytaking).
select cs.courseID, c.courseName
from CourseSection cs
join StudentCourses sc on sc.CSID = cs.CSID
join Courses c on c.CourseID = cs.CourseId
join Student s on s.StdID = sc.StdID
where s.FirstName ='Ab' and s.LastName = 'Rehman'
and cs.Semester != 'Fall 2017';

--Query_04: Which course (rather a specific section of a course) has the most students enrolled in it.
select top 1 cs.CourseID, c.CourseName, cs.Section, count(*) as EnrolledStudents
from CourseSection cs
join StudentCourses sc on sc.CSID = cs.CSID
JOIN Courses c on c.CourseID = cs.CourseID
group by cs.CourseID, c.Coursename, cs.Section
order by count(*) desc;

--Query_05. For which course have students registered for the most (in all times).
select top 1 cs.CourseID, c.CourseName, count(*) as RegistrationCount
from CourseSection cs
join StudentCourses sc on sc.CSID = cs.CSID
join Courses c on c.CourseID = cs.CourseID
group by cs.CourseID, c.CourseName
order by count(*) desc;

--Query_06. Which student have repeated the same course more than once.
select distinct S.StdID, S.FirstName, S.LastName
from Student S
join StudentCourses SC1 on S.StdID = SC1.StdID
join StudentCourses SC2 on S.StdID = SC2.StdID AND SC1.CSID <> SC2.CSID

--Query_07. Write down the names of all students who are class fellows of either 'Momina Qureshi' or 'AlizehIrfan?
select s.FirstName ,s.LastName
from Student s
where s.StdID in (select sc.StdID
				from StudentCourses sc
				join Student s on s.StdID = sc.StdID
				join CourseSection cs on cs.CSID = sc.CSID
				where s.FirstName = 'Momina' and s.LastName = 'Qureshi') 
or s.StdID in (select sc.StdID from StudentCourses sc
				join Student s on s.StdID =sc.StdID
				join CourseSection cs on cs.CSID=sc.CSID
				where s.FirstName ='Alizeh' and s.LastName= 'Irfan')