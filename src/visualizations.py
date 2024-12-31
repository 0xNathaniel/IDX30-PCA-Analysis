import matplotlib.pyplot as plt

def plot_cumulative_variance(cumulative_variance):
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_variance, marker='o')
    plt.title('Cumulative Explained Variance by Principal Components')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.grid()
    plt.show()

def plot_weights(weights, tickers, title):
    plt.figure(figsize=(12, 8))
    plt.bar(range(len(tickers)), weights, tick_label=tickers)
    plt.xticks(rotation=90)
    plt.title(title)
    plt.ylabel('Weight')
    plt.grid()
    plt.show()

def plot_cumulative_returns(cumulative_returns, dates):
    plt.figure(figsize=(12, 8))
    for name, cum_ret in cumulative_returns.items():
        plt.plot(dates, cum_ret, label=name)
    plt.title("Cumulative Returns of Portfolios")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid()
    plt.show()
