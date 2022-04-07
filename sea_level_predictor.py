import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def get_lobf(df, rng_start, rng_stop):
    slope, intercept, rvalue, pvalue, stderr = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level'])

    xline = list(range(rng_start, rng_stop))
    yline = []

    for xl in xline:
        yt = (slope * xl) + intercept
        yline.append(yt)

    return xline, yline


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='b')

    # Create first line of best fit
    xline, yline = get_lobf(df, 1880, 2051)

    plt.plot(xline, yline, 'r')

    # Create second line of best fit
    df_filtered = df.loc[df['Year'] >= 2000]

    xline2, yline2 = get_lobf(df_filtered, 2000, 2051)

    plt.plot(xline2, yline2, 'g')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
