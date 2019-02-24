import numpy as np


def WaterStoredInPlatform(platform):
    rows,columns = platform.shape
   
   # Define matrices from 4 sides to find maximum storage from each side
    right = np.zeros((rows,columns))
    left  = np.zeros((rows,columns))
    top = np.zeros((rows,columns))
    bottom = np.zeros((rows,columns))

    #intialize water storage
    water = 0
 


    print(platform)

    # Fill  max storage from left
    left[:,0] = platform[:,0]
    for i in range( 0, rows): 
        for j in range(1,columns):
            if( platform[i][j]==0):
                for k in range(j+1,columns):
                    p = min(platform[i][j-1],platform[i][-1])
                    if(platform[i][k]<p):
                        platform[i][k]=0
                    else:
                        break
            else:

                left[i][j] = max(left[i][j-1], platform[i][j])

  
    
    # Fill  max storage from right
    right[:,-1] = platform[:,-1]
    for i in range( 0, rows):
        for j in range(columns-2, -1, -1): 
            if( platform[i][j]==0):
                for k in range(columns-j,-1,-1):
                    p = min(platform[i][j+1],platform[i][0])
                    if(platform[i][k]<p):
                        platform[i][k]=0
                    else:
                        break
            else:

                right[i][j] = max(right[i][j+1], platform[i][j])


    # Fill  max storage from top 
    top[0,:] = platform[0,:]
    for i in range( 0, columns): 
        for j in range(1,rows):
            if( platform[j][i]==0):
                for k in range(j+1,rows):
                    p = min(platform[j-1][i],platform[-1][i])
                    if(platform[k][i]<p):
                        platform[k][i]=0
                    else:
                        break
            else:

                top[j][i] = max(top[j-1][i], platform[j][i])
 

    # Fill  max storage from bottom 
    bottom[-1,:] = platform[-1,:]
    for i in range( 0, columns):
        for j in range(rows-2, -1,-1):
            if( platform[j][i]==0):
                for k in range(rows-j,-1,-1):
                    p = min(platform[j+1][i],platform[0][i])
                    if(platform[k][i]<p):
                        platform[k][i]=0
                    else:
                        break
            else:

                bottom[j][i] = max(bottom[j+1][i], platform[j][i])


    # Calculate the accumulated water element by element 
    # the amount of water accumulated on this particular 
    # bar will be equal to min(left[i][j], right[i][j],top[i][j],bottom[i][j[]) - platform[i][j] .



    for i in range(1,rows):
        for j in range(1,columns):
            if( platform[i][j]!=0):
                water += min(left[i][j],right[i][j],top[i][j],bottom[i][j]) - platform[i][j] 
  
    return water 
  


                   
