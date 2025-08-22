import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Lightsabers(db.Model):
    __tablename__ = 'lightsabers'

    saber_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('padawans.padawan_id'), nullable=False)
    crystal_id = db.Column(UUID(as_uuid=True), db.ForeignKey('crystals.crystal_id'), nullable=False)
    saber_name = db.Column(db.String(100), nullable=False)
    hilt_material = db.Column(db.String(100), nullable=False)
    blade_color = db.Column(db.String(50), nullable=False)
    is_complete = db.Column(db.Boolean, nullable=False, default=True)


    owner = db.relationship('Padawans', backpopulates='lightsabers')
    crystal = db.relationship('Crystals', back_populates='lightsabers')

    def __init__(self, owner_id, crystal_id, saber_name, hilt_material, blade_color, is_complete=True):
        self.owner_id = owner_id
        self.crystal_id = crystal_id
        self.saber_name = saber_name
        self.hilt_material = hilt_material
        self.blade_color = blade_color
        self.is_complete = is_complete

class LightsabersSchema(ma.Schema):
    class Meta:
        fields = ['saber_id', 'owner_id', 'crystal_id', 'saber_name', 'hilt_material', 'blade_color', 'is_complete']
    
    saber_id = ma.fields.UUID()
    owner_id = ma.fields.Nested('PadawansSchema', exclude=['lightsabers'])
    crystal_id = ma.fields.Nested('CrystalsSchema', exclude=['lightsabers'])
    saber_name = ma.fields.String(required=True)
    hilt_material = ma.fields.String(required=True)
    blade_color = ma.fields.String(required=True)
    is_complete = ma.fields.Boolean(required=True, default=True)

lightsaber_schema = LightsabersSchema()
lightsabers_schema = LightsabersSchema(many=True)