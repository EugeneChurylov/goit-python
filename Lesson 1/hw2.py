a = float(input("Enter 'a': "))
b = float(input("Enter 'b': "))
c = float(input("Enter 'c': "))

d = (b**2) - (4*a*c)

x1 = (-b + d**0.5) / 2*a
x2 = (-b - d**0.5) / 2*a

print('x1 = {0}; x2 = {1}'.format(x1, x2))