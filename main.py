import random

_rate5 = .006   # 0.6%
_rate4 = .051   # 5.1%
_pity5 = 73	    # 5* pity starts after 73 attempts
_pity4 = 8      # 4* pity starts after 8 attempts
stack = 0
stack4 = [0, False] # stack of 4 star
stack5 = [0, False] # stack of 5 star
get = {'3W' : 0, '4PC' : 0, '4PW' : 0, '4C' : 0, '4W' : 0, '5PC' : 0, '5PW' : 0, '5C' : 0, '5W' : 0}
def clearGet():
    global get
    get = {'3W' : 0, '4PC' : 0, '4PW' : 0, '4C' : 0, '4W' : 0, '5PC' : 0, '5PW' : 0, '5C' : 0, '5W' : 0}
prob5, prob4, x = 0,0,0
def setPer():
    global x, prob5, prob4
    x = random.randint(1, 10) * 0.01 # between 0.0 and 1.0
    prob5 = _rate5 + max(0, (stack5[0]-_pity5) * 10 * _rate5)
    prob4 = _rate4 + max(0, (stack4[0]-_pity4) * 10 * _rate4)
def pickUp():
    if (x < prob5):
        print("5star")
        get['5C'] = get['5C'] + 1
        stack5[0] = 0
        stack4[0] += 1
    elif (x < prob4 + prob5):
        print("4star")
        get['4C'] = get['4C'] + 1
        stack5[0] += 1
        stack4[0] = 0
    else:
        print("3star")
        get['3W'] = get['3W'] + 1
        stack5[0] += 1
        stack4[0] += 1
def printResult():
    print(
        f"""
        5 star List[
            character : {get['5PC'] + get['5C']}
            weapon : {get['5PW'] + get['5W']}
        ]
        4 star List[
            character : {get['4PC'] + get['4C']}
            weapon : {get['4PW'] + get['4W']}
        ]
        3 star : {get['3W']}
    """
    )