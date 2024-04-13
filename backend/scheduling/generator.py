from collections import defaultdict
import random
from scheduling.serializers import ScheduleEntrySerializer
from scheduling_config.models import SchedulingData, Section
from scheduling_config.serializers import SchedulingDataSerializer
import datetime

# data = {
#         "id": 4,
#         "department": 4,
#         "year": 2015,
#         "batch": 11,
#         "number_of_sections": 5,
#         "rooms": [
#             5,
#             6,
#             7
#         ],
#         "scheduling_courses": [
#             {
#                 "id": 8,
#                 "time_durations": [
#                     '45',
#                     '45',
#                     '45',
#                     '45',
#                     '45',
#                     '45',
#                     '45'
#                 ],
#                 "scheduling_data": 4,
#                 "course": 7,
#                 "instructors": [
#                     5
#                 ]
#             },
#             {
#                 "id": 9,
#                 "time_durations": [
#                     "45",
#                     "45",
#                     "45",
#                     "45",
#                     "45",
#                     "45",
#                     "45",
#                     "45"
#                 ],
#                 "scheduling_data": 4,
#                 "course": 5,
#                 "instructors": [
#                     6,
#                     7
#                 ]
#             },
#             {
#                 "id": 10,
#                 "time_durations": [
#                     "45",
#                     "45",
#                     "45",
#                     "45",
#                     "45",
#                     "45"
#                 ],
#                 "scheduling_data": 4,
#                 "course": 6,
#                 "instructors": [
#                     7
#                 ]
#             }
#         ],
#         "possible_durations": {
#             "45": [
#                 datetime.time(14, 0, 0),
#                 datetime.time(10, 45, 0),
#                 datetime.time(9, 15, 0),
#                 datetime.time(14, 45, 0),
#                 datetime.time(11, 30, 0),
#                 datetime.time(8, 30, 0),
#                 datetime.time(10, 0, 0)
#             ]
#         }
#     }
# days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  
# {'id': 4,
#   'department': 4, 
#   'year': 2015, 
#   'batch': 11, 
#   'number_of_sections': 5,
#     'rooms': [5, 6, 7], 
#     'scheduling_courses': [
#         {
#             'id': 8,
#               'time_durations': [45, 45, 45, 45, 45, 45, 45], 
#               'scheduling_data': 4, 'course': 7, 
#               'instructors': [5]
#               }, 
#               {
#                   'id': 9, 
#                   'time_durations': [45, 45, 45, 45, 45, 45, 45, 45], 
#                   'scheduling_data': 4, 
#                   'course': 5, 
#                   'instructors': [6, 7]
#                   }, 
#                   {
#                     'id': 10,
#                    'time_durations': [45, 45, 45, 45, 45, 45], 
#                   'scheduling_data': 4,
#                    'course': 6,
#                    'instructors': [7]
#                   }
#                   ], 
#                   'possible_durations': defaultdict(<class 'set'>, {
#                       45: {
#                         datetime.time(8, 30),
#                        datetime.time(11, 30), 
#                       datetime.time(9, 15),
#                        datetime.time(10, 45), 
#                       datetime.time(14, 0),
#                        datetime.time(14, 45), 
#                       datetime.time(10, 0)
#                       }
#                       })}

def generate_schedule(scheduling_data_id, days):

    output = []

    scheduling_data = SchedulingData.objects.get(id=scheduling_data_id)
    serializer = SchedulingDataSerializer(scheduling_data)
    data = serializer.data
    
    def verify_and_save(schedule):
        timechange = datetime.timedelta(minutes=int(schedule[1]))
        end_time = (datetime.datetime.combine(datetime.date(1,1,1),schedule[6]) + timechange).time()
                
        schedule = {
                    'parent_schedule': data['id'],
                    'temp_section': schedule[0],
                    'course': schedule[2],
                    'instructor': schedule[5],
                    'day': schedule[3],
                    'room': schedule[4],
                    'start_time': schedule[6],
                    'end_time': end_time
                }
        
        new_entry = ScheduleEntrySerializer(data=schedule)
        
        if new_entry.is_valid():
            new_entry.save()
            return True
        # else:
        #     print(new_entry.data)
        #     print(new_entry.errors)
   
    def dfs(variable, value, result):
        if found[0]:
            return
        if variable == 'course':
            for day in days:
                dfs('day', day, result)
        if variable == 'day':
            result.append(value)
            for room in scheduling_course['rooms']:
                dfs('room', room, result)
            result.pop()
        if variable == 'room':
            result.append(value)
            for instr in scheduling_course['instructors']:
                dfs('instructor', instr, result)
            result.pop()
        if variable == 'instructor':
            result.append(value)
            for time in data['possible_durations'][result[1]]:
                result.append(time)
                count[0] += 1
                if verify_and_save(result):
                    found[0] = True
                    return
                result.pop()
            result.pop()
            
    count = [0]
    durations = []
    converted_courses = defaultdict(dict)
    for scheduling_course in data['scheduling_courses']:
        converted_courses[scheduling_course['id']] = scheduling_course
        for duration in scheduling_course['time_durations']:
            durations.append((scheduling_course['id'], duration))
    
    durations.sort(key=lambda x: x[1], reverse=True)
    data['scheduling_courses'] = converted_courses
    
    for i in range(data['number_of_sections']):
        section = str(i+1)
        for course_id, duration in durations:
            scheduling_course = data['scheduling_courses'][course_id]
        # for scheduling_course in data['scheduling_courses']:
        #     for duration in scheduling_course['time_durations']:
            found = [False]
            random.shuffle(days)
            random.shuffle(scheduling_course['rooms'])
            random.shuffle(scheduling_course['instructors'])

            dfs('course', None, [section, duration, scheduling_course['course']])

    print(count)
