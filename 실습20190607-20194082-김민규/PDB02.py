import sqlite3

connect = sqlite3.connect("sales.db")

if (connect):
    print("성공적으로 sales.db 를 열였습니다.")
else:
    print("sales.db 를 여는데 실패했습니다.")

cursor = connect.cursor()
cursor.execute('''create table saleitems (\
            id int primary key,\
            itemname text,\
            price int,\
            snum int,\
            stock int )
''')

connect,commit()
connect.close()
