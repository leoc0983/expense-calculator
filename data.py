#runs the program
def main() -> None:
    data = get_input()
    process_input(data)

#asks the user for input and formats it as a list
def get_input() -> list[tuple(str, float)]:
    expenses = []
    name = input('Enter the name of the expense (or x to quit): ')
    cost = input('Enter the cost of the expense: ')
    while(name != 'x'):
        expenses.append(tuple(name, cost))
        name = input('Enter the name of the expense (or x to quit): ')
        cost = input('Enter the cost of the expense: ')
    return expenses

#performs calculations with the obtained data
def process_input(data: list[tuple(str, float)]) -> None:
    pass

if __name__ == '__main__':
    main()