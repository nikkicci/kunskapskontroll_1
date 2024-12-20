# Currency downloader 

This Python code implements a program that retrieves exchange rates from an API, converts the data into a table, and saves it to a SQLite database. After this, tests and a schedule are run in the Windows scheduler.

## Used extensions in Visual Studio Code
```bash
Python
Pylance
Python Debugger
Python Environment Manager
SQLite
Conda Env Activator
```

## Installation
```bash
conda create
conda install pandas
conda install requests
```

## Imported modules
```bash
requests:   Used to make HTTP requests to an API.
json:       Used to interpret JSON responses from the API.
pandas:     A data management library used to structure currency information in a table.
sqlite3:    Provides access to SQLite databases to store the data.
sys:        Used to terminate the program in case of critical errors.
logging:    Used to log messages and errors.
```

## Functions
```bash
bail(message)
```
* Logs an error message and exits the program.
* Used to handle critical errors that prevent the program from continuing.
```bash
fetch_currencies()
```
* Sends a GET request to an API.
* If the API responds with a status code other than 200, or if an exception occurs, an error is thrown.
* Returns the JSON response as a Python data structure.
```bash
convert_currencies(json_currencies)
```
* Converts the JSON data from the API into a pandas DataFrame.
* Each currency code and its rate is represented as a row in the table.
* Ensures that the exchange rates (rate) are numeric.
* If the data is not in the correct format, an exception is thrown.
```bash
export_currencies(df)
```
* Saves the DataFrame contents to a SQLite database (currencies.db).
* The "currencies" table is created or replaced if it already exists.
* If the database cannot be accessed or saved, an exception is thrown.

## Headfunction: main()

* Sets up logging to a file (currencies.log).
* Run the three main functions:

    1. fetch_currencies(): Retrieves exchange rates from the API.
    2. convert_currencies(payload): Converts the JSON data to a table.
    3. export_currencies(df): Saves the table in an SQLite database.

* If something goes wrong, the error is logged and the program exits.

Upon successful execution, a message is logged that the currencies have been exported.