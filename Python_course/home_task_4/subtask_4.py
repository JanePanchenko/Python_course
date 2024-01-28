input_data = list(input("Enter your text: "))
characters_statistics = {}

for character in input_data:
    character_count = characters_statistics.get(character, 0)
    characters_statistics.update({character: character_count + 1})

print(characters_statistics)
