general_list = {
    'australia_blacklist': ['Alex', 'Pol', 'Will', 'John'],
    'poker_blacklist': ['Jack', 'Pol', 'Kate', 'John'],
    'alcohol_blacklist': ['Alex', 'Rio', 'Pol', 'John']
}

winners = set(list(general_list.values())[0])

for value in list(general_list.values())[1:]:
    winners = winners & set(value)

print(winners)

