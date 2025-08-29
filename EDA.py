import matplotlib.pyplot as plt
import seaborn as sns

# 1. Survival count
sns.countplot(x='Survived', data=train)
plt.title("Survival Count")
plt.show()

# 2. Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=train)
plt.title("Survival by Gender")
plt.show()

# 3. Survival by Passenger Class
sns.countplot(x='Pclass', hue='Survived', data=train)
plt.title("Survival by Passenger Class")
plt.show()

# 4. Age distribution by Survival
plt.figure(figsize=(8,6))
sns.histplot(train[train['Survived']==1]['Age'], bins=20, color='green', label='Survived', kde=False)
sns.histplot(train[train['Survived']==0]['Age'], bins=20, color='red', label='Not Survived', kde=False)
plt.title("Age Distribution by Survival")
plt.legend()
plt.show()

# 5. Fare distribution by Survival
plt.figure(figsize=(8,6))
sns.boxplot(x='Survived', y='Fare', data=train)
plt.title("Fare Distribution by Survival")
plt.show()
