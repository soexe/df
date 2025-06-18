from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
    static_folder='.',
    static_url_path='',
    template_folder='.')

@app.route('/')
def index():
    return render_template('double_your_crypto_bonus_no_emoji.html')

@app.route('/<path:path>')
def serve_static(path):
    if path.startswith(('styles/', 'images/', 'fonts/', 'assets/', 'scripts/')):
        return send_from_directory('.', path)
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Note: Running on port 80 typically requires admin/root privileges
    app.run(host='0.0.0.0', port=80, debug=True) 