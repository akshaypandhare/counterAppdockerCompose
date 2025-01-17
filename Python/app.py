from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL configuration from environment variables
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'akshay')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'akshay')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'akshay')

# Connect to PostgreSQL
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
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Retrieve counter value from the database
    cursor.execute('SELECT counter FROM counter_table WHERE id = 1')
    result = cursor.fetchone()

    # If no result found, initialize counter
    if result is None:
        cursor.execute('INSERT INTO counter_table (id, counter) VALUES (1, 0)')
        conn.commit()
        count = 0
    else:
        count = result[0]

    cursor.close()
    conn.close()

    # Return the counter as a message
    return jsonify(message=f'Current count: {count}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
