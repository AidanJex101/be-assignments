import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Location(db.Model):
    __tablename__ = 'Locations'

    location_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    realm_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Realms.id'), nullable=False)
    location_name = db.Column(db.String(), nullable=False, unique=True)
    danger_level = db.Column(db.Integer())

    def __init__(self, location_id, realm_id, location_name, danger_level=None):
        self.location_id = location_id
        self.realm_id = realm_id
        self.location_name = location_name
        self.danger_level = danger_level
    
    def new_location_obj():
        return Location(uuid.uuid4(), uuid.uuid4(), '', None)
    
class LocationSchema(ma.Schema):
    class Meta:
        fields = ['location_id', 'realm_id', 'location_name', 'danger_level']
    
    location_id = ma.fields.UUID()
    realm_id = ma.fields.UUID(required=True)
    location_name = ma.fields.String(required=True)
    danger_level = ma.fields.Integer()

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
    