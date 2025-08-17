import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Locations(db.Model):
    __tablename__ = 'Locations'

    location_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    route = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    def __init__(self, route, name, description=None):
        self.route = route
        self.name = name
        self.description = description
    
    def new_location_obj():
        return Locations(0, '', '')
    
class LocationsSchema(ma.Schema):
    class Meta:
        fields = ['location_id', 'route', 'name', 'description']

    location_id = ma.fields.UUID()
    route = ma.fields.Integer(required=True)
    name = ma.fields.String(required=True)
    description = ma.fields.String()

location_schema = LocationsSchema()
locations_schema = LocationsSchema(many=True)