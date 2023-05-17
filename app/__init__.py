"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi628t269vf5qab7av0-a.oregon-postgres.render.com",
        database="to_do_50pu",
        user="to_do_50pu_user",
        password="6DGC2LeWl11dFplV9QuJrhz2rPxk3O6M")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
