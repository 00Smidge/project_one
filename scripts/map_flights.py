import datetime
import folium
import pandas as pd

craft_categories = {
    0: {"No information at all": "gray"},
    1: {"No ADS-B Emitter Category Information": "black"},
    2: {"Light (< 15500 lbs)": "lightblue"},
    3: {"Small (15500 to 75000 lbs)": "green"},
    4: {"Large (75000 to 300000 lbs)": "orange"},
    5: {"High Vortex Large (aircraft such as B-757)": "red"},
    6: {"Heavy (> 300000 lbs)": "darkred"},
    7: {"High Performance (> 5g acceleration and 400 kts)": "purple"},
    8: {"Rotorcraft": "lightgreen"},
    9: {"Glider / sailplane": "darkgreen"},
    10: {"Lighter-than-air": "cadetblue"},
    11: {"Parachutist / Skydiver": "pink"},
    12: {"Ultralight / hang-glider / paraglider": "lightyellow"},
    13: {"Reserved": "gray"},
    14: {"Unmanned Aerial Vehicle": "lightgray"},
    15: {"Space / Trans-atmospheric vehicle": "beige"},
    16: {"Surface Vehicle – Emergency Vehicle": "red"},
    17: {"Surface Vehicle – Service Vehicle": "darkblue"},
    18: {"Point Obstacle (includes tethered balloons)": "blue"},
    19: {"Cluster Obstacle": "darkpurple"},
    20: {"Line Obstacle": "darkgray"},
}


def map_flights(df):

    feature_groups = {}

    for index, row in df.iterrows():
        if pd.notna(row["longitude"]) and pd.notna(row["latitude"]):
            map = folium.Map(
                location=(48.3769, -99.9962),
                zoom_control=True,
                zoom_start=4,
                tiles=folium.TileLayer(no_wrap=True),
            )
            category = row["category"]

            if category not in craft_categories:
                description = "Unknown"
                color = "grey"
            else:
                description, color = list(craft_categories[category].items())[0]

            popup_html = call_to_action(row, color, description)

            if category not in feature_groups:
                feature_groups[category] = folium.FeatureGroup(
                    name=f"{description} ({category})"
                )

            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                tooltip=f"📞🪧: {row['callsign']}",
                popup=popup_html,
                icon=folium.Icon(icon="plane", color=color, description=description),
            ).add_to(feature_groups[category])

    for feature in feature_groups.values():
        feature.add_to(map)

    folium.LayerControl().add_to(map)
    return map._repr_html_()


def call_to_action(row, color, description):  # noqa: F811
    return f"""
            <div style='width: max-content;'>
                <p><strong>Flight:</strong> {row['callsign']}</p>
                <h2>Flight Details</h2>
                <p><strong>Flight Number:</strong> {row['callsign']}</p>
                <p><strong>Departure:</strong> {row['origin_country']}</p>
                <p><strong>Speed:</strong> {row['velocity']}</p>
                <p><strong>Category:</strong> {description}</p>
                <a href='/flight_path/{row['icao24']}/{color}' target="_parent">See Flight Path</a>
            </div>
            """
