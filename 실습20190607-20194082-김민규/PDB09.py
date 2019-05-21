import sqlite3

connect = sqlite3.connect("sales.db")
if(connect is None):
    print("sales.db를 여는데 실패했습니다.")
    exit()

connect.row_factory = sqlite3.Row
cursor = connect.cursor()

cursor.execute("select * from saleitems where id=4")
rows = cursor.fetchall()

print("[수정전]\t품명\t판매수량\t재고")
for row in rows:
    print("\t%s\t%-4d\t%-4d" % (row["itemname"], row["snum"], row["stock"]))

cursor.execute("update saleitems set stock=20 where id=4")
connect.commit()

cursor.execute("select * from saleitems where id=4")
rows = cursor.fetchall()

print("[수정후]\t품명\t판매수량\t재고")
for row in rows:
    print("\t%s\t%-4d\t%-4d" % (row["itemname"], row["snum"], row["stock"]))

connect.close()
