from collections import namedtuple
from typing import List, Union, Dict

# -----------------------------------------------------------------------------
# creating named tuple
Person = namedtuple('Person', 'name age weight')
Product = namedtuple('Product', 'name price')
john: Person = Person('John', '26', 77)
rihanna: Person = Person('Rihanna', '26', 66)
apple: Product = Product('Apple', '2$')

# ------------------------------------------------------------------------------
# creating object by using existing data
person_data: List[Union[str, int]] = ['Ali', 23, 45]
product_data: List[str] = ['Orange', '5$']
ali: Person = Person(*person_data)  # or Person.make(data)
orange: Product = Product(*product_data)
person_dict_data: Dict[str, Union[str, int]] = {'name': 'Vali', 'age': 20, 'weight': 100}
vali: Person = Person(**person_dict_data)

# print(vali.name, vali.age, vali.weight)
# print(orange.name, orange.price)  # we can also print(vali[0], vali[1], vali[2])
# print(vali._fields)  # print(Person._fields) for printing fields of named tuple

# ----------------------------------------------------------------------------------
# using default values

Person = namedtuple('Person', 'name age weight', defaults=[18, 20])  # giving defaults to named tuple
Product = namedtuple('Product', 'name price', defaults=['1$'])
gani: Person = Person('Gani')
watermelon: Product = Product('Watermelon')

# print(gani._field_defaults)
# print(watermelon._field_defaults)  # printing default values
# print(gani.name, gani.age, gani.weight)
# print(watermelon.name, watermelon.price)
# --------------------------------------------------------------------------

# Convert named tuples to dictionaries
data3: Dict[str, Union[str, int]] = gani._asdict()
data4: Dict[str, Union[str, int]] = watermelon._asdict()

# print(data3)
# print(data4)
# ------------------------------------------------------------------------------------------
# creating new object by replacing existing object

abduvali = vali._replace(name='Abduvali')
cherry = watermelon._replace(name='Cherry')

# print(abduvali.name, abduvali.age, abduvali.weight)
# print(cherry.name, cherry.price)
