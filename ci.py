from math import sqrt
from math import pi
from math import e
from numpy import linspace
from matplotlib import pyplot as plt
from matplotlib import patches as pt

test_type = str(input("would you like to calculate the confidence intervals of a mean or a population? "))
cl = int(input("input the confidence level (%): "))
m = float(input("input the sample mean: "))
n = float(input("input the sample size: "))
S = float(input("input the standard deviation: "))
if cl == 99:
    z = 2.575
if cl == 95:
    z = 1.960
if cl == 90:
    z = 1.645
if cl == 80:
    z = 1.282

if test_type == "mean":
    CI_high = m + z * (S / sqrt(n))
    CI_low = m - z * (S / sqrt(n))
    
    print("the lower confidence interval of the mean is: ")
    print(str(CI_low) + "%")

    print("the higher confidence interval of the mean is: ")
    print(str(CI_high) + "%")
    

if test_type == "population":
    Ss = float(input("input the number of successful observations"))
    p_val = (Ss + (0.5 * (z ** 2))) / (n + (z ** 2))
    W_val = z * sqrt(p_val * (1 - p_val) / (n + (z ** 2)))

    CI_low = (p_val - W_val) * 100
    CI_high = (p_val + W_val) * 100

    print("the value of p, the sampling population is: ")
    print(p_val)

    print("the value of W, the margin of error is: ")
    print(W_val)

    print("the lower confidence interval for the proportion is: ")
    print(str(CI_low) + "%")

    print("the higher confidence interval for the proportion is: ")
    print(str(CI_high) + "%")

graph = str(input("would you like a graph of the confidence intervals? (y/n): "))

if graph == "y":
    sp = 1 - z
    x = linspace(m-3*S, m+3*S, 300)
    func = (1 / (S*sqrt(2*pi))) * e ** ((-1/2) * (((x-m)/S) ** 2))
            
    plt.grid(color='k')
    plt.fill_between(x, func, 0,
                where=(x > CI_low) & (x < CI_high),
                color='lightsteelblue')
    plt.plot(x,func, color='k')
    mY = (1 / (S * sqrt(2 * pi))) * e ** ((-1 / 2) * (((m - m) / S) ** 2))
            
    plt.plot(m, mY, marker=".", color="m")
    plt.text(m, mY, f"μ={m}", fontsize=10)
            
    plt.text(m - S / 3, mY / 2, f"z = {z}%")
    plt.plot(CI_low, 0, marker=".", color="m")
    plt.text(CI_low, mY/25, f"x={round(CI_low)}")
    plt.plot(CI_high, 0, marker=".", color="m")
    plt.text(CI_high, 0, f"y={round(CI_high)}")
    a = (1 / (S * sqrt(2 * pi))) * e ** (
                    (-1 / 2) * (((((m - 3 * S) + CI_low) / 2 - m) / S) ** 2))
    b = (1 / (S * sqrt(2 * pi))) * e ** (
                    (-1 / 2) * (((((m + 3 * S) + CI_high) / 2 - m) / S) ** 2))
    handles = [pt.Rectangle((0,0), 1, 1, fc="w", ec="w", alpha=0)] * 4
    labels = []
    labels.append(f"μ={m}")
    labels.append(f"z = {z}%")
    labels.append(f"x={round(CI_low)}")
    labels.append(f"y={round(CI_high)}")

    plt.legend(handles, labels, loc='best', fontsize='small', framealpha=1, edgecolor="k")

    plt.show()