import psycopg2


def create_db(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        cur.execute(f'create database {database}')
        print(f'Database created successfully')
    except Exception as e:
        print('Error creating a database:', str(e))


def create_tables(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()


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

def add_client(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        first_name = input("Enter the client's first name: ")
        last_name = input("Enter the client's last name: ")
        email = input("Enter the client's email: ")
        cur.execute("""
                    insert into users(first_name, last_name, email)
                    values (%s, %s, %s)
                    """, (first_name, last_name, email))
        print('Client added successfully')
    except Exception as e:
        print('Error trying to add a client: ', str(e))


def add_phone_number(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        user_id = input("Enter the client's id to add a phone number: ")
        phone_number = input("Enter the phone number: ")
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
            print(f'Phone number added successfully')
        else:
            print(f'User with {user_id} does not exist')
    except Exception as e:
        print('Error finding a client: ', str(e))

def update_client_info(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        user_id = int(input("Enter the client's id for the client you want to update: "))

        cur.execute("""
                    select * from users
                    where id = %s
                    """, (user_id,))
        result = cur.fetchone()

        if result:
            column_name = input('Enter the column name(s) you would like to update separated by comma: ')
            columns = [col.strip() for col in column_name.split(',')]

            for col in columns:
                new_value = input(f'Enter the new value for {col}: ')
                cur.execute(f"""
                            update users
                            set {col} = %s
                            where id = %s
                            """, (new_value, user_id))

            print('Client information updated successfully')
        else:
            print(f'Client with user_id {user_id} does not exist')
    except Exception as e:
        print("Error updating client's info: ", str(e))

def delete_phone_number(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        user_id = input("Enter client's id for client for whom you want to delete the phone number: ")
        cur.execute("""
                    select * from phone_numbers
                    where user_id = %s
                    """, (user_id,))
        result = cur.fetchone()

        if result:
            cur.execute("""
                        delete from phone_numbers
                        where user_id = %s
                        """, (user_id,))
            print("Client's phone number deleted successfully")
        else:
            print(f'User with {user_id} does not exist')
    except Exception as e:
        print("Error updating client's info: ", str(e))

def delete_client(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        user_id = input('Enter the user_id for client who you wish to delete: ')
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

def find_client(database, user, password):
    conn = psycopg2.connect(database=database, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()

    try:
        value = input("Enter client's first name, last name, email or phone number: ")
        cur.execute("""
                    select u.*, pn.phone_number from users u
                    left join phone_numbers pn on pn.user_id = u.id
                    where u.first_name = %s
                        or u.last_name = %s
                        or u.email = %s
                        or pn.phone_number = %s
                        """, (value, value, value, value))
        result = cur.fetchall()

        if result:
            print('Client info: ')
            for row in result:
                print(row)
        else:
            print('Input value does not match any info')

    except Exception as e:
        print('Error finding a client: ', str(e))



with psycopg2.connect(database='personal_info', user='postgres', password='Ulik2054768') as conn:
    # create_db('personal_info', 'postgres', 'Ulik2054768')
    # create_tables('personal_info', 'postgres', 'Ulik2054768')
    # add_client('personal_info', 'postgres', 'Ulik2054768')
    # add_phone_number('personal_info', 'postgres', 'Ulik2054768')
    # update_client_info('personal_info', 'postgres', 'Ulik2054768')
    # delete_phone_number('personal_info', 'postgres', 'Ulik2054768')
    # delete_client('personal_info', 'postgres', 'Ulik2054768')
    find_client('personal_info', 'postgres', 'Ulik2054768')
