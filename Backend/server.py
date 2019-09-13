from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import json



app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/mydb'
db = SQLAlchemy(app)
db.init_app(app)



class Key_Table(db.Model):
    __tablename__ = 'halo'
    key = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)


    def get_value_by_key(self, user_key):
        result = Key_Table.query.filter_by(key=user_key).first()
        d={}
        d.update(key=result.key,value=result.value)
        return d

    def update_key_value(self, get_key, get_value):
        result = Key_Table(key=get_key, value=get_value)
        db.session.add(result)
        db.session.commit()

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    def update_users(self,get_user, get_password):
        result = User(username=get_user, password=get_password)
        db.session.add(result)
        db.session.commit()


@app.route('/getvalue', methods=['POST'])
def key():
    obj = Key_Table()
    data = request.data
    print(data)
    data = eval(data)
    key_value=data['key']
    result = obj.get_value_by_key(key_value)
    return result


@app.route('/insert', methods=['GET','POST'])
def key_value():
    obj = Key_Table()
    data = request.data
    data = eval(data)
    print(data)
    get_key=data['key']
    get_value=data['value']
    obj.update_key_value(get_key, get_value)
    return "inserted"

@app.route('/updatevalue', methods=['GET','POST'])
def update_value():
    data = request.data
    data = eval(data)
    get_key = data['key']
    get_value = data['value']
    user = Key_Table.query.filter_by(key=get_key).first()
    print(user)
    user.value=get_value
    db.session.commit()
    return "updated"


@app.route('/login', methods=['GET','POST'])
def get_users():
    data = json.loads(request.data)
    username=data['username']
    password=data['password']
    user= User.query.filter_by(username=username, password=password).first()   
    if not user:
        return "invalid user"
    return "valid user"



@app.route('/sign_up', methods=['POST'])
def update_users():
    obj = User()
    data = json.loads(request.data)
    get_user=data['username']
    get_password=bcrypt.generate_password_hash(data['password'])
    obj.update_users(get_user, get_password)
    return "inserted"

    
if __name__ == '__main__':
    app.run(debug=True)