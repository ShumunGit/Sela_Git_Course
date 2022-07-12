
# targil 1.
# A sorted dict. 
symbols = "aaabbbbbfvvfmv!!@@**&&fvfvf@@$$**#########$"
set_sym = set(symbols)
dict_sym = {key: symbols.count(key) for key in set_sym}
sorted_dict = {key: dict_sym.get(key) for key in sorted(dict_sym)}
# print("Sorted dict: {}\n".format(sorted_dict))

# B values as keys. 
value_as_key = {}
for key in sorted_dict:
    value = sorted_dict[key]
    if value not in value_as_key.keys():
        value_as_key[value] = key
    else:
        key2 = value_as_key.get(value), key
        value_as_key[value] = key2
# print("Keys as values: {}".format(value_as_key))

# targil 2.
lst_1 = [1, 2, 2, 2, 3, 4, 5, 5, 5]
lst_2 = [2, 4, 5, 7, 8, 9]
lst_3 = [10, 2, 30, 40, 5]
lst_4 = [11, 22, 30, 40, 5]
all_lst = [lst_1, lst_2, lst_3, lst_4]
set_lst = []
cnt = 0
# A.
for i in range(len(all_lst)):
    if len(set(all_lst[i])) != len(all_lst[i]):
        print("list number {} have duplicate values.".format(i))
    else:
        set_lst.append(set(all_lst[i]))
        print("list {} is a uniq list".format(i), set_lst[cnt])
        cnt += 1

if (len(set_lst)) % 2 == 0:
    for i in range(len(set_lst) // 2):
        num = i + 1
        print("list {} & list {} have common values. {}".format(i, num, set_lst[i].intersection(set_lst[num])))
else:
    for i in range(len(set_lst) // 2):
        num = i + 1
        print("list {} & list {} have common values. {}".format(i, num, set_lst[i].intersection(set_lst[num])))
    print("list {} is a uniq. {}".format(len(set_lst), set_lst[-1]))
# Targil 3.
distinc_lst = [31, 99, 3, 1943, 44, 88, 22, 334, 221]
str_int = ""
for num in distinc_lst:
    str_int += str(num)

str_int = set(str_int)
lst_unique = [int(x) for x in str_int]

lst_unique_ascending = sorted(lst_unique)
lst_unique_descending = sorted(lst_unique, reverse=True)
# print("Sorted: {}".format(lst_unique_ascending))
# print("Sorted reverse: {}".format(lst_unique_descending))
