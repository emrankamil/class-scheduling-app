from collections import defaultdict
from scheduling.serializers import ScheduleEntrySerializer
from scheduling_config.models import SchedulingData
from scheduling_config.serializers import SchedulingDataSerializer
import datetime
# data = {
#         "id": 4,
#         "department": 4,
#         "year": 2015,
#         "batch": 11,
#         "number_of_sections": 5,
#         "rooms": [
#             3,
#             5,
#             6,
#             7
#         ],
#         "scheduling_courses": [
#             {
#                 "id": 5,
#                 "time_durations": {
#                     "45": 8
#                 },
#                 "scheduling_data": 4,
#                 "course": 5,
#                 "instructors": [
#                     5,
#                     6
#                 ]
#             },
#             {
#                 "id": 6,
#                 "time_durations": {
#                     "45": 7
#                 },
#                 "scheduling_data": 4,
#                 "course": 6,
#                 "instructors": [
#                     7
#                 ]
#             },
#             {
#                 "id": 7,
#                 "time_durations": {
#                     "45": 7
#                 },
#                 "scheduling_data": 4,
#                 "course": 7,
#                 "instructors": [
#                     5
#                 ]
#             }
#         ],
#         "possible_durations": {
#             "45": [
#                 "14:00:00",
#                 "10:45:00",
#                 "09:15:00",
#                 "14:45:00",
#                 "11:30:00",
#                 "08:30:00",
#                 "10:00:00"
#             ]
#         }
# }
# days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  


def generate_schedule(scheduling_data_id, days):

    output = []

    serializer = SchedulingDataSerializer(SchedulingData.objects.get(id=scheduling_data_id))
    data = serializer.data
    # print(data)
    # print(data['possible_durations'])

    def verify_and_save(schedule):
        timechange = datetime.timedelta(minutes=int(schedule[0]))
        end_time = (datetime.datetime.combine(datetime.date(1,1,1),schedule[5]) + timechange).time()
                
        schedule = {
                    'parent_schedule': data['id'],
                    'course': schedule[1],
                    'instructor': schedule[4],
                    'day': schedule[2],
                    'room': schedule[3],
                    'start_time': schedule[5],
                    'end_time': end_time
                }
        new_entry = ScheduleEntrySerializer(data=schedule)
        if new_entry.is_valid():
            response = new_entry.save()
            print(response)


   
    def dfs(variable, value, result):
        if variable == 'course':
            for day in days:
                dfs('day', day, result)
        if variable == 'day':
            result.append(value)
            for room in data['rooms']:
                dfs('room', room, result)
            result.pop()
        if variable == 'room':
            result.append(value)
            for instr in scheduling_course['instructors']:
                dfs('instructor', instr, result)
            result.pop()
        if variable == 'instructor':
            result.append(value)
            for time in data['possible_durations'][result[0]]:
                result.append(time)
                verify_and_save(result)
                output.append(result[:])
                result.pop()
            result.pop()
            

    for scheduling_course in data['scheduling_courses']:
        for duration in scheduling_course['time_durations']:
            dfs('course', None, [duration, scheduling_course['course']])
    print(output)
    return output
    # print('duration' + ' ' + 'course' + ' ' + 'day' + ' ' + 'room' + ' ' + 'instructor' )
    # for _ in range(10):
    #     print(output[_])
        

        