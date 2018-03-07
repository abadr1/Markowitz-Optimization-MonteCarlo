import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_data import *

#-----------------------------------------------------------------
start = '2014-1-1'
end = '2016-12-31'
securities = ['CNP', 'F', 'WMT', 'GE', 'TSLA']


#-----------------------------------------------------------------

def select_feature(data,feature):
    tickers = list(data.keys())
    feature_list = []
    for tick in tickers:
        feature_list.append(data[tick][feature])
    df = pd.concat(feature_list ,axis=1)
    df.columns = tickers
    return(df)


if __name__ == "__main__":

    raw_data = quandl_data(securities,start,end,api_key)
    data = raw_data.data

    num_portfolios = 5000
    data = select_feature(data,'Adj. Close')

    ##df = portfolio_combinations(data,securities,num_portfolios)



#GRAPHING




