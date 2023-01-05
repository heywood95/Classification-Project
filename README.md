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
|Winning Pieces| The color of pieces the winning player was moving|
|White Rating| Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess|
|Black Rating| Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess|
|Rating Difference| The difference in rating between the players in the game|
|Game Rating| The average rating of the two players in the game|
|Lower Rated White| True or False, The lower rated player is moving the white pieces|
|Opening Name| The name of the opening played in the game|
|Time Control Group| The amount of time allotted to each player to make their moves, **Standard** (60 min or more), **Rapid** (30 - 15 min), **Blitz** (5 - 3 min), or **Bullet** (2 or less), **Other** (any other time limit)|
|Upset (Target)| True or False, The lower rated player won the game|
|Additional Features|Encoded and values for categorical data and scaled versions continuous data|
 
# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from [Kaggle](https://www.kaggle.com/datasnaek/chess)
3) Put the data in the file containing the cloned repo.
4) Run notebook.
 
# Takeaways and Conclusions
* Upsets occur in 1/3 of games
* In games where the lower rated player moves first there is a 4% greater chance of an upset
* Games that are rated have a 3% higher chance of an upset
* Games with a "quick" time control (30 min or less) have about a 1 in 3 chance of upset
* Games with a "slow" time control (60 min or more) have about a 1 in 5 chance of upset
* The mean rating of players in a game is not a driver of upsets
* The difference in player rating is a driver of upsets
* A player's choice of opening is a driver of upsets, however its influence is complicated and I would need more time to discover what role it plays
 
# Recommendations
* To increase the skill intensity of a game add to the length of time players are able to consider their moves
* Based on the data longer time controls make it less likely for a less skilled player to beat a more skilled player
