from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "mysql",
    "port": "3306",
    "user": "root",
    "password": "root",
    "database": "edutrack"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notifications', methods=['GET'])
def get_schedules():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM schedules")
    schedules = cursor.fetchall()
    connection.close()
    return jsonify(schedules)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
