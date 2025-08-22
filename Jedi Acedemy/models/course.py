import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID



from db import db

class Courses(db.Model):
    __tablename__ = 'courses'

    course_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    instructor_id = db.Column(UUID(as_uuid=True), db.ForeignKey('masters.master_id'), nullable=False)
    course_name = db.Column(db.String(100), nullable=False, unique=True)
    difficulty = db.Column(db.String(50), nullable=False)
    duration_weeks = db.Column(db.Integer, nullable=False)
    max_students = db.Column(db.Integer, nullable=False, default=0)

    instructor = db.relationship('Masters', backpopulates='courses')

    def __init__(self, instructor_id, course_name, difficulty, duration_weeks, max_students=0):
        self.instructor_id = instructor_id
        self.course_name = course_name
        self.difficulty = difficulty
        self.duration_weeks = duration_weeks
        self.max_students = max_students
        
class CoursesSchema(ma.Schema):
    class Meta:
        fields = ['course_id', 'instructor_id', 'course_name', 'difficulty', 'duration_weeks', 'max_students']
    
    course_id = ma.fields.UUID()
    instructor_id = ma.fields.Nested('MastersSchema', exclude=['courses'])
    course_name = ma.fields.String(required=True)
    difficulty = ma.fields.String(required=True)
    duration_weeks = ma.fields.Integer(required=True)
    max_students = ma.fields.Integer(required=True, default=0)

course_schema = CoursesSchema()
courses_schema = CoursesSchema(many=True)