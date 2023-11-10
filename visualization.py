# -*- coding: utf-8 -*-
"""
Name: Shaik Mohammed Sohail
Student ID: 
Module: 7PAM2000-0901-2023 - Applied Data Science 1
Course: Msc Data Science (SW) with Placement Year
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def barGraph(df):
    """
    Parameters
    ----------
    df : This parsed argument for the dataframe which is received from main funtion
    size: variable for setting the value width of the bar
    plotLocation: defining the graph position

    Returns
    -------
    This function used to plot the bar graph from the parsed dataframe
    """
    plt.figure()
    
    # Set width and positions for the bar graph
    size = 0.20
    plotLocation = range(len(df['Country Name']))
    plotLocation1 = [x + size for x in plotLocation]
    plotLocation2 = [x + size for x in plotLocation1]
    plotLocation3 = [x + size for x in plotLocation2]
    
    Countries = ['USA','India','UK','Australia','Japan','China']

    # Plot the Bar graph for total number of cases
    # Plotting the bars
    plt.bar(plotLocation, df['1991'], color='b', width=size, edgecolor='grey', label='1991')
    plt.bar(plotLocation1, df['2001'], color='r', width=size, edgecolor='grey', label='2001')
    plt.bar(plotLocation2, df['2011'], color='g', width=size, edgecolor='grey', label='2011')
    plt.bar(plotLocation3,df['2021'],width=size,edgecolor='grey',label='2021')
    # Label the plot for X and Y axes
    plt.xlabel('Countries')
    plt.ylabel('%')
    plt.title('Grouped Bar graph represents unemployment rate over year 1991-2021')
    plt.xticks(plotLocation1, Countries)
    plt.legend()
    
    # Display the Graph
    plt.show()
    
def lineGraph(df):
    """
    Parameters
    ----------
    df : This parsed argument for the dataframe which is received from main funtion
    year: defines the value of years which is ranging from 1991-2021 with an interval of 5 years
    countries: define list of countries

    Returns
    -------
    This function used to plot the line graph from the parsed dataframe
    """
    plt.figure()
    
    countries = ['India','United States','United Kingdom','China']
    year=['1991','1995','2000','2005','2010','2015','2021']
    
    #plotting the points for defined year with respective country
    for country in countries:
        value = df[df['Country Name'] == country][year].values.tolist()
        plt.plot(year,value[0],Label=country)
        
    
    #plotting graph with assigned values
    plt.legend()
    plt.show()

import numpy as np

def scatter_unemployment(df):
    """
    Parameters
    ----------
    df : This parsed argument for the dataframe which is received from main funtion
    year: defines the value of years which is ranging from 1991-2021 with an interval of 5 years
    columns: define list of years

    Returns
    -------
    This function used to plot the scatter plot from the parsed dataframe
    """
    columns = [str(i) for i in range(1991, 2022)]
    
    country_data = df[df['Country Name'] == 'United Kingdom'][columns].values
    years = np.array([int(col) for col in columns])
    
    for row in country_data:
        plt.scatter(years, row)
        plt.xlabel('Year')
        plt.ylabel('Unemployment Rate')
        plt.title('Unemployment Rate in United Kingdom (1991-2021)')
        plt.show()

#importing dataset
dataframe = pd.read_csv("unemployment analysis.csv")
country = ['United States','India','United Kingdom','Australia','Japan', 'China']
dataframe = dataframe[dataframe['Country Name'].isin(country)]
barGraph(dataframe)
lineGraph(dataframe)
scatter_unemployment(dataframe)