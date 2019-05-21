while True:
    dualnum = int(input("양수 입력(3보다 작으면 종료)"))
    if dualnum < 3:
        print("프로그램을 종료합니다.")
        break
    else:
        check = False

        for i in range(2,dualnum):
            if dualnum % i == 0:
                print(dualnum, "는 소수가 아니다")
                check = True
                break

        if check == False:
            print(dualnum, "는 소수이다.")
