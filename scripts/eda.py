import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def plot_distributions(df):
    """Plot distributions of the features."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['distance'], kde=True)
    plt.title('Distance Distribution')
    plt.xlabel('Distance (km)')
    plt.ylabel('Frequency')
    plt.show()

def plot_correlation_matrix(df):
    """Plot the correlation matrix."""
    plt.figure(figsize=(12, 8))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

if __name__ == "__main__":
    # Load the feature-engineered data
    completed_orders = load_data('../data/nb.csv')

    # Plot distributions and correlation matrix
    plot_distributions(completed_orders)
    plot_correlation_matrix(completed_orders)
