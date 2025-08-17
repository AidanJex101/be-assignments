import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trainer_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Trainers.trainer_id'), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String())
    active = db.Column(db.Boolean(), nullable=False, default=True)
    role = db.Column(db.String(), nullable=False, default='user')

    trainer = db.relationship('Trainers', back_populates='users')
    auth = db.relationship('AuthTokens', back_populates='users')

    def __init__(self, trainer_id, first_name, last_name, email, password, phone=None, active=True, role='user'):
        self.trainer_id = trainer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.active = active
        self.role = role

    
    
    def new_user_obj():
        return Users("", "", "", "", "", None, True, 'user')

class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'trainer_id', 'first_name', 'last_name', 'email', 'phone', 'active', 'role']
    
    user_id = ma.fields.UUID()
    first_name = ma.fields.String(required=True)
    last_name = ma.fields.String(required=True)
    email = ma.fields.Email(required=True)
    phone = ma.fields.String()
    active = ma.fields.Boolean(required=True, dump_default=True)
    role = ma.fields.String(required=True, dump_default='user')

    trainer_id = ma.fields.Nested('TrainersScheme', only=['trainer_id'], dump_only=True)



user_schema = UsersSchema()
users_schema = UsersSchema(many=True)