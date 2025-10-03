from joblib import load
import os
import pandas as pd 
import numpy as np

# Get numeric values

try:
    age = float(input('Enter age: '))
    children = float(input('Enter number of children: '))
    bmi = float(input('Enter the value of the bmi: '))
except:
    print('Values must be numeric!')
    exit()

# Get other values

smoker_state = input('Are you a smoker? (Y/N): ').upper()
region = input('Enter your region (southwest/southeast/northwest/northeast): ').lower()
sex = input('Enter gender (f/m): ').lower()

values = [age, bmi, children]
columns = ['age', 'bmi', 'children', 'region_northeast', 'region_northwest',
       'region_southeast', 'region_southwest', 'sex_female', 'sex_male',
       'smoker_encoded']

# Region Check

regions = [False, False, False, False]

if (region == 'northeast'):
    regions[0] = True
elif (region == 'northwest'):
    regions[1] = True
elif (region == 'southeast'):
    regions[2] = True
elif (region == 'southwest'):
    regions[3] = True
else:
    print('This region is not valid')
    exit()

values.extend(regions)

# Gender Check

genders = [False, False]

if (sex == 'f'):
    genders[0] = True
elif (sex == 'm'):
    genders[1] = True
else:
    print('This gender is not valid')
    exit()

values.extend(genders)

# Smoker Check

if (smoker_state == 'Y'):
    values.extend([1])
else:
    values.extend([0])

# Load model

loaded_model = load(os.getcwd() + '/models/svr.joblib')

# Test and make prediction

test = pd.DataFrame([values], columns=columns)

pred = np.exp(loaded_model.predict(test)[0])

print(pred)

#19,female,27.9,0,yes,southwest,
# 16884.924