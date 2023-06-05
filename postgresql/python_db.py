import psycopg2


def create_db(database, cur):
    try:
        cur.execute('create database ' + database)
        print(f'Database created successfully')
    except Exception as e:
        print('Error creating a database:', str(e))


def create_tables(cur):
    try:
        cur.execute("""
                       create table if not exists users (
                       id SERIAL primary key,
                       first_name VARCHAR(100) not null,
                       last_name VARCHAR(100) not null,
                       email VARCHAR(100) not null
                       )
                       """)
        cur.execute("""
                    create table if not exists phone_numbers (
                    id SERIAL primary key,
                    user_id integer references users(id),
                    phone_number VARCHAR(20)
                    )
                    """)

        print('Table created successfully')
    except Exception as e:
        print('Error creating tables:', str(e))

def add_client(cur, first_name, last_name, email):
    try:
        cur.execute("""
                    insert into users(first_name, last_name, email)
                    values (%s, %s, %s)
                    """, (first_name, last_name, email))
        print('Client added successfully')
    except Exception as e:
        print('Error trying to add a client: ', str(e))


def add_phone_number(cur, user_id, phone_number):
    try:
        cur.execute("""
                    select id from users
                    where id = %s              
                    """, (user_id,))
        result = cur.fetchall()

        if result:
            cur.execute("""
                        insert into phone_numbers(user_id, phone_number)
                        values (%s, %s)
                        """, (user_id, phone_number))
            print(f'Phone number {phone_number} added successfully')
        else:
            print(f'User with {user_id} does not exist')
    except Exception as e:
        print('Error finding a client: ', str(e))

def update_client_info(cur, user_id, column_name, new_value):
    try:
        cur.execute("""
                    select * from users
                    where id = %s
                    """, (user_id,))
        result = cur.fetchone()

        if result:
            query = """
                    update users
                    set {} = %s
                    where id = %s
                    """.format(column_name)
            cur.execute(query, (new_value, user_id))

            print('Client information updated successfully')
        else:
            print(f'Client with user_id {user_id} does not exist')
    except Exception as e:
        print("Error updating client's info: ", str(e))

def delete_phone_number(cur, phone_number):
    try:
        cur.execute("""
                    select * from phone_numbers
                    where phone_number = %s
                    """, (phone_number,))
        result = cur.fetchone()

        if result:
            cur.execute("""
                        delete from phone_numbers
                        where phone_number = %s
                        """, (phone_number,))
            print("Client's phone number deleted successfully")
        else:
            print(f'Phone_number {phone_number} does not exist')
    except Exception as e:
        print("Error deleting a phone number: ", str(e))

def delete_client(cur, user_id):
    try:
        cur.execute("""
                    select * from users
                    where id = %s
                    """, (user_id,))
        result = cur.fetchone()

        if result:
            cur.execute("""
                        delete from phone_numbers
                        where user_id = %s
                        """, (user_id,))
            cur.execute("""
                        delete from users
                        where id = %s
                        """, (user_id,))
            print(f"Client with {user_id} and their phone number deleted successfully")

        else:
            print(f'User with {user_id} does not exist')


    except Exception as e:
        print("Error updating client's info: ", str(e))

def find_client(cur, value):
    try:
        query =  """
                    select u.*, pn.phone_number from users u
                    left join phone_numbers pn on pn.user_id = u.id
                    where 1=1
                    """
        parameters = []
        value_parts = value.split(' ')

        if len(value_parts) >= 1:
            query += " and (u.first_name = %s or u.last_name = %s or u.email = %s or pn.phone_number = %s)"
            parameters.extend([value_parts[0], value_parts[0], value_parts[0], value_parts[0]])
        if len(value_parts) >= 2:
            query += " and (u.first_name = %s or u.last_name = %s or u.email = %s or pn.phone_number = %s)"
            parameters.extend([value_parts[1], value_parts[1], value_parts[1], value_parts[1]])
        if len(value_parts) >= 3:
            query += " and (u.first_name = %s or u.last_name = %s or u.email = %s or pn.phone_number = %s)"
            parameters.extend([value_parts[2], value_parts[2], value_parts[2], value_parts[2]])
        if len(value_parts) >= 4:
            query += " and (u.first_name = %s or u.last_name = %s or u.email = %s or pn.phone_number = %s)"
            parameters.extend([value_parts[3], value_parts[3], value_parts[3], value_parts[3]])
        cur.execute(query, parameters)
        result = cur.fetchall()

        if result:
            print('Client info: ')
            for row in result:
                print(row)
        else:
            print('Input value does not match any info')

    except Exception as e:
        print('Error finding a client: ', str(e))

if __name__ == '__main__':
    with psycopg2.connect(database='personal_info', user='postgres', password=password) as conn:
        conn.autocommit = True
        cur = conn.cursor()
        print('1 = create database, 2 = create tables, \n'
              '3 = add a client, 4 = add a phone number, \n'
              '5 = update client info, 6 = delete phone number, \n'
              '7 = delete client, 8 = find a client')
        command = (input('Enter a command: ')).lower()
        if command == '1':
            create_db('personal_info', cur)
        elif command == '2':
            create_tables(cur)
        elif command == '3':
            first_name = input("Enter the client's first name: ")
            last_name = input("Enter the client's last name: ")
            email = input("Enter the client's email: ")
            add_client(cur, first_name, last_name, email)
        elif command == '4':
            user_id = input("Enter the client's id to add a phone number: ")
            phone_number = input("Enter the phone number: ")
            add_phone_number(cur, user_id, phone_number)
        elif command == '5':
            user_id = int(input("Enter the client's id for the client you want to update: "))
            column_name = input('Enter the column name you would like to update: ')
            new_value = input('Enter the new value for the column: ')
            update_client_info(cur, user_id, column_name, new_value)
        elif command == '6':
            phone_number = input('Enter a phone number you would like to delete: ')
            delete_phone_number(cur, phone_number)
        elif command == '7':
            user_id = input('Enter the user_id for client who you wish to delete: ')
            delete_client(cur, user_id)
        elif command == '8':
            value = input("Enter client's first name, last name, email or phone number: ")
            find_client(cur, value)
