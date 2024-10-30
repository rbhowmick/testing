import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    target = request.args["target"]

    # BAD: user has full control of URL
    resp = requests.get("https://" + target + ".example.com/data/")

    # GOOD: `subdomain` is controlled by the server.
    subdomain = "europe" if target == "EU" else "world"
    resp = requests.get("https://" + subdomain + ".example.com/data/")

@app.route("/login")
def login():

  username = request.values.get('username')
  password = request.values.get('password')

  # Prepare database connection
  db = pymysql.connect("localhost")
  cursor = db.cursor()

  # Execute the vulnerable SQL query concatenating user-provided input.
  cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))

  # If the query returns any matching record, consider the current user logged in.
  record = cursor.fetchone()
  if record:
    session['logged_user'] = username

  # disconnect from server
  db.close()



print("hello world")
