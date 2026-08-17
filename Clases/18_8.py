def sumar(a,b):
	c = a + b
	if (a > b):
		a = a + 10
		c = a + b
	return c;
print(sumar(10,20))
