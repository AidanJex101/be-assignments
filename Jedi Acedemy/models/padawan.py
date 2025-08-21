import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Padawans(db.Model):
    __tablename__ = 'padawans'
    
    padawan_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    master_id = db.Column(UUID(as_uuid=True), db.ForeignKey('masters.master_id'), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('app_users.user_id'), nullable=False)
    species_id = db.Column(UUID(as_uuid=True), db.ForeignKey('species.species_id'), nullable=False)
    padawan_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    training_level = db.Column(db.Integer(), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, master_id, user_id, species_id, padawan_name, age, training_level, is_active=True):
        self.master_id = master_id
        self.user_id = user_id
        self.species_id = species_id
        self.padawan_name = padawan_name
        self.age = age
        self.training_level = training_level
        self.is_active = is_active

class PadawansSchema(ma.Schema):
    class Meta:
        fields = ['padawan_id', 'master_id', 'user_id', 'species_id', 'padawan_name', 'age', 'training_level', 'is_active']
    
    padawan_id = ma.fields.UUID()
    master_id = ma.fields.UUID(required=True)
    user_id = ma.fields.UUID(required=True)
    species_id = ma.fields.UUID(required=True)
    padawan_name = ma.fields.String(required=True)
    age = ma.fields.Integer(required=True)
    training_level = ma.fields.Integer(required=True, default=0)
    is_active = ma.fields.Boolean(required=True, default=True)

padawan_schema = PadawansSchema()
padawans_schema = PadawansSchema(many=True)