
# O(1) time
# O(1) memory
def find_largest_contiguous_sequence(list):

    current_sub = [[-1, -1], 0]
    last_sub = [[-1, -1], 0]
    large_sub = [[-1, -1], 0]

    index = 0

    while index < len(list):
        if list[index] < 0:
            current_sub[0][1] = index - 1
            large_sub[0][1] = index - 1

            if large_sub[1] > last_sub[1] and large_sub[1] > current_sub[1]:
                last_sub = large_sub
                current_sub = [[-1, -1], 0]
            elif current_sub[1] >= last_sub[1] and current_sub[1] >= large_sub[1]:
                last_sub = current_sub
                large_sub = current_sub
                current_sub = [[-1, -1], 0]
            elif last_sub[1] > large_sub[1] and last_sub[1] > current_sub[1]:
                large_sub = current_sub

        else:
            current_sub[1] += list[index]
            if current_sub[0][0] == -1:
                current_sub[0][0] = index
        large_sub[1] += list[index]
        index += 1

    return large_sub

if __name__ == "__main__":
    array = [-2, 5, 4, -3, 7, 2, -1, 3, -4]
    sub = find_largest_contiguous_sequence(array)
    print(sub)

    array = [-2, 5, 4, -10, 3, 3, -1, 3, -4]
    sub = find_largest_contiguous_sequence(array)
    print(sub)
