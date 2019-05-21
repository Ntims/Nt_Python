lt = []
lt.append({'Name':'홍길동','Tel':'010-1111-0001','Dept':'그린화학과'})
lt.append({'Name':'홍길서','Tel':'010-1111-0002','Dept':'컴퓨터공학과'})
lt.append({'Name':'홍길남','Tel':'010-1111-0003','Dept':'전자공학과'})
lt.append({'Name':'홍길북','Tel':'010-1111-0004','Dept':'바이오생명공학과'})

print ("리스트 데이터")
print (lt)
print ()

print ("전체 학생 이름")
for count in range(0, len(lt)):
    print (lt[count]['Name'] + " ", end='')

print ()
print ()

print("전체 학생 명단")
for count in range(0, len(lt)):
    print (lt[count]['Name'] + " [전화번호] " + lt[count]['Tel'] + " [학과] " + lt[count]['Dept'])


print()
print("컴퓨터 공학과 학생 명단")
for count in range(0, len(lt)):
    if lt[count]['Dept'] == "컴퓨터공학과":
        print (lt[count]['Name'])
