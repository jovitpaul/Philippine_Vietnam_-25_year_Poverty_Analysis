import pandas as pd
import statsmodels.api as sm

# 1. Load the data from your previous extraction
df = pd.read_csv('ph_vn_data.csv', header=[0, 1], index_col=0)

# 2. Isolate Vietnam
vn_data = df['VNM'].copy()

# 3. Fill the Gaps (Interpolation)
# Vietnam's poverty data is even "lumpier" than the PH, so we must interpolate
vn_data['Poverty'] = vn_data['Poverty'].interpolate(method='linear')

# 4. Handle missing data at the start of the 2000s
vn_data = vn_data.dropna()

# 5. The Vietnam Regression
Y = vn_data['Poverty']
X = vn_data[['Manufacturing', 'Services']]
X = sm.add_constant(X)

model_vn = sm.OLS(Y, X).fit()

print("\n--- VIETNAM POVERTY REGRESSION RESULTS ---")
print(model_vn.summary())
