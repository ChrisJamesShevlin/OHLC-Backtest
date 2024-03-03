# Function to fetch stock market data from MySQL database
def fetch_stock_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data")  # Modified to select from 'data' table
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)
        cursor.close()
        return df
    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")

# Function to analyze buy order strategy
def analyze_buy_order_strategy(data):
    num_trades = 0
    profit = 0

    for i in range(len(data) - 1):
        open_price_today = data['Open'][i]
        close_price_next_day = data['Close'][i + 1]

        if close_price_next_day > open_price_today:
            profit += close_price_next_day - open_price_today
            num_trades += 1

    return num_trades, profit

# Main function
def main():
    # Connect to MySQL database
    connection = connect_to_mysql()

    if connection:
        # Fetch stock market data
        stock_data = fetch_stock_data(connection)

        if stock_data is not None:
            # Analyze buy order strategy
            num_trades, profit = analyze_buy_order_strategy(stock_data)

            print(f"Number of trades: {num_trades}")
            print(f"Total profit: ${profit:.2f}")
        else:
            print("No data fetched from the database.")

        # Close database connection
        connection.close()
        print("Connection to MySQL database closed.")

if __name__ == "__main__":
    main()
