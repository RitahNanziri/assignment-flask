from flask import Flask, render_template, request

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Username
@app.route('/<username>')
def show_user(username):
    return render_template('user.html', username=username)

# Form handling
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Handle POST request
        name = request.form.get('name')
        email = request.form.get('email')
        return render_template('submit.html', name=name, email=email)
    else:
        # Handle GET request with a more descriptive default name
        default_name = "Ritah Doe"
        return render_template('submit_form.html', default_name=default_name)

if __name__ == '__main__':
    app.run(debug=True)