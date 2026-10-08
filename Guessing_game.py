import random

print("Welcome to Guessing Game\n")


list_cars = [
    "BMW", "Mercedes", "Toyota", "Honda", "Ford",
    "Audi", "Tesla", "Porsche", "Ferrari", "Lamborghini",
    "Nissan", "Hyundai", "Kia", "Volkswagen", "Volvo",
    "Mazda", "Subaru", "Chevrolet", "Jeep", "Mitsubishi"
]

list_animals = [
    "Lion", "Tiger", "Elephant", "Giraffe", "Monkey",
    "Wolf", "Fox", "Bear", "Rabbit", "Horse",
    "Dog", "Cat", "Eagle", "Dolphin", "Shark",
    "Penguin", "Crocodile", "Zebra", "Kangaroo", "Panda"
]


class Hints:
    def __init__(self):
        self.hints_cars = {
            "BMW": [
                "It is a German car brand.",
                "Its logo has blue and white colors.",
                "Its name has only three letters.",
                "It is famous for luxury and performance."
            ],

            "Mercedes": [
                "It is a German car brand.",
                "Its logo has three points.",
                "Its logo is inside a circle.",
                "Its name starts with M."
            ],

            "Toyota": [
                "It is a Japanese car brand.",
                "Its logo has several overlapping ovals.",
                "It is one of the world's most famous car brands.",
                "Its name starts with T."
            ],

            "Honda": [
                "It is a Japanese brand.",
                "It makes both cars and motorcycles.",
                "Its logo contains a capital H.",
                "Its name has five letters."
            ],

            "Ford": [
                "It is an American car brand.",
                "Its logo is blue and oval-shaped.",
                "Its name has four letters.",
                "It made the famous Mustang."
            ],

            "Audi": [
                "It is a German car brand.",
                "Its logo has four connected rings.",
                "Its name has four letters.",
                "Its name starts with A."
            ],

            "Tesla": [
                "It is strongly associated with electric cars.",
                "Its logo looks like a stylized T.",
                "Its name starts with T.",
                "It is named after a famous inventor."
            ],

            "Porsche": [
                "It is a German sports-car brand.",
                "Its logo contains a horse.",
                "Its name starts with P.",
                "The 911 is one of its famous models."
            ],

            "Ferrari": [
                "It is an Italian car brand.",
                "Its logo contains a horse.",
                "It is famous for sports cars.",
                "Its name starts with F."
            ],

            "Lamborghini": [
                "It is an Italian luxury car brand.",
                "Its logo contains a bull.",
                "Its name is quite long.",
                "Its logo is shaped like a shield."
            ],

            "Nissan": [
                "It is a Japanese car brand.",
                "Its name starts with N.",
                "It has produced the famous GT-R.",
                "Its logo contains a circular element."
            ],

            "Hyundai": [
                "It is a South Korean car brand.",
                "Its logo looks like a tilted H.",
                "Its name starts with H.",
                "Its name has seven letters."
            ],

            "Kia": [
                "It is a South Korean car brand.",
                "Its name has only three letters.",
                "Its logo is made mostly from letters.",
                "It is part of Hyundai Motor Group."
            ],

            "Volkswagen": [
                "It is a German car brand.",
                "Its logo contains V and W.",
                "Its name is made from two German words.",
                "The Golf is one of its famous models."
            ],

            "Volvo": [
                "It is associated with Sweden.",
                "It is famous for safety.",
                "Its logo has a circle and an arrow.",
                "Its name starts with V."
            ],

            "Mazda": [
                "It is a Japanese car brand.",
                "Its logo looks like a wing.",
                "Its name starts with M.",
                "It makes the MX-5."
            ],

            "Subaru": [
                "It is a Japanese car brand.",
                "Its logo contains stars.",
                "Its name starts with S.",
                "Its name is connected to a group of stars."
            ],

            "Chevrolet": [
                "It is an American car brand.",
                "Its logo looks like a bowtie.",
                "Its name starts with C.",
                "The Camaro is one of its famous models."
            ],

            "Jeep": [
                "It is an American car brand.",
                "It is strongly associated with off-road vehicles.",
                "Its name has only four letters.",
                "It is famous for its rugged vehicles."
            ],

            "Mitsubishi": [
                "It is a Japanese car brand.",
                "Its logo contains three diamond shapes.",
                "Its name starts with M.",
                "Its logo is made from three diamonds."
            ]
        }

        self.hints_name_of_animals = {
            "Lion": [
                "It is a wild animal.",
                "It is a large member of the cat family.",
                "It often lives in groups.",
                "The male can have a large mane."
            ],

            "Tiger": [
                "It is a wild animal.",
                "It is a large member of the cat family.",
                "It is an excellent swimmer.",
                "Its body has black and orange stripes."
            ],

            "Elephant": [
                "It is one of the largest land animals.",
                "It has very large ears.",
                "It has a very long nose.",
                "It uses its trunk for many tasks."
            ],

            "Giraffe": [
                "It is a land animal.",
                "It can reach things that others cannot.",
                "It has a very long neck.",
                "Its body has a distinctive pattern."
            ],

            "Monkey": [
                "It is a primate.",
                "Many species are very agile.",
                "It is strongly associated with trees.",
                "Some species have tails."
            ],

            "Wolf": [
                "It is a wild animal.",
                "It is closely related to the domestic dog.",
                "It often hunts in groups.",
                "It is known for howling."
            ],

            "Fox": [
                "It is a wild animal.",
                "It is smaller than many wild dogs.",
                "It has a long bushy tail.",
                "It is often described as clever."
            ],

            "Bear": [
                "It can be found in forests and mountains.",
                "Some species are excellent swimmers.",
                "It can stand on two legs.",
                "Some species sleep for long periods in winter."
            ],

            "Rabbit": [
                "It is generally a small animal.",
                "It has very long ears.",
                "It moves quickly by jumping.",
                "It mainly eats plants."
            ],

            "Horse": [
                "Humans have used it for transportation.",
                "It can run very fast.",
                "It is commonly associated with riding.",
                "It has hooves instead of paws."
            ],

            "Dog": [
                "It is commonly kept by humans.",
                "It has a strong sense of smell.",
                "It can learn many commands.",
                "It is often called man's best friend."
            ],

            "Cat": [
                "It is commonly kept as a pet.",
                "It can climb very well.",
                "It often lands on its feet.",
                "It has retractable claws."
            ],

            "Eagle": [
                "It is a bird of prey.",
                "It can fly very high.",
                "It has powerful eyesight.",
                "It uses its claws to catch prey."
            ],

            "Dolphin": [
                "It lives in water.",
                "It is not a fish.",
                "It breathes air.",
                "It is known for being highly intelligent."
            ],

            "Shark": [
                "It lives in oceans and seas.",
                "It is a fish.",
                "It has several rows of teeth in many species.",
                "Some species must keep moving to breathe."
            ],

            "Penguin": [
                "It is a bird.",
                "It cannot fly.",
                "It is adapted to life in water.",
                "It uses its wings for swimming."
            ],

            "Crocodile": [
                "It is a reptile.",
                "It spends a lot of time in water.",
                "It has a very powerful jaw.",
                "It has a long tail."
            ],

            "Zebra": [
                "It lives mainly in Africa.",
                "It is related to horses.",
                "Its body has a very recognizable pattern.",
                "It has black and white stripes."
            ],

            "Kangaroo": [
                "It is strongly associated with Australia.",
                "It has powerful back legs.",
                "It moves mainly by jumping.",
                "Its young develops in a pouch."
            ],

            "Panda": [
                "It is strongly associated with China.",
                "It belongs to the bear family.",
                "It spends a lot of time eating.",
                "Its favorite food is bamboo."
            ]
        }


def numbers(num):
    secret_number = random.randint(1, num)
    return secret_number


def cars(list_cars):
    secret_car = random.choice(list_cars)
    return secret_car


def animals(list_animals):
    secret_animal = random.choice(list_animals)
    return secret_animal


brbr = Hints()


def hihi(blabla, hint_number, type):
    if type == "car":
        hint = brbr.hints_cars[blabla][hint_number]
    else:
        hint = brbr.hints_name_of_animals[blabla][hint_number]

    return hint

while True:

    print("\n1 Guessing the numbers")
    print("2 Guessing car names")
    print("3 Guessing the names of animals")
    print("4 Exit")

    choice = input("Enter your choice: ")

    # ================= NUMBERS =================

    if choice == "1" or choice == "Guess the numbers" or choice == "numbers":

        while True:
            try:
                num = int(input("Enter the upper limit for the numbers to guess (starting from 1): "))
                break
            except ValueError:
                print("Please enter a number")

        xx = numbers(num)

        while True:
            try:
                cho = int(input("Enter a number: "))

                if cho == xx:
                    print("Congratulations! You win!")
                    break

                elif cho < xx:
                    print(f"The secret number is greater than {cho}! Try again")

                else:
                    print(f"The secret number is smaller than {cho}! Try again")

            except ValueError:
                print("Please enter a number")

    # ================= CARS =================

    elif choice == "2" or choice == "Guess car names" or choice == "car":

        dd = cars(list_cars)

        hint_number = 0
        attempts = 0

        while True:

            hhh = input("Enter a car name: ")

            if hhh.lower() == dd.lower():

                print("Congratulations! You win!")
                break

            else:

                attempts += 1

                if attempts <= 4:

                    print(f"Wrong! Hint: {hihi(dd, hint_number, "car")}")

                    hint_number += 1

                else:

                    print(f"You lose! The car was {dd}.")
                    break

    # ================= ANIMALS =================

    elif choice == "3" or choice == "Guess the names of animals" or choice == "animals":

        cc = animals(list_animals)

        hint_number = 0
        attempts = 0

        while True:

            kaka = input("Enter an animal name: ")

            if kaka.lower() == cc.lower():

                print("Congratulations! You win!")
                break

            else:
                attempts += 1
                if attempts <= 4:

                    print(f"Wrong! Hint: {hihi(cc, hint_number, "animal")}")

                    hint_number += 1

                else:

                    print(f"You lose! The animal was {cc}.")
                    break
                

    # ================= EXIT =================

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Please enter a valid choice")
