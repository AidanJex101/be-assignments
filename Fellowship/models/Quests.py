import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Quests(db.Model):
    __tablename__ = 'quests'

    quest_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey('locations.id'), nullable=False)
    quest_name = db.Column(db.String(), nullable=False, unique=True)
    difficulty = db.Column(db.String())
    reward_gold = db.Column(db.Integer())
    is_completed = db.Column(db.Boolean(), default=False)

    def __init__(self, quest_id, location_id, quest_name, difficulty=None, reward_gold=None, is_completed=False):
        self.quest_id = quest_id
        self.location_id = location_id
        self.quest_name = quest_name
        self.difficulty = difficulty
        self.reward_gold = reward_gold
        self.is_completed = is_completed
    
    def new_quest_obj():
        return Quests(uuid.uuid4(), uuid.uuid4(), '', None, None, False)
    
class QuestsSchema(ma.Schema):
    class Meta:
        fields = ['quest_id', 'location_id', 'quest_name', 'difficulty', 'reward_gold', 'is_completed']
    
    quest_id = ma.fields.UUID()
    location_id = ma.fields.UUID(required=True)
    quest_name = ma.fields.String(required=True)
    difficulty = ma.fields.String()
    reward_gold = ma.fields.Integer()
    is_completed = ma.fields.Boolean(required=True, dump_default=False)

quest_schema = QuestsSchema()
quests_schema = QuestsSchema(many=True)