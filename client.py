import socket

def start_client():
    with socket.socket() as expense_socket:

        connect_address = ('127.0.0.1', 8000)
        expense_socket.connect(connect_address)

        input_stream = expense_socket.makefile('r')
        output_stream = expense_socket.makefile('w')

        output_stream.write(get_input())
        output_stream.flush()

        for line in input_stream.readlines():
            print(line.strip())

def get_input() -> str:
    expenses = ''
    name = input('Enter the name of the expense (or q to quit): ')
    while name != 'q':
        cost = input('Enter the cost of ' + name + ': ')
        expenses += name + ': $' + cost + '\n'
        name = input('Enter the name of the expense (or q to quit): ')
    return expenses

if __name__ == '__main__':
    start_client()