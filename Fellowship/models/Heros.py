import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Heros(db.Model):
    __tablename__ = 'Heros'
    
    hero_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    race_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Races.race_id'), nullable=False)
    hero_name = db.Column(db.String(), nullable=False, unique=True)
    age = db.Column(db.Integer())
    health_points = db.Column(db.Integer())
    is_alive = db.Column(db.Boolean(), default=True)

    def __init__(self, hero_id, race_id, hero_name, age=None, health_points=None, is_alive=True):
        self.hero_id = hero_id
        self.race_id = race_id
        self.hero_name = hero_name
        self.age = age
        self.health_points = health_points
        self.is_alive = is_alive

    def new_hero_obj():
        return Heros(uuid.uuid4(), uuid.uuid4(), '', None, None, True)
    

class HerosSchema(ma.Schema):
    class Meta:
        fields = ['race_id', 'hero_name', 'age', 'health_points', 'is_alive']

        race_id = ma.fields.UUID()
        hero_name = ma.fields.String(required=True)
        age = ma.fields.Integer()
        health_points = ma.fields.Integer()
        is_alive = ma.fields.Boolean(required=True, dump_default=True)
    
hero_schema = HerosSchema()
heros_schema = HerosSchema(many=True)