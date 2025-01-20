# Cost of Living Index: 
Type of data that will be used for the representation: float/number

Default value: 100 (defined as the average cost of living in the US)

Range of value : [97.018833 , 178.6]

Simplified analysis of the distribution of values

Distribution:

count    377.000000

mean      97.018833

std       13.515109

min       81.300000

25%       88.300000

50%       92.800000

75%      101.700000

max      178.600000

Are these values unique? No, the Number of Unique values: 216

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? no

Is this a required value? yes

Do you plan to use this attribute/feature in the analysis? If so, how?
Yes, the cost of living is the only data we have about the city, which can be used to infer the cost of traveling to / visiting that city. Therefore, it is one attribute that should be considered when analyzing travel locations based on budget.

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?

Cost of living data typically includes information on expenses such as housing, utilities, groceries, transportation, and healthcare, among other basic needs. While this data is generally not sensitive in terms of personal privacy (since it's aggregated and anonymized), it can highlight economic disparities between different regions, which might be sensitive from a socio-economic perspective.

# City: 
Type of data that will be used for the representation: string/text

Default value: NA

Range of value: NA

Simplified analysis of the distribution of values: NA

Are these values unique?
Number of Unique Values: 358. Not all values for this attribute are unique since some cities share the same name. To distinguish between them, it's necessary to include the state name as well.

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?
Yes, we will use city names in conjunction with state names to merge cost of living data with safety data. These fields in combination also help in identifying and managing potential duplicate records effectively.

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how?
Yes, city names will be integral to our analysis as they directly relate to the locations we recommend based on budget and safety rankings. Furthermore, the analysis will investigate possible correlations between a city's population and its cost of living, along with safety and crime indexes. This process involves statistical analysis to uncover patterns or connections that could lead to more informed travel recommendations.

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?
City names, populations, and cost of living data are generally not considered sensitive information as they are usually publicly available and do not pertain to individual privacy. However, when combining this data with safety and crime indexes, care must be taken to ensure that the analysis does not inadvertently stigmatize certain locations or communities.

# Population: 
Type of data that will be used for the representation: Integer values

Default value: In thousands or millions (NA)

Range of value: [4220, 8379043]

Simplified analysis of the distribution of values
Distribution:
count    3.770000e+02
mean     1.689528e+05
std      5.423131e+05
min      4.220000e+03
25%      3.128100e+04
50%      5.797300e+04
75%      1.226570e+05
max      8.379043e+06

Are these values unique? Yes

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? No

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how? Population count could have an effect on the living cost and other attributes a lot. 

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? No
# V_crime 
Type of data that will be used for the representation: Integer	

Default value: A number in thousands

Range of value. [5, 47821]

Simplified analysis of the distribution of values 
Distribution:
count      377.000000
mean      1186.068966
std       3789.149158
min          5.000000
25%        110.000000
50%        292.000000
75%        782.000000
max      47821.000000

Are these values unique? No

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? No

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how? Yes, it will be required in our analysis. We will use it in the analyses related to crime and safety.

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? No
# Address: 
Type of data that will be used for the representation: a string containing the region, street address and postal code of the hotel

Default value address: {"region": "NY", "street-address": "147 West 43rd Street", "postal-code": "10036", "locality": "New York City"}

Range of value: NA

Simplified analysis of the distribution of values: NA

Are these values unique? Yes

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?  Since the values are unique, we could use them to detect duplicates.

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how? Yes, we will utilize the city name to associate it with our analysis

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? No, they are publicly available address
# Hotel Class / Rating: 
Type of data that will be used for the representation: floating point number

Default value: NA

Range of value [1.0,5.0]

Simplified analysis of the distribution of values: Possible values - [1.0, 1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
Are these values unique? No

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? NA

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how? Yes, we will utilize the hotel class to associate it with our analysis 

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? No
# Robbery
Type of data that will be used for the representation: integer

Default value: NA

Range of value [0,13396]

Simplified analysis of the distribution of values
Distribution:
count      377.000000
mean       303.668435
std       1151.518904
min          0.000000
25%         15.000000
50%         48.000000
75%        148.000000
max      13396.000000

Are these values unique? No

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? No

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how? Yes, it will be required in our analysis. We will use it in the analyses related to crime and safety.

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? No
# Burglary
Type of data that will be used for the representation: integer

Default value NA

Range of value. [2,17,038]

Simplified analysis of the distribution of values
Distribution:
count      377.000000
mean       831.450928
std       1801.067811
min          2.000000
25%        126.000000
50%        269.000000
75%        703.000000
max      17038.000000

Are these values unique? No

Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how? No

Is this a required value? Yes

Do you plan to use this attribute/feature in the analysis? If so, how?  Yes, it will be required in our analysis. We will use it in the analyses related to crime and safety.

Does this feature include potentially sensitive information? If so, how do you suggest handling such issues? No

