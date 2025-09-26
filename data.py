#runs the program
def main() -> None:
    data = get_input()
    print(get_report(data))

#asks the user for input and formats it as a list sorted by cost
def get_input() -> list[tuple]:
    expenses = []
    name = input('Enter the name of the expense (or x to quit): ')
    while(name != 'x'):
        try:
            cost = float(input('Enter the cost of ' + str(name) + ': '))
            expenses.append((cost, name))
            name = input('Enter the name of the expense (or x to quit): ')
        except:
            print('Error: cost must be a valid number')
    return sorted(expenses)

#obtains the total cost of all items
def get_total_cost(data: list[tuple]) -> float:
    total_cost = 0
    for item in data:
        total_cost += item[0]
    return total_cost

#returns a string with the cost report
def get_report(data: list[tuple]) -> str:
    total_cost = get_total_cost(data)
    ret = 'Total cost of all items: ' + str(total_cost) + '\n'
    for item in data:
        percent_cost = round((item[0] / total_cost), 2)
        ret += 'Expense: ' + item[1] + ' Price: ' + str(item[0]) + ' Percent of total cost: ' + str(percent_cost) + '\n'
    return ret

if __name__ == '__main__':
    main()