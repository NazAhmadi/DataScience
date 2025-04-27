# Presentation
We uploaded our recorded presetation video on youtube.
[Click here for the video](https://youtu.be/6pdXso0WR9k)


# Analysis

## Hypothesis testing component
The group must formulate a minimum of three distinct research hypotheses and test them using a statistical testing method.

### 1. Cities with higher median family incomes will have lower crime rates.
crime rate = sum(crimes) / population

#### Why did you use this statistical test or ML algorithm?
I used  statistical tests: T-Test and Chi-Squared

#### Which other tests did you consider or evaluate?
I used Chi-squared. This was used alongside the t-test to provide a more comprehensive analysis of the relationship.

#### Did you have to clean or restructure your data?
Yes, data cleaning was essential, especially for removing NaN values that could interfere with statistical testing. The data contained commas within numbers, which needed to be removed to convert the values to integers. Furthermore, the restructuring of the data required categorizing continuous data into discrete bins, determined by the mean values for the Chi-squared test. It was also necessary to ensure that all data types were correctly formatted for analysis. Additionally, the crime rate calculation involved summing up all categories of crimes and then dividing by the city's population to obtain a crime rate per capita.

#### What is your interpretation of the results?
The results from the t-test suggested a non-significant trend where cities with above-average(or median) median family incomes tend to have lower crime rates, although not conclusively at the 5% significance level. The Chi-squared test indicated a significant association between income levels and crime rate categories, suggesting some dependency between economic status and crime rates. As a result, A larger number of cities with above-average income have a below-average crime rate compared to those with an above-average crime rate. Similarly, cities with below-average income have more occurrences of below-average crime rates, but the ratio of above to below-average crime rates is closer than in the above-average income group.

#### Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
Based on the t-test, I would not conclusively accept the hypothesis due to the varying p-values (both significant and non-significant results) observed under different criteria for splitting between median family income groups. This suggests that additional data or alternative analytical approaches might be required. The Chi-squared test supports the hypothesis of an association between income levels and crime rates; however, this does not directly imply causality or ensure robust prediction accuracy.

#### Intuitively, how do you react to the results?
The results make sense as higher income areas might have more resources for crime prevention and community programs, leading to lower crime rates. However, the weak correlation and non-significant t-test result caution against overgeneralization.

#### Are you confident in the results
I can say that the results are as reliable as the data and the methodology employed. However, it is essential to remember that statistical tests can only indicate the presence or absence of a statistically significant effect or association; they do not confirm causation. Additional analyses, possibly with more comprehensive data and consideration of more variables, would bolster confidence in the findings.




### 2. Cities that are more densely populated have higher crime rates.
#### Why did you use this statistical test or ML algorithm? 
We used a one-way ANOVA test, breaking density into 5 categories according to [Urban Observatory](https://www.urbanobservatory.org/compare/index.html?group%3Df4373b6eae144e26a634937269d336ec%26noun%3DPeople%26theme%3DPopulation%2520Density%26cities%3DNew%2520York%26cities%3DPeterborough%26cities%3DTokyo%26minLevel%3D8%26level%3D9%26maxLevel%3D16%26dualPane%3Dfalse). We chose an ANOVA because we had 5 samples which were not paired.

#### Which other tests did you consider or evaluate?
We started by considering a Chi-squared test, but found it better to avoid breaking crime rates into categories unnecessarily. We refined our goal to fit more appropriately to an ANOVA with 5 categorical variables.

#### Did you have to clean or restructure your data?
We created a “crime rate” value, which is the sum of all crimes in the city per person in the city. Additionally, we broke the density values into 5 categories: "Very High", "High", "Medium", "Low", and "Very Low".

#### What is your interpretation of the results?
The results from the ANOVA were not statistically significant (F=0.0622, p=0.9929). The result is corroborated by inspecting the mean crime rates for each density category, which do not differ greatly.

#### Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? 
Since the result of our test was not statistically significant, we do not have evidence to support the notion that cities that are more densely populated have higher crime rates. We are satisfied with the accuracy of the result, since the p-value is not near our boundary of acceptance (alpha=0.05).

#### Intuitively, how do you react to the results?
The result is somewhat surprising, since we formulated the hypothesis with the preconception that more dense cities would have higher crime rates. Interestingly, “Very Low” density cities had the highest average crime rates, and “Low” density cities had the highest average total number of crimes.

#### Are you confident in the results?
We are fairly confident in our results, since we have faith in the data we have collected and the statistical test we have chosen.




### 3. Cities with higher number of property crimes also have higher housing tests.
Cities in the upper third/half of property crime are also in the upper third of housing costs.

According to the dataset of the cities that we have, do cities where property crime rates rank within the upper third or half, have a corresponding trend of higher housing costs?

#### Why did you use this statistical test?
The chi-squared test is used because it assesses whether there's a significant association between two categorical variables—property crime levels and housing cost levels. It's appropriate because both variables are categorical, and we're interested in determining if they're independent or related. This test compares observed frequencies with expected frequencies under the assumption of independence, allowing us to formally test hypotheses about the association between the variables. 

#### Which other tests did you consider or evaluate?
When evaluating tests to assess the relationship between Property crime and Housing cost, we initially considered the t-test due to its suitability for comparing the means of two continuous variables. The t-test stat was around -184.67423824469677 with a p-value: 0.0.The t-test results indicate a highly significant difference between the means of the Property crime and Housing cost columns. 

#### What metric(s) did you use to measure success or failure, and why did you use it?
In this analysis, the metric used to measure success or failure was the p-value obtained from the chi-squared test.

#### What challenges did you face evaluating the model?
The primary challenge faced in evaluating the model was the nature of the data columns being analyzed. Both Property crime and Housing cost were numerical variables, which initially led to the consideration of parametric tests like the t-test for assessing the relationship between them. However, as the analysis progressed, it became evident that the assumptions of the t-test might not be entirely met, potentially affecting the validity of the results.

#### Did you have to clean or restructure your data?
To prepare the data for analysis, we categorized both the housing cost and property crime variables into discrete groups. For housing cost, we created categories of 'Low', 'Medium', and 'High' based on quantiles. Similarly, for property crime, we categorized it into 'Low Crime', 'Medium Crime', and 'High Crime'. This allowed us to analyze the association between the two variables using the chi-squared test. We also removed the NaN values that could interfere with statistical testing. The data contained commas within numbers, which needed to be removed to convert the values to integers as well. It was also necessary to ensure that all data types were correctly formatted for analysis.

#### What is your interpretation of the results?
The results indicate a significant association between Property crime and Housing cost categories. With a chi-squared statistic of approximately 451.93 and an extremely low p-value of about 1.66e-96, we reject the null hypothesis of independence. This suggests that areas with different levels of Property crime also exhibit distinct patterns of Housing cost, and vice versa.

#### Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? 
With a chi-squared statistic of approximately 451.93 and an extremely low p-value of about 1.66e-96, we reject the null hypothesis of independence. 

#### Intuitively, how do you react to the results?
Intuitively, the results align with expectations. It's not surprising to find a significant association between Property crime and Housing cost. Higher levels of Property crime often correlate with areas of lower socioeconomic status, where housing may be less affordable or of lower quality. Conversely, neighborhoods with lower crime rates may tend to have higher housing costs due to factors such as perceived safety and desirability.

#### Are you confident in the results?
Yes, we are confident in the results. The chi-squared test is a widely accepted statistical method. With a large chi-squared statistic and an extremely low p-value, the evidence strongly supports the conclusion that there is a significant association between Property crime and Housing cost categories. Additionally, the sample size and degrees of freedom provide further support for the reliability of the results.


## Machine learning component
You should use at least two of the Machine Learning techniques shown in class. You can use either a supervised or unsupervised learning method. 

### 1. Regression
Predict total_cost based on ('housing_cost', 'taxes', 'other_necessities_cost', 'median_family_income','Crime Rate’)

#### Why did you use this statistical test or ML algorithm?
Linear regression is a straightforward, interpretable model that is excellent for understanding relationships between multiple independent variables (like crime rate, housing cost, taxes, and median family income) and a dependent variable (total cost).

#### Which other tests did you consider or evaluate?
Besides linear regression, we considered regularization techniques like Ridge, Lasso, and Elastic Net regression. These methods help prevent overfitting and are particularly useful when dealing with multicollinearity or when you need to improve the model's generalizability by penalizing the magnitude of the coefficients.

#### What metric(s) did you use to measure success or failure, and why did you use it?
We used the R² score to measure the performance of the model, which provides an understanding of the amount of variance in the dependent variable that can be explained by the independent variables in the model. A higher R² value indicates a better fit of the model to the data. Additionally, Mean Squared Error (MSE) was considered to quantify the model's prediction error.

#### What challenges did you face evaluating the model?
Challenges included handling missing values and ensuring the model did not overfit. Missing data required imputation, and model complexity had to be managed through regularization. Ensuring the model’s robustness involved using cross-validation techniques to validate results across multiple subsamples of the data.

#### Did you have to clean or restructure your data?
Yes, data cleaning involved imputing missing values and selecting relevant features for the model by the help of correlation matrix. This step was crucial to prevent errors during model training and to improve the model’s accuracy.

#### What is your interpretation of the results?
The results from the cross-validation and regularization techniques suggest that the model is quite robust, as indicated by the consistently high R² values across different models and folds. This implies a strong explanatory power of the selected features on the total cost. 

#### Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
The hypothesis that the independent variables selected ('housing_cost', 'taxes', 'other_necessities_cost', 'median_family_income','Crime Rate’) significantly influence the total cost can be accepted. The prediction accuracy is satisfactory.

#### For prediction projects, we expect you to argue why you got the accuracy/success metric you have.
The accuracy achieved can be attributed to several factors: careful selection of relevant features, proper handling of missing data, and the use of regularization to enhance the model’s generalizability. Moreover, the nature of the data and the linear relationships assumed in the hypothesis seem to align well, which often results in higher performance metrics.

#### Intuitively, how do you react to the results?
The results are encouraging as they confirm the expected influences of economic factors on total costs. The high R² values reinforce confidence in the model's predictions and its usefulness in real-world applications.

#### Are you confident in the results?
Yes, The use of cross-validation and regularization further supports the reliability of the model in predicting new, unseen data.

![download](https://github.com/csci1951a-spring-2024/final-project-coolerthanicecream/assets/77646409/423c3e6a-1440-4490-81ca-8016f0530cda)

### 2. Clustering
#### Why did you use this statistical test or ML algorithm?
We chose K-Means clustering because we wanted to group cities together by their common attributes. We did not have access to accurate and clearly defined labels, so we chose an unsupervised learning algorithm. 

#### Which other tests did you consider or evaluate?
We considered using a multi-class classification algorithm that used supervised learning, using “importance ranking” as the label. Upon further inspection, however, we found that the data was not particularly interesting (it only had 2 values) and was not well defined, since we are unaware of how importance was assigned to each city. As such, an unsupervised learning algorithm was chosen.

#### What metric(s) did you use to measure success or failure, and why did you use it?
We ran a K-fold cross-validation to test our model. We did this so that we could test different unique parts of the data for validation, which allows us to have much more validation data than we otherwise would have.

#### What challenges did you face evaluating the model?
Aside from the aforementioned change from supervised learning to unsupervised, we had some other challenges involving the clusters. First, we had a hard time choosing the number of distinct clusters, since the elbow curve plot we generated suggested using 3 clusters, but that seemed like not enough to capture the data; it did end up the best, however. Additionally, the clusters that Kmeans finds are slightly overlapping, making the distinctions not very clear between clusters.

#### Did you have to clean or restructure your data?
Other than the “Crime rate” column which was added for other analyses and the NaN values discussed earlier, we also applied min-max scaling to normalize the data. 

#### Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
The mean accuracy using 5-fold cross-validation was 0.66. We are satisfied with this accuracy, because we expected cities to share lots of attributes and fall into “archetypes” which would become clusters.

#### For prediction projects, we expect you to argue why you got the accuracy/success metric you have.
The accuracy of 0.66 is good, but not incredibly high. We expect this has to do with the shape of the data. See below for a visualization of the clusters (using PCA with 3 dimensions so it can be visualized). As can be seen, the clusters to group some similar data points together, but also fails to capture some of the nuance of the shape of the data. As such, we feel a 0.66 accuracy is appropriate.

![download](https://github.com/csci1951a-spring-2024/final-project-coolerthanicecream/assets/77646409/e8fe5fa0-063b-4716-8aaa-0a81f362a8cd)

#### Intuitively, how do you react to the results?
We expected to see a much higher accuracy (especially after completing the linear regression, which had a very high confidence). We are pleased to see an accuracy above chance, but intuitively expected an even higher accuracy.

#### Are you confident in the results?
With an average accuracy of 0.66, we are fairly confident in the results, but are not too overconfident, since a different model might have captured this shape better. That being said, we are still confident in our current model.


## Provide comments and an interpretation of the results you obtained
#### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?
For some results, the outcome aligned with our hypotheses (such as H1, H3, regression, and clustering); for others, it did not (such as H1, H2, and clustering). Additionally, some results partially corroborated our initial beliefs. For each of these cases, the difference simply comes down to our initial beliefs not aligning with the data we found; we concede that it could either be the case that our beliefs were incorrect, or be based our beliefs on different data that we did not choose for analysis.

#### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?
Yes, we believe that the tools were appropriate. In each case, we carefully considered the question we wanted to answer and chose the best tool to answer it. Additionally, for many of the questions, we had to pivot after starting the analysis to better fit our original intentions, furthering our confidence that we considered multiple options and chose the best one.

#### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?
In terms of the questions presented in this report, we do believe that the data is sufficient. We would not have been able to confidently achieve out original goals (before data collection) with the data we ended up with, so we had to pivot to answering questions that were better suited to our data. As a fortunate consequence of that, we believe that our data is very well-suited for answering our questions here.



