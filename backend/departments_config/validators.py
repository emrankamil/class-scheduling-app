from django.core.exceptions import ValidationError

def isInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
def validate_course_data(value):
    from .models import Course
    try:
        data = value
        if not isinstance(data, dict):
            raise ValidationError('Invalid JSON: Must be a dictionary.')
        
        for course_id, course_info in data.items():
            if not isInteger(course_id):
                raise ValidationError('Invalid course_id: Must be integers.')
            
            if not isinstance(course_info, dict):
                raise ValidationError(f'Invalid value for course {course_id}: Must be a dictionary.')
            
            if not Course.objects.filter(id=int(course_id)).exists():
                raise ValidationError(f'Course with ID {course_id} does not exist.')
                
            for duration, frequency in course_info.items():
                if not isInteger(duration) or not isInteger(frequency):
                    raise ValidationError(f'Invalid duration or frequency for course {course_id}.')
    except ValueError:
        raise ValidationError('Invalid JSON format.')
    
def validate_instructor_data(value):
    from .models import Instructor, Course
    try:
        data = value
        if not isinstance(data, dict):
            raise ValidationError('Invalid input data: Must be a dictionary')
            
        for instructor_id, course_id in data.items():
            if not isInteger(instructor_id) or not isInteger(course_id):
                raise ValidationError('Invalid instructor_id or course_id: Must be Integer.')
            
            if not Instructor.objects.filter(id=int(instructor_id)).exists():
                raise ValidationError(f'instructor with ID {instructor_id} does not exist.')
            
            if not Course.objects.filter(id=int(course_id)).exists():
                raise ValidationError(f'Course with ID {course_id} does not exist.')
    except ValueError:
        raise ValidationError('Invalid JSON format.')