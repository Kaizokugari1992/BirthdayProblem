
import math, time
import matplotlib.pyplot as plt
from decimal import Decimal

def BirthdayProblem(people, birthdays = 365):
    print(f" Welcome to the Birthday Problem Calculator!")
    i = 0
    permutation = Decimal(math.factorial(birthdays))/Decimal(math.factorial(birthdays-people))
    probability = float(1 - (permutation/(birthdays**people)))*100

    print(f"For your chosen input of {people} people and {birthdays} "
          f"possible birthdays per year, \nthe probability of "
          f"at least one pair of people with common birthdays is {probability:.4f} %", flush = True)
    while True:
        try:
            plotgraph = input("Do you want to generate a graph for all possible entries? (Y/N):")
            if plotgraph.upper() == "Y":
                print("----Generating graph with all probabilities of at least one pair of people with "
                    "common birthdays for all possible ranges of people----", flush=True)
                x_axis = [_ for _ in range(0, birthdays+1)]
                probability_axis_table = [float(
                    1 - ((Decimal(math.factorial(birthdays)) / Decimal(math.factorial(birthdays - i))) / (
                                birthdays ** i))) * 100 for i in range(birthdays+1)]
                plt.ylabel("Possibility of at least two participants with common birthdays P (%)",
                           fontfamily="Calibri",fontsize="small")
                plt.xlabel("People(#)", fontfamily="Calibri", fontsize="small")
                plt.plot(x_axis, probability_axis_table, marker="o", ms=1, linewidth=0.1)
                plt.grid(visible=True, which='both', axis="both", ls="--")
                plt.title("Birthday Problem Solutions", fontfamily="Calibri", fontsize="25")
                time.sleep(1)
                print("Graph generated", flush=True)
                plt.show()
                break
            elif plotgraph.upper() == "N":
                return
            else:
                raise ValueError
        except ValueError:
            print("Only acceptable entries are (Y/N)!")

    return

if __name__ == "__main__":
    while True:
        try:
            a = input("Please enter the number of people that exist in your experiment (no more than 365 please!) "
                          "\n (You can press 'E' to exit at any time):")
            if a.upper() == "E":
                print("See you around")
                exit()
            elif int(a)<0 or int(a)>365:
                raise ValueError
        except ValueError:
            print("Hey, only numerical values below 365 and above 0 please!!!")
        else:
            BirthdayProblem(int(a))








