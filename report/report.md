# The Survival of the Titanic 

In this project, we use the Titanic dataset from Kaggle available [here](https://www.kaggle.com/competitions/titanic/overview). The objective is to predict whether a given passenger survived the sinking of the Titanic. Each passenger is described by a set of attributes that the machine learning (ML) models use to learn how they relate to the probability of survival.

We evaluate several different models: Logistic Regression (our baseline model), with and without regularization and polynomial features; Random Forest; Support Vector Machines (SVMs); Gradient Boosting; and a Neural Network.

# 1. Exploratory Data Analysis 

## 1.1 The Dataset

The training dataset has `891` rows and `12` columns. Of these `12` columns, one is the unique identifier of the passenger, `PassengerId`, while `Survived` is the target variable.

The test dataset has `418` rows and `11` columns (the `PassengerId` and the remaining 10 features).

### 1.1.1 Variables

The variables presented in the dataset, together with their data types are:
- `PassengerId`: Unique identifier of each passenger, `int`;
- `Pclass`: The ticket class of the passenger, `1 = 1st, 2 = 2nd, 3 = 3rd`, `int`;
- `Name`: Name of the passenger, `object`;
- `Sex`: Sex of the passenger, `object`;
- `Age`: Passenger's age, in years, `int`;
- `SibSp`: The number of siblings/spouses aboard, `int`;
- `Parch`: Number of parents/children aboard the Titanic, `int`;
- `Ticket`: Ticket number, `object`;
- `Fare`: Passenger fare, `float`;
- `Cabin`: Cabin number, `object`;
- `Embarked`: Port of embarkation, `C = Cherbourg, Q = Queenstown, S = Southampton`, `object`;
- `Survived`: If the passenger survived, `0 = No, 1 = Yes`, `int`.

This concludes the information about the columns of the dataset. In the next subsection, we explore general statistics about our variables.

### 1.1.2 General Information 

By inspecting the available features of possible interest to an ML model, we discard the `PassengerId`, the `Name` and the `Ticket` columns.  

Among the feature columns, `177` values are missing from the `Age` feature and `687` values are missing from the `Cabin` feature. The average age, number of siblings/spouses and parents/children of the passengers aboard the Titanic are `29.7`, `0.52` and `0.38`, respectively. 

Out of the `891` passengers, `549` did not survive, while `342` did survive, which accounts for a mortality rate of `61%` against a `39%` survival rate. This results in a moderately imbalanced dataset, which should be taken into account during preprocessing and model evaluation. The distribution shown below confirms that the dataset contains considerably more non-survivors than survivors:

<p align="center">
    <img src="/report/images/y_bar_plot.png">
</p>

Besides the target distribution, it is also useful to examine the distribution of some categorical features. Hence, we also examine the distribution of passengers by sex and embarkation ports. Most of the passengers are male, accounting for `577`, or `65%`, while there are only `314` women aboard, or `35%`.
The majority of the Titanic passengers embarked from Southampton, `72%`, followed by Cherbourg with `19%` of the passengers and Queenstown last with the remaining `9%`.

Lastly, we categorize passengers into age groups to provide a more direct and concise analysis of the age distribution.

(insert conclusion of this section)

### 1.1.3 Correlation and Skewness