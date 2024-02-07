import numpy as np

print("ques 1")
arr = np.array([1, 2, 3, 6, 4, 5])
print(arr[::-1])

print("ques 2")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])
# print(arr1 == arr2)
print(np.array_equal(arr1,arr2))

print("ques 3")
import collections
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1,1,1,2,3,4,2,4,3,3]) 
d={"num":0,"occur":0}
c=collections.Counter(x)
max=0
for i in (c.keys()):
    if c[i]>max:
        max=c[i]
        d["num"]=i
print(d["num"])

print("ques 4")
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
print("Sum all elements",np.sum(gfg))
print("Sum all elements (Column)",np.sum(gfg,axis=0))
print("Sum all elements (Rows)\n",np.sum(gfg,axis=1))
