import torch as t

def line():
    print("--------------------")

x = t.tensor([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(x[0]) #first element
print(x[-1]) #last element
print(x[0:3]) #first 3 elements
print(x[3:]) #all elements from index 3 onwards
print(x[::2]) #all elements with a step of 2


y = t.tensor([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(y[0]) #first row
print(y[0][1]) #first row, second column
print(y[:,0]) #all rows, first column
print(y[0,:]) #first row, all columns
print(y[1,2]) #second row, third column
print(y[1][2])
print(y[0:2,0])