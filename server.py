import socket
import sqlite3

def start_server(host_address, host_port):
    with socket.socket() as srv:
        srv.bind((host_address, host_port))

        srv.listen()
        print('Expense calculator server listening on port', host_port)

        connection, address = srv.accept()
        print(f'Client at: {address}')

        with connection:
            print('Client connected')

            rec_msg = connection.recv(4096)

            print(rec_msg.decode())

            connection.sendall(rec_msg)

            print('Client disconnected')

def create_db():
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cost INTEGER NOT NULL
    ''')
    connection.commit()
    connection.close()

if __name__ == '__main__':
    start_server('localhost', 8000)