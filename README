                              AI Developer Test
                                    by
                               Harsha Renkila  
                              Integrated Mtech
                           University of Hyderabad
---------------------------------------------------------------------------------------------------

Program Usage:

python3 test_file.py
output : 1) Given structure of platform in Matrix
         2) Maximum Water strored in platform

- zero_test.py is the file where WaterStoredInPlatform is defined

if you want to provide a new test case provide as a list as row major elements and provide its dimensions. 

---------------------------------------------------------------------------------------------------


Approach For Solving:-
---------------------------------------------------------------------------------------------------

-Since the platform is an 2D array the water has 4 ways to flow. If the 4 Ways is blocked and bottom cube is there then the water will store.

-So we have to check the maximum storage from 4 directions.
i,e, From Left,
     From Right,
     From Top,
     From Bottom,

1)How to find Maximum  strorage from Direction?

a)Start from one end and move on to next cell untill the end 
if next cell < present cell 
   next cell = present cell

2)How to handle with the zero cells(holes) in platform ?

a)If a Cell has hole then go to next cell and if that next cell is less than minof two extremes in a particular direction make that next cell as a hole until we find the cell value greater than min of two extremes.

if(next cell < max(left extereme,right extreme))
   next cell = 0

-For a particular storage of cell we have find the minimum of Left,Right,Top,Bottom of a particular storage cell. By the addition of individual cells value we can get maximum storage.If a individual cell is zero the skip the cell.

-By adding all individual values we get final Maximum storage of water.
---------------------------------------------------------------------------------------------------
