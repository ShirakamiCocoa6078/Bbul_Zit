import random as r
"5weapon 80 chunjyang, 66~ %up, 2 pickddul 1pickup, 4 10stack"
"5character 90 chunhyang, 76~ %up, 1 pickddul 1 pickup, 4 10stack"
#확률은 0.600부터 시작, %up부터 76 32%~ 89까지 33%, 1회당 0.08333333333333333씩 퍼센트업
#4성 5.100%, 무기는 6.000%
#픽업과 상시 여부는 random.randint(1, 2)
#https://namu.wiki/w/%EC%9B%90%EC%8B%A0/%EA%B8%B0%EC%9B%90#s-3
stack = 0
4stack = [0, False]
5stack = [0, False]
def clearGet():
    get = {'3weapon' = 0, '4pickCharacter' = 0, '4pickWeapon' = 0, '4character' = 0, 
    '4weapon' = 0, '5pickCharacter' = 0, '5pickWeapon' = 0, '5character' = 0, '5weapon' = 0}
def PickChar1():
    if 5stack[0] == 90: #5성 천장
        if 5stack[1]:
            print('5Star pickup')
        else:
            e = r.randint(1,2)
            if e == 1:
                print('5star pickup')
            else:
                print('5star pickddul')
    elif 4stack[0] == 10:
        if 4stack[1]:
            print('4star pickup')
        else:
            e = r.randint(1,2)
            f = r.randint(1,2)
            if e == 1:
                if f == 1:
                    print('4star character')
                    
                    
#===========================================================여기 하다 말았음
    firstPer = r.randint(1, 100000)
    if firstPer<= 5100:#4성
        
        
        
value = input('kind of gacha(weapon/character) : ')
if value = "character":
