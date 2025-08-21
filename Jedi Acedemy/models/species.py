import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Species(db.Model):
    __tablename__ = 'species'

    species_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    species_name = db.Column(db.String(100), nullable=False, unique=True)
    homeworld = db.Column(db.String(200), nullable=False)
    force_sensitive = db.Column(db.Boolean, nullable=False, default=False)
    avg_lifespan = db.Column(db.Integer, nullable=True)

    def __init__(self, species_name, homeworld, force_sensitive=False, avg_lifespan=None):
        self.species_name = species_name
        self.homeworld = homeworld
        self.force_sensitive = force_sensitive
        self.avg_lifespan = avg_lifespan

class SpeciesSchema(ma.Schema):
    class Meta:
        fields = ['species_id', 'species_name', 'homeworld', 'force_sensitive', 'avg_lifespan']
    
    species_id = ma.fields.UUID()
    species_name = ma.fields.String(required=True)
    homeworld = ma.fields.String(required=True)
    force_sensitive = ma.fields.Boolean(required=True, default=False)
    avg_lifespan = ma.fields.Integer()

species_schema = SpeciesSchema()
species_list_schema = SpeciesSchema(many=True)