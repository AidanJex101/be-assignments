import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Stats(db.Model):
    __tablename__ = 'Stats'

    stat_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def __init__(self, attack, defense, speed, special_attack, special_defense, level):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.level = level

    def new_stats_obj():
        return Stats(0, 0, 0, 0, 0, 1)
    
class StatsSchema(ma.Schema):
    class Meta:
        fields = ['stat_id', 'attack', 'defense', 'speed', 'special_attack', 'special_defense', 'level']

    stat_id = ma.fields.UUID()
    attack = ma.fields.Integer(required=True)
    defense = ma.fields.Integer(required=True)
    speed = ma.fields.Integer(required=True)
    special_attack = ma.fields.Integer(required=True)
    special_defense = ma.fields.Integer(required=True)
    level = ma.fields.Integer(required=True)

stat_schema = StatsSchema()
stats_schema = StatsSchema(many=True)