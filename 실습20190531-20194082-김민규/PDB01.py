import sqlite3

connect = sqlite3.connect("my_database.db")

if (connect):
    print("성공적으로 my_database.db 를 열었습니다.")
else:
    print("my_database.db 를 여는데 실패했습니다.")

connect.close()
