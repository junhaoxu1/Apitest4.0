from Settings import *
import json

db = SQLAlchemy(app)

class Games(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'score': self.score,
            'image': self.image
        }

    def add_game(_name, _genre, _score, _image):
        new_game = Games(name=_name, genre=_genre, score=_score, image=_image)
        db.session.add(new_game)
        db.session.commit()

    def get_all_games():
        return [Games.json(game) for game in Games.query.all()]

    def get_game(_id):
        return [Games.json(Games.query.filter_by(id=_id).first())]

    def update_game(_id, _name, _genre, _score, _image):
        game_to_update = Games.query.filter_by(id=_id).first()
        game_to_update.name = _name
        game_to_update.genre = _genre
        game_to_update.score = _score
        game_to_update.image = _image
        db.session.commit()

    def delete_game(_id):
        Games.query.filter_by(id=_id).delete()
        db.session.commit()



