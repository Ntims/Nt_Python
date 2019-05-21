import sqlite3

connect = sqlite3.connect("sales.db")
if (connect is None):
    print("sales.db 를 여는데 실패했습니다.")
    exit()

connect.row_factory = sqlite3.Row
cursor = connect.cursor()

cursor.execute("select * from saleitems")
rows = cursor.fetchall()

print("[삭제전]\t품명\t판매수량\t재고")
for row in rows:
    print("\t\t%s\t%-4d\t\t%-4d" % (row["itemname"], row["snum"], row["stock"]))

cursor.execute("delete from saleitems where id=6")
connect.commit()

cursor.execute("select * from saleitems")
rows = cursor.fetchall()

print("[삭제후]\t품명\t판매수량\t재고")
for row in rows:
    print("\t\t%s\t%-4d\t\t%-4d" % (row["itemname"], row["snum"], row["stock"]))

connect.close()
