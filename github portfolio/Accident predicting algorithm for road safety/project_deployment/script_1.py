import pandas as pd

df_test = pd.DataFrame({'Value_1': [1, 1, 1], 'Value_2': [2, 2, 2]})

"""
    This function takes a string value, a values list and a list with standardized values. The function returns the standardized number correlating to the value input.
    
    Parameters:
    - value: The value you want the standardized number for.
    - values_list: The list of all possible values.
    - standardized_list: The list of all standardized number correlating to each possible value.

    Returns:
    - new_value: The standardized number correlating with the passed value.
"""

print("This script prints a test DataFrame:")
print(df_test)