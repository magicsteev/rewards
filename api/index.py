from http.server import BaseHTTPRequestHandler
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
        )
        # Création d'un curseur pour exécuter les requêtes SQL
        cursor = conn.cursor()
        cursor.close()
        conn.close()
        return
