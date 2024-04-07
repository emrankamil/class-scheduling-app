data = [
    {
      "id": 1,
      "scheduling_courses": [
          {
              "id": 2,
              "time_durations": ["120","120", "240"],
              "scheduling_data": 1,
              "course": 1,
              "instructors": [
                  1,
                  2,
                  3,
                  4
              ]
          }
      ],
      "year": 2015,
      "batch": 2,
      "number_of_sections": 3,
      "department": 1,
      "rooms": [
          1,
          2,
      ]
  }
][0]

# courses = {
#     'course1':{
#         'instructors': ['instr1', 'instr2', 'instr3'],
#         'durations': [60, 120, 240]
#         },
#     'course2':{
#         'instructors': ['instr4', 'instr5', 'instr6'],
#         'durations': [120, 240]
#         },
#     'course3':{
#         'instructors': ['instr7', 'instr8', 'instr9'],
#         'durations': [60, 240]
#         },
#     }

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  
# rooms = [201, 202, 203, 204, 205, 206]

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
