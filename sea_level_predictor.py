from re import X
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():

    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    result = linregress(x,y)#two-sided
    year_predict = pd.DataFrame(range(1880,2051,1)) #create predict year for x axis
    plt.plot(year_predict,result.slope*year_predict+ result.intercept,color='red') # y = mx + c
    x_tick = np.arange(1850,2100,25)
    plt.xticks(x_tick)
    # Create second line of best fit
    df_filter = df[df['Year'] >= 2000]
    x2 = df_filter['Year']
    y2 = df_filter['CSIRO Adjusted Sea Level']
    result2 = linregress(x2,y2)
    year_predict2 = year_predict[year_predict >= 2000]
    year_predict2 = year_predict2.dropna()
    plt.plot(year_predict2,result2.slope*year_predict2 + result2.intercept,color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()