from flask import Flask, jsonify, request, json
from quote import quotes_api

app = Flask(__name__)
FILE = "quotes.json"


def load_quotes():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_quotes(quotes):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)


def find_quote_by_id(quote_id):
    quotes = load_quotes()
    for quote in quotes:
        if quote["id_q"] == quote_id:
            return quote
    return None


def create_new_quote(post_data):
    quotes = load_quotes()
    new_id = len(quotes) + 1
    new_quote = {
        "id_q": new_id,
        "q": post_data["q"],
        "a": post_data["a"]
    }
    quotes.append(new_quote)
    save_quotes(quotes)
    return new_quote


@app.route("/")
def home():
    return "Hello, it's main page 'app_zen' by REST API "


@app.route("/quotes/", methods=["GET"])
def get_random_quote():
    return quotes_api()


@app.route("/quotes/<int:quote_id>/", methods=["GET"])
def get_quote_by_id(quote_id):
    quote = find_quote_by_id(quote_id)
    if quote:
        return jsonify(quote)
    return jsonify({"message": f"user {quote_id} not found"}), 404


@app.route("/quotes/", methods=["POST"])
def add_quote():
    post_data = request.get_json()
    new_quote = create_new_quote(post_data)
    return jsonify(new_quote), 201


if __name__ == "__main__":
    app.run(debug=True)
