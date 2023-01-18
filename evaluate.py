import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import wrangle

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score




def plot_residuals(y, yhat):
    '''takes in actual vale and predicated value to create a scatter plot graph'''
    
    residuals =  yhat -y
    
    plt.scatter(x=y , y=residuals)
    plt.xlabel('Actual Tax value')
    plt.ylabel('Residuals')
    plt.title('Residual vs Actual Value')
    plt.show()

    
def regression_errors(y, yhat):
    '''takes in actual value and predicted value and return SSE, ESS, TSS, MSE, RMSE'''
    
    # compute SSE 
    SSE = mean_squared_error(y, yhat)*len(y)
    
    # compute ESS
    ESS = ((yhat-y.mean()) ** 2).sum()
    
    # compute TSS
    TSS = SSE + ESS
    
    # compute MSE 
    MSE = mean_squared_error(y, yhat)
    
    # compute RMSE 
    RMSE = mean_squared_error(y, yhat, squared=False )
    
    return SSE, ESS, TSS, MSE, RMSE


def baseline_mean_errors(y):
    '''takes in actual value and return SSE, MSE, RMSE'''

   # compute yhat_baseline
    baseline = np.repeat(y.mean(), len(y))
    
    # compute SSE 
    SSE_baseline = mean_squared_error(y,baseline)*len(y)
    
    # compute MSE 
    MSE_baseline = mean_squared_error(y, baseline)
    
    # compute RMSE 
    RMSE_baseline = mean_squared_error(y,baseline, squared=False )
    
    return SSE_baseline, MSE_baseline, RMSE_baseline


def better_than_baseline(y, yhat):
    '''takes in actual value and predicted value and returns true if model performs better 
    than the baseline, otherwise false'''
    
    # call function to get SSE, MSE, RMSE of model
    SSE, ESS, TSS, MSE, RMSE = regression_errors(y, yhat)
    
    # call function to SSE, MME, RMSE of baseline model
    SSE_baseline, MSE_baseline, RMSE_baseline = baseline_mean_errors(y)
    
    # compare REMSE of model and baseline model
    if RMSE < RMSE_baseline: 
        return True
    else:
        return False
