import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, color='black', s=5)

    # Create first line of best fit
    m, b = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])[:2] 
    x = range(1880, 2051)
    plt.plot(x, m*x + b, color='blue')

    # Create second line of best fit
    m, b = linregress(x=range(2000, 2014), y=df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])[:2]
    x = range(2000, 2051)
    plt.plot(x, m*x + b, color='red') 

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()