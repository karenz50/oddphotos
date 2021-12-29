def get_input_from_terminal():
    total_cows = input("").replace("\n", "")
    cow_id_list = input("").replace("\n", "").split(" ")

    return int(total_cows), [int(i) for i in cow_id_list]

def sort_into_odd_even( total_cows, cow_id_list ):
    odd_list, even_list = [], []
    for i in range(total_cows):
        cur_cow = cow_id_list[i]
        if cur_cow % 2 == 0:
            even_list.append(cur_cow)
        else:
            odd_list.append(cur_cow)

    return odd_list, even_list

def calc_max_groups( total_cows, cow_id_list ):
    odd_list, even_list = sort_into_odd_even(total_cows, cow_id_list)
    max_group_count = 0

    if len(odd_list) != 0:
        for i in range(total_cows):
            if max_group_count % 2 != 0:
                if (len(odd_list) == 2 and len(even_list) == 0) or len(odd_list) == 0:
                    break
                else:
                    odd_list.remove(odd_list[0])
            else:
                if len(even_list) > 0:
                    even_list.remove(even_list[0])
                elif len(odd_list) < 2:
                    break
                else:
                    odd_list.remove(odd_list[0])
                    odd_list.remove(odd_list[0])

            max_group_count += 1

            if len(odd_list) == 0 and len(even_list) == 0:
                break
    else:
        max_group_count = 1

    return max_group_count

if __name__ == "__main__":
    total_cows, cow_id_list = get_input_from_terminal()
    #total_cows, cow_id_list = 10, [84, 87, 78, 16, 94, 36, 87, 93, 50, 22]
    max_group_count = calc_max_groups(total_cows, cow_id_list)
    print(max_group_count)