"""
표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
	남자 : 키(m) * 키(m) * 22
	여자 : 키(m) * 키(m) * 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
	* 함수명 : std_weight
	* 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

height = int(input("키는? : "))
gender = input("성별은? : ")

def std_weight(height, gender):
	if gender == '남자':
		standard = height * height * 22
	elif gender == '여자':
		standard = height * height * 21
	return standard

standard = round((std_weight(height, gender)  / 10000), 2)
print("표준 체중은 {0}kg입니다.".format(standard))
