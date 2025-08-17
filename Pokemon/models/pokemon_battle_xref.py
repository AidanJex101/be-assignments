from db import db

pokemon_battle_association_table = db.Table(
    "PokemonBattleAssociation",
    db.Model.metadata,
    db.Column("pokemon_id", db.ForeignKey("Pokemon.pokemon_id", ondelete='CASCADE'), primary_key=True),
    db.Column("battle_id", db.ForeignKey("Battles.battle_id", ondelete='CASCADE'), primary_key=True)
)