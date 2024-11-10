import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import time
# from scipy.stats import proportion_confint
from statsmodels.stats.proportion import proportion_confint

# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
    
data = pd.read_csv("obesity.csv")
df = data

## Separate boys and girls

men = data[data['Gender'] == 'Male']
women = data[data['Gender'] == 'Female']


###### MEN CI for 
# cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(

category_counts = df['NObeyesdad'].value_counts()
print(category_counts)
total_count = len(df)

# Calculate 95% confidence intervals for each category
confidence_intervals = {}
for category, count in category_counts.items():
    # 95% confidence level, using the normal approximation method
    ci_low, ci_high = proportion_confint(count, total_count, alpha=0.05, method='normal')
    confidence_intervals[category] = (ci_low, ci_high)

print(confidence_intervals)



## Splitting up men into various weight categories

in_w = men[men['NObeyesdad'] == 'Insufficient_Weight']
norm_w = men[men['NObeyesdad'] == 'Normal_Weight']
over_w_i = men[men['NObeyesdad'] == 'Overweight_Level_I']
over_w_ii = men[men['NObeyesdad'] == 'Overweight_Level_II']
obes_t_i = men[men['NObeyesdad'] == 'Obesity_Type_I']
obes_t_ii = men[men['NObeyesdad'] == 'Obesity_Type_II']
obes_t_iii = men[men['NObeyesdad'] == 'Obesity_Type_III']

# print(obes_t_iii)
print(obes_t_iii.describe())
weight_categories_men = [
    in_w, 
    norm_w, 
    over_w_i, 
    over_w_ii, 
    obes_t_i, 
    obes_t_ii, 
    obes_t_iii, 
]

## Splitting up the women into various weight categories

in_w = women[women['NObeyesdad'] == 'Insufficient_Weight']
norm_w = women[women['NObeyesdad'] == 'Normal_Weight']
over_w_i = women[women['NObeyesdad'] == 'Overweight_Level_I']
over_w_ii = women[women['NObeyesdad'] == 'Overweight_Level_II']
obes_t_i = women[women['NObeyesdad'] == 'Obesity_Type_I']
obes_t_ii = women[women['NObeyesdad'] == 'Obesity_Type_II']
obes_t_iii = women[women['NObeyesdad'] == 'Obesity_Type_III']

weight_categories_women = [
    in_w, 
    norm_w, 
    over_w_i, 
    over_w_ii, 
    obes_t_i, 
    obes_t_ii, 
    obes_t_iii, 
]

## Weight category and Height Men
print()

print("==========================Weight and Height category===================")
print("====================MEN===============")
for weight_category in weight_categories_men:
    cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(weight_category["Height"]), scale=stats.sem(weight_category["Height"]))
    print("CI for men in weight category", weight_category['NObeyesdad'].iloc[0], "and height:", cinterval)
    print("Actual mean for Height:", np.mean(weight_category["Height"]))
    print()


## Weight category and Height Women

print("====================WOMEN===============")
for weight_category in weight_categories_women:
    cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(weight_category["Height"]), scale=stats.sem(weight_category["Height"]))
    print("CI for women in weight category", weight_category['NObeyesdad'].iloc[0], "and height:", cinterval)
    print("Actual mean for Height:", np.mean(weight_category["Height"]))
    print()


## Weight category and Weight measurement
print("==========================Weight and weight category===================")

print("====================MEN===============")
for weight_category in weight_categories_men:
    cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(weight_category["Weight"]), scale=stats.sem(weight_category["Weight"]))
    print("CI for men in weight category", weight_category['NObeyesdad'].iloc[0], "and weight:", cinterval)
    print("Actual mean for Weight:", np.mean(weight_category["Weight"]))
    print()


## Weight category and Weight Women

print("====================WOMEN===============")
for weight_category in weight_categories_women:
    cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(weight_category["Weight"]), scale=stats.sem(weight_category["Weight"]))
    print("CI for women in weight category", weight_category['NObeyesdad'].iloc[0], "and weight:", cinterval)
    print("Actual mean for Weight:", np.mean(weight_category["Weight"]))
    print()


print("==========================Weight and age category===================")
print("====================MEN===============")
for weight_category in weight_categories_men:
    cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(weight_category["Age"]), scale=stats.sem(weight_category["Age"]))
    print("CI for men in weight category", weight_category['NObeyesdad'].iloc[0], "and weight:", cinterval)
    print("Actual mean for Age:", np.mean(weight_category["Age"]))
    print()


## Age category and Age Women

print("====================WOMEN===============")
for weight_category in weight_categories_women:
    cinterval = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(weight_category["Age"]), scale=stats.sem(weight_category["Age"]))
    print("CI for women in weight category", weight_category['NObeyesdad'].iloc[0], "and weight:", cinterval)
    print("Actual mean for Age:", np.mean(weight_category["Age"]))
    print()


# TODO
# Compare mean weight with family history overweight, FAVC, FCVC, NCP

CATEGORIES = [
"family_history_with_overweight",
"FAVC",
# "FCVC",
"NCP",
"CAEC",
"SMOKE",
# "CH2O",
"SCC",
# "FAF",
# "TUE",
"CALC",
# "MTRANS",
]

CATMAP = {
        "family_history_with_overweight": "family_history_with_overweight",
        "FAVC": "high calorie food frequently",
        "FCVC": "eats vegetables",
        "NCP": "how many meals",
        "CAEC": "eat between meals",
        "SMOKE": "smokes",
        "SCC": "monitors calories",
        "CALC": "how often drink alcohol"
}

df["NCP"] = df["NCP"].round()

for category in CATEGORIES:
    print("===============CI for {}==============".format(category))
    for value in df[category].unique():
        weight_category = df[df[category] == value]["Weight"]
        
        if len(weight_category) > 1:  # Only calculate if more than one entry
            # Mean calculation
            actual_mean = np.mean(weight_category)
            
            # Confidence interval calculation
            cinterval = stats.t.interval(
                alpha=0.95,
                df=len(weight_category) - 1,
                loc=actual_mean,
                scale=stats.sem(weight_category)
            )
            print(f"95% Confidence Interval for Weight in {CATMAP[category]} = {value}: {cinterval}")
            print(f"Actual mean for Weight in {CATMAP[category]} = {value}: {actual_mean:.2f}")
            print()
        else:
            pass
            # print(f"{value}: Not enough data for confidence interval.")
