import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import uuid

from db import db

class Organizations(db.Model()):
    __tablename__ = 'Organizations'

    org_id = db.Column(uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    active = db.Column(db.String(), nullable=False, default=True)

    def __init__(self, name, email, phone=None, active=True):
        self.name = name
        self.email = email
        self.phone = phone
        self.active = active
    
    def new_org_obj():
        return Organizations('', None, '', True)

class OrganizationsSchema(ma.Schema):
    class Meta:
        fields = ['org_id', 'name', 'phone', 'email', 'active']


org_schema = OrganizationsSchema()
orgs_schema = OrganizationsSchema(many=True)