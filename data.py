#runs the program
def main() -> None:
    data = get_input()
    print(get_report(data))

#asks the user for input and formats it as a list sorted by cost
def get_input() -> list[tuple(float, str)]:
    expenses = []
    name = input('Enter the name of the expense (or x to quit): ')
    cost = input('Enter the cost of the expense: ')
    while(name != 'x'):
        expenses.append(tuple(cost, name))
        name = input('Enter the name of the expense (or x to quit): ')
        cost = input('Enter the cost of the expense: ')
    return sorted(expenses)

#obtains the total cost of all items
def get_total_cost(data: list[tuple(float, str)]) -> float:
    total_cost = 0
    for item in data:
        total_cost += item[1]
    return total_cost

#returns a string with the data report
def get_report(data: list[tuple(float, str)], total_cost: float) -> str:
    pass

if __name__ == '__main__':
    main()