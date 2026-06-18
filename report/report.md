# The Survival of the Titanic 

In this project we make use of the Titanic dataset from Kaggle available [here](https://www.kaggle.com/competitions/titanic/overview). The objective is to predict if a given passenger of the ship survived the wreck. Each passenger has a set of attributes that our ML models will make use in order to understand how they relate to the chance of survival.

We make use of 4 different models: Logistic Regression as our baseline model, Random Forest as our first attempt to capture non-linearity, Gradient Boosting as a more advanced model and a Neural Network.

## The Datasets 

The training dataset has 891 rows and 12 columns. Out of this 12 columns, one is a unique identifier of the passenger, `PassengerId`, 10 are assumed to be features and `Survived` is the target variable.

The test dataset has 419 rows and 11 columns (the `PassengerId` and the remaining 10 features).

### Variables

The variables presented in the dataset are:
- `PassengerId`: Unique identifier of each passenger;
- `Pclass`: The ticket class of the passenger, `1 = 1st, 2 = 2nd, 3 = 3rd`;
- `Name`: Name of the passenger;
- `Sex`: Sex of the passenger;
- `Age`: Age, in years, of the passenger;
- `SibSp`: The number of siblings / spouses aboard;
- `Parch`: Number of parents / children aboard the Titanic;
- `Ticket`: Ticket number;
- `Fare`: Passenger fare;
- `Cabin`: Cabin number;
- `Embarked`: Sort of Embarkation, `C = Cherbourg, Q = Queenstown, S = Southampton`;
- `Survived`: If the passenger survided, `0 = No, 1 = Yes`.

### Exploratory Data Analysis

