import pandas as pd
import numpy as np

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and correcting data types."""
    # Handle missing values
    df = df.dropna()  # Example: drop missing values
    # # Convert date columns to datetime
    # df['created_at'] = pd.to_datetime(df['created_at'])
    # df['updated_at'] = pd.to_datetime(df['updated_at'])
    return df

def preprocess_data(df):
    if 'created_at' not in df.columns:
        print("'created_at' column not processed.")
        return df  # Return the original DataFrame unchanged
    else:
        df['created_at'] = pd.to_datetime(df['created_at'])
        # Continue with other preprocessing steps...
        return df

if __name__ == "__main__":
    # Load the data
    delivery_requests = load_data('../data/driver_locations.csv')
    completed_orders = load_data('../data/nb.csv')

    # Clean the data
    delivery_requests = clean_data(delivery_requests)
    completed_orders = clean_data(completed_orders)

    # Preprocess the data
    delivery_requests = preprocess_data(delivery_requests)
    completed_orders = preprocess_data(completed_orders)

    # Save the cleaned data
    delivery_requests.to_csv('../data/processed/delivery_requests_cleaned.csv', index=False)
    completed_orders.to_csv('../data/processed/completed_orders_cleaned.csv', index=False)
