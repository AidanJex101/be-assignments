
import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Warranties(db.Model):
    __tablename__ = "Warranties"

    warranty_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Products.product_id"), nullable=False)
    warranty_months = db.Column(db.Integer(), nullable=False) 

    product = db.relationship("Products", foreign_keys='[Warranties.product_id]', back_populates='warranty')

    def __init__(self, product_id, warranty_period):
        self.product_id = product_id
        self.warranty_period = warranty_period

class WarrantiesSchema(ma.Schema):
    class Meta:
        fields = ['warranty_id', 'product_id', 'warranty_months']
        
warranty_schema = WarrantiesSchema()
warranties_schema = WarrantiesSchema(many=True)