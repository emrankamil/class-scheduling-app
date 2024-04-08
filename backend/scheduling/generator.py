data = {
        "id": 4,
        "department": 4,
        "year": 2015,
        "batch": 11,
        "number_of_sections": 5,
        "rooms": [
            3,
            5,
            6,
            7
        ],
        "scheduling_courses": [
            {
                "id": 5,
                "time_durations": {
                    "45": 8
                },
                "scheduling_data": 4,
                "course": 5,
                "instructors": [
                    5,
                    6
                ]
            },
            {
                "id": 6,
                "time_durations": {
                    "45": 7
                },
                "scheduling_data": 4,
                "course": 6,
                "instructors": [
                    7
                ]
            },
            {
                "id": 7,
                "time_durations": {
                    "45": 7
                },
                "scheduling_data": 4,
                "course": 7,
                "instructors": [
                    5
                ]
            }
        ],
        "possible_durations": {
            "45": [
                "14:00:00",
                "10:45:00",
                "09:15:00",
                "14:45:00",
                "11:30:00",
                "08:30:00",
                "10:00:00"
            ]
        }
    }

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  

output = []

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
        output.append(result[:])
        result.pop()
        

for scheduling_course in data['scheduling_courses']:
    for duration in scheduling_course['time_durations']:
        dfs('course', None, [duration, scheduling_course['course']])

print('duration' + ' ' + 'course' + ' ' + 'day' + ' ' + 'room' + ' ' + 'instructor' )
for _ in range(10):
    print(output[_])
