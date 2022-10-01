'''
problem 02
get a positive integer n as input
-must check if the input is vaild or not

Display all possible 2-d matrix by reshape with the number of elementx,1, from 1 to n


'''
import numpy as np


#가능한 모든 모양의 2차원 행렬을 반환하는 함수
def _2d_matrix():
    try:
        n = int(input("A positive integer n:"))
        for i in range(1,n+1):
            if n%i==0:
                print(i,n)
                print(f"Shape ({i},{int(n/i)}):")
                print(np.ones((i,int(n/i)),dtype=np.int32))

    except ValueError as e:
        print("양수를 입력하세요.")






def print_line():
    print("-------------------------------------------------------------------------------")

def print_result():
    print_line()
    print("가능한 모든 모양의 2차원 행렬: ")
    _2d_matrix()
    print_line()

print_result()


