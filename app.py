from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
            <form action='/greet' method='POST'>
                Enter your Name : <input type="text" name="username">
                <input type="submit" value="submit">
            </form>
        </body>
        </html>
        '''
@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['username']
    return f"Hello {user_input}, Welcome to this app. Live long and prosper"


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)