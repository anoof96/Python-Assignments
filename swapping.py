a = 10
b = 20
temp = a
a = b
b = temp
print(a)
print(b,"\n")

#or

a = 10
b = 20
a = a + b #10 + 20
b = a - b #30-20
a = a - b #30-10
print(a)
print(b,"\n")

#or

a, b = b, a
print(a)
print(b)