import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Abilities(db.Model):
    __tablename__ = 'Abilities'

    ability_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hero_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Heroes.hero_id'), nullable=False)
    abiltity_name = db.Column(db.String(), nullable=False, unique=True)
    power_level = db.Column(db.Integer(), default=1)

    def __init__(self, hero_id, abiltity_name, power_level):
        self.hero_id = hero_id
        self.abiltity_name = abiltity_name
        self.power_level = power_level
    
    def new_ability_obj():
        return Abilities(uuid.uuid4(), '', 1)
    
class AbilitiesSchema(ma.Schema):
    class Meta:
        fields = ['ability_id', 'hero_id', 'abiltity_name', 'power_level']
    
    ability_id = ma.fields.UUID()
    hero_id = ma.fields.UUID(required=True)
    abiltity_name = ma.fields.String(required=True)
    power_level = ma.fields.Integer(required=True, dump_default=1)

ability_schema = AbilitiesSchema()
abilities_schema = AbilitiesSchema(many=True)