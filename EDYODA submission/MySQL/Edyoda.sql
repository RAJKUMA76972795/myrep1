mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| demo               |
| edyoda1            |
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| pets               |
| sakila             |
| students           |
| sys                |
| world              |
+--------------------+
12 rows in set (30.43 sec)

-- creating database named edyoda

mysql> create database edyoda;
Query OK, 1 row affected (0.77 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| demo               |
| edyoda             |
| edyoda1            |
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| pets               |
| sakila             |
| students           |
| sys                |
| world              |
+--------------------+
13 rows in set (0.02 sec)

mysql> use edyoda;
Database changed

-- creating SalesPeople table ad inserting values in it

mysql> create table SalesPeople(
    -> Snum int,
    -> Sname varchar(20),
    -> City varchar(20),
    -> Comm int,
    -> primary key (Snum),
    -> unique (Sname));
Query OK, 0 rows affected (4.17 sec)

mysql> desc SalesPeople;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| Snum  | int         | NO   | PRI | NULL    |       |
| Sname | varchar(20) | YES  | UNI | NULL    |       |
| City  | varchar(20) | YES  |     | NULL    |       |
| Comm  | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
4 rows in set (0.32 sec)


mysql> insert into SalesPeople
    -> values
    -> (1001,'Peel','London',12),
    -> (1002,'Serres','Sanjose',13),
    -> (1004,'Motika','London',11),
    -> (1007,'Rifkin','Barcelona',15),
    -> (1003,'Axelrod','Newyork',10);
Query OK, 5 rows affected (0.43 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from SalesPeople;
+------+---------+-----------+------+
| Snum | Sname   | City      | Comm |
+------+---------+-----------+------+
| 1001 | Peel    | London    |   12 |
| 1002 | Serres  | Sanjose   |   13 |
| 1003 | Axelrod | Newyork   |   10 |
| 1004 | Motika  | London    |   11 |
| 1007 | Rifkin  | Barcelona |   15 |
+------+---------+-----------+------+
5 rows in set (0.08 sec)

-- creating Customers table ad inserting values in it

mysql> create table Customers(
    -> Cnum int,
    -> Cname varchar(20),
    -> City varchar(20) not null,
    -> Snum int,
    -> primary key (Cnum),
    -> foreign key (Snum) references SalesPeople (Snum));
Query OK, 0 rows affected (2.20 sec)

mysql> insert into Customers
    -> values
    -> (2001,'Hoffman','London',1001),
    -> (2002,'Giovanni','Rome',1003),
    -> (2003,'Liu','Sanjose',1002),
    -> (2004,'Grass','Berlin',1002),
    -> (2006,'Clemens','London',1001),
    -> (2008,'Cisneros','Sanjose',1007),
    -> (2007,'Pereira','Rome',1004);
Query OK, 7 rows affected (0.69 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> select * from Customers;
+------+----------+---------+------+
| Cnum | Cname    | City    | Snum |
+------+----------+---------+------+
| 2001 | Hoffman  | London  | 1001 |
| 2002 | Giovanni | Rome    | 1003 |
| 2003 | Liu      | Sanjose | 1002 |
| 2004 | Grass    | Berlin  | 1002 |
| 2006 | Clemens  | London  | 1001 |
| 2007 | Pereira  | Rome    | 1004 |
| 2008 | Cisneros | Sanjose | 1007 |
+------+----------+---------+------+
7 rows in set (0.00 sec)

-- creating Orders table ad inserting values in it

mysql> create table Orders(
    -> Onum int,
    -> Amt float(10,2),
    -> Odate date,
    -> Cnum int,
    -> Snum int,
    -> primary key(Onum),
    -> foreign key (Cnum) references Customers (Cnum),
    -> foreign key (Snum) references SalesPeople (Snum));
Query OK, 0 rows affected, 1 warning (2.58 sec)

mysql> desc Orders;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| Onum  | int         | NO   | PRI | NULL    |       |
| Amt   | float(10,2) | YES  |     | NULL    |       |
| Odate | date        | YES  |     | NULL    |       |
| Cnum  | int         | YES  | MUL | NULL    |       |
| Snum  | int         | YES  | MUL | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.08 sec)

mysql> insert into Orders
    -> values
    -> (3001,18.69,'1990-10-03',2008,1007),
    -> (3003,767.19,'1990-10-03',2001,1001),
    -> (3002,1900.10,'1990-10-03',2007,1004),
    -> (3005,5160.45,'1990-10-03',2003,1002),
    -> (3006,1098.16,'1990-10-03',2008,1007),
    -> (3009,1713.23,'1990-10-04',2002,1003),
    -> (3007,75.75,'1990-10-04',2004,1002),
    -> (3008,4273.00,'1990-10-05',2006,1001),
    -> (3010,1309.95,'1990-10-06',2004,1002),
    -> (3011,9891.88,'1990-10-06',2006,1001);
Query OK, 10 rows affected (0.20 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select * from Orders;
+------+---------+------------+------+------+
| Onum | Amt     | Odate      | Cnum | Snum |
+------+---------+------------+------+------+
| 3001 |   18.69 | 1990-10-03 | 2008 | 1007 |
| 3002 | 1900.10 | 1990-10-03 | 2007 | 1004 |
| 3003 |  767.19 | 1990-10-03 | 2001 | 1001 |
| 3005 | 5160.45 | 1990-10-03 | 2003 | 1002 |
| 3006 | 1098.16 | 1990-10-03 | 2008 | 1007 |
| 3007 |   75.75 | 1990-10-04 | 2004 | 1002 |
| 3008 | 4273.00 | 1990-10-05 | 2006 | 1001 |
| 3009 | 1713.23 | 1990-10-04 | 2002 | 1003 |
| 3010 | 1309.95 | 1990-10-06 | 2004 | 1002 |
| 3011 | 9891.88 | 1990-10-06 | 2006 | 1001 |
+------+---------+------------+------+------+
10 rows in set (0.00 sec)

-- 1. Count the number of Salesperson whose name begin with ‘a’/’A’.

mysql> select count(*) from SalesPeople where Sname like 'A%';
+----------+
| count(*) |
+----------+
|        1 |
+----------+
1 row in set (0.22 sec)

mysql> select count(*) from SalesPeople where Sname like 'a%';
+----------+
| count(*) |
+----------+
|        1 |
+----------+
1 row in set (0.00 sec)

-- 2.Display all the Salesperson whose all orders worth is more than Rs. 2000.

mysql> select distinct Snum,Sname from SalesPeople where Snum in (select Snum from Orders where Amt>2000);
+------+--------+
| Snum | Sname  |
+------+--------+
| 1001 | Peel   |
| 1002 | Serres |
+------+--------+
2 rows in set (0.08 sec)

-- 3.Count the number of Salesperson belonging to Newyork.

mysql> select count(*) from SalesPeople where City='Newyork';
+----------+
| count(*) |
+----------+
|        1 |
+----------+
1 row in set (0.00 sec)

-- 4.Display the number of Salespeople belonging to London and belonging to Paris.

mysql> select count(*) from SalesPeople where City='London' or City='Paris';
+----------+
| count(*) |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)

-- 5.Display the number of orders taken by each Salesperson and their date of orders

mysql> select Snum, count(*) , Odate from Orders group by Snum;
+------+----------+------------+
| Snum | count(*) | Odate      |
+------+----------+------------+
| 1001 |        3 | 1990-10-03 |
| 1002 |        3 | 1990-10-03 |
| 1003 |        1 | 1990-10-04 |
| 1004 |        1 | 1990-10-03 |
| 1007 |        2 | 1990-10-03 |
+------+----------+------------+
5 rows in set (0.00 sec)


mysql> select Snum, count(*) from Orders group by Snum;
+------+----------+
| Snum | count(*) |
+------+----------+
| 1001 |        3 |
| 1002 |        3 |
| 1003 |        1 |
| 1004 |        1 |
| 1007 |        2 |
+------+----------+
5 rows in set (0.00 sec)


mysql> select Snum, Odate from Orders;
+------+------------+
| Snum | Odate      |
+------+------------+
| 1007 | 1990-10-03 |
| 1004 | 1990-10-03 |
| 1001 | 1990-10-03 |
| 1002 | 1990-10-03 |
| 1007 | 1990-10-03 |
| 1002 | 1990-10-04 |
| 1001 | 1990-10-05 |
| 1003 | 1990-10-04 |
| 1002 | 1990-10-06 |
| 1001 | 1990-10-06 |
+------+------------+
10 rows in set (0.00 sec)

