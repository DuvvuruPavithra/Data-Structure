def prime_numbers(num1, num2):
    total_list = []
    for i in range(num1, num2):
        value = 0
        for j in range(2, i):
            if i % j == 0:
                value = value + 1
        if value >= 2:
            continue
        if value < 2:
            total_list.append(i)
    return total_list


if __name__ == "__main__":
    array = []
    arr1 = 1
    arr2 = 100
    while arr2 < 1000:
        out_list = prime_numbers(arr1, arr2)
        array.append(out_list)
        arr1 += 100
        arr2 += 100

    print(array)
