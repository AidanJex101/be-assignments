import marshmallow as ma
import uuid
import sqlalchemy.dialects.postgresql import uuid

from db import db

class AppUsers(db.models):
    __tablename__ = "AppUsers"

    user_id = db.Column(uuid(as_uuid=True), primary_key = True, default=uuid.uuid4)
    ord_id = db.Column(uuid(as_uuid=True), db.ForeignKey('Organizations.org_id'), nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String())
    active = db.Column(db.Boolean(), nullable=False, default=True)
    role = db.Column(db.String(), nullable=False, default='user')

    def __init__(self, org_id, first_name, last_name, email, password, phone=None, active=True, role='user'):
        self.ord_id = org_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.active = active
        self.role = role

    
    
    def new_user_obj():
        return AppUsers("", "", "", "", "", None, True, 'user')

class AppUsersScheme(ma.Scheme):
    class Meta:
        fields = ['user_id', 'org_id', 'first_name', 'last_name', 'email', 'phone', 'active', 'role']



app_user_schema = AppUsersScheme()
app_users_schema = AppUsersScheme(many=True)