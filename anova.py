import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
pd.set_option('display.max_columns', None)
data = pd.read_csv('/Users/michael/Desktop/Applied Stats/stats-final/obesity.csv')

# Display basic stats
print("Descriptive Statistics:\n", data.describe())

# Re-running ANOVA for representative variables from each group across the 'NObeyesdad' categories

# Group 1: Weight (Physical Attributes)
model_weight = ols('Weight ~ C(NObeyesdad)', data=data).fit()
anova_weight = sm.stats.anova_lm(model_weight, typ=2)

# Group 2: NCP (Eating Habits - Number of main meals per day)
model_ncp = ols('NCP ~ C(NObeyesdad)', data=data).fit()
anova_ncp = sm.stats.anova_lm(model_ncp, typ=2)

# Group 3: FAF (Activity Level - Physical activity frequency)
model_faf = ols('FAF ~ C(NObeyesdad)', data=data).fit()
anova_faf = sm.stats.anova_lm(model_faf, typ=2)

# Displaying the results in organized tables for each group
print("\nANOVA Results - Weight (Physical Attributes):")
print(anova_weight)

print("\nANOVA Results - NCP (Eating Habits):")
print(anova_ncp)

print("\nANOVA Results - FAF (Activity Level):")
print(anova_faf)

# Optional: Visualize group differences with boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(x='NObeyesdad', y='Weight', data=data)
plt.title('Weight by Obesity Category')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='NObeyesdad', y='NCP', data=data)
plt.title('NCP (Number of Main Meals) by Obesity Category')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='NObeyesdad', y='FAF', data=data)
plt.title('FAF (Frequency of Physical Activity) by Obesity Category')
plt.show()
