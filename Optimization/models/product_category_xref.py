
import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db

class ProductCategoryXref(db.Model):
    __tablename__ = "products_category_association_table"

    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Products.product_id"), primary_key=True)
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Categories.category_id"), primary_key=True)

    product = db.relationship("Products", back_populates='categories')
    category = db.relationship("Categories", back_populates='products')

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

class ProductCategoryXrefSchema(ma.Schema):
    class Meta:
        fields = ['product_id', 'category_id']
    
product_category_xref_schema = ProductCategoryXrefSchema()
product_category_xrefs_schema = ProductCategoryXrefSchema(many=True)