def merge_dictionaries(dict_1, dict_2):
    result = dict(dict_1)  # copy the first dictionary
    for key, value in dict_2.items():
        result[key] = value
    return result


dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

print(merge_dictionaries(dict_1, dict_2))
