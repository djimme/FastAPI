thing: str = "yeti"

print(thing)

from typing import Tuple, Dict, List, Any

tuple_things: Tuple = ('yeti','bigfoot')
tuple_things2: Tuple = 'yeti','bigfoot'
list_things: List = ['yeti', 'bigfoot']
dict_things: Dict = {'mountain':'yeti', 'forest':'bigfoot'}

print(tuple_things)
print(tuple_things2)
print(list_things)
print(dict_things)

dict_anything: dict[str,Any] = {'marco':'polo', 'answer':42}
print(dict_anything)

dict_anything2: dict[str, str|int] = {'marco':'polo', 'answer':42}
print(dict_anything2)

thing = 42
print(thing)