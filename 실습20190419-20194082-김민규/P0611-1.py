dan = 1
while dan <= 9:
    num = 1
    while num <= 9:
        print("%d*%d=%d" % (dan, num, (dan * num)))
        num = num + 1
    dan = dan + 1
    print()
