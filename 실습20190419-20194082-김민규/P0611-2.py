dan = 1
while dan <= 9:
    num = 1
    while num <= 9:
        print("%d*%d=%d" %(num, dan, (dan * num)), end = "\t")
        num = num + 1
    dan = dan + 1
    print()
