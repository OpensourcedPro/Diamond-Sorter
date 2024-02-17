import requests
import sqlite3
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

import requests
import mysql.connector
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a table widget
        self.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

    def display_results(self, results):
        # Set the table dimensions
        self.table_widget.setRowCount(len(results))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Website", "Number of Cookies", "Min Age", "Max Age"])

        # Populate the table with results
        for row, result in enumerate(results):
            domain, num_cookies, min_age, max_age = result
            self.table_widget.setItem(row, 0, QTableWidgetItem(domain))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(num_cookies)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(min_age)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(max_age)))


def retrieve_data(website):
    # Send request to the specified URL
    url = f"https://api.cookieserve.com/get_scan_result?url={website}"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data as JSON
        data = response.json()

        # Connect to the SQLite database
        conn = sqlite3.connect('cookie_data.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS cookies
                          (domain TEXT, cookie_name TEXT, cookie_id TEXT, url TEXT, duration TEXT, type TEXT, storage_type TEXT, description TEXT, request_datetime TEXT)''')

        # Insert the data into the table
        for category, cookies_list in data.items():
            for cookie in cookies_list:
                cookie_name = cookie.get("cookie_name")
                cookie_id = cookie.get("cookie_id")
                url = cookie.get("url")
                duration = cookie.get("duration")
                cookie_type = cookie.get("type")
                storage_type = cookie.get("storage_type")
                description = cookie.get("description")
                request_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("INSERT INTO cookies (domain, cookie_name, cookie_id, url, duration, type, storage_type, description, request_datetime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (website, cookie_name, cookie_id, url, duration, cookie_type, storage_type, description, request_datetime))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print(f"Data stored for {website} successfully.")
    else:
        print(f"Error occurred while retrieving data for {website}.")



    # Connect to the SQLite database
    conn = sqlite3.connect('cookie_data.db')
    cursor = conn.cursor()

    # Query the database to get the number of cookies and age ranges for each website
    cursor.execute('''SELECT domain, COUNT(*) AS num_cookies, MIN(duration) AS min_age, MAX(duration) AS max_age
                      FROM cookies
                      GROUP BY domain''')
    results = cursor.fetchall()

    # Display the results
    for result in results:
        domain, num_cookies, min_age, max_age = result
        print(f"Website: {domain}")
        print(f"Number of Cookies: {num_cookies}")
        print(f"Age Range: {min_age} - {max_age} \n")

    # Close the connection
    conn.close()

# Prompt the user to enter websites separated by commas
websites = input("Enter websites (comma-separated): ").split(",")

# Create a thread pool executor
with ThreadPoolExecutor() as executor:
    # Submit retrieval tasks for each website
    for website in websites:
        executor.submit(retrieve_data, website.strip())


if __name__ == "__main__":
    # Prompt the user to enter websites separated by commas
    websites = input("Enter websites (comma-separated): ").split(",")

    # Create a thread pool executor
    with ThreadPoolExecutor() as executor:
        # Submit retrieval tasks for each website
        for website in websites:
            executor.submit(retrieve_data, website.strip())

    # Fetch the results
    results = fetch_results()

    # Create the application and main window
    app = QApplication([])
    window = MainWindow()
    window.display_results(results)
    window.show()

    # Run the application event loop
    app.exec_()