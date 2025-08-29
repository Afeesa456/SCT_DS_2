import pandas as pd

train = pd.read_csv("train (1).csv")

# Show first 5 rows
train.head()


# Fill missing Age with median
train['Age'] = train['Age'].fillna(train['Age'].median())

# Fill missing Embarked with mode
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])

# Check missing values again
print(train.isnull().sum())



