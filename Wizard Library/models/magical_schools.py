import uuid 
from sqlalchemy.dialects.postgresql import UUID

from db import db

class MagicalSchools(db.Model):
    __tablename__ = 'Magical Schools'

    school_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_name = db.Column(db.String(100), nullable=False, unique=True)
    location = db.Column(db.String(100))
    founded_year = db.Column(db.Integer)
    headmaster = db.Column(db.String(100))

    def __init__(self, school_name, location=None, founded_year=None, headmaster=None):
        self.school_name = school_name
        self.location = location
        self.founded_year = founded_year
        self.headmaster = headmaster