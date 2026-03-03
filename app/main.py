import os
import time
import psycopg2
from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = 10
RETRY_DELAY = 3

for attempt in range(MAX_RETRIES):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Conectado ao banco com sucesso.")
        break
    except psycopg2.OperationalError:
        print(f"Tentativa {attempt + 1} falhou. Aguardando banco subir...")
        time.sleep(RETRY_DELAY)
else:
    raise Exception("Não foi possível conectar ao banco.")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO vendas (produto, quantidade, preco, data_venda)
VALUES ('Notebook', 2, 3500.00, CURRENT_DATE);
""")

conn.commit()
cursor.close()
conn.close()

print("Inserção realizada com sucesso.")
