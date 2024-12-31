import numpy as np

def calculate_portfolio_weights(components, explained_variance_ratio, num_components):
    weights = {
        'PC1': components[0] / np.sum(np.abs(components[0])),
        'Top_3_PC': np.sum(components[:3], axis=0) / np.sum(np.abs(np.sum(components[:3], axis=0))),
        'Top_5_PC': np.sum(components[:5], axis=0) / np.sum(np.abs(np.sum(components[:5], axis=0))),
        'Top_10_PC': np.sum(components[:10], axis=0) / np.sum(np.abs(np.sum(components[:10], axis=0))),
        '95_Variance': np.sum(components[:num_components], axis=0) / np.sum(np.abs(np.sum(components[:num_components], axis=0))),
        'Equal_Weight': np.ones(len(components[0])) / len(components[0])
    }
    return weights

def calculate_custom_weights(idx30_tickers, top_10_weights):
    remaining_tickers = [ticker for ticker in idx30_tickers if ticker not in top_10_weights]
    remaining_weight = 1 - sum(top_10_weights.values())
    equal_weight_remaining = remaining_weight / len(remaining_tickers)

    custom_portfolio_weights = {}
    for ticker in idx30_tickers:
        if ticker in top_10_weights:
            custom_portfolio_weights[ticker] = top_10_weights[ticker]
        else:
            custom_portfolio_weights[ticker] = equal_weight_remaining

    return custom_portfolio_weights


def calculate_portfolio_performance(returns, portfolio_weights):
    portfolio_returns = {}
    for name, weights in portfolio_weights.items():
        portfolio_returns[name] = np.dot(returns.values, weights)
    return portfolio_returns

def calculate_cumulative_returns(portfolio_returns):
    cumulative_returns = {name: np.cumprod(1 + ret) - 1 for name, ret in portfolio_returns.items()}
    return cumulative_returns

def calculate_metrics(cumulative_returns, portfolio_returns):
    final_returns = {name: cum_ret[-1] for name, cum_ret in cumulative_returns.items()}
    portfolio_std_dev = {name: np.std(ret) for name, ret in portfolio_returns.items()}
    risk_adjusted_returns = {name: final_returns[name] / portfolio_std_dev[name] if portfolio_std_dev[name] > 0 else np.nan
                             for name in final_returns}
    return final_returns, portfolio_std_dev, risk_adjusted_returns
