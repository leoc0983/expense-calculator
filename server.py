import socket
import sqlite3

def start_server(host_address, host_port):
    with socket.socket() as srv:
        srv.bind((host_address, host_port))

        #set up to be ready to establish connection with client
        srv.listen()
        print('Expense calculator server listening on port', host_port)

        connection, address = srv.accept()
        print(f'Client at: {address}')

        with connection:
            print('Client connected')

            #receive data from client
            rec_msg = connection.recv(4096)

            data = rec_msg.decode().strip()

            create_db()

            #reformat received data and store it in the SQL database
            for line in data.splitlines():
                if ':' in line:
                    name, cost = line.split(':', 1)
                    real_cost = round(float(cost.strip()), 2)
                    store_expense(name.strip(), real_cost)
                    print(f'{name}: ${real_cost}')

            #send sorted data back to client
            expenses = get_expenses()
            response = []
            for name, cost in expenses:
                response.append(f'{name}: ${cost}')
            response_text = '\n'.join(response) + '\n'
            connection.sendall(response_text.encode())

            print('Client disconnected')

def create_db():
    #creates and/or gets the database ready for next steps
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cost INTEGER NOT NULL
        ) STRICT;'''
    )
    connection.commit()
    connection.close()

def store_expense(name, cost):
    #obtains formatted data and inserts it into the database
    cost_in_cents = int(round(cost * 100))
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO expenses (name, cost)
        VALUES (?, ?);''', (name, cost_in_cents)
    )
    connection.commit()
    connection.close()

def get_expenses():
    #obtains all data from the database to send back to the client
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT name, cost
    FROM expenses
    ORDER BY cost DESC;'''
    )
    entries = cursor.fetchall()
    connection.close()
    return [(name, cost/100.00) for name, cost in entries]

if __name__ == '__main__':
    start_server('localhost', 8000)