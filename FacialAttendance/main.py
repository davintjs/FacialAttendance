import camera

def main():
    print("Welcome to the facial attendance system\n")
    print("1. Register new student")
    print("2. Take attendance")
    print("3. Exit\n")
    option = int(input("To get started, please input an option: "))
    
    if option == 1:
        camera.RegisterNew()

    elif option == 2:
        print("Taking attendance...")
    elif option == 3:
        exit()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()