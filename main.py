from math import sqrt
z = input('input the confidence level')
S = int(input('input the value of S - the number of successful observations'))
n = int(input('input the value of n - the sample size'))

p_val = (S + (0.5 * (z ** 2)))/(n + (z ** 2))
W_val = z * sqrt(p * (1 - p)/(n + (z ** 2))

CI_low = ((p_val - W_val)*100)
CI_high = ((p_val + W_val)*100)

print('the value of p, the sampling population is:')
print(p)

print('the value of W, the margin of error is:')
print(W)

print('the lower confidence interval for the proportion is:')
print(str(CI_low) + '%')

print('the higher confidence interval for the proportion is:')
print(str(CI_high) + '%')
