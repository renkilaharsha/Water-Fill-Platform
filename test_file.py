import numpy as np
from  zero_test import WaterStoredInPlatform

#case 1
plat=[2,2,2,2,2,2,2,2,2]
platform = np.array(plat).reshape((3,3))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 2
plat = [5,5,5,5,5,9,1,1,1,5,5,1,5,1,5,5,1,1,1,5,5,5,5,5,5]
platform = np.array(plat).reshape((5,5))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 3 
plat = [3,3,3,3,3,3,3,1,2,3,1,3,3,1,2,3,1,3,3,3,3,1,3,3]
platform = np.array(plat).reshape((4,6))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 4
plat = [2,2,2,2,2,1,2,1,2,2,2,1]
platform = np.array(plat).reshape((3,4))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 5
plat=[4,4,4,4,4,4,3,6,3,4,4,6,0,6,4,4,3,6,3,4,4,4,4,4,4]
platform = np.array(plat).reshape((5,5))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 6
plat=[4,4,4,4,4,4,0,6,3,4,4,6,1,6,4,4,3,6,3,4,4,4,4,4,4]
platform = np.array(plat).reshape((5,5))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 7
plat = [3,3,3,3,5,3,3,0,2,3,1,3,3,1,2,3,1,3,3,3,3,1,3,3]
platform = np.array(plat).reshape((4,6))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 8
plat = [3,3,3,3,5,3,3,0,2,3,1,3,3,1,2,3,0,3,3,3,3,1,3,3]
platform = np.array(plat).reshape((4,6))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))

#case 9 
plat=[1,2,1,2,2,2,1,2,1]
platform = np.array(plat).reshape((3,3))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))


#case 10 
plat=[4,4,4,4,4,4,4,4,1,1,1,1,1,4,4,1,4,4,4,1,4,4,1,4,1,4,1,4,4,1,4,4,4,1,4,4,1,1,1,1,1,4,4,4,4,4,4,4,4]
platform = np.array(plat).reshape((7,7))
print("Maximum Water stroted in Platform: ",WaterStoredInPlatform(platform))
