import random as r
#5W 80 chunjyang, 66~ %up, 2 pickddul 1pickup, 4 10stack
#5character 90 chunhyang, 76~ %up, 1 pickddul 1 pickup, 4 10stack
#확률은 0.600부터 시작, %up부터 74 6.6, 76 32%~ 89까지 33%, 1회당 0.08333333333333333씩 퍼센트업
#4성 5.100%, 무기는 6.000%
#픽업과 상시 여부는 random.randint(1, 2)
#https://namu.wiki/w/%EC%9B%90%EC%8B%A0/%EA%B8%B0%EC%9B%90#s-3
"""
_rate5 = .006   # 0.6%
_rate4 = .051   # 5.1%
_pity5 = 73	    # 5* pity starts after 73 attempts
_pity4 = 8      # 4* pity starts after 8 attempts
# counter5 and counter4 are the (persistent) user state for this banner (initialize to 1)
x = random()    # between 0.0 and 1.0
prob5 = _rate5 + max(0, (counter5-_pity5) * 10 * _rate5)
prob4 = _rate4 + max(0, (counter4-_pity4) * 10 * _rate4)
if (x < prob5) {
	drop(5star)
	counter5 = 1;
	counter4 += 1
} else if (x < prob4 + prob5) {
	drop(4star)
	counter5 += 1;
	counter4 = 1;
} else {
	drop(3star)
	counter5 += 1;
	counter4 += 1;
}
"""
stack = 0
stack4 = [0, False]
stack5 = [0, False]
get = {'3W' : 0, '4PC' : 0, '4PW' : 0, '4C' : 0, '4W' : 0, '5PC' : 0, '5PW' : 0, '5C' : 0, '5W' : 0}
def clearGet():
    get = {'3W' : 0, '4PC' : 0, '4PW' : 0, '4C' : 0, '4W' : 0, '5PC' : 0, '5PW' : 0, '5C' : 0, '5W' : 0}
def PickChar1(): #캐릭뽑
    if stack5[0] == 90: #5성 천장
        if stack5[1]: #5성 확정
            print('5Star pickup')
            stack5 = [0, False]
            stack4[0] += 1
            get['5PC'] += 1
        else: #미확정
            e = r.randint(1,2)
            if e == 1: #픽업
                print('5star pickup')
                stack5 = [0, False]
                stack4[0] += 1
                get['5PC'] += 1
            else: #픽뚫
                print('5star pickddul')
                stack5 = [0, True]
                stack4[0] += 1
                get["5C"] += 1
                
                
    elif stack4[0] >= 10:
        if stack4[1]: #확정4성 스택
            print('4star pickup')
            stack4 = [0, False]
            stack5[0] += 1
            get['4PC'] += 1
        else:
            e = r.randint(1,2) #픽업여부
            f = r.randint(1,2) #캐릭터 혹은 무기
            if e == 1: #픽뚫
                if f == 1: #캐릭터
                    print('4star character')
                    stack4[0, True]
                    stack5[0] += 1
                    get['4C'] += 1
                else:
                    print('4star Weapon')
                    stack4[0, True]
                    stack5[0] += 1
                    get['4W'] += 1
            else: #픽업
                print('4star pickup')
                stack4 = [0, False]
                stack5[0] += 1
                get['4PC'] += 1
                
                
    else: #일반 가챠(확률 적용)
        firstPer = r.randint(1, 100000) #100.000
        if stack5[0] >= 74: # 확률상승
            StackValue = stack5[0] - 74
            if firstPer <= 660+(StackValue*0.08333333333333333):
                
        else: #5성 확률 상승 이전
            if firstPer<= 5100: # 5.100% 4성
                e = r.randint(1,2) #픽업여부
                f = r.randint(1,2) #캐릭터 혹은 무기
                if e == 1: #픽뚫
                    if f == 1: #캐릭터
                        print('4star character')
                        stack4 = [0, True]
                        stack5[0] += 1
                        get['4C'] += 1
                    else:
                        print('4star Weapon')
                        stack4 = [0, True]
                        stack5[0] += 1
                        get['4W'] += 1
                else: #픽업
                    print('4star pickup')
                    stack4 = [0, False]
                    stack5[0] += 1
                    get['4C'] += 1
            elif firstPer >= 9400: #0.600% 5성
                if stack5[1]: #5성 확정
                    print('5Star pickup')
                    stack5 = [0, False]
                    stack4[0] += 1
                    get['5PC'] += 1
                else: #불확정
                    e = r.randint(1,2)
                    if e == 1: #픽업
                        print('5star pickup')
                        stack5 = [0, False]
                        stack4[0] += 1
                        get['5PC'] += 1
                    else: #픽뚫
                        print('5star pickddul')
                        stack5 = [0, True]
                        stack4[0] += 1
                        get['5C'] += 1
            else: #3성
                print('3star Weapon')
                stack4[0] += 1
                stack5[0] += 1
                get['3W'] += 1
        
        
#value = input('kind of gacha(W/character) : ')
#if value == "character":
    




















































