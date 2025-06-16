from flask import Blueprint, request, jsonify
from .Models import Hero, Power, HeroPower, db


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return {"message": "Superheroes API is working!"}

# GET /heroes
@main.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

# GET /heroes/<int:id>
@main.route("/heroes/<int:id>", methods=["GET"])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    data = hero.to_dict()
    data["powers"] = [hp.power.to_dict() for hp in hero.hero_powers]
    return jsonify(data), 200

# POST /heroes
@main.route("/heroes", methods=["POST"])
def create_hero():
    data = request.get_json()
    try:
        hero = Hero(name=data["name"], super_name=data["super_name"])
        db.session.add(hero)
        db.session.commit()
        return jsonify(hero.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET /powers/<int:id>
@main.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

# PATCH /powers/<int:id>
@main.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json()
    try:
        power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

# POST /hero_powers
@main.route("/hero_powers", methods=["POST"])
def assign_power_to_hero():
    data = request.get_json()
    try:
        hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(hero_power)
        db.session.commit()

        hero = Hero.query.get(hero_power.hero_id)
        return jsonify(hero.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400