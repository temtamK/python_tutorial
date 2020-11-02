menu = ("돈까스", "치즈까스", "생선까스")
print(menu[0])
print(menu[1])

#튜플은 add를 지원하지 않는다

(name, age, hobby) = ('김종국', 20, '코딩')
print(name, age, hobby)

# 인덱싱
menu[0]

# 슬라이싱
menu[1:] #치즈까스, 생선까스 출력

# 튜플 더하기
menu2 = ("된장국", "김치찌개")
print(menu + menu2)

# 튜플 곱하기
print(menu * 3) # menu의 값이 순서대로 3번 출력됨

# 튜플 길이
print(len(menu))

# 요소를 지울 때
del menu[0]
