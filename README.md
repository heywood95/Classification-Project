# Classification-Project
 
# Project Description
 
The churn rate at Teleco will be investigated using a variety of target variables to predict customer churn using classification techniques, and make predictions for a group of customers. I have decided to look into four different areas that may affect churn rate.
 
# Project Goal
 
* Find drivers for customer churn at Telco. Why are customers churning?
* Construct a ML classification model that accurately predicts customer churn.
* Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

 
# Initial Thoughts
 
My initial hypothesis is that drivers of churn will depend on the type of service used by a customer and the amount of the montly payments.
 
# The Plan
 
* Aquire data from telco_churn database
 
* Prepare data
   * Create Engineered columns from existing data
       * online_security_Yes
       * internet_service_type_Fiber optic
       * monthly_encoded
       * monthly_charges_greater_than_80
 
* Explore data in search of drivers of upsets
   * Answer the following initial questions
       * Are customers with Fiber Optic more or less likely to churn?
       * Does the type of contract (one year, two year, or month to month) affect if a customer churns?
       * Is there a service that is associated with more churn than expected?
       * Do customers who churn have a higher average monthly spend than those who don't?
      
* Develop a Model to predict if a customer will churn
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest validate and difference accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Churn| True or False, Has the customer left the company|
|Gender| Female or Male|
|Senior Citizen| Is the customer a senior citizen, yes or no|
|Partner| Does the customer have a partner designated upon signing a contract, yes or no|
|Dependents| Are there any dependents on file for the customer, yes or no|
|Tenure| How long, in weeks, have the customer been with Telco|
|Phone Service| Does the customer have phone service, yes or no|
|Multiple Lines| Does the customer have multiple lines of service, yes or no|
|Online Security| Does the customer have online security, yes, no, or no internet|
|Online Backup| Does the customer have backup for their internet, yes, no or no internet|
|Device Protection|Does the customer have device protection, yes, no, or no internet|
|Streaming Movies|Does the customer have the ability to stream movies, yes or no|
|Streaming TV|Does the customer have the ability to stream TV, yes or no|
|Contract Type|Does the customer have a one year, two year, or month to month contract|
|Internet Service Type|What type of internet service does the customer have, fiber optic, DSL, or no internet|
|Payment Type|How does the customer pay their bill, credit card, electronic check, or mailed check|
 
# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from Codeup DB Server/telco_churn
3) Put the data in the file containing the cloned repo.
4) Run notebook.
 
# Takeaways and Conclusions
* About 43% of customers with fiber optic churned.
* About 13% of customers without fiber optic churned.
* It is more likely that customers who have fiber optic churned versus customers who did not have fiber optic.
* Month to month contracts have the highest level of churn.
* One year contracts are the next highest, but still relatively low churn.
* Two year contracts have the lowest level of churn.
* While it is no surprise that month to month contracts produce the highest level of churn, the drastic drop from month to month to one       year and two year contracts should be looked at and possible incentives or discounts for the one year and two year contracts could reduce   the amount of month to month contracts and level of churn.
* Customers with online security have 17% churn rate.
* Customers with no internet service have an 11% churn rate.
* Customers withouth online security have a 40% churn rate.
* The major contributor for customer churn is more correlated with internet services that provide security such as tech support, device       protection, online backup, and online security.
* Other services for entertainment purposes such as streaming tv and movies had less of an impact on customer churn.
* As charges increase, churn increases until the rate reaches over 100 dollars.
* The largest proportion of customers spent between 20-30 dollars.
* It would appear that the more money that was spent by the customer, the more likely they are to churn.
* The large majority of those that churned spent 500 dollars or less on total charges.
* Those customers who spent about 80 dollars a month were the most likely to churn.
* Total charges produced insufficient data to support a correlation between total charges and churn.
 
# Recommendations
* To reduce churn decrease the amount of month to month contracts and increase the amount of one and two year contracts.
* Provide online security to all of the customers, this area produced the highest probability of customer churn.
