from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Sample book data
BOOKS = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 4, "title": "Moby-Dick", "author": "Herman Melville"},
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    result = [book for book in BOOKS if query in book['title'].lower() or query in book['author'].lower()]
    return jsonify(result)

# if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
