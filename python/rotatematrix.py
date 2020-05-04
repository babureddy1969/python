def rotateMatrixByK(matrix, K) :

    p = 0# start row index
    m = len(matrix)# end row index

    q = 0# start column index
    n = len(matrix[0])# end column index

    temp = []
    tempIndx = 0
    start = 0
    end = 0

    while (p < m and q < n) :

        #copy first row of matrix
        for  i in range( q, n) :
            temp[tempIndx] = matrix[p][i]
            tempIndx+=1
            end+=1

        p+=1

        # copy last column of matrix
        for i in range( p, m) :
            temp[tempIndx] = matrix[i][n - 1]
            tempIndx+=1
            end+=1

        n-=1

        # copy last row of matrix
        if (p < m) :
            for i in range( n - 1, q+1 ) :
                temp[tempIndx] = matrix[m - 1][i]
                tempIndx+=1
                end+=1
            m-=1

        # copy first column of matrix
        if (q < n) :
            for i in range(m - 1, p, -1):
                temp[tempIndx] = matrix[i][q]
                tempIndx+=1
                end+=1
            
            q+=1


        if (end - start > K) :
            # rotate array by K elements using reversal algorithm
            reverse(temp, start, start + K - 1)
            reverse(temp, start + K, end - 1)
            reverse(temp, start, end - 1)
            # after rotation for next ring reset the start
            start = end
        else :
            # array is less than reversal capacity break the loop
            break

    return temp

def reverse(array, start, end) :
    while (start <= end) :

        temp = array[start]
        array[start] = array[end]
        array[end] = temp

        #// array[start] ^= array[end];
        #// array[end] ^= array[start];
        #// array[start] ^= array[end];

        start+=1
        end-=1
	
def fillSpiral(array, temp ,  M,  N):
		
    #//rows
    p = 0
    m = M
    
    #//columns
    q = 0
    n = N
    
    indx = 0
    
    while( p < m and q < n):
        #//fill first row
        
        for i in range (q , n ):
            array[p][i] = temp[indx]
            indx+=1
        p+=1
        
        #//fill last column
        for i in range (p ,  m ):
            array[i][n-1] = temp[indx]
            indx+=1
        n-=1
        
        #//fill last row
        if(p < m):
            for i in range (n-1 , q, -1):
                array[m-1][i] = temp[indx]
                indx+=1
        m-=1        
        #//fill first column
        if(q < n):
            for i in range (m-1 , p ,-1):
                array[i][q] = temp[indx]
                indx+=1
        q+=1
def display(m):
    for i in range(len(m)):
        print(m[i])			
matrix= [[ 2, 3, 4, 6 ], [ 6, 7, 8, 9 ], [ 2, 9, 4, 2 ],
            [ 3, 7, 5, 2 ]]

display(matrix)
m=rotateMatrixByK(matrix,1)
    
fillSpiral(matrix,m,4,4)
