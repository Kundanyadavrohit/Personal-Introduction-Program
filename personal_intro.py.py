# Project Name: Personal Introduction Program

def main():
    print("=" * 45)
    print("WELCOME TO THE DEVELOPERS ARENA")
    print("=" * 45)
    print()

    # Get and validate name
    name = input("What is your name? ").strip()
    while not name:
        name = input("Name cannot be empty. What is your name? ").strip()

    # Get and validate age
    age = input("How old are you? ").strip()
    while not age:
        age = input("Age cannot be empty. How old are you? ").strip()

    # Get and validate hobby
    hobby = input("What is your favorite hobby? ").strip()
    while not hobby:
        hobby = input("Hobby cannot be empty. What is your favorite hobby? ").strip()

    print("\n" + "-" * 45)
    print("Creating your profile...")
    print("-" * 45)

    print(f"\nWelcome {name}!")
    print(f"You are {age} years old and your favorite hobby is {hobby}.")
    print("\nGood luck on your coding journey in Week 1!")
    print("=" * 45)


# Run the program
if __name__ == "__main__":
    main()