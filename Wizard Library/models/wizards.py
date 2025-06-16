import uuid 
from sqlalchemy.dialects.postgresql import UUID

from db import db
from models.magical_schools import MagicalSchools

class Wizards(db.Model):
    __tablename__ = 'Wizards'
    
    wizard_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_id = db.Column(UUID(as_uuid=True), db.ForeignKey(MagicalSchools.school_id), nullable=False)
    wizard_name = db.Column(db.String(100), nullable=False, unique=True)
    house = db.Column(db.String(50))
    year_enrolled = db.Column(db.Integer)
    magical_power_level = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True)

    school = db.relationship('MagicalSchools', foreign_keys='[Wizards.school_id]', back_populates='wizards')

    def __init__(self, school_id, wizard_name, house=None, year_enrolled=None, magical_power_level=None, active=True):
        self.school_id = school_id
        self.wizard_name = wizard_name
        self.house = house
        self.year_enrolled = year_enrolled
        self.magical_power_level = magical_power_level
        self.active = active