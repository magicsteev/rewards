from http.server import BaseHTTPRequestHandler
import psycopg2
import json


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        
        
        conn = psycopg2.connect(
        host="ep-bitter-term-594574-pooler.eu-central-1.postgres.vercel-storage.com",
        database="verceldb",
        user="default",
        password="iTr5WyGdCo1p"
        
        cursor = conn.cursor()
)
        
        query = "SELECT timestamp, validateur, denom, amount FROM rewards"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        data = {
                "labels": [],
                "datasets": []
            }

            # Dictionnaire pour stocker les données de chaque label
            label_data = {}

            for row in rows:
                timestamp, validateur, denom, amount = row

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
                label_data[timestamp]["data"].append(amount)

                # Ajouter le label s'il n'est pas déjà présent dans la liste des labels
                if timestamp not in data["labels"]:
                    data["labels"].append(timestamp)

            # Ajouter les données de chaque label dans le dataset
            for label, label_info in label_data.items():
                data["datasets"].append(label_info)
        
        
        cursor.close()
        conn.close()
        return
