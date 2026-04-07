# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


employee_data = pd.read_sql("""SELECT * FROM employees""", conn)

order_details = pd.read_sql("SELECT * from orderDetails", conn)

# STEP 2
# Replace None with your code
df_first_five_query = """
SELECT employeeNumber, lastName
FROM employees
"""

df_first_five = pd.read_sql(df_first_five_query, conn)

# STEP 3
# Replace None with your code
df_five_reverse_query = """
SELECT lastName, employeeNumber
FROM employees
"""

df_five_reverse = pd.read_sql(df_five_reverse_query, conn)

# STEP 4
# Replace None with your code
df_alias_query = """
SELECT lastName, employeeNumber AS 'ID'
FROM employees
"""

df_alias = pd.read_sql(df_alias_query, conn)

# STEP 5
# Replace None with your code
df_executive_command = """
SELECT *, 
    CASE 
        WHEN jobTitle = 'President' 
          OR jobTitle = 'VP Sales' 
          OR jobTitle = 'VP Marketing' 
          THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
"""
df_executive = pd.read_sql(df_executive_command, conn)


# STEP 6
# Replace None with your code
df_name_length_query = """
SELECT LENGTH(lastName) AS name_length
FROM employees
"""
df_name_length = pd.read_sql(df_name_length_query, conn)

# STEP 7
# Replace None with your code
df_short_title_query = """
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees;
"""

df_short_title = pd.read_sql(df_short_title_query, conn)

# STEP 8
# Replace None with your code
print(order_details)

sum_total_price_query = """
SELECT SUM(ROUND(priceEach * quantityOrdered)) AS totalPrice
FROM orderDetails
"""

sum_total_price = pd.read_sql(sum_total_price_query, conn)

print(sum_total_price)

# STEP 9
# Replace None with your code
test = """
SELECT 
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders;
"""

df_day_month_year = pd.read_sql(test, conn)

