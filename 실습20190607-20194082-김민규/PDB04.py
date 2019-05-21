import sqlite3

connect = sqlite3.connect("sales.db")

if (connect):
    print("성공적으로 sales.db 를 열었습니다.")
else:
    print("sales.db 를 여는데 실패했습니다.")

v_itemname = "사이다"
v_price = 1000
v_snum = 8
v_stock = 12

cursor = connect.cursor()

cursor.execute("insert into saleitems (itemname, price, snum, stock) values (?,?,?,?)",\
(v_itemname, v_price, v_snum, v_stock))

connect.commit()
connect.close()
