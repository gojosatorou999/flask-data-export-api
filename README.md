# Flask Data Export API

A simple Flask application that serves an API to export database records (SQLite) as a CSV file.

## Features
- **CSV Export**: Stream database data directly to a downloadable CSV file.
- **SQLite Integration**: Uses lightweight SQLite for data storage.
- **Efficient Streaming**: Leverages `stream_with_context` for handling large datasets without high memory overhead.

## Setup :

1. **Install Dependencies**
   ```bash
   pip install flask
   ```

2. **Initialize Database**:
   Run the initialization script to create the SQLite database and populate it with sample data.
   ```bash
   python init_db.py
   ```

3. **Run the API**:
   ```bash
   python app.py
   ```

## API Endpoints

### 1. `GET /`
Returns a simple JSON response with API information.

### 2. `GET /export`
Triggers a file download of the `users` table in CSV format.
- **Filename**: `users_export.csv`
- **MIME Type**: `text/csv`

## Project Structure
- `app.py`: Main Flask application logic and export routes.
- `init_db.py`: Database setup and seeding script.
- `data.db`: SQLite database file (generated after running `init_db.py`).
- `README.md`: Project documentation.
