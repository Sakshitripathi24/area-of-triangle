# area of triangles with sides

a = int(input("enter the length of first side: "))
b = int(input("enter the length of second side: "))
c = int(input("enter the length of third side: "))

p = (a+b+c)
s = p/2

area = (s*(s-a)*(s-b)*(s-c)**0.5)

print("area of triangle is: ",area)
print("paramater of the triangle is: ",p)
print("semi of triangle is: ",s)