print("Введите параметры согласно формуле ax^2 + bx + c = 0 ")

a = float(input("a << "))
b = float(input("b << "))
c = float(input("c << "))

D = b**2-4*a*c

print(D)
if D > 0: 
	print("\nУравнение имеет 2 корня: ")
	D = D**(0.5)
	print("x1 = " + str((-b+D)/(2*a)))
	print("x2 = " + str((-b-D)/(2*a)))
elif D == 0:
	print("\nУравнение имеет 1 корень:\nx = " + str(-b/2*a))
elif D < 0: 
	print("\nУравнение не имеет корней")