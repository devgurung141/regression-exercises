# imports

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def plot_variable_pairs(df):
    '''takes a datafreame and plot graph of pairplots '''

    sns.pairplot(data=df.sample(10000),diag_kind='kde', kind='reg',corner = True, plot_kws={'line_kws':{'color':'red'}})
    

def plot_categorical_and_continuous_vars(df, cont_var, cat_var):
    '''takes a dataframe, a continuous variable, a categorical variable and make 3 graah of categorical
    variables and a continuous vairable'''
    
    plt.figure(figsize = (15,5))
    plt.subplot(131)
    sns.boxplot(x=cat_var, y=cont_var, data=df.sample(10000))
    plt.subplot(132)
    sns.violinplot(x=cat_var, y=cont_var, data=df.sample(10000))
    plt.subplot(133)
    sns.barplot(x=cat_var, y=cont_var, data=df.sample(10000))
    plt.show()