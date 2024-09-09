my_dict = {'Moscow': 1147, 'Saint-Petersburg': 1703, 'Ekaterenburg': 1723}
print(my_dict)
print(my_dict['Moscow'])
print(my_dict.get('Kazan'))
my_dict.update({'Vladivostok': 1860, 'Omsk': 1716})
year_of_foundation = my_dict.pop('Ekaterenburg')
print(year_of_foundation)
print(my_dict)
my_set = {1, 1, 'apple', 2.5, 3, 3}
print(my_set)
my_set.add((2, 5))
my_set.discard(2.5)
print(my_set)