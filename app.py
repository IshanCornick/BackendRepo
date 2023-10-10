from flask import Flask, render_template

app = Flask(__name__)

# Sample data for demonstration
sample_data = {
    'title': 'My Awesome Flask App',
    'message': 'Welcome to my Flask App!',
    'items': [
        {'name': 'Item 1', 'description': 'This is the first item.'},
        {'name': 'Item 2', 'description': 'This is the second item.'},
        {'name': 'Item 3', 'description': 'This is the third item.'}
    ]
}

@app.route('/')
def home():
    # Render the 'index.html' template with dynamic data
    return render_template('index.html', data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)




