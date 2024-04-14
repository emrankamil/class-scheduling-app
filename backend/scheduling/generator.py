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

def generate_schedule(scheduling_data_id, days):

    scheduling_data = SchedulingData.objects.get(id=scheduling_data_id)
    serializer = SchedulingDataSerializer(scheduling_data)
    data = serializer.data

    def handle_reserved_rooms(room, duration, day):
        possible_start_times = []
        for reservation in room['reservations']:
            if reservation['reserved_days'] == day:
                for start_time in data['possible_durations'][duration]:
                    timechange = datetime.timedelta(minutes=int(duration))
                    end_time = (datetime.datetime.combine(datetime.date(1,1,1),start_time) + timechange).time()
                    reservation_start_time = datetime.datetime.strptime(reservation["start_time"], "%H:%M:%S").time()
                    reservation_end_time = datetime.datetime.strptime(reservation["end_time"], "%H:%M:%S").time()
                    if start_time >= reservation_start_time and end_time <= reservation_end_time:
                        possible_start_times.append(start_time)
        return possible_start_times
        
    def verify_and_save(schedule):
        timechange = datetime.timedelta(minutes=int(schedule[1]))
        end_time = (datetime.datetime.combine(datetime.date(1,1,1),schedule[6]) + timechange).time()
                
        schedule = {
                    'parent_schedule': data['id'],
                    'section': schedule[0],
                    'course': schedule[2],
                    'instructor': schedule[3],
                    'day': schedule[4],
                    'room': schedule[5],
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
                     
            reserved_rooms = [res_room for res_room in data["reserved_rooms"] if res_room["id"] in scheduling_course['rooms']]
            department_rooms = [dep_room for dep_room in data["department_rooms"] if dep_room["id"] in scheduling_course['rooms']]
            
            for room in reserved_rooms:
                result.append(room["id"])
                start_times = handle_reserved_rooms(room, result[1], value)
                print(start_times)
                for start_time in start_times:
                    result.append(start_time)
                    if verify_and_save(result):
                        found[0] = True
                        return
                    result.pop()
                result.pop()
            
            for room in department_rooms:
                dfs('room', room["id"], result)
            result.pop()

        if variable == 'room':
            result.append(value)
            for time in data['possible_durations'][result[1]]:
                result.append(time)
                if verify_and_save(result):
                    found[0] = True
                    return
                result.pop()
            result.pop()

        # if variable == 'day':
        #     result.append(value)
        #     for room in scheduling_course['rooms']:
        #         dfs('room', room, result)
        #     result.pop()
        # if variable == 'room':
        #     result.append(value)
        #     for instr in scheduling_course['instructors']:
        #         dfs('instructor', instr, result)
        #     result.pop()
        # if variable == 'instructor':
        #     result.append(value)
        #     for time in data['possible_durations'][result[1]]:
        #         result.append(time)
        #         count[0] += 1
        #         if verify_and_save(result):
        #             found[0] = True
        #             return
        #         result.pop()
        #     result.pop()
            
    count = [0]
    durations = []
    converted_courses = defaultdict(dict)
    for scheduling_course in data['scheduling_courses']:
        converted_courses[scheduling_course['id']] = scheduling_course
        for duration in scheduling_course['time_durations']:
            durations.append((scheduling_course['id'], duration))
    
    durations.sort(key=lambda x: x[1], reverse=True)
    data['scheduling_courses'] = converted_courses
    
    for section in data['sections']:
        for course_id, duration in durations:
            scheduling_course = data['scheduling_courses'][course_id]
            instructor = [instructor['instructor'] for instructor in scheduling_course["scheduling_instructors"] if section['id'] in instructor['sections']][0]
            found = [False]

            random.shuffle(days)
            random.shuffle(scheduling_course['rooms'])
            random.shuffle(scheduling_course['instructors'])

            dfs('course', None, [section["id"], duration, scheduling_course['course'], instructor])

    print(count)