score=[95,80,99,93,22,48,53,35,59,66]
grade=[]

def getGrade(score):
    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D+"
    elif score >= 60:
        return "D"
    else :
        return "F"

for i in range(10):
    grade.append(getGrade(score[i]))
    print("%s %s" %(score[i], grade[i]))
