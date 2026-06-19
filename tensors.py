import torch

def line():
    print("--------------------")



#scalar - 0D tensor 
x = torch.tensor(5)
print(x)
print(x.ndim)
print(x.shape)

line()

#vector - 1D tensor
y = torch.tensor([1,2,3])
print(y)
print(y.ndim)
print(y.shape)

line()

#matrix - 2D tensor
z = torch.tensor([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(z)
print(z.ndim)
print(z.shape)

line()

#tensor - 3D tensor
a = torch.tensor([[[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                  [[10,11,12],
                   [13,14,15],
                   [16,17,18]],
                  [[19,20,21],
                   [22,23,24],
                   [25,26,27]]])
print(a)
print(a.ndim)
print(a.shape)

line()

#commonly used tensors
#zeros
zeros = torch.zeros(3,4)
print("zeroes = ",zeros)
#ones
ones = torch.ones(3,4)
print("ones = ",ones)
#eye
eye = torch.eye(5)
print("eye = ",eye)
#rand
rand = torch.rand(3,4)
print("rand = ",rand)
#randn
randn = torch.randn(3,4)
print("randn = ",randn)
#arange
arange = torch.arange(0,10,2)
print("arange = ",arange)

