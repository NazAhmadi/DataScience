import pandas as pd
csv_file_path = './crime.csv'
crime_data = pd.read_csv(csv_file_path)

# Display the first few rows to understand the structure
# crime_data.head()

# Replace NaN in 'State' column with the previous valid state name
crime_data['State'] = crime_data['State'].fillna(method='ffill')

# Confirm the changes by displaying the first few rows again
# crime_data.head()

# Save the modified DataFrame back to a CSV file
output_file_path = './cleaned_crime_data.csv'
crime_data.to_csv(output_file_path, index=False)


######### step 2 #########
cleaned_crime_file_path = './cleaned_crime_data.csv'
cleaned_crime_data = pd.read_csv(cleaned_crime_file_path)

# Load the cost of living data
cost_of_living_file_path = './cost_of_living_index.csv'
cost_of_living_data = pd.read_csv(cost_of_living_file_path)

# Display the first few rows to understand the structure
# cost_of_living_data.head()
# Clean up the State column in the cleaned_crime_data to remove numerical suffixes
cleaned_crime_data['State'] = cleaned_crime_data['State'].str.replace(r'\d+', '', regex=True).str.strip()

# As we need to merge the data on both city and state, we should have the full state name in the cost_of_living_data
# We would typically look up a state abbreviation to full name mapping, but for this example, let's assume we have it ready
# For simplicity, let's say we have the following abbreviated mapping
state_abbreviation_to_name = {
    'AL': 'ALABAMA', 'AK': 'ALASKA', 'AZ': 'ARIZONA', 'AR': 'ARKANSAS', 'CA': 'CALIFORNIA',
    'CO': 'COLORADO', 'CT': 'CONNECTICUT', 'DE': 'DELAWARE', 'FL': 'FLORIDA', 'GA': 'GEORGIA',
    'HI': 'HAWAII', 'ID': 'IDAHO', 'IL': 'ILLINOIS', 'IN': 'INDIANA', 'IA': 'IOWA',
    'KS': 'KANSAS', 'KY': 'KENTUCKY', 'LA': 'LOUISIANA', 'ME': 'MAINE', 'MD': 'MARYLAND',
    'MA': 'MASSACHUSETTS', 'MI': 'MICHIGAN', 'MN': 'MINNESOTA', 'MS': 'MISSISSIPPI', 'MO': 'MISSOURI',
    'MT': 'MONTANA', 'NE': 'NEBRASKA', 'NV': 'NEVADA', 'NH': 'NEW HAMPSHIRE', 'NJ': 'NEW JERSEY',
    'NM': 'NEW MEXICO', 'NY': 'NEW YORK', 'NC': 'NORTH CAROLINA', 'ND': 'NORTH DAKOTA', 'OH': 'OHIO',
    'OK': 'OKLAHOMA', 'OR': 'OREGON', 'PA': 'PENNSYLVANIA', 'RI': 'RHODE ISLAND', 'SC': 'SOUTH CAROLINA',
    'SD': 'SOUTH DAKOTA', 'TN': 'TENNESSEE', 'TX': 'TEXAS', 'UT': 'UTAH', 'VT': 'VERMONT',
    'VA': 'VIRGINIA', 'WA': 'WASHINGTON', 'WV': 'WEST VIRGINIA', 'WI': 'WISCONSIN', 'WY': 'WYOMING'
}

# Add a new column for the full state name to the cost_of_living_data using the mapping
cost_of_living_data['State Name'] = cost_of_living_data['State'].map(state_abbreviation_to_name)

# Confirm the changes by displaying the first few rows again
# cost_of_living_data.head()

# Merge the two datasets on both City and State Name columns
merged_data = pd.merge(
    cleaned_crime_data, 
    cost_of_living_data, 
    how='inner', 
    left_on=['City', 'State'], 
    right_on=['City', 'State Name']
)

# Drop one of the state name columns to avoid redundancy since they contain the same information now
merged_data.drop('State Name', axis=1, inplace=True)

# Let's take a look at the merged data
merged_data.head()


# Rename the columns for clarity
merged_data.rename(columns={'State_x': 'State Name', 'State_y': 'State Abbreviation'}, inplace=True)

# Save the final merged dataset to a new CSV file
final_output_file_path = './final_merged_data.csv'
merged_data.to_csv(final_output_file_path, index=False)

final_output_file_path

