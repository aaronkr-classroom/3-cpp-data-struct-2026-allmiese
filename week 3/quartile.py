# 3-2
import numpy as np

def print_quartiles(data):
    #Sort the data in ascending order
    sorted_data = sorted(data)

    #Calculate quartiles
    q1 = np.percentile(sorted_data, 25);  #First quartile (25%)
    q2 = np.percentile(sorted_data, 50);  #Second quartile (median, 50%)
    q3 = np.percentile(sorted_data, 75);  #Third quartile (75%)

    #Print results
    print(f"Sorted data: {sorted_data}")
    print(f"First quartile (Q1): {q1}")
    print(f"Second quartile (Q2/Median): {q2}")
    print(f"Third quartile (Q3): {q3}")

#Example usage
numbers = [7, 15, 49, 40, 41, 36, 39, 78, 65, 89, 32, 24, 65]
print_quartiles(numbers)