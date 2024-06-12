import pandas as pd
from geopy.distance import geodesic

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def compute_distance(row):
    """Compute the distance between origin and destination."""
    origin = (row['origin_lat'], row['origin_lng'])
    destination = (row['destination_lat'], row['destination_lng'])
    return geodesic(origin, destination).kilometers

def add_features(df):
    """Add new features to the dataset."""
    # Example: Add distance feature
    df['distance'] = df.apply(compute_distance, axis=1)
    return df

if __name__ == "__main__":
    # Load the cleaned data
    completed_orders = load_data('../data/nb.csv')

    # Add new features
    completed_orders = add_features(completed_orders)

    # Save the feature-engineered data
    completed_orders.to_csv('../data/nb.csv', index=False)
