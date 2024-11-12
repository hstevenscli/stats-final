import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('/Users/michael/Desktop/Applied Stats/stats-final/obesity.csv')

# Define the predictor (independent variable) and outcome (dependent variable)
X = data['Height']  # Height as the best predictor
y = data['Weight']  # Weight as the dependent variable

# Add a constant to the predictor variable (for the intercept in statsmodels)
X = sm.add_constant(X)

# Fit the regression model
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())

# Plot the data and the regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Height', y='Weight', data=data, label="Data Points")
plt.plot(data['Height'], model.predict(X), color='red', label="Regression Line")
plt.xlabel('Height (m)')
plt.ylabel('Weight (kg)')
plt.title('Simple Linear Regression: Weight vs. Height')
plt.legend()
plt.show()
