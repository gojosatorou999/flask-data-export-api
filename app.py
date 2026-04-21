import sqlite3
from flask import Flask, Response, stream_with_context
import csv
import io

app = Flask(__name__)

DB_NAME = 'data.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return {
        "message": "Flask Data Export API",
        "endpoints": {
            "/export": "Export users table as CSV"
        }
    }

@app.route('/export')
def export_csv():
    def generate():
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Execute query
        cursor.execute('SELECT * FROM users')
        
        # Get column headers
        headers = [description[0] for description in cursor.description]
        
        # Use io.StringIO to gather CSV rows
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write headers
        writer.writerow(headers)
        yield output.getvalue()
        output.seek(0)
        output.truncate(0)
        
        # Fetch and write rows
        for row in cursor:
            writer.writerow(list(row))
            yield output.getvalue()
            output.seek(0)
            output.truncate(0)
            
        conn.close()

    return Response(
        stream_with_context(generate()),
        mimetype='text/csv',
        headers={"Content-disposition": "attachment; filename=users_export.csv"}
    )

if __name__ == '__main__':
    app.run(debug=True)
