#Tuple Unpacking: Given a tuple with three elements (x, y, z), write a Python program to unpack the tuple and assign the values to three variables.
tuple01 = ('Malon','Mango','Strawberry')
tuple02 = ('Malon','Mango','Strawberry','Banana','Apple')

(x,y,z) = (tuple01)
(u,v,*w) = (tuple02)

print(x)
print(y)
print(z)
print(u)
print(v)
print(w)