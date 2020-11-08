# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# 	# print문에 end=를 넣으면 print 문이 끝나고 줄바꿈을 하지 않고 end값이 출력된다.
# 	print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
# 	print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
	print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
	for lang in language:
		print(lang, end=" ")
	print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 26, "Kotilin", "Swift", "", "", "")
