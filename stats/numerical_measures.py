import numpy as np
from scipy import stats

def main():

    """
    Identifying  most common numerical measures
    from a sample using statistical tools.
    """

    sample_values = [26, 15, 8, 44, 26, 13, 38, 24, 17, 29]
    
    print(f"Sample values are {sample_values}")
    print(f"Mean is {np.mean(sample_values)}")
    print(f"Median is {np.median(sample_values)}")
    print(f"Mode is {stats.mode(sample_values)[0][0]}")
    print(f"1st(Q1) and 3rd(Q3) quartiles are {np.percentile(sample_values,[25,75])}")
    print(f"IQR(Q3 - Q1) is {stats.iqr(sample_values, rng=(25,75))}")
    print(f"Skewness is {round(stats.skew(sample_values),2)}")
    print(f"Kurtosis is {round(stats.kurtosis(sample_values),2)}")

if __name__ == "__main__":
    main()    