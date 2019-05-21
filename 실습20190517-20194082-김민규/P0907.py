Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> phone_book = {}
>>> phone_book ={"홍길동":"010-1111-2222"}
>>> print(phone_book)
{'홍길동': '010-1111-2222'}
>>> phone_book["강감찬"] = "010-1234-5679"
>>> phone_book["이순신"] = "010-1234-5680"
>>> print(phone_book)
{'홍길동': '010-1111-2222', '강감찬': '010-1234-5679', '이순신': '010-1234-5680'}
>>> print(phone_book["강감찬"])
010-1234-5679
>>> print(phone_book.keys())
dict_keys(['홍길동', '강감찬', '이순신'])
>>> print(phone_book.values())
dict_values(['010-1111-2222', '010-1234-5679', '010-1234-5680'])
>>> for key in sorted(phone_book.keys()):
	print(key, phone_book[key])

	
강감찬 010-1234-5679
이순신 010-1234-5680
홍길동 010-1111-2222
>>> del phone_book["홍길동"]
>>> 
>>> print(phone_book)
{'강감찬': '010-1234-5679', '이순신': '010-1234-5680'}
>>> phone_book.clear()
>>> print(phone_book)
{}
>>> 
