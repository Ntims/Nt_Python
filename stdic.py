items = {"커피" : [3000,5,10], "펜" : [1000,10,20], "종이컵" : [20,1050,550], "우유" : [500,10,5], "콜라" : [1050,22,10]}

def printItem():
    for key in items.values():
        print("가격=", key[0], "\t 판매량=", key[1], "\t 재고=", key[2])

def statusPrint():
    for key in items.keys():
        print(key)

while True:
    cmd = input("명령을 입력하시오(중지,출력):")
    if cmd == "중지":
        print("재고관리 프로그램을 중지합니다.")
        break
    elif cmd == "출력":
        print(statusPrint(),printItem())

    else:
        print("적합하지 않은 명령입니다.")
