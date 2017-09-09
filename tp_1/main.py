from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return "Hola mundo!"


@app.route('/user/<string:username>', methods=['GET'])
def show_user_profile(username):
    """
    :type username: str
    """
    return 'User {}'.format(username)


@app.route('/add', methods=['POST'])
def add_entry():
    print "El nombre recibido es {}".format(request.headers['nombre'])
    return "Done!"
