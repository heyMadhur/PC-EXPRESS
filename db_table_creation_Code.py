import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("Create Database PC_Express")

# creating tables for project

# table 1 for motherboards in stock and price

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Motherboard(Name varchar(100),Company varchar(50),Socket_type varchar(50),Chipset varchar(50),Qty char(100),Price char(100))")


# table 2 for processor

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Processor(Company varchar(100),Name varchar(50),Cores int(4),Socket_type varchar(100),Base_clock varchar(100),Boost_clock varchar(100),Qty char(100),Price int(100))")

# table 3 for Ram

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Rams(Company varchar(100),Name varchar(50),Size varchar(5),Speed varchar(100),Ram_type varchar(100),Qty varchar(100),Price varchar(100))")

# table 4 for storage

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Storage(Company varchar(100),Name varchar(50),Type varchar(100),Speed varchar(100),Qty varchar(100),Price varchar(100))")

# table 5 for GPU

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Graphic_Cards(Company varchar(100),Name varchar(100),Memory_type varchar(100),Vram varchar(100),Qty varchar(100),Price varchar(100))")

# table 6 for power supply

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Power_supply(Company varchar(100),Name varchar(100),Type varchar(100),Watts varchar(100),Qty varchar(100),Price varchar(100))")

# table 7 for cabinet

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Cabinet(Company varchar(100),Name varchar(100),Form_Factor varchar(100),Qty varchar(100),Price varchar(100))")

# table 8 for Sales and customer details

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="pc_express")
mycursor=mydb.cursor()
mycursor.execute("create table Sales_Details(C_name varchar(100),Phone_NO varchar(100),Description_of_Goods varchar(100),Date_of_purchase date,Qty varchar(100),Price varchar(100))")
