import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db

class Spells(db.Model):
    __tablename__ = 'Spells'

    spell_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    spell_name = db.Column(db.String(100), nullable=False, unique=True)
    incantation = db.Column(db.String(500))
    difficulty_level = db.Column(db.Float())
    spell_type = db.Column(db.String(50))
    description = db.Column(db.String(500))

    def __init__(self, spell_name, incantation, difficulty_level, spell_type, description):
        self.spell_name = spell_name
        self.incantation = incantation
        self.difficulty_level = difficulty_level
        self.spell_type = spell_type
        self.description = description