from flask import Flask, render_template, jsonify, request
import wiki_retrieval

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    result = wiki_retrieval.get_random_page_content()
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)


