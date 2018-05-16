import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_data import *

def portfolio_combinations(data,securities,num_portfolios):

    returns_daily = data.pct_change()
    returns_annual = returns_daily.mean() * 250
    cov_daily = returns_daily.cov()
    cov_annual = cov_daily * 250

    port_returns = []
    port_volatility = []
    stock_weights = []
    sharpe_ratio = []
    num_assets = len(securities)
    num_portfolios = 50000
    portfolio = {'Returns': port_returns,
        'Volatility': port_volatility,
        'Sharpe Ratio': sharpe_ratio}

    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, returns_annual)
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
        port_returns.append(returns)
        sharpe = returns / volatility
        sharpe_ratio.append(sharpe)
        port_volatility.append(volatility)
        stock_weights.append(weights)

    for counter,symbol in enumerate(securities):
        portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

    df = pd.DataFrame(portfolio)
    column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in securities]
    df = df[column_order]
    return(df)

def select_feature(data,feature):
    tickers = list(data.keys())
    feature_list = []
    for tick in tickers:
        feature_list.append(data[tick][feature])
    df = pd.concat(feature_list ,axis=1)
    df.columns = tickers
    return(df)

def optimize_portfolio(data,op_type='max_sharpe'):
    if op_type == 'max_sharpe':
            max_sharpe = data['Sharpe Ratio'].max()
            sharpe_portfolio = data.loc[data['Sharpe Ratio'] == max_sharpe]
            return(sharpe_portfolio)
    if op_type == 'min_variance':    
        min_volatility = data['Volatility'].min()
        min_variance_port = data.loc[data['Volatility'] == min_volatility]
        return(min_variance_port.T)

if __name__ == "__main__":

    raw_data = quandl_data(securities,start,end,api_key)
    data = raw_data.data

    num_portfolios = 5000
    data = select_feature(data,'Adj. Close')

    ##df = portfolio_combinations(data,securities,num_portfolios)



#GRAPHING

#finding optimal portfolio

    min_volatility = df['Volatility'].min()
    max_sharpe = df['Sharpe Ratio'].max()


    sharpe_portfolio = df.loc[df['Sharpe Ratio'] == max_sharpe]
    min_variance_port = df.loc[df['Volatility'] == min_volatility]

    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='red', marker='D', s=200)
    plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='blue', marker='D', s=200 )
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.show()





