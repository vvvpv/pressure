# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:46:21 2020

@author: Kosta
"""

import sqlite3
import random
from datetime import date, timedelta
from matplotlib import pyplot as plt

def make_date():
    d1 = date(2020, 8, 13)  # начальная дата
    d2 = date(2020, 9, 13)  # конечная дата
    delta = d2 - d1         # timedelta
    date_ = [str (d1 + timedelta(i)) for i in range(delta.days + 1)]
    return date_

def make_data(n):
 #[(id, date, upper,lower,pusle)]
    data = []
    for i in range(n):
        _id = i
        date = make_date()[i]
        upper = random.randint(110, 130)
        lower = random.randint(70, 90)
        pusle = random.randint(70, 150)
        data.append ((_id, date, upper, lower, pusle))
    return data
 
def database():
    conn = sqlite3.connect('pressure.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS pressure(
                   id INTEGER PRIMARY KEY,
                   date TEXT NOT NULL,
                   upper_pressure INTEGER NOT NULL,
                   lower_pressure INTEGER NOT NULL,
                   pulse INTEGER NOT NULL);
                   """)
    conn.commit()
    conn.close()

def database_insert():
    conn = sqlite3.connect('pressure.sqlite')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO pressure VALUES (?,?,?,?,?)", make_data(11))
    conn.commit()
    
def database_data():
    conn = sqlite3.connect('pressure.sqlite')
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM pressure")
    results = cursor.fetchall()
    conn.commit()
    #print(results)
    return results
    
def plot():
    data = database_data()
    date = [row[1] for row in data]
    lower = [row[2] for row in data]
    upper = [row[3] for row in data]
    plt.plot (date, lower, color='black', marker = 'o', linestyle = 'solid')
    plt.plot (date, upper, color='green', marker = 'o', linestyle = 'solid')
    plt.show()
    
    
if __name__ == "__main__":
    database()
    database_insert()
    #database_show()
    plot()

