#퀴즈 4

from random import*
lst=range(1,21)
lst=list(lst)

winners=sample(lst,4)

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")


#퀴즈 5
from random import*
cnt = 0
for i in range(1,51): 
    time=randrange(5,51)
    if 5<=time<=15:
        print("[O]] {0}번째 손님 (소요시간 : {1}분".format(i,time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,time))

print("총 탑승 승객 : {0}분".format(cnt))