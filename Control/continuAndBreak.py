absent = [2, 5] # �Ἦ
no_book = [7]
for student in range(1, 11): # 1 ~ 10
	if student in absent:
		continue
	elif student in no_book:
		print("���� ���� �������. {}�� �����Ƿ� �����".format(student))
		break
	print("{}, å�� �о��".format(student))
