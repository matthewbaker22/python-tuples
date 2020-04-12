zoo = ("rhino", "penguin", "giraffe", "lizard", "snake", "lion", "tiger", "elephant", "zebra", "dog")

animal_to_find = "kangaroo"
if animal_to_find in zoo:
    print(animal_to_find)
else:
    print("Animal not found")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo

# print(first_animal)
# print(second_animal)
# print(third_animal)
# print(fourth_animal)
# print(fifth_animal)
# print(sixth_animal)
# print(seventh_animal)
# print(eighth_animal)
# print(ninth_animal)
# print(tenth_animal)

zoo_list = [first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal]
zoo_list.extend(["donkey", "monkey", "fish"])
print(zoo_list)

zoo_tuple = tuple(zoo_list)
print(zoo_tuple)

