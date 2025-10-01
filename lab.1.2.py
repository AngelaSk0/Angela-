my_list = [12, 5, 8, 33, 2, 19, 42, 7, 16, 3,
           "яблуко", "груша", "банан", "ананас", "вишня",
           "апельсин", "диня", "ківі", "персик", "слива"]


ints = [x for x in my_list if isinstance(x, int)]
strings = [x for x in my_list if isinstance(x, str)]

ints_sorted = sorted(ints)                 
strings_sorted = sorted(strings, key=str.lower) 


sorted_list = ints_sorted + strings_sorted

even_numbers = [x for x in ints_sorted if x % 2 == 0]

strings_caps = [s.upper() for s in strings_sorted]

print("Основний список:", my_list)
print("Відсортований список:", sorted_list)
print("Кратні двом:", even_numbers)
print("Рядки у CAPS:", strings_caps)
