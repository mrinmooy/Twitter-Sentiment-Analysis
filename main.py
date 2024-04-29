import pymysql
from pymysql import Error

def connect_to_database():
    """ Connect to MySQL database server and insert data """
    connection = None
    try:
        connection = pymysql.connect(
            host='sql5.freesqldatabase.com',
            user='sql5702693',  # Replace with your actual username
            password='HfQNBBzFVX',  # Replace with your actual password
            database='sql5702693',
            port=3306
        )
        
        print("Successfully connected to MySQL database.")
      

        # Inserting data
        my_string = "first tweet"
        my_bool = 0
        
        # Truncate string to the first 100 characters if longer
        my_string = my_string[:100]
        
     

        with connection.cursor() as cursor:
            insert_query = """
            INSERT INTO allTweets (Content, Sentiment) VALUES (%s, %s);
            """
            cursor.execute(insert_query, (my_string, my_bool))
            connection.commit()
            print(f"Data inserted: {my_string}, {my_bool}")

    except Error as e:
        print("Error while connecting to MySQL or operating", e)

    finally:
        if connection and connection.open:
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_to_database()

#do i really need this?
#or maybe not
#okay maybe i do