from flask import Flask, render_template

# Serve templates from ./Pages and static assets (Images/, etc.) from this folder.
# With static_folder='.', URLs like /Images/about.png will work.
app = Flask(__name__, template_folder='Pages', static_folder='.', static_url_path='')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
