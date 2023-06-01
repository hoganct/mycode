import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# reading csv made from artist_explorer.py
df = pd.read_csv('50_tracks.csv', encoding='latin1') # using 'latin1' encoding due to some weird errors for some songs, only thing that seems to consistently work

# select the columns from the 8th field onwards - just the floats and tempo, no strings
data_columns = df.columns[7:]

# normalizing with Min-Max scaling - this will take tempo and convert it into a 0-1 value
scaler = MinMaxScaler()
df[data_columns] = scaler.fit_transform(df[data_columns])

# calculate the variances for each field
variances = df[data_columns].var()

# sort the fields based on their variances in descending order
sorted_variances = variances.sort_values(ascending=False)
print("All of the variances:")
print(sorted_variances)

# select the top two fields with the highest variances
top_two_fields = sorted_variances.head(2)

# print the names of the top two fields
print("Top two fields with the most variance:")
for field_name, variance in top_two_fields.items():
    print(field_name)
