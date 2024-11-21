from datetime import date
from utils.data_handler import save_data

def get_daily_input():
    """Get user input for daily health metrics."""
    print("📊 Enter your daily health data:")
    steps = int(input("Steps walked: "))
    sleep = float(input("Sleep hours: "))
    water = float(input("Water intake (cups): "))
    exercise = float(input("Exercise hours: "))
    reading = float(input("Reading hours: "))
    studying = float(input("Studying hours: "))

    data = [date.today(), steps, sleep, water, exercise, reading, studying]
    save_data(data)
    print("✅ Your data has been saved!")
