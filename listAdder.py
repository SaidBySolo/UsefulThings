def list_adder(list1, list2):
    final_list = []
    if len(list1) >= len(list2):
        for x in range(0, len(list2)):
            final_list.append(list1[x] + list2[x])
        for y in range(len(list2), len(list1)):
            final_list.append(list1[y])
    else:
        for x in range(0, len(list1)):
            final_list.append(list1[x] + list2[x])
        for y in range(len(list1), len(list2)):
            final_list.append(list2[y])
    return final_list
