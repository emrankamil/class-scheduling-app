from django.core.exceptions import ValidationError

def isInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
def validate_time_durations_data(value):
    try:
        data = value
        if not isinstance(data, dict):
            raise ValidationError('Invalid input data: Must be a dictionary')
            
        for duration, frequency in data.items():
            if not isInteger(duration) or not isInteger(frequency):
                raise ValidationError('Invalid duration or frequency: Must be Integer.')
    except ValueError:
        raise ValidationError('Invalid JSON format.')