schedule_data = {
    "department": "Computer Science",
    "subjects": {
        "Communicative English": [1, "Mr. Smith", "Ms. Johnson", "Dr. Brown"],
        "Mathematics": [2, "Prof. Davis", "Ms. Wilson", "Dr. Lee"],
        "Physics": [1, "Mr. Clark", "Ms. Parker", "Dr. Garcia"],
        "Biology": [1, "Dr. White", "Prof. Martinez", "Ms. Lopez"],
        "Chemistry": [1, "Dr. Rodriguez", "Prof. Nguyen", "Mr. Kim"],
        "ICT": [1, "Mr. Taylor", "Ms. Moore", "Dr. Patel"],
        "Moral Education": [1, "Ms. Thomas", "Prof. Baker", "Dr. Jones"]
    },
    "time_for_a_single_period": "45:00",
    "rooms": ["Room 101", "Room 102", "Room 103"],
    "break_times": [
        {
        "start_time": "12:00 PM",
        "end_time": "1:00 PM"
        },
        {
        "start_time": "12:00 PM",
        "end_time": "1:00 PM"
        },
    ]
}

final_schedule =  []

# def backtrack(schedule, cur_schedule_data, cur_idx):
#     if cur_schedule_data == 'instructors':

#     for data in cur_schedule_data:
#         schedule.append(subject)
#         backtrack(schedule, schedule_data[subject], cur_idx + 1)
#         schedule.pop()

def generate_schedule(schedule_data):
    for subject in schedule_data['subjects']:
        for instructor in schedule_data['subjects'][subject]:
            for room in schedule_data['rooms']:
                schedule = [subject, instructor, room]
                if is_valid(schedule):
                    final_schedule.append()