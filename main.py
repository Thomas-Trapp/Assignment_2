"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    return annual_cost / SEMESTERS_PER_YEAR   #Give back what one semester costs.
    


def cost_per_month(annual_cost):
    return annual_cost / MONTHS_PER_YEAR  #Give back what one month of the academic year costs.
    


def cost_per_day(annual_cost):
    return cost_per_semester(annual_cost) / CLASS_DAYS_PER_SEMESTER   #Give back what one class day costs.
     


def cost_per_credit(annual_cost, credits):
    return cost_per_semester(annual_cost) / credits  #Give back what one credit costs. credits is the number taken this semester.


def cost_per_class(annual_cost, credits):
    return cost_per_credit(annual_cost, credits) / CS1430_MEETINGS_PER_SEMESTER * CS1430_CREDITS #Give back what one 50-minute CS 1430 class meeting costs.


def cost_per_bathroom(annual_cost, credits):
    return cost_per_class(annual_cost, credits) / 10

# ---- PROGRAM ----

def main():
    annual_cost = float(input("input annual cost: "))  # Ask for the total cost for one year here.
    credits = int(input("Input number of credits: "))  # Then ask for the credits this semester.

    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost per bathroom")
        print("Q. Close menu")

        choice = input("Choose an option: ")

        if choice == "1":
            sem_cost = cost_per_semester(annual_cost)
            print(f"{sem_cost:.2f}")

        elif choice == "2":
            month_cost = cost_per_month(annual_cost)
            print(f"{month_cost:.2f}")

        elif choice == "3":
            day_cost = cost_per_day(annual_cost)
            print(f"{day_cost:.2f}")

        elif choice == "4":
            credit_cost = cost_per_credit(annual_cost, credits)
            print(f"{credit_cost:.2f}")

        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"{class_cost:.2f}")

        elif choice == "6":
            break_cost = cost_per_bathroom(annual_cost, credits)
            print(f"{break_cost:.2f}")

        elif choice == "Q":
            break

        else:
            print("Invalid choice. Please choose again")

        


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()