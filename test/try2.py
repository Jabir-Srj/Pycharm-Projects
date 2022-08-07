for i in  range(5):
	try:
		print(i/1)
	except NameError:
		print("Division by 0 is just wrong!")
	print("The rest of the code...")
