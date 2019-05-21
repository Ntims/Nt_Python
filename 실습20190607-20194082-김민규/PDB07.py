import sqlite3

connect = sqlite3.connect("sales.db")

if(connect is None):
    print("sales.db를 여는데 실패했습니다.")
    exit()

connect.row_factory = sqlite3.Row

cursor = connect.cursor()

cursor.execute("select itemname, price from saleitems")
rows = cursor.fetchall()

for row in rows:
    print("%s\t가격=%-4d" % (row["itemname"], row["price"]))

connect.close()
