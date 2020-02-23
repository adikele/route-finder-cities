'''
@Aditya Kelekar
Program finds the shortest distance between two given cities. 
Names of a few cities and distances between them is fed to a 
sqlite database. This data is subsequently represented as a 
Networkx graph, with cities as nodes. The Dijkstra function 
is then used to find the shortest path, which is printed out. 
A graph of the cities is also displayed,
but this does not currently show the shortest path.

Development points:
1. Display shortest route on the graph 
2. Use an online database of geographical locations of 
cities and calcuate distances between required cities
3. Provide a web interface to the program.

prints:
   Enter start city: Helsinki
   Enter destination city: Rovaniemi
   0         1          2    3
0  1  Helsinki    Tampere   50
1  2     Espoo    Tampere   30
2  3     Espoo   Helsinki   15
3  4   Tampere  Rovaniemi  115
4  5      Oulu    Tampere   70
['Helsinki', 'Espoo', 'Tampere', 'Rovaniemi']
160
'''

import sqlite3
from pandas import DataFrame
import networkx as nx
import matplotlib.pyplot as plt


def create_database():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()
    sql_command = """
    CREATE TABLE cities (
    serial_no INTEGER PRIMARY KEY,
    city_1 VARCHAR(20),
    city_2 VARCHAR(20),
    distance INTEGER);"""
    cursor.execute(sql_command)


def fill_database():
    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()
    sql_command = """INSERT INTO cities (serial_no, city_1, city_2, distance)
        VALUES (1, 'Helsinki', 'Tampere', 180);"""
    cursor.execute(sql_command)
    sql_command = """INSERT INTO cities (serial_no, city_1, city_2, distance)
        VALUES (2, 'Seinäjoki', 'Tampere', 178);"""
    cursor.execute(sql_command)
    sql_command = """INSERT INTO cities (serial_no, city_1, city_2, distance)
        VALUES (3, 'Turku', 'Tampere', 163);"""
    cursor.execute(sql_command)
    sql_command = """INSERT INTO cities (serial_no, city_1, city_2, distance)
        VALUES (4, 'Oulu', 'Rovaniemi', 166);"""
    cursor.execute(sql_command)
    sql_command = """INSERT INTO cities (serial_no, city_1, city_2, distance)
        VALUES (5, 'Turku', 'Helsinki', 165);"""
    cursor.execute(sql_command)
    sql_command = """INSERT INTO cities (serial_no, city_1, city_2, distance)
        VALUES (6, 'Seinäjoki', 'Oulu', 322);"""
    cursor.execute(sql_command)
    connection.commit()


def read_input(city_type):
    name_city = input("   Enter %s city: " % city_type)
    return name_city


def main():
    create_database()
    fill_database()

    connection = sqlite3.connect("cities.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cities")
    result = cursor.fetchall()
    print("Enter two cities to find the shortest route between them")
    print("Options are: Helsinki, Tampere, Turku, Seinäjoki, Oulu, Rovaniemi")
    city_1 = read_input("start")
    city_2 = read_input("destination")
    df = DataFrame(result)
    G = nx.from_pandas_edgelist(df, 1, 2, 3)

    print("Distances shown are approximate distances, not real ones!")
    path = nx.dijkstra_path(G, city_1, city_2, weight=3)
    print("The shortest path between the given cities is:")
    print(path)
    distance = nx.dijkstra_path_length(G, city_1, city_2, weight=3)
    print("Distance between the given cities is:")
    print(distance)

    nx.draw(G, with_labels=True, node_color="skyblue")
    plt.show()

    connection.close()


main()
