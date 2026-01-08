import pandas as pd
import mysql.connector

df = pd.read_csv("E:\Data Analysis\AdvanceSQL_Metabase\datasets\Coffe Sales\CoffeeShopSales.csv")
# print(df.shape)
# change date format to mysql friendly format
# df["transaction_date"] = pd.to_datetime(df["transaction_date"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Tayeb680364#",
        database="coffee_shop_sales"
    )
    print("✅ MySQL connected")

    cur = conn.cursor()

    # Define the Sql Query

    sql = """
        INSERT INTO coffee_sales(
            transaction_id,
            transaction_date,
            transaction_time,
            transaction_qty,
            store_id,
            store_location,
            product_id,
            unit_price,
            product_category,
            product_type,
            product_detail 
        ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    # convert dataframe to list of tuples
    data = [tuple(row) for row in df.itertuples(index=False)]

    # Use executemany for bulk insert
    cur.executemany(sql, data)

    # cur.execute("SELECT USER(), CURRENT_USER(), DATABASE();")
    # print("Connected as:", cur.fetchone())

    #commit and close
    conn.commit()
    cur.close()
    conn.close()

    print("Bulk Insertion Completed Successfully")

except Exception as e:
    print("Error:", e)


