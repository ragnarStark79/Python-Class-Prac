from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/previous-semester')
def previous_semester():
    return render_template('previous_semester.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    # host='0.0.0.0' allows access from any network interface
    # Use port 80 for standard HTTP (requires sudo) or 5001 for development
    import sys
    port = 80 if '--production' in sys.argv else 5001
    app.run(debug=(port != 80), host='0.0.0.0', port=port)
