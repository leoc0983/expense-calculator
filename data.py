def main() -> None:
    data = get_input()

def get_input() -> list[tuple(str, float)]:
    expenses = []
    name = input('Enter the name of the expense (or x to quit): ')
    cost = input('Enter the cost of the expense: ')
    while(name != 'x'):
        expenses.append(tuple(name, cost))
        name = input('Enter the name of the expense (or x to quit): ')
        cost = input('Enter the cost of the expense: ')
    return expenses

if __name__ == '__main__':
    main()