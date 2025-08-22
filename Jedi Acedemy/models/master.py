import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Masters(db.Model):
    __tablename__ = 'masters'
    
    master_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('app_users.user_id'), nullable=False)
    master_name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    years_training = db.Column(db.Integer, nullable=False)
    max_padawans = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('AppUsers', back_populates='masters')

    def __init__(self, user_id, master_name, specialization, years_training, max_padawans=0):
        self.user_id = user_id
        self.master_name = master_name
        self.specialization = specialization
        self.years_training = years_training
        self.max_padawans = max_padawans

class MastersSchema(ma.Schema):
    class Meta:
        fields = ['master_id', 'user_id', 'master_name', 'specialization', 'years_training', 'max_padawans']
    
    master_id = ma.fields.UUID()
    user_id = ma.fields.Nested('AppUsersSchema', exclude=['masters'])
    master_name = ma.fields.String(required=True)
    specialization = ma.fields.String(required=True)
    years_training = ma.fields.Integer(required=True)
    max_padawans = ma.fields.Integer(required=True, default=0)

master_schema = MastersSchema()
masters_schema = MastersSchema(many=True)