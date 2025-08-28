import datetime
expenses = []

CATEGORIES = [
    "Food 🍔",
    "Transport 🚗",
    "Rent 🏠",
    "Entertainment 🎬",
    "Savings 💰",
    "Shopping 🛍️",
    "Healthcare 🏥",
    "Other 📝",
]

def add_expense():
    amount = float(input("Enter expense amount: ₹"))
    print("Select category:")
    for idx, name in enumerate(CATEGORIES, 1):
        print(f"{idx}. {name}")
    while True:
        try:
            cat_choice = int(input("Enter category number: "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            else:
                print("Invalid number! Try again.")
        except ValueError:
            print("Please enter a valid number.")
    date = input("Enter date (DD-MM-YYYY) or press Enter for today: ")
    if not date:
        date = datetime.date.today().isoformat()
    expenses.append({"amount": amount, "category": category, "date": date})
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n📌 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['category']} : ₹{exp['amount']}")
    print()

def summarize_expenses():
    if not expenses:
        print("No expenses to summarize.\n")
        return
    summary = {}
    total = 0
    for exp in expenses:
        cat = exp["category"]
        amt = exp["amount"]
        summary[cat] = summary.get(cat, 0) + amt
        total += amt
    print("\n📊 Expense Summary:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print(f"Total: ₹{total}\n")

def main():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
