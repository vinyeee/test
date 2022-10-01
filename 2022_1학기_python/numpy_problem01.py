'''
problem 01
get a positive integer n as input
print out n*n matrix with the following pattern using numpy

'''
import numpy as np

#0과 1을 반복하는 nxn 행렬을 반환하는 함수
def n_by_n_matrix():
    n = int(input("positive integer n:"))
    mat = np.zeros((n, n), dtype=np.int32)
    for i in range(n):
        for j in range(n):
           mat[i,j]=(i+j+1)%2
    return mat



def print_line():
    print("-------------------------------------------------------------------------------")

def print_result(data):
    print_line()
    print("0과 1을 반복하는 nxn 행렬: ", data)
    print_line()


data=n_by_n_matrix()
print_result(data)