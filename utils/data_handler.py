import os
import csv
import pandas as pd

FILE_PATH = "data/health_data.csv"

def save_data(data):
    """Save data to a CSV file."""
    os.makedirs("data", exist_ok=True)  # Ensure the folder exists
    file_exists = os.path.exists(FILE_PATH)
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            # Write header if file doesn't exist
            writer.writerow(["Date", "Steps", "Sleep (hours)", "Water (cups)", "Exercise (hours)", "Reading (hours)", "Studying (hours)"])
        writer.writerow(data)

def load_data():
    """Load data from CSV file."""
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    else:
        print("⚠️ No data found. Please log some entries first!")
        return None
