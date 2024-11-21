from utils.input_handler import get_daily_input
from utils.data_handler import load_data
from utils.visualisation import plot_trends
from utils.goals_checker import check_goals

def main():
    """Main menu for the health tracker."""
    while True:
        print("\n💡 What would you like to do?")
        print("1. Log today's data")
        print("2. View all data")
        print("3. Visualize trends")
        print("4. Check goals")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            get_daily_input()
        elif choice == "2":
            data = load_data()
            if data is not None:
                print(data)
        elif choice == "3":
            data = load_data()
            plot_trends(data)
        elif choice == "4":
            data = load_data()
            check_goals(data)
        elif choice == "5":
            print("👋 Goodbye! Stay healthy!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
