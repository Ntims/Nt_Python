import sqlite3

connect = sqlite3.connect("sales.db")

if(connect is None):
    print("sales.db를 여는데 실패했습니다.")
    exit()

connect.row_factory = sqlite3.Row

cursor = connect.cursor()

cursor.execute("select itemname, snum, stock from saleitems where snum >= 10 and stock <= 5")
rows = cursor.fetchall()

print("품명\t판매수량\t재고")
for row in rows:
    print("%s\t%-4d\t%-4d" % (row["itemname"], row["snum"], row["stock"]))

connect.close()
