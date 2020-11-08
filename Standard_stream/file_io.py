# utf8 인코딩 지정 권장
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close

# a는 append의 약자, 기존 파일에 내용을 이어쓴다.
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
# write()에는 줄바꿈이 포함되어 있지 않아서 줄바꿈을 명시해줘야한다.
score_file.write("\n코딩 : 100")
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
print(score_file.readline()) #줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
	line = score_file.readline()
	if not line:
		break
	print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
	print(line, end="")
score_file.close()
