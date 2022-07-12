
# create indexd nested dict.
def nested_dict(*args):
    """ receives dicts & return nested dict """

    data_set = {i: args[i] for i in range(len(args))}
    return data_set

# A.
def split_male_female(dict_people):
    """ receives nested dictionary & return two dictionary,
        male & female """

    dict_of_male = {}
    dict_of_female = {}
    key_male = 0
    key_female = 0
    for i in range(len(dict_people)):
        if dict_people[i]["gender"] == "male":
            dict_of_male[key_male] = dict_people[i]
            key_male += 1
        else:
            dict_of_female[key_female] = dict_people[i]
            key_female += 1

    return dict_of_female, dict_of_male

# B.
def find_median_average(dickt_people):
    """ find ages average, find ages medien """
        # var for devide the avg.
    avg_ages = 0
        # var for sum of all ages.
    sum_age = 0

    lst_ages = []
        # looping to count the sum of average.
    for i in range(len(dickt_people)):
        sum_age += dickt_people[i]["age"]
        # find the average.
        avg_ages = sum_age/len(dickt_people)
        lst_ages.append(dickt_people[i]["age"])
        lst_ages = sorted(lst_ages)

    # find median.
    med_ages = len(lst_ages)//2
    if med_ages % 2 == 0:
        med_ages = lst_ages[med_ages-1]
    else:
        med_ages = lst_ages[med_ages]
    return avg_ages, med_ages

# C.
def print_values_above(people, num=0):
        """ received nested dict & print all if num == 0 else print only ages > num """
        if num > 0:
            for i in range(len(people)):
                if people[i]["age"] > num:
                    print(people[i])
        else:
            for i in range(len(people)):
                print(people[i])

def main():
    dict_1 = {"name": "John", "gender": "male", "age": 32}
    dict_2 = {"name": "Mike", "gender": "male", "age": 21}
    dict_3 = {"name": "Alex", "gender": "male", "age": 40}
    dict_4 = {"name": "Marina", "gender": "female", "age": 54}
    data_set = nested_dict(dict_1, dict_2, dict_3, dict_4)

    dict_female, dict_male = split_male_female(data_set)
    #print("dict of female:", dict_female)
    #print("dick of male:", dict_male)

    avg_ages, median_ages = find_median_average(data_set)
    print("Average of ages:", avg_ages, "median of ages:", median_ages)

    #print_values_above(data_set,33)

if __name__ == "__main__":
    main()
