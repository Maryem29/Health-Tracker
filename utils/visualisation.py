import os
import matplotlib.pyplot as plt

def plot_trends(data):
    """Generate and display health trends."""
    if data is None or data.empty:
        print("No data available for visualisation!")
        return

    os.makedirs("visualisations", exist_ok=True)
    data['Date'] = pd.to_datetime(data['Date'])
    metrics = ["Steps", "Sleep (hours)", "Water (cups)", "Exercise (hours)", "Reading (hours)", "Studying (hours)"]

    for metric in metrics:
        plt.figure(figsize=(10, 5))
        plt.plot(data['Date'], data[metric], marker='o', label=metric)
        plt.title(f"{metric} Over Time")
        plt.xlabel("Date")
        plt.ylabel(metric)
        plt.legend()
        plt.grid()
        filepath = f"visualisations/{metric.replace(' ', '_').lower()}_trend.png"
        plt.savefig(filepath)
        print(f"📊 {metric} trend saved as {filepath}")
        plt.show()
