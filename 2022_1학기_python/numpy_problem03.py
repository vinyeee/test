'''
problem 03
get two arrays, A and B, as input

Test each element in A: if the element in A is also in B,
True.Else false


'''
import numpy as np


#가능한 모든 모양의 2차원 행렬을 반환하는 함수

def test_matrix():
    A = input("A(a,b,...)")
    arr1 = np.array([int(a) for a in A.split(",")])
    B = input("B(a,b,...)")
    arr2 = np.array([int(b) for b in B.split(",")])
    print(f"array A:{arr1}")
    print(f"array B:{arr2}")
    result=[]
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            result.append(True)
        else:
            result.append(False)
    print(np.array(result))
'''
테스트 출력 
A(a,b,...)0,10,20,40,60,80
B(a,b,...)0,20
array A:[ 0 10 20 40 60 80]
array B:[ 0 20]
[ True False  True False False False]

'''


def print_line():
    print("-------------------------------------------------------------------------------")

def print_result():
    print_line()
    print("테스트 출력 ")
    test_matrix()
    print_line()


print_result()