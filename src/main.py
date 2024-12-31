import numpy as np
from pca import svdPCA
from data_preprocessing import download_data
from quantitative_analysis import (calculate_portfolio_weights,
                                   calculate_custom_weights,
                                   calculate_portfolio_performance,
                                   calculate_cumulative_returns,
                                   calculate_metrics)
from visualizations import (plot_cumulative_variance,
                            plot_weights,
                            plot_cumulative_returns)

# Define IDX30 tickers
idx30_tickers = [
    "BBCA.JK", "BBRI.JK", "BMRI.JK", "TLKM.JK", "ASII.JK", "BBNI.JK",
    "ICBP.JK", "AMRT.JK", "UNTR.JK", "GOTO.JK", "BRPT.JK", "CPIN.JK",
    "ADRO.JK", "UNVR.JK", "INDF.JK", "KLBF.JK", "MBMA.JK", "PGEO.JK",
    "MDKA.JK", "PGAS.JK", "INKP.JK", "INCO.JK", "ANTM.JK", "ARTO.JK",
    "PTBA.JK", "MEDC.JK", "MAPI.JK", "SMGR.JK", "AKRA.JK", "ACES.JK"
]

# Download data (historical data's date range may vary according to the intended analysis)
#prices, returns = download_data(idx30_tickers, "2024-11-01", "2024-12-30") # For the most updated data
prices, returns = download_data(idx30_tickers, "2024-01-01", "2024-12-30") # For backtracking purposes

# Perform PCA
transformed_returns, components, explained_variance_ratio, singular_values = svdPCA(returns.values)

# Plot cumulative explained variance
cumulative_variance = np.cumsum(explained_variance_ratio)
plot_cumulative_variance(cumulative_variance)

# Calculate portfolio weights
num_components_95 = len([x for x in cumulative_variance if x < 0.95]) + 1
portfolio_weights = calculate_portfolio_weights(components, explained_variance_ratio, num_components_95)

# Define custom weights for the top 10 stocks
top_10_weights = {
    "BBCA.JK": 0.1581,
    "BBRI.JK": 0.1473,
    "BMRI.JK": 0.1464,
    "TLKM.JK": 0.0901,
    "ASII.JK": 0.0661,
    "BBNI.JK": 0.0527,
    "GOTO.JK": 0.0471,
    "AMRT.JK": 0.0357,
    "UNTR.JK": 0.0250,
    "INDF.JK": 0.0226
}

# Calculate custom portfolio weights
custom_portfolio_weights = calculate_custom_weights(idx30_tickers, top_10_weights)

# Add the custom portfolio weights to the portfolio weights dictionary
portfolio_weights['Custom_Weighted'] = np.array([custom_portfolio_weights[ticker] for ticker in idx30_tickers])


# Calculate portfolio performance
portfolio_returns = calculate_portfolio_performance(returns, portfolio_weights)
cumulative_returns = calculate_cumulative_returns(portfolio_returns)
final_returns, portfolio_std_dev, risk_adjusted_returns = calculate_metrics(cumulative_returns, portfolio_returns)

# Visualizations
for name, weights in portfolio_weights.items():
    plot_weights(weights, idx30_tickers, f"Stock Weights for {name} Portfolio")

plot_cumulative_returns(cumulative_returns, returns.index)

# Print metrics

# Print Final Portfolio Performance
final_returns = {name: cum_ret[-1] for name, cum_ret in cumulative_returns.items()}
print("Final Portfolio Returns:")
for name, ret in final_returns.items():
    print(f"{name}: {ret:.2f}")

# Print Portfolio Standard Deviations
print("Portfolio Standard Deviations:")
for name, std_dev in portfolio_std_dev.items():
    print(f"{name}: {std_dev:.4f}")

# Print Risk-Adjusted Returns
print("Risk-Adjusted Returns (Final Return / Standard Deviation):")
for name, ra_return in risk_adjusted_returns.items():
    print(f"{name}: {ra_return:.4f}")