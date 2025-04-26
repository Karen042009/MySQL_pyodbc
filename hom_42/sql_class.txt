-- lite AUTOINCREMENT   my  AUTO_INCREMENT

CREATE TABLE IF NOT EXISTS Teachers (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(20),
  last_name VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS Classes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  class_name VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS TeachersClasses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  teacher_id INT,
  class_id INT,
  FOREIGN KEY (teacher_id) REFERENCES Teachers(id),
  FOREIGN KEY (class_id) REFERENCES Classes(id)
);
CREATE TABLE IF NOT EXISTS Students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(20),
  last_name VARCHAR(20),
  class_id INT,
  FOREIGN KEY (class_id) REFERENCES Classes(id));

CREATE TABLE IF NOT EXISTS Subjects (
  id INT PRIMARY KEY AUTO_INCREMENT,
  subject_name VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS Gradebooks (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  student_id INT, 
  FOREIGN KEY (student_id) REFERENCES Students(id)
);
CREATE TABLE IF NOT EXISTS Grades (
  grade_id INTEGER PRIMARY KEY AUTO_INCREMENT,
  gradebook_id INT,
  subject_id INT,
  grade INT,
  FOREIGN KEY (gradebook_id) REFERENCES Gradebooks(id),
  FOREIGN KEY (subject_id) REFERENCES Subjects(id)
);


INSERT INTO Teachers (teacher_id, first_name, last_name)
VALUES ('Մերուժ', 'ՈՒնանյան');
INSERT INTO Teachers (teacher_id, first_name, last_name)
VALUES ('...', 'Սարդարյան');
INSERT INTO Teachers (teacher_id, first_name, last_name)
VALUES ('․․․', 'Ֆրունզվնա');

INSERT INTO Classes (class_id, class_name, teacher_id)
VALUES ("10-ԱԲ", 1);
INSERT INTO Classes (class_id, class_name, teacher_id)
VALUES ("10-Ֆիզմատ", 2);
INSERT INTO Classes (class_id, class_name, teacher_id)
VALUES ('Պատմական մահ', 3);

INSERT INTO Students (student_id, first_name, last_name, class_id)
VALUES ('Կարեն', 'Պողոսյան', 1);
INSERT INTO Students (student_id, first_name, last_name, class_id)
VALUES ('․․․', '․․․', 2);
INSERT INTO Students (student_id, first_name, last_name, class_id)
VALUES ('․․․', '․․․', 3);

INSERT INTO Grades (grade_id, student_id, subject, grade)
VALUES (1, 'Ծրագրավորում', '9');
INSERT INTO Grades (grade_id, student_id, subject, grade)
VALUES (1, 'Մաթեմ', '9');
INSERT INTO Grades (grade_id, student_id, subject, grade)
VALUES (1, 'Պատմ', '7');

-- 1
SELECT Students.first_name, Classes.class_name FROM Students
INNER JOIN Classes ON Students.class_id = Classes.class_id;

-- 2
SELECT Teachers.first_name, Teachers.last_name, Classes.class_name FROM Teachers
INNER JOIN Classes ON Teachers.teacher_id = Classes.teacher_id;

-- 3
SELECT Students.first_name, Grades.subject, Grades.grade FROM Students
INNER JOIN Grades ON Students.student_id = Grades.student_id;

-- 4
SELECT Classes.class_name, COUNT(Students.student_id) AS number_of_students FROM Class
LEFT JOIN Students ON Classes.class_id = Students.class_id
GROUP BY Classes.class_name;

-- 5
SELECT Students.first_name, Students.last_name
FROM Students
INNER JOIN Classes ON Students.class_id = Classes.class_id
WHERE Classes.class_name = '10-ԱԲ';