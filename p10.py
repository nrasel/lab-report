import pandas as pd


data = {
    'SI': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Height': [197, 165, 179, 191, 177, 153, 169, 178, 184, 177, 167, 176, 161, 168, 164, 181, 182, 143, 169, 175],
    'Weight': [93, 59, 71, 78, 72, 61, 72, 29, 85, 75, 59, 70, 57, 60, 66, 67, 71, 46, 53, 66],
    'Sex': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
}

df = pd.DataFrame(data)

df['Height_m'] = df['Height'] / 100


df['BMI'] = df['Weight'] / (df['Height_m'] ** 2)

male_bmi = df[df['Sex'] == 1]['BMI']
female_bmi = df[df['Sex'] == 2]['BMI']


print("Male BMI values:\n", male_bmi)
print("\nFemale BMI values:\n", female_bmi)