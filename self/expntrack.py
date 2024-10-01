import csv
import os
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

FILE_NAME = 'expenses.csv'

def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            
def add_expense():
    while  True:
        try:
            date = input(Fore.YELLOW+"Enter date (YYYY-MM-DD): ")
            datetime.strptime(date,  '%Y-%m-%d')
            break
        except ValueError:
            print(Fore.RED+"Invalid date. Please use YYYY-MM-DD format.")
            
    while True:
        try:
            amount = float(input(Fore.YELLOW+"Enter amount: $"))
            break
        except ValueError:
            print(Fore.RED+"Invalid amount. Please enter a number.")
            
    category =  input(Fore.YELLOW+"Enter category(e.g.,  food, transportation, etc.): ").capitalize()
    description = input(Fore.YELLOW+"Enter  description(optional): ")
    
    with  open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount,  category, description])

    print(Fore.GREEN+"\n Expense  added successfully!\n")
    
def  view_expenses():
    print(Fore.CYAN+"\nExpenses\n")
    with open(FILE_NAME, mode='r') as  file:
        reader =  csv.reader(file)
        data = list(reader)
        if len(data) > 1:
            print(tabulate(data[1:], headers=[0], tablefmt='fancy_grid'))
        else:
            print(Fore.RED+"No expenses recorded yet.")
            
    print()

def delete_expense():
    view_expenses()
    data_to_delete = input(Fore.YELLOW+"Enter the data of the expense to delete(YYYY-MM-DD): ")
    
    with open(FILE_NAME, mode='r') as  file:
        lines = file.readlines()
        
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for line in lines:
            if not line.startswith(data_to_delete):
                file.write(line)

    print(Fore.GREEN+"\nExpense deleted successfully !\n")

def show_summary():
    total_spent = 0
    category_breakdown = {}
    
    with open(FILE_NAME, mode='r') as file:
        reader  = csv.reader(file)
        next(reader)
        for row in reader:
            amount = float(row[1])
            category  = row[2]
            total_spent += amount
            if category in  category_breakdown:
                category_breakdown[category] += amount
            else:
                category_breakdown[category] = amount
    print(Fore.CYAN + f"\nTotal spend: $(total _spent:.2f)")
    print(Fore.CYAN+"\nCategory  breakdown:")
    for  category, amount in category_breakdown.items():
        print(f"{category}: ${amount:.2f}")
        
    print()
    
def filter_expenses_by_date():
    start_date = input(Fore.YELLOW+"Enter start date(YYYY-MM-DD): ")
    end_date = input(Fore.YELLOW+"Enter end date(YYYY-MM-DD): ")
    
    filtered_expenses = []
    with  open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for  row in reader:
            date = row[0]
            if start_date <= date <= end_date:
                filtered_expenses.append(row)

    if  filtered_expenses:
        print(Fore.CYAN+f"\nExpenses from  {start_date} to {end_date}: \n")
        print(tabulate(filtered_expenses, headers=["Date", "Amount",  "Category", "Description"], tablefmt="fancy_grid"))
    else:
        print(Fore.RED+f"\nNo expenses found for the given date range.\n")
    print()
    
def menu():
    while  True:
        print(Fore.LIGHTGREEN_EX + "---- Personal Expense Tracker ----")
        print(Fore.LIGHTBLUE_EX + "1. Add Expense")
        print(Fore.LIGHTBLUE_EX + "2. View Expenses")
        print(Fore.LIGHTBLUE_EX + "3. Delete Expense")
        print(Fore.LIGHTBLUE_EX + "4. Show Summary")
        print(Fore.LIGHTBLUE_EX + "5. Filter Expenses by Date")
        print(Fore.LIGHTRED_EX + "6. Exit")

        choice = input(Fore.LIGHTGREEN_EX + "Enter your choice(1-6): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            filter_expenses_by_date()
        elif choice == '6':
            print(Fore.LIGHTRED_EX + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
            
if  __name__ == "__main__":
    initialize_csv()
    menu()
