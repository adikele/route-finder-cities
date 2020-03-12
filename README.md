# route-finder-cities
Program finds the shortest distance between two cities 


@Aditya Kelekar
Project Overview:
This is a hobby project to find the shortest route from one city to another. 
Distances between a few cities is fed into a database; these distances are obtained from the Internet and may not be accurate.
The project demonstrates how the capabilities of Networkx library can be used in finding the shortest route.

Description:
Program finds the shortest distance between two cities selected by the user. 
Names of a few cities and distances between them is fed to a sqlite database. 
This data is subsequently represented as a Networkx graph, with cities as nodes. 
Networkx library's Dijkstra function is then used to find the shortest path, which is printed out. 
A graph of the cities is also displayed, but this does not currently show the shortest path.

Libraries used:
matplotlib 3.1.3  
networkx 2.4    
numpy 1.18.1  
pandas 1.0.1  


Development points:
1. Display the shortest route on the graph
2. Use a database with more popularity such as PostgreSQL 
3. Use an online database of geographical locations of 
cities and calculate distances between required cities
4. Provide a web interface to the program.
