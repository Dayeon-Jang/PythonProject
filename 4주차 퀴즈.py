'''
남자:키*키*22
여자:키*키*21

함수명 std_Weight
전달값 키 height 성별 gender

소수점 둘째자리까지
'''

def std_Weight(height,gender):
    if gender == "m":
        print("키",round((height*100)),"cm 남자의 표준 체중은",round((height*height*22),2),"입니다.")
        
    else:
        print("키",round((height*100)),"cm 여자의 표준 체중은",round((height*height*21),2),"입니다.")

std_Weight(1.75,"m")

