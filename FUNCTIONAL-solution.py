


def flatten_and_sort(lst):
    out_list = []
    for item in lst:
        if type(item) == list:
            for i in item:
                out_list.append(i)
        else:
            out_list.append(item)

    return sorted(out_list)


nested = [0,2,5,4,3,2,1,[5,5353,5,15],[123,12312]]
print(nested)

print(flatten_and_sort(nested))