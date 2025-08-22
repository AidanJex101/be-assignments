import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Pokemon(db.Model):
    __tablename__ = 'Pokemon'

    pokemon_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stat_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Stats.stat_id'), nullable=False)
    trainer_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Trainers.trainer_id'), nullable=False)
    name = db.Column(db.String(), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    xp = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(), nullable=False)

    stats = db.relationship('Stats', backpopulates='pokemons')
    trainer = db.relationship('Trainers', backpopulates='pokemons')

    def __init__(self, stats_id, trainer_id, name, health, xp, type):
        self.stats_id = stats_id
        self.trainer_id = trainer_id
        self.name = name
        self.health = health
        self.xp = xp
        self.type = type
    
    def new_pokemon_obj():
        return Pokemon(uuid.uuid4(), uuid.uuid4(), '', 0, 0, '')
    
class PokemonSchema(ma.Schema):
    class Meta:
        fields = ['pokemon_id', 'stat_id', 'trainer_id', 'name', 'health', 'xp', 'type']

    pokemon_id = ma.fields.UUID()
    stat_id = ma.fields.Nested('StatsSchema', only=['stat_id'], dump_only=True)
    trainer_id = ma.fields.Nested('TrainersSchema', only=['trainer_id'], dump_only=True)
    name = ma.fields.String(required=True)
    health = ma.fields.Integer(required=True)
    xp = ma.fields.Integer(required=True)
    type = ma.fields.String(required=True)

pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)