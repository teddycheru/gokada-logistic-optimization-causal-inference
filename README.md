# gokada-logistic-optimization-causal-inference
Optimizing the placement of delivery drivers for Gokada, a last-mile delivery service in Nigeria, using causal inference techniques.
This project aims to analyze driver locations, perform exploratory data analysis (EDA), and create causal graphs to gain insights into various operational scenarios.

## Table of Contents

- [Installation](#installation)
- [Data Description](#data-description)
- [Usage](#usage)
- [Causal Inference Analysis](#causal-inference-analysis)

## Installation

To get started with this project, follow the steps below:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/teddycheru/gokada-logistic-optimization-causal-inference.git
    cd gokada-logistic-optimization-causal-inference
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv myenv
    source env/bin/activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Install the `causallearn` package from the cloned repository:**
    ```bash
    git clone https://github.com/py-why/causal-learn.git
    cd causal-learn
    pip install .
    ```

## Data Description

The dataset consists of two main files:

1. `driver_locations.csv`: Contains delivery requests by clients, including completed and unfulfilled requests.
    - Columns:
        - `id`: Unique identifier for the entry.
        - `order_id`: Unique identifier for the order.
        - `driver_id`: Unique identifier for the driver.
        - `driver_action`: Action taken by the driver (e.g., accepted, rejected).
        - `lat`: Latitude of the driver's location.
        - `lng`: Longitude of the driver's location.
        - `created_at`: Timestamp of the record creation.
        - `updated_at`: Timestamp of the record update.

2. `nb.csv`: Contains completed trip details.
    - Columns:
        - `TripID`: Unique identifier for the trip.
        - `TripOrigin`: Origin coordinates of the trip.
        - `TripDestination`: Destination coordinates of the trip.
        - `TripStartTime`: Start time of the trip.
        - `TripEndTime`: End time of the trip.

## Usage

### Preprocessing and Cleaning Data

1. **Remove `created_at` and `updated_at` columns:**
    ```python
    driver_locations = driver_locations.drop(columns=['created_at', 'updated_at'])
    ```

2. **Fill missing values with the column mean:**
    ```python
    driver_locations = driver_locations.fillna(driver_locations.mean())
    ```

### Exploratory Data Analysis (EDA)

Perform EDA to understand the data distribution, trends, and patterns. Examples include:

- Visualizing the distribution of trip start and end locations.
- Analyzing the number of accepted and rejected orders.
- Clustering delivery starting locations and destinations.

### Causal Inference Analysis

1. **Split the data into training and hold-out sets:**
    ```python
    from sklearn.model_selection import train_test_split

    train_data, holdout_data = train_test_split(driver_locations, test_size=0.2, random_state=42)
    ```

2. **Create and visualize a causal graph using the `causallearn` package:**
    ```python
    from causallearn.search.ConstraintBased.PC import pc
    from causallearn.utils.GraphUtils import GraphUtils

    # Ensure training data has no missing values
    train_data_clean = train_data.dropna()

    # Select relevant variables
    variables = ['driver_action', 'lat', 'lng']  # Example variables

    # Prepare the data for the causal model
    data_array = train_data_clean[variables].to_numpy()

    # Run the PC algorithm to learn the causal graph
    cg = pc(data_array, fisherz, 0.05, True, 0.1, None)

    # Convert the learned graph to DOT format string
    dot_str = GraphUtils.to_dot(cg.G)
    print(dot_str)

    # Visualize the learned graph using Graphviz (optional)
    from graphviz import Source
    Source(dot_str).render('causal_graph', format='png', cleanup=True)
    ```

### Running the Script

To run the script, go to the project directory, then simply execute:`python3 app.py`

```bash
cd app
python3 app.py
