import pandas as pd

# Load your dataset
data = pd.read_csv('./final_merged_data.csv')

# Define a function to analyze an attribute
def analyze_attribute(df, attribute_name):
    print(f"Analyzing {attribute_name}:")
    # Check if there are any missing values
    missing = df[attribute_name].isnull().sum()
    print(f"Missing values: {missing}")

    # Check for uniqueness
    unique_values = df[attribute_name].nunique()
    print(f"Unique values: {unique_values}")

    # Get a basic distribution if the attribute is numerical
    if df[attribute_name].dtype in ['int64', 'float64']:
        print(f"Distribution:\n{df[attribute_name].describe()}")
    else:
        # For non-numerical attributes, show the top 5 most frequent values
        print(f"Top 5 values:\n{df[attribute_name].value_counts().head(5)}")

    # Check if this attribute could be part of a key for identifying duplicates
    if unique_values == len(df):
        print("This attribute could uniquely identify each record.")
    else:
        print("This attribute cannot uniquely identify each record.")
    print("\n")

# Analyze specified attributes
attributes_to_analyze = ['State Name', 'City', 'Population', 'Murder', 'Rape', 'Robbery', 'Property crime', 'Cost of Living Index']
for attribute in attributes_to_analyze:
    analyze_attribute(data, attribute)
