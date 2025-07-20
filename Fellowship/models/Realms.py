import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Realms(db.Model):
    __tablename__ = 'Realms'
    
    realm_id = db.Column(UUID(as_uuid=True), db.ForeignKey('realms.id'), primary_key=True)
    realm_name = db.Column(db.String(), nullable=False, unique=True)
    ruler = db.Column(db.String())

    def __init__(self, realm_id, realm_name, ruler=None):
        self.realm_id = realm_id
        self.realm_name = realm_name
        self.ruler = ruler
    
    def new_realm_obj():
        return Realms(uuid.uuid4(), '', None)
    
class RealmsSchema(ma.Schema):
    class Meta:
        fields = ['realm_id', 'realm_name', 'ruler']
    
    realm_id = ma.fields.UUID()
    realm_name = ma.fields.String(required=True)
    ruler = ma.fields.String()

realm_schema = RealmsSchema()
realms_schema = RealmsSchema(many=True)