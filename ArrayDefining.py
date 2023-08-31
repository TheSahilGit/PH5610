import numpy as np

# Examples of defining.

a0 = np.zeros([3,1])
a1 = np.ones([3,1])
a2 = np.random.rand(3,2)
a3 = np.array([1,2,3,4,5,6,7,8,9,10])
a4 = np.arange(10)
a5 = np.array([1, 2, 3, 4], ndmin=2)
a6 = np.linspace(0,10,11)
a7 = np.array([[1,2],[3,5]])
a8 = np.array([[4,6],[2,9]])



# Examples of different operations.

con = np.concatenate([a1,a2], axis=1)
s = np.sum(a0)
p = np.multiply(a4,a4)
tran = np.transpose(a2)
matmul = np.matmul(a7,a8)
normmul = np.multiply(a7,a8)




print(a7)
print(a8)
print(matmul)
print(normmul)



# for r in a7:
#     print(r)

# for r in a8:
#     print(r)


#print(np.shape(con))
#print(np.shape(a6))
#print(np.shape(a0))
#print(np.shape(tran))
# print(a2)
# print(tran)
#print(np.shape(a7))