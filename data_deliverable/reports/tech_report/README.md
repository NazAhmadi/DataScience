## 1. How many data points are there in total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? 
Hotel - 4333 hotels
Crime & cost of living Data - 377 cities
More like a regression problem, just to see how one attribute affects the other. Yes, we think is enough data to perform your analysis later on. Since the project is at a very initial stage, we can still add more data afterwards.

## 2. What are the identifying attributes?
City name, state, hotel_id

## 3. Where is the data from?
Crime data: https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/tables/table-8/table-8.xls/view 
Cost of living data: https://advisorsmith.com/data/coli/
Hotel review data: https://www.cs.cmu.edu/~jiweil/html/hotel-review.html 

#### Is the source reputable? 
Yes
#### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?
The sample represents all the cities in the United States. Since it encompasses all cities, it is large in that respect, but it is also limited since the data only comes from one year of crime statistics. There could be some bias in the particular year we are chosen since we are generalizing to the locations across all years, but there are lots of data points representing each attribute, so there is less room for bias there.

#### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)
Our original plan involved creating travel recommendations based on the attributes of the cities. We have slightly pivoted, but it’s worthwhile to mention one of our attributes – safety. In the data we have chosen, we are using FBI crime reports as a proxy for city safety. We plan to include in our final report an analysis on the usage of aggregate crime statistics (Violent crime, Murder and nonnegligent manslaughter, Rape, Robbery, Aggravated assault, Property crime, Burglary, Larceny-theft, Motor vehicle theft, Arson), how this data is and is not representative of safety, and how this data is collected and reported.

We also want to acknowledge that our data exists in two datasets; this is partially due to the aforementioned design pivot and also the fact that the data is not one-to-one and we want to preserve the data so that we can use it in different ways during the analysis.


#### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

Initial Format: The data was initially in an unclean .xls format.

Actions Taken: We eliminated the unnecessary text and converted the file to a .csv format for ease of handling. Additionally, we prepended the state name to each corresponding city to enhance clarity. This required transforming state names from their full form to abbreviations, necessitating a dictionary for this conversion, as evidenced in our code.

Challenges: The primary challenge existed in the initial format and the lack of state abbreviations, critical for merging with the cost of living data.

#### Did you implement any mechanism to clean your data? If so, what did you do? 

Initial Examination and Fill Missing Values:

The crime data was loaded from a CSV file, and an initial examination likely occurred through uncommented crime_data.head() calls.

Missing values in the 'State' column of the crime data were filled using the forward fill method (ffill). This method propagates the last valid observation forward to the next valid one, ensuring no city is left without a state due to missing values.

State Name Cleanup:

The crime data underwent further cleaning to remove numerical suffixes from the 'State' column, which might have been added inadvertently. This was achieved using a regular expression that finds and replaces digits.

State Name Standardization for Merging:

To facilitate merging with the cost of living data, the crime data needed state names in full rather than abbreviations. A dictionary mapping state abbreviations to full names was prepared and used to add a 'State Name' column to the cost of living data.

Data Merging:

The cleaned crime data and the enhanced cost of living data were merged on the city and state name columns to create a comprehensive dataset. This step required ensuring both datasets used consistent naming conventions for cities and states.

Final Adjustments:

After merging, redundant state name columns were removed to eliminate duplication.
Column names were then updated for clarity, presumably to make the dataset more intuitive for analysis.

#### Are there missing values? Do these occur in fields that are important for your project's goals? 
Missing values in the 'State' column of the crime data were filled using the forward fill method (ffill). We filled them in cleaning so they are no longer missing. 
#### Are there duplicates? Do these occur in fields that are important for your project's goals?
Yes, there was. Yes we eliminated duplication.
#### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)

Population: The distribution is heavily right-skewed, with a few cities having significantly larger populations than most others. The min/max values range from 4,220 to 8,379,043.

Violent Crime (V_crime): This field also shows a right-skewed distribution, indicating that most cities have relatively low violent crime numbers, with a few exceptions having much higher values. The range is from 5 to 47,821 incidents.

Murder, Rape, Robbery, Aggravated Assault: These fields related to specific types of violent crimes all exhibit right-skewed distributions, with most cities having low numbers but with outliers indicating higher crime rates in some areas. The maximum values for murder, rape, robbery, and aggravated assault are 492, 2,770, 13,396, and 31,336 incidents, respectively.

Property Crime, Burglary, Larceny-theft, Motor Vehicle Theft: These fields, related to property crimes, also show right-skewed distributions with several outliers, reflecting higher crime rates in certain cities. The property crime has the highest range, with values from 88 to 122,299 incidents.

Arson2: The arson data is highly skewed, with most cities reporting low numbers but with some outliers indicating higher frequencies. The range is from 0 to 1,672 incidents.

Cost of Living Index: The distribution of the cost of living index is less skewed compared to the crime-related fields but still shows some right skewness. The index ranges from 81.3 to 178.6, indicating variation in the cost of living across different cities.

Overall, the data is characterized by right-skewed distributions in most fields, especially those related to crime, suggesting that a majority of cities have lower crime rates with a few exceptions having significantly higher rates. There are noticeable outliers in almost all fields, indicating extreme values that are far from the mean. The min/max values provide a sense of the range and scale of the data across different metrics.

#### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them? 
Yes, some text in crime data which is eliminated. Some numbers in state name coming from converting data to .csv format. We eliminate any number after the letters in state full name column.
#### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw? 
Yes, the duplication and the crime index data for cities which we dont have any data for their cost of living.

