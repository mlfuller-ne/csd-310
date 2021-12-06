# Marlene Fuller
#CSD-310 Module 10
# Python Scripts to create tables

import mysql.connector
from mysql.connector import errorcode

#conn = mysql.connector.connect(
#    user='root', password='TabyTigr#082021', host='127.0.0.1', database='outland_adventures'
#)
config = {
    "user": "root",
    "password": "TabyTigr#082021",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
   # cursor = db.cursor()
    cursor.execute = ("USE outland_adventures")
    db.commit()
    cursor.execute = ("DROP USER IF EXISTS 'outland_adventures_user'@'localhost")
    db.commit()
    cursor.execute = ("CREATE USER 'out_adventures_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!'")
    db.commit()
    cursor.execute = ("GRANT ALL PRIVILEGES ON outland_adventures.*    TO'out_adventures_user'@'localhost'")
    db.commit()    
    
       
    cursor.execute = ("DROP TABLE IF EXISTS visa_tracker")
    db.commit()
    
    sql = """CREATE TABLE visa_tracker (    visa_id     INT(11) NOT NULL   AUTO_INCREMENT,
    visa_type   VARCHAR(25) NOT NULL,
    customer_id INT         NULL,    
    employee_id INT         NULL,
    received_date          DATE       NULL,
    expiration_date        DATE       NULL,
    isactive        BOOLEAN    NULL,
    PRIMARY KEY(visa_id))"""
    print(sql)
    cursor.execute = (sql)
    db.commit() 
    
    cursor.execute = ("DROP TABLE IF EXISTS passport_tracker")
    db.commit()

    sql = '''CREATE TABLE passport_tracker (
    passport_id     INT(11) NOT NULL   AUTO_INCREMENT,
    customer_id INT         NULL,    
    employee_id INT         NULL,
    issuing_country       VARCHAR(25) NOT NULL,
    type                   VARCHAR(25) NOT NULL,
    start_date             DATE       NULL,
    expiration_date        DATE       NULL,
    isactive        BOOLEAN    NULL,
    PRIMARY KEY(passport_id))'''
    cursor.execute = (sql)
    db.commit() 

    cursor.execute = ("DROP TABLE IF EXISTS innoculation_tracker")
    db.commit() 
    
    sql = '''CREATE TABLE innoculation_tracker (
    innoculation_id     INT(11)  NOT NULL   AUTO_INCREMENT,
    customer_id INT         NULL,    
    employee_id INT         NULL,
    type                   VARCHAR(25) NOT NULL,
    received_date          DATE       NULL,
    expiration_date        DATE       NULL,
    isactive        BOOLEAN    NULL,
    PRIMARY KEY(innoculation_id))'''
    cursor.execute = (sql) 
    db.commit() 

 
    cursor.execute = ("DROP TABLE IF EXISTS rentals")
    db.commit() 
  
    sql = """CREATE TABLE rentals (
    rental_id   INT(11)  NOT NULL    AUTO_INCREMENT,
    equipment_id INT        NOT NULL,
    date_out     DATE       NOT NULL,   
    date_in      DATE            NULL,  
    end_date     DATE            NULL,
    isactive     BOOLEAN         NULL,
    PRIMARY KEY(rental_id),
    CONSTRAINT fk_equipment_rentals
    FOREIGN KEY(equipment_id)
        REFERENCES equipment(equipment_id))"""
    cursor.execute = (sql)
    db.commit() 

    cursor.execute = ("DROP TABLE IF EXISTS equipment_sales")
    db.commit() 

    sql = """CREATE TABLE equipment_sales (
    sale_id   INT(11)   NOT NULL    AUTO_INCREMENT,
    equipment_id INT        NOT NULL,
    date_of_sale DATE       NOT NULL,   
    final_equipment_price  float(7,2) NULL,  
    end_date       DATE            NULL,
    isactive       BOOLEAN         NULL,
    PRIMARY KEY(sale_id),
    CONSTRAINT fk_equipment_sales
    FOREIGN KEY(equipment_id)
        REFERENCES equipment(equipment_id))"""
    cursor.execute = (sql)
    db.commit() 


    cursor.execute = ("DROP TABLE IF EXISTS customer") 
    db.commit() 
    
    sql = """CREATE TABLE customer ( 
    customer_id INT(11)   NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75) NOT NULL,
    last_name   VARCHAR(75) NOT NULL,
    passport_id     INT        NULL,
    visa_id     INT            NULL,
    innoculation_id  INT       NULL,
    start_date      DATE       NULL,
    end_date        DATE       NULL,
    isactive        BOOLEAN    NULL,
    PRIMARY KEY(customer_id) )"""
    cursor.execute = (sql)
    db.commit() 
     

    cursor.execute = ("DROP TABLE IF EXISTS employee")
    db.commit() 

    sql = """CREATE TABLE employee (
    employee_id INT(11)   NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75) NOT NULL,
    last_name   VARCHAR(75) NOT NULL,
    position    VARCHAR(25) NOT NULL,
    passport_id     INT        NULL,
    visa_id     INT            NULL,
    innoculation_id  INT       NULL,
    start_date      DATE       NULL,
    end_date        DATE       NULL,
    isactive        BOOLEAN    NULL,
    PRIMARY KEY(employee_id))"""
    cursor.execute = (sql)
    db.commit()  


    cursor.execute = ("DROP TABLE IF EXISTS airfare_packages")
    db.commit() 

    sql = """CREATE TABLE airfare_package (
    airfare_pkg_id    INT(11)  NOT NULL    AUTO_INCREMENT,
    airfare_carrier  VARCHAR(25)  NOT  NULL,    
    origination_location VARCHAR(50)   NOT NULL,
    destination_location VARCHAR(50)   NOT NULL,
    airfare_pkg_cost_amt FLOAT(7,2)    NOT NULL,
    airfare_pkg_retail_price FLOAT(7,2)     NULL,
    start_date      DATE       NULL,   
    end_date        DATE       NULL,
    isactive    BOOLEAN         NULL,    
    PRIMARY KEY(airfare_pkg_id) )"""
    cursor.execute = (sql)
    db.commit() 
    
    cursor.execute = ("DROP TABLE IF EXISTS supply_packages")
    db.commit() 
    
    sql = """CREATE TABLE supply_packages (
    supply_pkg_id    INT(11) NOT NULL    AUTO_INCREMENT,
    supply_type         VARCHAR(25)  NOT  NULL,    
    supply_type_descr   VARCHAR(50)       NULL,
    season_type         VARCHAR(25)      NULL,
    supply_pkg_cost_amt FLOAT(7,2)    NOT NULL,
    supply_pkg_retail_price FLOAT(7,2)     NULL,
    purchase_date          DATE       NULL,   
    expiration_date        DATE       NULL,
    isactive          BOOLEAN         NULL,    
    PRIMARY KEY(supply_pkg_id) )"""
    cursor.execute = (sql)
    db.commit() 
    
    cursor.execute = ("DROP TABLE IF EXISTS equipment")
    db.commit() 
    
    sql = """CREATE TABLE equipment (
    equipment_id   INT(11)  NOT NULL    AUTO_INCREMENT,
    equipment_type VARCHAR(50) NOT NULL,
    equipment_use  VARCHAR(10)     NULL,
    rental_price   FLOAT(7,2)      NULL,  
    sales_price   FLOAT(7,2)       NULL,  
    equipment_cost  FLOAT(7,2)     NOT NULL,    
    equipment_date_bought DATE     NOT NULL,   
    total_service_life_years INT   NULL,   
    start_date     DATE            NULL,  
    expiration_date DATE           NULL,
    isactive       BOOLEAN         NULL,
    PRIMARY KEY(equipment_id) )"""
    cursor.execute = (sql)
    db.commit() 

    
    cursor.execute = ("DROP TABLE IF EXISTS trek")
    db.commit()
    
    
    sql = """CREATE TABLE trek (
    trek_id   INT(11) NOT NULL    AUTO_INCREMENT,
    trek_type      VARCHAR(25) NOT NULL,
    location       VARCHAR(50) NOT NULL,
    season_type    VARCHAR(10)     NULL,
    trek_cost_amt  FLOAT(10,2)      NULL,
    trek_retail_amt FLOAT(10,2)          NULL, 
    start_date     DATE        NOT NULL,
    end_date       DATE            NULL,
    isactive       BOOLEAN         NULL,
    PRIMARY KEY(trek_id))"""
    cursor.execute = (sql)
    db.commit()
    
 
    cursor.execute = ("DROP TABLE IF EXISTS orders")
    db.commit() 
   
    sql = """CREATE TABLE orders (
    order_id    INT(11)         NOT NULL    AUTO_INCREMENT,
    trek_id     INT         NOT  NULL,    
    customer_id INT         NOT NULL, 
    employee_id  INT            NULL,
    airfare_pkg_id INT          NULL,
    rental_id   INT             NULL,
    sale_id     INT             NULL,
    supply_pkg_id INT           NULL,
    order_date  DATE        NOT NULL,
    fulfillment_date DATE       NULL,   
    end_date         DATE       NULL,
    isactive    BOOLEAN         NULL,    
    PRIMARY KEY(order_id)
    CONSTRAINT fk_trek
    FOREIGN_KEY(trek_id)
    REFERENCES trek(trek_id) )"""
    cursor.execute = (sql)
    db.commit()
    
   
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist.")

    else:
        print(err)
    
else:
    db.close()