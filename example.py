import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./FEV-1.csv")
print("Stats on the data:\n", data.drop(columns="Id").describe())
print()

data['Age'].plot(kind='box')
plt.title("Boxplot of Age, boys and girls")
plt.savefig("./charts/age_boxplot.png")
plt.close()

data['FEV'].plot(kind='box')
plt.title("FEV of boys and girls")
plt.savefig("./charts/fev_boxplot.png")
plt.close()

data['Hgt'].plot(kind='box')
plt.title("Heights of boys and girls")
plt.savefig("./charts/height_boxplot.png")
plt.close()

data.drop(columns="Id").hist()
plt.savefig("./charts/histograms.png")
plt.close()

data['Age'].value_counts().plot.pie()
plt.title("Ages of boys and girls")
plt.savefig("./charts/age_pieplot.png")
plt.close()

lbl = ["Male", "Female"]
data['Sex'].value_counts().plot.pie(labels=lbl)
plt.title("Number of Males and Females")
plt.savefig("./charts/sex_pieplot.png")
plt.close()

data["Gender_m"] = data["Sex"]
print()
print("Number of Males:", np.sum(data["Gender_m"]))
print()

smoke = data[data['Smoke']==1]
nosmoke = data[data['Smoke']==0]
print("Stats on smokers:\n", smoke.drop(columns="Id").describe())
print()
print("Stats on non-smokers:\n", nosmoke.drop(columns="Id").describe())
print()

smoke_b = data[(data['Smoke']==1) & (data['Sex'] ==1)]
smoke_g = data[(data['Smoke']==1) & (data['Sex'] ==0)]

print("Stats on boys who smoke:\n", smoke_b.drop(columns="Id").describe())
print()
print("Stats on girls who smoke:\n", smoke_g.drop(columns="Id").describe())
print()

# plt.boxplot([smoke['FEV'], nosmoke['FEV']])
# plt.title("Smokers and non-smokers")
# plt.close()

smoke_bar = data["Smoke"].value_counts().plot.bar(title="Do They Smoke")
print("Number of smokers:\n", data["Smoke"].value_counts())
print()
smoke_bar.set_xlabel("")
smoke_bar.set_ylabel("Number")
smoke_bar.set_xticklabels(["No", "Yes"])
plt.savefig("./charts/smoking_count.png")
plt.close()


# fev_smoke = data.groupby(["Smoke"])['FEV'].value_counts()
# print(fev_smoke)
barpl = sns.barplot(data=data, x='Smoke', y='FEV', palette=['red', 'skyblue'])
barpl.set_xticklabels(["No", "Yes"])
plt.title("Smoking and FEV: Boys and Girls")
plt.savefig("./charts/smoke_barplot.png")
plt.close()


height_bar = data["Hgt"].value_counts().sort_index().plot.bar(title="Heights")
height_bar.set_xlabel("")
height_bar.set_ylabel("Number of People")
plt.savefig("./charts/age_counts_barplot.png")
plt.close()

# print(data["Age"])

## ii

bins = [0,4,9,14,19]
labels = ['3-4', '5-9', '10-14', '15-19']

data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=True)
sex_group_stats = data.groupby("Sex")
boys_data = sex_group_stats.get_group(1)
girls_data = sex_group_stats.get_group(0)




boy_age_group_stats = boys_data.groupby('AgeGroup').mean()
girl_age_group_stats = girls_data.groupby('AgeGroup').mean()

girl_height_group_stats = girls_data.groupby("Hgt").mean()
boy_height_group_stats = boys_data.groupby("Hgt").mean()

# print(boy_age_group_stats)
# print(girl_age_group_stats)

# print(girl_height_group_stats)
# print(boy_height_group_stats)

##################### Mean fev by age group

fev_mean_by_age = data.groupby(['Sex', 'AgeGroup'])['FEV'].mean().unstack()

print("FEV and Age:\n", fev_mean_by_age)
print()

fev_mean_by_age.T.plot(kind='line', marker='o')

plt.title('Mean FEV by Age for Boys and Girls')
plt.xlabel('Age')
plt.ylabel('Mean FEV')
plt.legend(['Girls', 'Boys'], title="Sex")
plt.grid(True)
plt.savefig("./charts/fev_and_age_lineplot.png")
plt.close()


##################### FEV and Smoking

fev_mean_by_smoking = data.groupby(['Sex', 'Smoke'])['FEV'].mean().unstack()

fev_mean_by_smoking.T.plot(kind='bar').set_xticklabels(["No", "Yes"])
print("FEV and Smoking:\n", fev_mean_by_smoking)
print()
plt.title("FEV and smoking")
plt.xlabel("Smoker")
plt.ylabel("FEV")
plt.legend(["Girls", "Boys"], title="Sex")
plt.savefig("./charts/fev_and_smoking_barplot.png")
plt.close()


##################### FEV and Height

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
fev_mean_by_height = data.groupby(['Sex', 'Hgt'])['FEV'].mean().unstack()
fev_mean_by_height.T.plot(kind='line', marker='o')
print("FEV and Height\n", fev_mean_by_height)
plt.title('Mean FEV and Height')
plt.xlabel('Height')
plt.ylabel('FEV')
plt.legend(['Girls', 'Boys'], title="Sex")
plt.grid(True)
plt.savefig("./charts/fev_and_height_lineplot.png")
plt.close()

##################### Correlation Coefficients

boys_fev_age_corr = boys_data['FEV'].corr(boys_data['Age'])
boys_fev_height_corr = boys_data['FEV'].corr(boys_data['Hgt'])
boys_fev_smoking_corr = boys_data['FEV'].corr(boys_data['Smoke'])

# Calculate correlations for girls
girls_fev_age_corr = girls_data['FEV'].corr(girls_data['Age'])
girls_fev_height_corr = girls_data['FEV'].corr(girls_data['Hgt'])
girls_fev_smoking_corr = girls_data['FEV'].corr(girls_data['Smoke'])

print("Boys: FEV to Age Correlation:", boys_fev_age_corr)
print("Boys: FEV to Height Correlation:", boys_fev_height_corr)
print("Boys: FEV to Smoking Correlation:", boys_fev_smoking_corr)

print("Girls: FEV to Age Correlation:", girls_fev_age_corr)
print("Girls: FEV to Height Correlation:", girls_fev_height_corr)
print("Girls: FEV to Smoking Correlation:", girls_fev_smoking_corr)




'''
Notes
assess the relationship of potability to the 
different qualities of water for different
sites


plot mean hardness for potable and nonpotable water on the same plot
to show the average. instead of doing the same thing on two different plots.

Bar plot,
plot potable water mean hardness (70%) and nonpotable water mean hardness (50%)
on the same bar graph next to each other, so you can visually see the difference
'''

########################### Water potability


data = pd.read_csv("./water_potability_new.csv")
data.describe()

print(data.describe())

data.drop(columns=['Id', 'site']).hist()
plt.savefig("./charts/water_overall_hist.png")
plt.close()

##### Looking at the effect of PH on potability

ph_mean_potability = data.groupby(['Potability'])['ph'].mean()
print(ph_mean_potability)
ph_mean_potability.plot(kind='bar')
plt.savefig("./charts/ph_potability_barplot.png")
plt.close()

potable = data[data['Potability'] == 1]
nonpotable = data[data['Potability'] == 0]

print(potable.describe())
print(nonpotable.describe())

####### hardness and potability
combined = data[['Hardness', 'Potability']]
combined.boxplot(column='Hardness', by='Potability')
plt.title('Hardness of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Hardness")
plt.savefig('./charts/hardness_and_p_boxplot.png')
plt.close()

########## solids and potability

combined = data[['Solids', 'Potability']]
combined.boxplot(column='Solids', by='Potability')
plt.title('Solids of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Solids")
plt.savefig('./charts/solids_and_p_boxplot.png')
plt.close()


########## Trihalomethanes and potability

combined = data[['Trihalomethanes', 'Potability']]
combined.boxplot(column='Trihalomethanes', by='Potability')
plt.title('Trihalomethanes of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Trihalomethanes")
plt.savefig('./charts/tri_and_p_boxplot.png')
plt.close()

######### Chloramines and potability


combined = data[['Chloramines', 'Potability']]
combined.boxplot(column='Chloramines', by='Potability')
plt.title('Chloramines of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Chloramines")
plt.savefig('./charts/chloramines_and_p_boxplot.png')
plt.close()


######### Sulfate and Potability


combined = data[['Sulfate', 'Potability']]
combined.boxplot(column='Sulfate', by='Potability')
plt.title('Sulfate of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Sulfate")
plt.savefig('./charts/boxplot.png')
plt.close()

########## Conductivity and Potability


combined = data[['Conductivity', 'Potability']]
combined.boxplot(column='Conductivity', by='Potability')
plt.title('Conductivity of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Conductivity")
plt.savefig('./charts/conductivity_and_p_boxplot.png')
plt.close()

############# Organic_carbon and Potability

combined = data[['Organic_carbon', 'Potability']]
combined.boxplot(column='Organic_carbon', by='Potability')
plt.title('Organic_carbon of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Organic_carbon")
plt.savefig('./charts/orgc_and_p_boxplot.png')
plt.close()

############## Turbidity and Potability

combined = data[['Turbidity', 'Potability']]
combined.boxplot(column='Turbidity', by='Potability')
plt.title('Turbidity of Potable vs Non-Potable Water')
plt.suptitle('')
plt.xlabel("Potability (0 = Non-potable, 1 = Potable)")
plt.ylabel("Turbidity")
plt.savefig('./charts/turbidity_and_p_boxplot.png')
plt.close()


############################## STATS per site


site1 = data[data['site']==1]
site2 = data[data['site']==2]
site3 = data[data['site']==3]

print(site1.describe())
print(site2.describe())
print(site3.describe())

features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
            'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Iterate over the list of features and create boxplots for each
for feature in features:
    plt.figure(figsize=(10, 6))

    # Create a boxplot of the feature with respect to 'Potability' and grouped by 'site'
    sns.boxplot(x='Potability', y=feature, hue='site', data=data, palette='Set2')

    plt.title(f'{feature} vs Potability by Site')
    plt.ylabel(f'{feature}')
    plt.xlabel('Potability')

    # Display the chart
    plt.legend(title="Site", loc='upper right')
    # plt.show()


    plt.savefig(f"./charts/{feature}_vs_potability_boxplot.png")
    plt.close()


data['Type'] = data['Potability'].map({1:"Potable", 0: "Non-Potable"})
plt.figure(figsize=(10, 6))

sns.scatterplot(data=data, x='ph', y='Organic_carbon', hue='Type')

plt.title('Organic Carbon Levels by pH for Potable and Non-Potable Water')
plt.xlabel('pH Level')
plt.ylabel('Organic Carbon Level')
plt.legend(title='Water Type')
plt.grid()
plt.savefig("./charts/ph_organic_carbon_and_potability.png")
plt.close()

ph_carbon_corr = data['ph'].corr(data['Organic_carbon'])
print(ph_carbon_corr)


plt.figure(figsize=(10, 6))

sns.scatterplot(data=data, x='ph', y='Hardness', hue='Type')

plt.title('Hardness Levels by ph for Potable and Non-Potable Water')
plt.xlabel('ph Level')
plt.ylabel('Hardness Level')
plt.legend(title='Water Type')
plt.grid()
plt.savefig("./charts/ph_hardness_and_potability.png")
plt.close()
