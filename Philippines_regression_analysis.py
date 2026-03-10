import pandas as pd
import statsmodels.api as sm

# 1. Load the data
df = pd.read_csv('ph_vn_data.csv', header=[0, 1], index_col=0)

# 2. Isolate the Philippines
ph_data = df['PHL'].copy()

# 3. Fill the Gaps (Interpolation)
# This turns those "NaN" values into a smooth line so the regression can run
ph_data['Poverty'] = ph_data['Poverty'].interpolate(method='linear')

# 4. Handle the "Ends"
# If the first or last years are still NaN, we drop them
ph_data = ph_data.dropna()

# 5. The Regression (The Eugene Xu Moment)
# Dependent Variable: Poverty
# Independent Variables: Manufacturing and Services
Y = ph_data['Poverty']
X = ph_data[['Manufacturing', 'Services']]

# Add the constant
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(Y, X).fit()

# Print the results
print("\n--- PHILIPPINES POVERTY REGRESSION RESULTS ---")
print(model.summary())
