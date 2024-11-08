import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
data = pd.read_csv("obesity.csv")
print(data.describe())

# data['Gender_m'] = data['Gender'].map({'Male':1, 'Female':0})

# Map the 'NObeyesdad' classes to numeric values
NObeyesdad_mapping = {
    'Insufficient_Weight': 1,
    'Normal_Weight': 2,
    'Overweight_Level_I': 3,
    'Overweight_Level_II': 4,
    'Obesity_Type_I': 5,
    'Obesity_Type_II': 6,
    'Obesity_Type_III': 7
}

data['NObeyesdad'] = data['NObeyesdad'].map(NObeyesdad_mapping)

# Map the 'family_history_with_overweight' classes to numeric values

family_history_mapping = {
    'yes': 1,
    'no': 0
}
data['family_history'] = data['family_history_with_overweight'].map(family_history_mapping)

SMOKE_mapping = {
    'yes': 1,
    'no': 0 
}
data['SMOKE'] = data['SMOKE'].map(SMOKE_mapping)



# plt.savefig("./charts/fev_and_smoking_barplot.png")
# plt.close()



# Male and Female Pie chart

lbl = ["Male", "Female"]
data['Gender'].value_counts().plot.pie(labels=lbl)
plt.title("Number of Males and Females")
plt.savefig("./charts/gender_pie.png")
plt.close()

# Histogram of Ages
plt.figure()
data['Age'].hist()
plt.title("Age Range")
plt.savefig("./charts/age_histogram.png")
plt.close()
# plt.show()

# smokers = data.groupby(['Smoke'])




# Create a scatter plot comparing Height and Weight, colored by the 'NObeyesdad' class
plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['Height'], data['Weight'], c=data['NObeyesdad'], cmap='viridis', alpha=0.5)

# Add labels and title
plt.title("Comparison of Height and Weight by Obesity Level", fontsize=16)
plt.xlabel("Height (m)", fontsize=12)
plt.ylabel("Weight (kg)", fontsize=12)

# Add a color bar to show what the colors represent
plt.colorbar(scatter, label='Obesity Class')

plt.savefig("./charts/scatter_color_nobesity.png")
plt.close()
# Display the plot

# Histogram of FAF
plt.figure()
data['FAF'].hist()
plt.title("Physical Activity")
plt.savefig("./charts/physical_activity_histogram.png")
plt.close()
# plt.show()


# SMOKING BAR GRAPH
plt.figure(figsize=(10, 6))

# Create a barplot to show the count of smokers and non-smokers across different obesity classes
sns.countplot(x='NObeyesdad', hue='SMOKE', data=data, palette='coolwarm')

# Add labels and title
plt.title("Obesity Levels by Smoking Status", fontsize=16)
plt.xlabel("Obesity Class", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Display the plot
plt.savefig("./charts/obesity_by_smoking.png")
plt.close()
# plt.show()

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Add title
plt.title("Correlation Heatmap of Variables", fontsize=16)

# Display the heatmap
plt.savefig("./charts/heatmap.png")
plt.close()
# plt.show()



# Create a box plot for Physical Activity Frequency (FAF) by Obesity Class
plt.figure(figsize=(10, 6))
sns.boxplot(x='NObeyesdad', y='FAF', data=data)

# Add labels and title
plt.title("Physical Activity Frequency by Obesity Class", fontsize=16)
plt.xlabel("Obesity Class", fontsize=12)
plt.ylabel("Physical Activity Frequency (FAF)", fontsize=12)

# Display the plot
plt.savefig("./charts/boxplot.png")
plt.close()
# plt.show()

