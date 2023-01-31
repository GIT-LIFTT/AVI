import psycopg2

DB_NAME = "template1"
DB_USER = "myusername"
#DB_PASS = "iYYtLAXVbid-i6MV3NO1EnU-_9SW2uEi"
DB_HOST = "192.168.203.214"
DB_PORT = "5432"

#try:
conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password="password",
                            host=DB_HOST,
                            port=DB_PORT)
cur = conn.cursor()
cur.execute("\dt")