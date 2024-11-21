GOALS = {
    "Steps": 8000,
    "Sleep (hours)": 7,
    "Water (cups)": 8,
    "Exercise (hours)": 0.5,
    "Reading (hours)": 1,
    "Studying (hours)": 3,
}

def check_goals(data):
    """Check progress against daily goals."""
    if data is None or data.empty:
        print("⚠️ No data available for goal tracking!")
        return

    last_entry = data.iloc[-1]
    print("\n🌟 Your Goal Progress:")
    for metric, goal in GOALS.items():
        actual = last_entry[metric]
        if actual >= goal:
            print(f"✅ {metric} goal met! ({actual}/{goal})")
        else:
            print(f"❌ {metric} goal not met. ({actual}/{goal})")
