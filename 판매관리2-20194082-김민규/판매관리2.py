items = {}
f_open = open('items.txt','r')
items = eval(f_open.read())

def printItem(key):
    print("가격=",list(items.values())[key][0],
    "\t판매량=", list(items.values())[key][1],
    "\t재고=", list(items.values())[key][2])

def statusprint(key):
    return (list(items.keys())[key])

def printKey():
    for key in items.keys():
        print(key)

def saleFunc():
    printKey()
    key = input("판매한 물품은?")
    if key in items.keys():
        print(key, end="\t")
        print("가격=",items[key][0],
        "\t판매량=", items[key][1],
        "\t재고=", items[key][2])
        amount = int(input("판매한 수량은?"))
        if amount > items[key][2]:
            print("판매한 수량이 재고보다 많습니다. 입력할 수 없습니다")
        else:
            items[key][2] = items[key][2] - amount
            items[key][1] = items[key][1] + amount
            print(key, end="\t")
            print("가격=",items[key][0],
            "\t판매량=", items[key][1],
            "\t재고=", items[key][2])
    else:
        print("판매하지 않는 물품입니다.")

def save():
    s_items = open('items.txt', 'w')
    test = f_items.write(str(items))
    s_items.close()
    print ("저장이 완료 되었습니다.")

def add():
    cmd = input("추가할 물품에 대한 정보를 입력하시오. ex)커피 3000 5 10 >> ")
    cmd = cmd.split(' ')
    items[cmd[0]] = [int(cmd[1]), int(cmd[2]), int(cmd[3])]

def items_input():
    cmd = input("입고할 물품과 수량을 입력하시오. ex)커피 5 >> ")
    cmd = cmd.split(' ')
    tmp = items[cmd[0]]
    tmp[2] += int(cmd[1])

def change():
    cmd = input("변경할 물품과 단가를 입력하시오. ex)커피 2000 >> ")
    cmd = cmd.split(' ')
    tmp = items[cmd[0]]
    tmp[0] = int(cmd[1])

while True:
    cmd = input("명령을 입력하시오(중지, 출력, 판매, 저장, 추가, 입고, 변경) : ")
    if cmd == "중지":
        print("재고관리 프로그램을 중지합니다.")
        break
    elif cmd == "출력":
        for i in range(0, len(items)):
            print(statusprint(i), end="\t")
            printItem(i)
    elif cmd == "저장":
        save()
    elif cmd == "추가":
        add()
    elif cmd == "판매":
        saleFunc()
    elif cmd == "입고":
        items_input()
    elif cmd == "변경":
        change()
    else:
        print("적합하지 않은 명령입니다.")
