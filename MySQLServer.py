import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="Localhost",
        user="root",
        Password="Preciousthomas28@"
    )

    mycursor = mydb.cursor()
    mycursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")
    print("Database created successfully")

except mysql.connector.Error:
    print("Please connect to a server")

finally:
    # Close connection
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
