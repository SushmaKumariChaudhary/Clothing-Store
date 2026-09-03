import oracledb

# Oracle database connection details
USERNAME = "CLOTHING_STORE"
PASSWORD = "Clothing123"
HOST = "localhost"
PORT = 1521
SERVICE_NAME = "xepdb1"

try:
    connection = oracledb.connect(
        user=USERNAME,
        password=PASSWORD,
        dsn=f"{HOST}:{PORT}/{SERVICE_NAME}"
    )

    print("Oracle connection successful!")

    cursor = connection.cursor()
    cursor.execute("SELECT SYSDATE FROM dual")

    result = cursor.fetchone()
    print("Oracle Server Date:", result[0])

    cursor.close()
    connection.close()

    print("Connection closed successfully.")

except oracledb.Error as error:
    print("Oracle connection failed!")
    print("Error:", error)