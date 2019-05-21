import sqlite3

connect = sqlite3.connect("sales.db")

if(connect):
    print("성공적으로 sales.db 를 열었습니다.")
else:
    print("sales.db 를 여는데 실패했습니다.")
    exit()

connect.row_factory = sqlite3.Row

cursor = connect.cursor()

cursor.execute("select * from saleitems")
rows = cursor.fetchall()

for row in rows:
    print("%s\t가격=%-4d \t판매량=%-4d \t재고=%-3d" \
    % (row["itemname"], row["price"], row["snum"], row["stock"]))

connect.close()
