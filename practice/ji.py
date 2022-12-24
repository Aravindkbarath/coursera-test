# def what(matrix,m,n):
#     if (m==n and m%2!=0):
#         count = 0
#         t = int((m-1)/2)
#         # print(t)
#         for i in range(m):
#             for j in range(n):
#                 # print(i,j)
#                 # print(matrix[i][j])
#                 # print(matrix[t][t])
#                 if (matrix[i][j] == matrix[t][t]):
#                     count+=1
#         print(count)

# what([[1,2,3],[1,2,3],[1,2,3]],3,3)

def countOdd(array):
    count = 0
    for i in array:
        if i%2 != 0:
            count+=1
    
    print(count)
countOdd([1,2,3,4,5])