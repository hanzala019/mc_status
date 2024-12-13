# host     = '192.168.10.254', 
# user     = 'hasib',  
# password  = 'hJ7FIHP57LvFSgRH', 
# database    = 'colorstyle', 
import pymysql
import pymysql
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from pywebpush import webpush, WebPushException
import json
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
CORS(app)

VAPID_PRIVATE_KEY = os.getenv("VAPID_PRIVATE_KEY")
VAPID_PUBLIC_KEY =os.getenv("VAPID_PUBLIC_KEY")
VAPID_CLAIMS = {
        "sub": os.getenv("VAPID_CLAIMS")
    }
# host = "localhost"         # Database host
# user = "root"     # Your database username
# password = "" # Your database password
# database = "ocms-knit-mc" # Your database name
# print(os.getenv("HOST"))
# print(os.getenv("USER"))
# print(os.getenv("PASSWORD"))
# print(os.getenv("DB"))
try:
    # Establish connection
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DB"),
       
    )
    print("Connected to the database!")
except pymysql.MySQLError as e:
    print(f"Error connecting to the database: {e}")

def getAll(query, params=None):
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)  # Execute with parameters
    else:
        cursor.execute(query)  # Execute without parameters
    results = cursor.fetchall()
    cursor.close()
    return results

def getOne(query, params=None):
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)  # Execute with parameters
    else:
        cursor.execute(query)  # Execute without parameters
    result = cursor.fetchone()
    cursor.close()
    return result


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route('/manifest.json')
# def manifest():
#     return send_from_directory(app.static_folder, 'manifest.json', mimetype='application/json')

@app.route("/api/mc-cause", methods=["GET"])
def home():
    result = getAll("SELECT * FROM lib_knit_mc_cause")
    print(result)
    return jsonify({"success":True, "result":result})

subscriptions = []

@app.route("/subscribe", methods=["POST"])
def subscribe():
    # Parse subscription info from request
    subscription_info = request.get_json()
    print(subscription_info)
    if not subscription_info:
        return jsonify({"success": False, "message": "Invalid subscription data"}), 400
    
    # Save the subscription info (replace with database storage in production)
    subscriptions.append(subscription_info)
    print(subscriptions)
    return jsonify({"success": True, "message": "Subscribed successfully!"}), 200

@app.route("/send_notification", methods=["POST"])
def send_notification():
    payload = {
        "title": "Hello from Backend",
        "body": "This is a test notification!"
    }
    
    for subscription in subscriptions:
        try:
            send_notification_to_subscription(subscription, payload)
        except WebPushException as ex:
            print("Failed to send notification:", repr(ex))  # Log detailed error
        except Exception as e:
            print(f"Unexpected error sending notification: {e}")  # Log general error
    
    return jsonify({"success": True, "message": "Notifications sent!"}), 200

def send_notification_to_subscription(subscription_info, payload):
    try:
        webpush(
            subscription_info=subscription_info,
            data=json.dumps(payload),
            vapid_private_key=VAPID_PRIVATE_KEY,
            
            vapid_claims=VAPID_CLAIMS,
        )
    except WebPushException as ex:
        raise ex  # Re-raise the exception to be caught in the outer try block


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))  # Use PORT from environment or default to 5000
    app.run(host="0.0.0.0", port=port)