def mutater(a_list, an_int):
    print("Inside mutater - Before:")
    print(f"a_list: {a_list}")
    print(f"an_int: {an_int}")
    
    an_int *= 5
    a_list[0] *= 5
    
    print("Inside mutater - After:")
    print(f"a_list: {a_list}")
    print(f"an_int: {an_int}")


def main():
    an_int = 10
    a_list = [an_int]

    print("Before calling mutater:")
    print(f"a_list: {a_list}")
    print(f"an_int: {an_int}")

    mutater(a_list, an_int)

    print("After calling mutater:")
    print(f"a_list: {a_list}")
    print(f"an_int: {an_int}")

if __name__ == "__main__":
    main()
