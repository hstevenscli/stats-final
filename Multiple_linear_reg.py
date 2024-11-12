import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('/Users/michael/Desktop/Applied Stats/stats-final/obesity.csv')

# Convert 'Yes'/'No' in family_history_with_overweight to binary (1/0)
data['family_history_with_overweight'] = data['family_history_with_overweight'].map({'yes': 1, 'no': 0})

# Define predictors and outcome
X = data[['Height', 'family_history_with_overweight', 'Age']]
y = data['Weight']

# Add constant for intercept
X = sm.add_constant(X)

# Fit the multiple regression model
model = sm.OLS(y, X).fit()

# Print model summary
print(model.summary())

# Plot predicted values vs. actual values
plt.figure(figsize=(10, 6))
predicted_values = model.predict(X)
sns.scatterplot(x=y, y=predicted_values, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Diagonal line for perfect prediction
plt.xlabel('Actual Weight')
plt.ylabel('Predicted Weight')
plt.title('Actual vs. Predicted Weight')
plt.show()

# Partial regression plots for each predictor
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.regplot(x='Height', y='Weight', data=data, scatter_kws={'alpha':0.5}, ax=axes[0], line_kws={'color': 'red'})
axes[0].set_title('Effect of Height on Weight')
axes[0].set_xlabel('Height')
axes[0].set_ylabel('Weight')

sns.regplot(x='family_history_with_overweight', y='Weight', data=data, scatter_kws={'alpha':0.5}, ax=axes[1], line_kws={'color': 'red'})
axes[1].set_title('Effect of Family History on Weight')
axes[1].set_xlabel('Family History with Overweight')
axes[1].set_ylabel('Weight')

sns.regplot(x='Age', y='Weight', data=data, scatter_kws={'alpha':0.5}, ax=axes[2], line_kws={'color': 'red'})
axes[2].set_title('Effect of Age on Weight')
axes[2].set_xlabel('Age')
axes[2].set_ylabel('Weight')

plt.tight_layout()
plt.show()
