import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Trainers(db.Model):
    __tablename__ = 'Trainers'

    trainer_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)

    def __init__(self, name):
        self.name = name

    def new_trainer_obj():
        return Trainers('')
    
class TrainersSchema(ma.Schema):
    class Meta:
        fields = ['trainer_id', 'name']

    trainer_id = ma.fields.UUID()
    name = ma.fields.String(required=True)

trainer_schema = TrainersSchema()
trainers_schema = TrainersSchema(many=True)