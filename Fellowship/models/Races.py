import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Races(db.Model):
    __tablename__ = 'Races'

    race_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    race_name = db.Column(db.String(), nullable=False, unique=True)
    homeland = db.Column(db.String())
    lifespan = db.Column(db.Integer())

    def __init__(self, race_id, race_name, homeland=None, lifespan=None):
        self.race_id = race_id
        self.race_name = race_name
        self.homeland = homeland
        self.lifespan = lifespan
    
    def new_race_obj():
        return Races(uuid.uuid4(), '', None, None)
    
class RacesSchema(ma.Schema):
    class Meta:
        fields = ['race_name', 'homeland', 'lifespan']

        
        race_name = ma.fields.String(required=True)
        homeland = ma.fields.String()
        lifespan = ma.fields.Integer()
    

race_schema = RacesSchema()
races_schema = RacesSchema(many=True)
        