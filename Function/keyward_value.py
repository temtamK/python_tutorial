def profile(name, age, main_lang):
	print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
		.format(name, age, main_lang))

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", name="유재석", age=25)
