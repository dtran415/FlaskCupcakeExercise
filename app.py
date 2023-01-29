"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'

connect_db(app)
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes_list = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=cupcakes_list)


@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    data = request.json

    try:
        cupcake = Cupcake(flavor=data['flavor'],
                        size=data['size'],
                        rating=data['rating'],
                        image=data['image'] or None)
        
        db.session.add(cupcake)
        db.session.commit()
    except:
        db.session.rollback()
        return ('', 400)

    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.image = data.get('image', cupcake.image)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(deleted=cupcake_id)