import numpy as np
import pandas as pd  #to read and work with .csv files
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from nicegui import ui    #pip install niceg
import os



#file outline
#1)ask the user for input
#2) read the .csv file
#3) filter and adjust data based on users choice
#4) plot(plotly?, matplotlib? seaborn?)
#5) save the plot as html or png


#tools to use: NiceGUI for user input
#NiceGUI: provides interface for output of plot. variables for user to select for the plot, adn table display fo csv content.
#pandas for reading .csv files
#matplotlib/seaborn/plotly for plotting



# --- Path to your data folder ---
data_folder = './supercon1/data'  # relative path



# Get list of CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Markdown area to show CSV content
data_display = ui.markdown('Select a CSV file to see its data.')

# Function to show CSV content
def show_csv(file_name):
    if not file_name:
        return
    file_path = os.path.join(data_folder, file_name)

    # Read all lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find header row (line that starts with 'T (K)')
    header_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith('T (K)'):
            header_index = i
            break
    if header_index is None:
        data_display.set_text('No valid header found in CSV.')
        return

    # Read CSV starting from the header row
    df = pd.read_csv(file_path, header=header_index)

    # Convert dataframe to string for display
    text = df.to_string(index=False)

    # Update markdown content
    data_display.set_text(f'```\n{text}\n```')

# Dropdown to select CSV file
ui.select(csv_files, label='Select CSV file', on_change=show_csv)

# Run NiceGUI
if __name__ in {"__main__", "__mp_main__"}:
    ui.run()