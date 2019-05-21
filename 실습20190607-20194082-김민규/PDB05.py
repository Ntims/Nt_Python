import sqlite3

connect = sqlite3.connect("sales.db")

if (connect):
    print("성공적으로 sales.db 를 열었습니다.")
else:
    print("sales.db 를 여는데 실패했습니다.")
    exit()

cursor = connect.cursor()

cursor.execute("select * from saleitems")
rows = cursor.fetchall()

print(rows)

for row in rows:
    print("%s\t가격=%-4d \t판매량=%-4d \t재고=%-3d" % (row[1], row[2], row[3], row[4]))

connect.close()
