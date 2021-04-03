''' 사이트별로 비밀번호를 만들어 주는 프로그램
1 http://부분은 제외
2 .이후 부분 제외
3 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e갯수+ !
'''

site="http://naver.com"
pw1=site[7:-4]
pw2=pw1[0:3]
pw3=len(pw1)
pw4=pw1.count("e")

print(pw2 + str(pw3) + str(pw4) + "!")


