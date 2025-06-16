import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db

from models.wizards import Wizards
from models.spells import Spells

class WizardSpecializations(db.Model):
    __tablename__ = 'Wizard Specializations'

    wizard_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Wizards.wizard_id), primary_key=True)
    spell_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Spells.spell_id), primary_key=True)
    proficency_level = db.Column(db.Float())
    date_learned = db.Column(db.DateTime)

    def __init__(self, wizard_id, spell_id, proficency_level, date_learned):
        self.wizard_id = wizard_id
        self.spell_id = spell_id
        self.proficency_level = proficency_level
        self.date_learned = date_learned