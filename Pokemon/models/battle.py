import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Battles(db.Model):
    __tablename__ = 'Battles'

    battle_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Locations.location_id'), nullable=False)
    type_advantage = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    def __init__(self, location_id, type_advantage, description=None):
        self.location_id = location_id
        self.type_advantage = type_advantage
        self.description = description
    
    def new_battle_obj():
        return Battles(uuid.uuid4(), '', '')
    
class BattlesSchema(ma.Schema):
    class Meta:
        fields = ['battle_id', 'location_id', 'type_advantage', 'description']

    battle_id = ma.fields.UUID()
    location_id = ma.fields.UUID(required=True)
    type_advantage = ma.fields.String(required=True)
    description = ma.fields.String()


battle_schema = BattlesSchema()
battles_schema = BattlesSchema(many=True)