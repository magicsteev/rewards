from http.server import BaseHTTPRequestHandler
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import psycopg2
import json



class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        conn = psycopg2.connect(
        host="ep-bitter-term-594574-pooler.eu-central-1.postgres.vercel-storage.com",
        database="verceldb",
        user="default",
        password="iTr5WyGdCo1p"
        )
        # Création d'un curseur pour exécuter les requêtes SQL
        cursor = conn.cursor()
        query = "SELECT TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI:SS') AS formatted_timestamp, validator_name, denom, ROUND(amount, 0) AS amount FROM rewards"
        cursor.execute(query)
        rows = cursor.fetchall()
        data = {
            "labels": [],
            "datasets": []
        }

        # Dictionnaire pour stocker les données de chaque label
        label_data = {}

        for row in rows:
            timestamp, validator_name, denom, amount = row

            # Ajouter le label si ce n'est pas déjà présent dans le dictionnaire
            if timestamp not in label_data:
                label_data[timestamp] = {
                    "data": [],
                    "label": timestamp,
                    "borderColor": "#000000",
                    "backgroundColor": "#000000",
                    "fill": False
                }

            # Ajouter les données dans le dictionnaire correspondant au label
            label_data[timestamp]["data"].append(int(amount))

            # Ajouter le label s'il n'est pas déjà présent dans la liste des labels
            if timestamp not in data["labels"]:
                data["labels"].append(timestamp)

        # Ajouter les données de chaque label dans le dataset
        for label, label_info in label_data.items():
            data["datasets"].append(label_info)
        cursor.close()
        conn.close()
        
        json_data = json.dumps(data)
        #json_data = print(data)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(json_data.encode('utf-8'))
         self.wfile.close()
        return


