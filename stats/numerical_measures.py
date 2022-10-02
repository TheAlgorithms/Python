import numpy as np
from scipy import stats

def main():

    """
    Identifying  most common numerical measures
    from a sample using statistical tools.
    """
  
    sample_values = []
    while True:
        sample_values.append(input('Please enter a number. Enter "Q" to quit: '))
        if sample_values[-1].upper()  == 'Q':
            break

    sample_values = [float(i)  for i in sample_values if i.isnumeric()]
    
    print(f"Sample values are {sample_values}")
    print(f"Mean is {round(np.mean(sample_values),2)}")
    print(f"Median is {np.median(sample_values)}")
    print(f"Mode is {stats.mode(sample_values)[0][0]}")
    print(f"1st(Q1) and 3rd(Q3) quartiles are {np.percentile(sample_values,[25,75])}")
    print(f"IQR(Q3 - Q1) is {stats.iqr(sample_values, rng=(25,75))}")
    print(f"Skewness is {round(stats.skew(sample_values),2)}")
    print(f"Kurtosis is {round(stats.kurtosis(sample_values),2)}")

if __name__ == "__main__":
    main()    