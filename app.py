from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:page_num>')
def page(page_num):
    return render_template(f'{page_num}.html')

@app.route('/search', methods=['POST'])
def search():
    # Dummy data for now
    dummy_results = [
        {
            "title": "The Role of AI in Transforming Education",
            "published": "2023",
            "citations": 150,
            "summary": "A comprehensive review of the current state of AI in education, covering applications, challenges, and future directions."
        },
        {
            "title": "Personalized Learning with AI: A Case Study",
            "published": "2022",
            "citations": 200,
            "summary": "An analysis of how AI tools are being used to personalize learning experiences and improve student outcomes."
        }
    ]
    return jsonify(dummy_results)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
