# Stock Market Data Analysis Script

This repository contains a Python script that connects to a **MySQL** database to fetch stock market data and analyze a simple buy order strategy. The script calculates the number of trades and the total profit based on the strategy where a "buy" occurs when the next day's closing price is higher than the current day's opening price.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Strategy Explanation](#strategy-explanation)
- [Customization](#customization)
- [Error Handling](#error-handling)


## Overview

The script performs the following tasks:
1. **Fetches stock market data** from a MySQL database.
2. **Analyzes a buy order strategy** where a trade is made if the next day’s closing price is higher than the current day’s opening price.
3. **Calculates the total number of trades and profit** based on the strategy.

## Prerequisites

To run this script, you need:
- A running **MySQL** database with a table named `data` containing stock market data.
- The stock market table should include at least the following columns: `Open`, `Close`, and possibly others such as `Date`.
- **Python 3** installed on your system.
- The required Python libraries installed.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/stock-market-analysis.git
   cd stock-market-analysis
   ```

2. **Install the required Python dependencies**:
   Install the necessary Python libraries using pip:
   ```bash
   pip install mysql-connector-python pandas
   ```

3. **Set up your MySQL database**:
   Make sure your MySQL server is running and the `data` table contains stock data with `Open` and `Close` columns.

## Usage

1. **Connect to your MySQL database**:
   Ensure that the `connect_to_mysql()` function is set up correctly to connect to your MySQL database. Replace the placeholder function `connect_to_mysql()` with your actual MySQL connection logic:

   ```python
   def connect_to_mysql():
       return mysql.connector.connect(
           host='localhost',
           user='your_username',
           password='your_password',
           database='your_database'
       )
   ```

2. **Run the script**:
   Execute the script to connect to the MySQL database, fetch stock data, analyze the buy order strategy, and print the results:
   ```bash
   python stock_analysis.py
   ```

### Example Output:
```bash
Number of trades: 50
Total profit: $1523.50
Connection to MySQL database closed.
```

## Strategy Explanation

The script follows a simple buy order strategy based on the following logic:
- **Buy Signal**: A trade is considered if the next day's closing price is higher than the current day's opening price.
- **Profit Calculation**: The profit for each trade is calculated as the difference between the next day's closing price and the current day's opening price. The script keeps track of the total profit and number of trades made.

### Example:
If on **Day 1** the stock's opening price is $100 and the closing price on **Day 2** is $105, the script would consider this a valid trade and add a profit of $5.

## Customization

1. **Modify the Buy Order Strategy**:
   You can adjust the buy order logic in the `analyze_buy_order_strategy()` function to suit your needs. For example, you could add more complex conditions for entering a trade, such as using moving averages, indicators, or volume data.

   ```python
   if close_price_next_day > open_price_today:
       # Add custom logic for determining a trade
   ```

2. **Change the SQL Query**:
   The current SQL query fetches all the data from the `data` table. You can modify the query to filter specific data, like a certain time range or a particular stock:

   ```python
   cursor.execute("SELECT * FROM data WHERE Date >= '2023-01-01'")
   ```

3. **Add More Metrics**:
   You can extend the script to calculate additional metrics such as the average trade profit, success rate, or maximum drawdown.

## Error Handling

The script includes basic error handling for the MySQL database connection and data fetching. If an error occurs during data fetching, the error message is printed, and the script proceeds to close the database connection.

```python
except mysql.connector.Error as err:
    print(f"Error fetching data: {err}")
```

Feel free to contribute or suggest improvements by opening an issue or submitting a pull request.
