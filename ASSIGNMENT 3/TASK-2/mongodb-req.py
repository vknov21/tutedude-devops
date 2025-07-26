
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, redirect
from urllib.parse import urlencode

app = Flask(__name__)


class MongoDBConn():
    def __init__(self, db_name):
        load_dotenv()
        # Create a new client and connect to the server
        client = MongoClient(os.getenv('MONGODB_URL'))
        self.db = client.__getattr__(db_name)

    def get_table(self, table_name):
        self.table = self.db[table_name]
        return self.table

    def get_all(self):
        cursor = self.table.find()
        return cursor


def create_conn(db_name, table_name):
    db_conn = MongoDBConn("user")
    table = db_conn.get_table("user_data")
    return db_conn, table


db_conn, table = create_conn("user", "user_data")


@app.route('/')
def home():
    return redirect("/form")


@app.route('/form')
def form_req():
    error = request.args.get("error", "")
    return render_template("index.html", error=error)


@app.route("/view", methods=["GET"])
def view():
    data = db_conn.get_all()
    output_data = [(entries["name"], entries["location"], entries["zip"]) for entries in data]
    return render_template("view.html", output_data=output_data)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        user_input = dict(request.form)
        if any(val=="" for val in user_input.values()):
            raise Exception("The values cannot be empty")
        try:
            int(user_input["zip"])
        except ValueError:
            raise Exception("Zip Code should be in integer format")
        table.insert_one(user_input)
        return redirect("/success")
    except Exception as e:
        query_string = urlencode({"error": str(e)})
        return redirect(f"/form?{query_string}")


@app.route("/success")
def success():
    return "Data submitted successfully!"


if __name__ == "__main__":
    app.run(debug=True)
