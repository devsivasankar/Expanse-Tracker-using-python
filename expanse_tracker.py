from colorama import Fore

# Expense list and total amount
expanse_list = []
total_amount = 0

def main():
    while True:
        print(Fore.RED, 'Expense Tracker')
        print(Fore.RED,'1. Add Your Expense\n 2. Show List\n 3. Download List\n 4. Exit')
        choice = input('Enter Your Choice (1-4): ')
        if choice == '1':
            add_expanse()
        elif choice == '2':
            show_list()
        elif choice == '3':
            download_list()
        elif choice == '4':
            print(Fore.YELLOW, "Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print(Fore.RED, "Invalid selection. Please try again.")




def add_expanse():
    """Add a new expense to the list and update the total amount."""
    global total_amount
    print(Fore.GREEN, 'ADD YOUR EXPENSE HERE...')
    grocery = input('Enter Grocery Name: ')
    try:
        amount = float(input('Enter Amount: '))
    except ValueError:
        print(Fore.RED, "Invalid input for amount. Please enter a number.")
        return
    date = input('Enter Date (yyyy-mm-dd): ')

    expanse_list.append({'Grocery': grocery, 'Amount': amount, 'Date': date})
    total_amount += amount




def show_list():
    """Display the list of expenses."""
    print(Fore.GREEN, 'YOUR EXPENSE LIST HERE...')
    if not expanse_list:
        print(Fore.YELLOW, 'Your expense list is empty.')
    else:
        print(f"{'Date':<15} {'Grocery':<20} {'Amount':<10}")
        print("-" * 45)
        for expanse in expanse_list:
            print(f"{expanse['Date']:<15} {expanse['Grocery']:<20} {expanse['Amount']:<10.2f}")
        print("-" * 45)
        print(Fore.CYAN, f"Your Total Expense is: {total_amount:.2f}")




def download_list():
    """Save the expense list to a text file."""
    if not expanse_list:
        print(Fore.YELLOW, 'No expenses to download.')
    else:
        filename = 'expense_list.txt'
        with open(filename, 'w') as file:
            file.write(f"{'Date':<15} {'Grocery':<20} {'Amount':<10}\n")
            file.write("-" * 45 + "\n")
            for expanse in expanse_list:
                file.write(f"{expanse['Date']:<15} {expanse['Grocery']:<20} {expanse['Amount']:<10.2f}\n")
            file.write("-" * 45 + "\n")
            file.write(f"Total Expense: {total_amount:.2f}\n")
        print(Fore.GREEN, f"File downloaded successfully with the name '{filename}'.")

# Run the program
if __name__ == '__main__':
    main()
