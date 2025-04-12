import psycopg

try:
    conn = psycopg.connect(
        host="mainline.proxy.rlwy.net",
        port=12916,
        dbname="railway",
        user="postgres",
        password="AMVBDAnaRyxYNxDYyyCXlrEwcHRPyXTj",
        sslmode="require"
    )
    print("PostgreSQL bağlantısı başarılı!")
    conn.close()
except Exception as e:
    print(f"Bağlantı hatası: {e}")