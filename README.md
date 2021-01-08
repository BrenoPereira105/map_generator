# map_generator
This code is based on the algorithm of the wave function collapse for a map generation. Here we start with a 2d grid 'A'. Each entry is in a superpostion of states 0,1,2, which is represented as a 3d grid. In this map, 0 = water(blue), 1 = sand(green) and 2 = land(brown).

For the first element we randomly chose a state and propagate this information to the neighbourhoods. To do this we follow adjacency rules such that:

-if entry = 0, then neighbourhoods = 0 or 1

-if entry = 1, then neighbourhoods = 0 or 1 or 2

-if entry = 2, then neighbourhoods = 1 or 2

In other words, we always have the neighbourhoods <water+sand> and <sand+land>, but never <water+land>.

The algorithm goes line by line and row by row propagating the information, while randomly choosing new values. In the end we pass the final states in the 3d grid 'A' to a 2d grid 'B' and plot the result.

To run the code the user must run in the terminal >python3 map.py size_num, where size_num is the number of the square map (size_num X size_num).
