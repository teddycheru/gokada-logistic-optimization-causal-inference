from flask import Flask, render_template, jsonify
import pandas as pd
from geopy.distance import geodesic
import folium

# Load the datasets
driver_locations = pd.read_csv('../data/driver_locations.csv')
completed_trips = pd.read_csv('../data/nb.csv')

# Clean and process the data
completed_trips['TripOriginLat'] = completed_trips['TripOrigin'].apply(lambda x: float(x.split(',')[0]))
completed_trips['TripOriginLng'] = completed_trips['TripOrigin'].apply(lambda x: float(x.split(',')[1]))
completed_trips['TripDestinationLat'] = completed_trips['TripDestination'].apply(lambda x: float(x.split(',')[0]))
completed_trips['TripDestinationLng'] = completed_trips['TripDestination'].apply(lambda x: float(x.split(',')[1]))

completed_trips['TripStartTime'] = pd.to_datetime(completed_trips['TripStartTime'])
completed_trips['TripEndTime'] = pd.to_datetime(completed_trips['TripEndTime'])

def calculate_distance(row):
    origin = (row['TripOriginLat'], row['TripOriginLng'])
    destination = (row['TripDestinationLat'], row['TripDestinationLng'])
    return geodesic(origin, destination).kilometers

completed_trips['Distance'] = completed_trips.apply(calculate_distance, axis=1)
completed_trips['Duration'] = (completed_trips['TripEndTime'] - completed_trips['TripStartTime']).dt.total_seconds() / 60.0  # duration in minutes

# Save processed data
completed_trips.to_csv('../data/processed_trips.csv', index=False)

app = Flask(__name__)

# Load data
completed_trips = pd.read_csv('../data/processed_trips.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    start_location = [completed_trips['TripOriginLat'].mean(), completed_trips['TripOriginLng'].mean()]
    m = folium.Map(location=start_location, zoom_start=12)

    for _, row in completed_trips.iterrows():
        folium.PolyLine(
            locations=[(row['TripOriginLat'], row['TripOriginLng']), (row['TripDestinationLat'], row['TripDestinationLng'])],
            color='blue', weight=2.5, opacity=0.8
        ).add_to(m)

    m.save('templates/map.html')
    return render_template('map.html')

@app.route('/data')
def data():
    return jsonify(completed_trips.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
