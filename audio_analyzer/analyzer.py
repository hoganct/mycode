import pandas as pd
from sklearn.preprocessing import MinMaxScaler
<<<<<<< HEAD

# reading csv made from artist_explorer.py
df = pd.read_csv('50_tracks.csv', encoding='latin1') # using 'latin1' encoding due to some weird errors for some songs, only thing that seems to consistently work
=======
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, CategoricalColorMapper
from bokeh.layouts import column
from bokeh.models.widgets import Div

# Reading CSV made from artist_explorer.py
df = pd.read_csv('50_tracks.csv', encoding='utf-8')
>>>>>>> cddf393 (formatting and bokeh improvements)

# Select the columns from the 8th field onwards - just the floats and tempo, no strings
data_columns = df.columns[7:-1]  # Exclude the last column "Embed Code"

# Normalizing with Min-Max scaling - this will take tempo and convert it into a 0-1 value
scaler = MinMaxScaler()
df[data_columns] = scaler.fit_transform(df[data_columns])

# Calculate the variances for each field
variances = df[data_columns].var()

# Sort the fields based on their variances in descending order
sorted_variances = variances.sort_values(ascending=False)
print("All of the variances:")
print(sorted_variances)

# Select the top two fields with the highest variances
top_two_fields = sorted_variances.head(2)

<<<<<<< HEAD
# print the names of the top two fields
print("Top two fields with the most variance:")
for field_name, variance in top_two_fields.items():
    print(field_name)
=======
print(f"The two fields with the greatest variance are {field1} and {field2}.\n")

# Ask the user if they want to use the fields with the greatest variance or define their own fields
user_choice = input("Would you like select your own categories to analyze? (Y/N): ")

if user_choice.lower() == 'y':
    field1 = input("Enter Field 1: ")
    field2 = input("Enter Field 2: ")

# Print the names of the selected fields
print("\nThe two selected fields are:")
print(field1)
print(field2)

# Get unique artists
artists = df['Artist Name'].unique()

# Define a distinct color palette with a vibrant orange
color_palette = ['#FF0000', '#FF8000', '#000080', '#008000', '#00FFFF']

# Create a color mapper mapping each artist to a color
num_artists = len(artists)
palette = color_palette[:num_artists]
color_mapper = CategoricalColorMapper(factors=artists, palette=palette)

# Create the scatterplot with colored points
scatterplot = figure()
scatterplot.circle(x=field1, y=field2, source=df, fill_color={'field': 'Artist Name', 'transform': color_mapper}, size=6, legend_field='Artist Name')

# Customize hover tooltips
hover = HoverTool(tooltips=[("Artist", "@{Artist Name}"), ("Track", "@{Track Name}")])
scatterplot.add_tools(hover)

# Set plot attributes
scatterplot.xaxis.axis_label = field1
scatterplot.yaxis.axis_label = field2

# Get the HTML data from the last field for each record
html_data = df.iloc[:, -1]

# Create a Div element to display the HTML data
html_content = Div(text='', width=800, height=200)

# Concatenate all the HTML data and update the Div element
html_content.text = '\n\n'.join(html_data)

# Create a layout with the scatterplot and the Div element
layout = column(scatterplot, html_content)

# Save the plot as an HTML file and show it
output_file("scatterplot.html")
show(layout)
>>>>>>> cddf393 (formatting and bokeh improvements)
