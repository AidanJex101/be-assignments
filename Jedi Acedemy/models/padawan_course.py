import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class PadawanCourses(db.Model):
    __tablename__ = 'padawan_courses'

    padawan_id = db.Column(UUID(as_uuid=True), db.ForeignKey('padawans.padawan_id'), nullable=False)
    course_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    enrollment_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    completion_date = db.Column(db.DateTime, nullable=True)
    final_score = db.Column(db.Float, nullable=True)

    course = db.relationship('Courses', back_populates='padawan_courses')
    
    def __init__(self, padawan_id, course_id, completion_date=None, final_score=None):
        self.padawan_id = padawan_id
        self.course_id = course_id
        self.completion_date = completion_date
        self.final_score = final_score
    
class PadawanCoursesSchema(ma.Schema):
    class Meta:
        fields = ['padawan_id', 'course_id', 'enrollment_date', 'completion_date', 'final_score']
    
    padawan_id = ma.fields.UUID(required=True)
    course_id = ma.fields.Nested('CoursesSchema', exclude=['padawan_courses'])
    enrollment_date = ma.fields.DateTime(required=True)
    completion_date = ma.fields.DateTime(allow_none=True)
    final_score = ma.fields.Float(allow_none=True)

padawan_course_schema = PadawanCoursesSchema()
padawan_courses_schema = PadawanCoursesSchema(many=True)