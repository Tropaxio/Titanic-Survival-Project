# The Survival of the Titanic 

In this project, we use the Titanic dataset from Kaggle available [here](https://www.kaggle.com/competitions/titanic/overview). The objective is to predict whether a given passenger survived the sinking of the Titanic. Each passenger is described by a set of attributes that the machine learning (ML) models use to learn how they relate to the probability of survival.

We evaluate several different models: Logistic Regression (our baseline model), with and without regularization and polynomial features; Random Forest; Support Vector Machines (SVMs); Gradient Boosting; and a Neural Network.

# 1. Exploratory Data Analysis

The training dataset has `891` rows and `12` columns. Of these `12` columns, one is the unique identifier of the passenger, `PassengerId`, while `Survived` is the target variable.

The test dataset has `418` rows and `11` columns.
## 1.1 Variables

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

## 1.2. General Information 

By inspecting the available features of possible interest to an ML model, we discard the `PassengerId`, the `Name` and the `Ticket` columns.  

Among the feature columns, `177` values are missing from the `Age` feature and `687` values are missing from the `Cabin` feature. The average age, number of siblings/spouses and parents/children of the passengers aboard the Titanic are `29.7`, `0.52` and `0.38`, respectively. 

Out of the `891` passengers, `549` did not survive, while `342` did survive, which accounts for a mortality rate of `61%` against a `39%` survival rate. This results in a moderately imbalanced dataset, which should be taken into account during preprocessing, model training and evaluation. The distribution shown below confirms that the dataset contains considerably more non-survivors than survivors:

<p align="center">
    <img src="/report/images/y_bar_plot.png">
</p>

Besides the target distribution, it is also useful to examine the distribution of some categorical features. Hence, we also examine the distribution of passengers by sex and embarkation ports. Most of the passengers are male, accounting for `577`, or `65%`, while there are only `314` women aboard, or `35%`.
The majority of the Titanic passengers embarked from Southampton, `72%`, followed by Cherbourg with `19%` of the passengers and Queenstown last with the remaining `9%`.

We categorize passengers into age groups to provide a more direct and concise analysis of the age distribution. For this we categorize the passenger's age into bins as follows: 
- If the passenger's age under `13` years old, they are categorised as `children`; 
- If the passenger's age is between `13` and `18` years old, they are categorised as `teenager`;
- If the passenger's age is between `18` and `64` years old, they are categorised as `adult`;
- If the passenger's age is over `64`, they are categorised as `elderly`.

As seen from the plot below, `adults` are the majority of passengers, counting for around `83%` of all passengers, followed by `children` with `9%`, `teenagers` with `6%` and lastly `elders` with `2%`:

<p align="center">
    <img src="/report/images/age_group_distribution.png">
</p>

We can also observe the distribution of survival rates across different age groups (although some `Age` data is missing as we've seen):

| Age Group | Survived | Relative Frequency of Survival | Not Survived | Relative Frequency of Not Survival  |
| ---------- | -------- | ------------------------------- | ------------ | ----------------------------------|
| Children   | 40       | 58                              | 29           | 42                                |
| Teenager   | 21       | 48                              | 29           | 52                                |
| Adult      | 228      | 39                              | 29           | 61                                |
| Elderly    | 1        | 8                               | 29           | 92                                |

As shown in the table, `children` have the highest survival rate, followed by `teenager`. A plausible explanation is that children were prioritized during the evacuation, in line with the “women and children first” protocol followed during the disaster. Teenagers also exhibit a relatively high survival rate, although not as pronounced as that of children. In contrast, `elderly` have the lowest survival rate, with approximately `92.3%` of elderly passengers not surviving. This may be attributed to reduced mobility and greater difficulty evacuating the ship under emergency conditions.

<p align="center">
    <img src="/report/images/survival_by_age_frequency.png">
</p>

Having this in mind, we can also verify the distribution of survival by sex to verify if `women` have a higher survival rate than `men`. We show those in the table below:

| Sex    | Survived | Relative Frequency of Survival | Not Survived | Relative Frequency of Not Survival |
| ------- | -------- | ------------------------------ | ------------ | ---------------------------------- |
| Female  | 233      | 74                             | 81           | 26                                 |
| Male    | 109      | 19                             | 468          | 81                                 |

In fact, `female` passengers show a much higher survival rate than `male` passengers (`74.2%` vs `18.9%`) which further validates our assumption that women and children were saved first.

<p align="center">
    <img src="/report/images/survival_rate_by_sex_frequeny.png">
</p>

## 1.3 Correlation and Skewness

(next steps)