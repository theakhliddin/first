def sum_w_loop(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum +1
    return sum

def sum_w_recurtion(number):
    if number == 1:
        return 1
    else:
        return number + sum_w_recurtion(number - 1)


def main():
    user_input = int(input("Enter the number: "))
    result = sum_w_loop(user_input)
    print(result)

    rec_result = sum_w_recurtion(user_input)
    print(rec_result)

if __name__ == "__main__":
    main()