import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class PokemonBattleXref(db.Model):
    __tablename__ = 'PokemonBattleXref'

    pokemon_battle_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pokemon_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Pokemon.pokemon_id'), nullable=False)
    battle_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Battles.battle_id'), nullable=False)

    pokemon = db.relationship('Pokemon', backref='pokemon_battles')
    battle = db.relationship('Battles', backref='pokemon_battles')

    def __init__(self, pokemon_id, battle_id):
        self.pokemon_id = pokemon_id
        self.battle_id = battle_id
    
    def new_pokemon_battle_xref_obj():
        return PokemonBattleXref(uuid.uuid4(), uuid.uuid4())

class PokemonBattleXrefSchema(ma.Schema):
    class Meta:
        fields = ['pokemon_battle_id', 'pokemon_id', 'battle_id']
    pokemon_battle_id = ma.fields.UUID()
    pokemon_id = ma.fields.Nested('PokemonSchema', only=['pokemon_id'], dump_only=True)
    battle_id = ma.fields.Nested('BattlesSchema', only=['battle_id'], dump_only=True)


pokemon_battle_xref_schema = PokemonBattleXrefSchema()
pokemon_battles_xref_schema = PokemonBattleXrefSchema(many=True)