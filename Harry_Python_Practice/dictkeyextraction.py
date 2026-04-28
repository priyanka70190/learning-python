dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 3, 'd': 4}

for key in dict1:
    if key in dict2:
        print(f"Common key: {key}, Values: {dict1[key]} vs {dict2[key]}")
    else:
        print(f"Key {key} only in dict1")