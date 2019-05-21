Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> heroes = []
>>> heroes.append("아이언맨")
>>> heroes
['아이언맨']
>>> heroes.append("닥터 스트레인지")
>>> print(heroes)
['아이언맨', '닥터 스트레인지']
>>> num=[1]
>>> num.append(2)
>>> num
[1, 2]
>>> list1=[1,2,3]
>>> list1.append(num)
>>> list1
[1, 2, 3, [1, 2]]
>>> list1.append("아이언맨")
>>> list1
[1, 2, 3, [1, 2], '아이언맨']
>>> letters=["A","B","C","D","E","F"]
>>> print(letters[0])
A
>>> print(letters[1])
B
>>> print(letters[2])
C
>>> letters=["A","B","C","D","E","F"]
>>> print(letters[0:3])
['A', 'B', 'C']
>>> print(letters[0:3])
['A', 'B', 'C']
>>> print(letters[3:])
['D', 'E', 'F']
>>> print(letters[:])
['A', 'B', 'C', 'D', 'E', 'F']
>>> letters=["a","b","c","d","e","f"]
>>> copy1 = letters
>>> copy1
['a', 'b', 'c', 'd', 'e', 'f']
>>> letters.append("g")
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> copy1
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> copy2=letters[:]
>>> copy2
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters.append("h")
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> copy2
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
>>> heroes[1] = "닥터 스트레인지"
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치']
>>> heroes.append("스파이더맨")
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
>>> 
>>> 
>>> heroes.insert(1,"배트맨")
>>> print(heroes)
['아이언맨', '배트맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']
>>> 
>>> heroes.remove("헐크")
>>> print(heroes)
['아이언맨', '배트맨', '닥터 스트레인지', '스칼렛 위치', '스파이더맨']
>>> if "배트맨" in heroes:
	heroes.remove("배트맨")

	
>>> print(heroes)
['아이언맨', '닥터 스트레인지', '스칼렛 위치', '스파이더맨']
>>> del heroes[0]
>>> print(heroes)
['닥터 스트레인지', '스칼렛 위치', '스파이더맨']
>>> 
>>> last_hero = heroes.pop()
>>> print(last_hero)
스파이더맨
>>> print(heroes)
['닥터 스트레인지', '스칼렛 위치']
>>> heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
>>> print(heroes.index("헐크"))
2
>>> print(heroes)
['아이언맨', '토르', '헐크', '스칼렛 위치']
>>> for hero in heroes:
	print(hero)

	
아이언맨
토르
헐크
스칼렛 위치
>>> print(heroes)
['아이언맨', '토르', '헐크', '스칼렛 위치']
>>> heroes.sort()
>>> print(heroes)
['스칼렛 위치', '아이언맨', '토르', '헐크']
>>> m = "파이썬은 정말 쉬운 언어다"
>>> mlist = m.split()
>>> mlist
['파이썬은', '정말', '쉬운', '언어다']
>>> mlist.sort(key=len)
>>> mlist
['정말', '쉬운', '언어다', '파이썬은']
>>> heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
>>> dir(heroes)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(heroes)
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
