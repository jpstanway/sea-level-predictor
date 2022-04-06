import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='b')

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])

    xline = list(range(1860, 2051))

    yline = []

    for xl in xline:
        yt = (slope * xl) + intercept
        yline.append(yt)

    plt.plot(xline, yline, 'r')

    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
