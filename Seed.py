from app import app, db
from app.Models import Hero, Power, HeroPower

with app.app_context():
    print("Seeding database...")

   
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

   
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    ]
    db.session.add_all(heroes)

   
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    db.session.add_all(powers)

    db.session.commit()

    
    hero_powers = [
        HeroPower(strength="Strong", hero_id=heroes[0].id, power_id=powers[1].id),
        HeroPower(strength="Average", hero_id=heroes[1].id, power_id=powers[0].id),
        HeroPower(strength="Weak", hero_id=heroes[2].id, power_id=powers[2].id),
    ]
    db.session.add_all(hero_powers)
    db.session.commit()

    print("Done seeding!")