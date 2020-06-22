
import numpy as np

data1 = np.array([[2,3,4],[4,2,1],[7,8,9]])
data2 = np.array([[1,2,3],[9,8,7],[4,5,6]])
print("Largest number of the set1 = {} ".format(np.argmax(data1)))
print("Largest number of the set2 = {} ".format(np.argmax(data2)))

print("\n Numpy Array")
print("\n Matrice A \n",data1)
print("\n Matrice B \n",data2)

trans1 , trans2 = data1.T , data2.T 
addition = trans1+trans2
print("\n Transpose Matrice1 \n" , trans1)
print("\n Transpose Matrice2 \n" , trans2)
print("\n ----------------------------")
print("\n Addition of Transpose Matrices \n" , addition)

print("\n After Sum Matrices A & B: \n")
print(np.add(data1,data2))
print("\n After Subtract Matrices A & B: \n")
print(np.subtract(data1,data2))
print("\n After Multiply Matrices A & B: \n")
print(np.multiply(data1,data2))

tn = np.array([[5,2,1],[7,9,5],[1,8,2]])
print("\n Original Matrice: \n" , tn)

tp = tn.T 
print("\n Tranpose Matrice \n" , tp)
print("\n Sum of 3 in tranpose Matrice \n" , np.array([3]) + tp)

z = np.array([3, 6 ,1])
print("Largest number of the set z = {} ".format(np.argmax(z)))
transpose = z.T
print("Largest number of the transpose set z = {} ".format(np.argmax(transpose)))
print("\n Original Matrix 1 x 1" , z)
print("\n Transpose Matrix 1 x 1")
print()
print(transpose)

a = np.array([1])
print()
print(a)
print()
print ("\n Sum transpose and single dimension matrice")
print()
print(transpose+a)

dictonary = np.array(['A','E','F','C','B','D'])
dict1 = np.array(['A','B','C','D','E','G'])
dict2 = np.array(['A','B','A','D','B','A'])
print("\n Dictonary : {}".format(dictonary))
transposeDictonary = dictonary.T

print("Transpose Dictonary: " , transposeDictonary)
# print("Sum Transpose Dictonary: " , sumTransposeDictonary)

sortDictonary = np.sort(dictonary)
print("\n Sorted Dictonary : {}".format(sortDictonary))
unsort= np.array([2,5,1,8,3,4,9,6,7])
#print(type(sort))
print("\n Unsorted Array" , unsort)
sorted = np.sort(unsort)
print("\n Sorted Array" , sorted)

intersect = np.intersect1d(dict1 , dict2)
union = np.union1d(dict1 , dict2)
setdiff = np.setdiff1d(dict1 , dict2)
ind = np.in1d(dict1,dict2)

print("\n Intersection \n " , intersect)
print("\n Union \n " , union)
print("\n SetDiff \n " , setdiff)
print("\n In1d \n " , ind)

uniqueFunction = np.array([5,1,4,2,3,9,7,8,6])
print("\n Unique Numbers : " , np.unique(uniqueFunction))

random = np.random.random([3,4])
print("\n Random Numbers")
print(random)