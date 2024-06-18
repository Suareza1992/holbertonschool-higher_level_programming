# 0x0D. SQL - Introduction

The purpose of this project is to introduce the use of SQL.

## Concepts to learn:
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements for SQL scripts
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- The length of your files will be tested using wc

---
File | Task
---|---
0-list_databases.sql | A script that lists all databases of the MySQL server
1-create_database_if_missing.sql | A script that creates the database ```htbn_0c_0``` in the MySQL server
2-remove_database.sql | A script that deletes the ```hbtn_0c_0``` in the MySQL server
3-list_tables.sql | A script that lists all the tables of a database in the MySQL server
4-first_table.sql | A script that creates a table called ```first_table``` in the current database in the MySQL server
5-full_table.sql | A script that prints the full description of the table ```first_table``` from the database ```hbtn_0c_0``` in your MySQL server
6-list_values.sql | A script that lists all rows of the table ```first_table``` from the database ```htbn_0c_0``` in the MySQL server
7-insert_value.sql | A script that inserts a new row in the tables ```first_table``` (database ```hbtn_0c_0```) in the MySQL server
8-count_89.sql | A script that displays the number of records with ```id = 89``` in the table ```first_table``` of the database ```hbtn_0c_0``` in the MySQL server
9-full_creation.sql | A script that creates a table ```second_table``` in the database ```hbtn_0c_0``` in the MySQL server and adds multiple rows
10-top_score.sql | A script that lists all records of the table ```second_table``` of the database ```hbtn_0c_0``` in the MySQL server
11-best_score.sql | A script that lists all records with a ```score >= 10``` in the table ```second_table``` of the database ```hbtn_0c_0``` in the MySQL server
12-no_cheating.sql | A script that updates the score of Bob to ```10``` in the table ```second_table```
13-change_class.sql | A script that removes all records with a ```score <= 5``` in the table ```second_table``` of the database ```hbtn_0c_0``` in the MySQL server
14-average.sql | A script that computes the score average of all records in the table ```second_table``` of the database ```hbtn_0c_0``` in the MySQL server
15-groups.sql | A script that lists the number of records with the same score in the table ```second_table``` of the database ```hbtn_0c_0``` in the MySQL server
16-no_link.sql | A script that lists all records of the table ```second_table``` of the database ```hbtn_0c_0``` in the MySQL server

## Author
Ángel Suárez
