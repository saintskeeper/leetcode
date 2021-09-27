# can use deque from collections lib for linkedl ists

from collections import deque

#can give an iterable to populate the list
deque(['a',2,'1'])

deque([{'data': 'a'}, {'data': 'b'}])

 llist = deque("abcde")
 llist
deque(['a', 'b', 'c', 'd', 'e'])

 llist.append("f")
 llist
deque(['a', 'b', 'c', 'd', 'e', 'f'])

 llist.pop()
'f'

 llist
deque(['a', 'b', 'c', 'd', 'e'])