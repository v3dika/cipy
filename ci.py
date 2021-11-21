from math import sqrt

test_type = str(input('would you like to calculate the confidence intervals of a mean or a population? '))

if test_type == 'mean':
    cl = int(input('input the confidence level (%): '))
    x = float(input('input the value of X - the sample mean: '))
    n = float(input('input the sample size: '))
    sd = float(input('input the value of sd - the sample standard deviation: '))

    ### obtain z-value from confidence level
    if cl == 99:
        z = 2.575
    if cl == 95:
        z = 1.960
    if cl == 90:
        z = 1.645
    if cl == 80:
        z = 1.282
        
    ### calculate CI
    CI_high = x + z * (sd/sqrt(n))
    CI_low = x - z * (sd/sqrt(n))

    ### report CI
    print('the lower confidence interval of the mean is: ')
    print(str(CI_low) + '%')

    print('the higher confidence interval of the mean is: ')
    print(str(CI_high) + '%');
    
if test_type == 'population':
    z = int(input('input the confidence level (%): '))
    S = int(input('input the number of successful observations: '))
    n = int(input('input the sample size: '))

    ### calculate p and W
    p_val = (S + (0.5 * (z ** 2)))/(n + (z ** 2))
    W_val = z * sqrt(p_val * (1 - p_val)/(n + (z ** 2)))

    ### calculate CI
    CI_low = ((p_val - W_val)*100)
    CI_high = ((p_val + W_val)*100)

    ### report values
    print('the value of p, the sampling population is: ')
    print(p_val)

    print('the value of W, the margin of error is: ')
    print(W_val)

    print('the lower confidence interval for the proportion is: ')
    print(str(CI_low) + '%')

    print('the higher confidence interval for the proportion is: ')
    print(str(CI_high) + '%')
