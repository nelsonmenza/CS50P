"""
This program allows the user to input the name of a fruit and checks if the fruit exists in a predefined dictionary of fruits and their calorie counts. If the fruit is found in the dictionary, it prints the calorie count for that fruit.

Usage:
1. Run the program.
2. Enter the name of a fruit when prompted.
3. The program will check if the fruit exists in the dictionary and, if found, will print the calorie count for that fruit.

Example:
Enter the fruit name: banana
Calories: 110
"""


def main():
    fruit_dict = {
        "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90,
        "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60,
        "orange": 80, "peach": 60, "pear": 100, "pineapple": 50, "plums": 70,
        "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80, "apple": 130
    }

    item = input("Enter the fruit name: ").lower()

    # Check if the item exists in the dictionary
    if item in fruit_dict:
        print(f"Calories: {fruit_dict[item]}")
    else:
        return


if __name__ == "__main__":
    main()
