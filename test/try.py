for i in range(5):
	try:
		print(i/0)
	except ZeroDivisionError as e:
		print(e, "--> Divsion by 0 is not alloed.")
		
