
import math, time
import matplotlib.pyplot as plt
from decimal import Decimal

def BirthdayProblem(people, birthdays = 365):
    i = 0
    permutation = Decimal(math.factorial(birthdays))/Decimal(math.factorial(birthdays-people))
    probability = float(1 - (permutation/(birthdays**people)))*100

    print(f" For your chosen input of {people} people and {birthdays} possible birthdays per year \n the probability of "
          f"at least one pair of people with common birthdays is {probability:.4f} %", flush = True)
    print("\nGenerating graph with all probabilities of at least one pair of people with common birthdays for all "
          "possible ranges of people ", flush = True)
    x_axis = [_ for _ in range(0, 366)]
    probability_axis_table = [float(
        1 - ((Decimal(math.factorial(birthdays)) / Decimal(math.factorial(birthdays - i))) / (birthdays ** i))) * 100
                              for i in range(366)]
    plt.ylabel("Possibility of at least two participants with common birthdays P (%)", fontfamily="Calibri",
               fontsize="small")
    plt.xlabel("People(#)", fontfamily="Calibri", fontsize="small")
    plt.plot(x_axis, probability_axis_table, marker = "o", ms = 1, linewidth = 0.1)
    plt.grid(visible=True, which='both', axis= "both", ls="--"  )
    time.sleep(1)
    plt.show()

    return

if __name__ == "__main__":
    while True:
        try:
            a = int(input("Please enter the number of people that exist in your experiment (no more than 365 please!):"))
            if a<0 or a>365:
                raise ValueError
        except ValueError:
            print("Hey, only numerical values below 365 and above 0 please!!!")
        else:
            BirthdayProblem(a)
            break






