import sqlite3

connect = sqlite3.connect("sales.db")

if (connect):
    print("성공적으로 sales.db 를 열었습니다.")
else:
    print("sales.db 를 여는데 실패했습니다.")


cursor = connect.cursor()
cursor.execute('''insert into saleitems (id, itemname, price, snum, stock) values (1, '커피', 3000, 5, 10)''')
cursor.execute('''insert into saleitems (id, itemname, price, snum, stock) values (2, '펜', 1000, 10, 20)''')
cursor.execute('''insert into saleitems values (3, '종이컵', 20, 1050, 550)''')
cursor.execute('''insert into saleitems values (4, '우유', 500, 10, 5)''')
cursor.execute('''insert into saleitems (itemname, price, snum, stock) values ('콜라', 1050, 22, 10)''')

connect.commit()
connect.close()
