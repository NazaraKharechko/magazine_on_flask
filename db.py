from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def seed_db():
    from models import User, Goods
    db.create_all()
    if len(User.query.all()) < 1:
        db.session.add(User(email="attacker@gmail.com",
                            name="Mr Attacker",
                            number="0976707690",
                            admin=False,
                            password="cool_password"))
        db.session.add(User(email="superuser@gmail.com",
                            name="Super User",
                            number="0976707690",
                            admin=True,
                            password="no_one_find_out"))
        db.session.commit()
    if len(Goods.query.all()) < 1:
        db.session.add(Goods(name="Pizza",
                             description="Pizza is an Italian national dish, namely, the cake should be round in "
                                         "shape, "
                                         "covered with tomato paste and cheese and baked",
                             price=46))
        db.session.add(Goods(name="Beer",
                             description="Beer is an alcoholic beverage obtained by fermentation. "
                                         "The third most popular drink in the world after water and tea.",
                             price=66))
        db.session.commit()
