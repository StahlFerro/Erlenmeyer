import string
from random import choices
from pprint import pprint
from server import app
from flask import render_template


def get_data():
    count = 100
    charlength = 20
    numlength = 25
    data = [{
        'id': x,
        'name': "".join(choices(string.ascii_letters, k=charlength)),
        'number': "".join(choices(string.digits, k=numlength))
    } for x in range(0, count)]
    return data


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'StahlFerro'}
    app_usefulness = 'shit'
    data = get_data()
    return render_template('index.html', title='Erlenmeyer', user=user, data=data, app_usefulness=app_usefulness)
