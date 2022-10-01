'''
1.Get a file name and a default value as input
2.Read the data and save them to a list The null value must be filled with default value.
3.The first line in the input file is column number.
4.You must check if the input is vaild or not

사용: 파일입출력, 예외처리
'''
import numpy as np

try:
    filename=input("파일 이름을 입력하세요:")#input.txt
    default_value=int(input("default value:"))
    f=open(filename,"r")
except FileNotFoundError:
    print("파일명을 확인하세요.")
else:
    col=int(f.readline())#7
    array=[]

    while True:
        line = f.readline()  # ['1', ' 3', ' 5', ' 6.1', ' 7', ' 0\n']
        if not line:
            break

        else:
            line = line.split(",")
            if len(line) != col:
                list = []
                for l in line:
                    if l != "":  # 공백이 아닌경우
                        list.append(eval(l.replace("\n", "")))
                    elif l == "":
                        list.append(default_value)
                while len(list) < col:
                    list.append(default_value)
                array.append(list)


    #print(array)
    '''
    [[1, 3, 5, 6.1, 7, 0, 5],
    [4, 5, 5.9, 5, 5.1, 4, 5],
    [5, 4.0, 3.1, 2.1, 5, 5, 5]]
    '''

#(1) show the average of diagonal: in the position of (x,x),Round down to 1st decimal place
total=0
row=len(array)
for i in range(row):
    total+=array[i][i]
    avg=round(total/row,1)
#print(avg)#3.0

#(2) Get a column number in [1,7], show the column menbers. convert the list to numpy array

num_array=np.array(array,)

try:
    input_col = int(input("col number:"))
    print(num_array[:, [input_col - 1]])
except IndexError:
    print(f"1열~{col}열 범위에서 선택하세요.")

#(3) Get a cut value as input and display the array with the above values of the cut
#Convert the list to a numpy array and utilze the numpy module,where

try:
    cut=eval(input("cut:").strip())
except NameError:
    print("숫자를 입력하세요")
else:
    result_arr=np.where(num_array>3.5,num_array,0)
    print(result_arr)








