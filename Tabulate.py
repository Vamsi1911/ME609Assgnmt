import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# List of function names corresponding to the CSV files
functions = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']

# Directory to save images
output_dir = 'tables/'

# Create the output directory if it doesn't exist
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate and save images for each CSV file
for func in functions:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f'{func}_results.csv')

    # Create a new figure
    fig, ax = plt.subplots(figsize=(12, 4))  # Set the size of the figure

    # Hide the axes
    ax.xaxis.set_visible(False)  
    ax.yaxis.set_visible(False)  
    ax.set_frame_on(False)  

    # Create a table from the DataFrame
    table_data = table(ax, df, loc='center', cellLoc='center', colWidths=[0.2]*len(df.columns))

    # Style the table (optional)
    table_data.auto_set_font_size(False)
    table_data.set_fontsize(10)
    table_data.scale(1.2, 1.2)  # Adjust scale as needed

    # Save the table as an image
    plt.title(f"Table for {func} function", fontsize=14)
    plt.savefig(f'{output_dir}{func}_table.png', bbox_inches='tight', pad_inches=0.1)
    plt.close()  # Close the figure to free up memory

print("Images of the tables have been created and saved.")
