from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection variables
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'akshay')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'akshay')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'akshay')

# Establish a connection to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB
    )
    return conn

@app.route('/')
def get_counter():
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()

    # Retrieve the current counter value
    cur.execute('SELECT counter FROM counter_table WHERE id = 1;')
    result = cur.fetchone()

    if result:
        current_count = result[0]
    else:
        # If no record exists, initialize counter to 0
        current_count = 0

    # Increment the counter value
    new_count = current_count + 1

    # Update the counter in the database (updating or inserting)
    cur.execute('INSERT INTO counter_table (id, counter) VALUES (1, %s) ON CONFLICT (id) DO UPDATE SET counter = %s;', (new_count, new_count))
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return f"Akshay Counter Value: {new_count}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)