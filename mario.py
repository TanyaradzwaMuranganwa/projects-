def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1<=value <=8:
                return value
            else:
                print("invalid input . Please enter a number between 1-8. ")
        except ValueError:
            print("Invalid input . Please enternumber between 1-8 ")

def main():
    height = get_int("Height: ")

    for i in range(1,height + 1):
        print(" " * (height -i)+ "#" * i)

if __name__ == "__main__":
    main()

