import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class HeroQuest(db.Model):
    __tablename__ = 'HeroQuest'

    hero_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Heros.hero_id'), primary_key=True)
    quest_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Quests.quest_id'), primary_key=True)
    date_joined = db.Column(db.DateTime(), nullable=False)

    def __init__(self, hero_id, quest_id, date_joined=None):
        self.hero_id = hero_id
        self.quest_id = quest_id

        if date_joined is None:
            self.date_joined = db.func.current_timestamp()
        else:
            self.date_joined = date_joined

    def new_hero_quest_obj():
        return HeroQuest(uuid.uuid4(), uuid.uuid4(), db.func.current_timestamp())
    
class HeroQuestSchema(ma.Schema):
    class Meta:
        fields = ['hero_id', 'quest_id', 'date_joined']
    
    hero_id = ma.fields.UUID(required=True)
    quest_id = ma.fields.UUID(required=True)
    date_joined = ma.fields.DateTime(required=True, dump_default=db.func.current_timestamp())