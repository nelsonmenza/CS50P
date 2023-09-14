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
