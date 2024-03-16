# lib/config.py
import sqlite3

CONN = sqlite3.connect('compani.db')
CURSOR = CONN.cursor()
