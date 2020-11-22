class Distribution:
    def __init__(self, rooms_info, students_info):
        self.rooms_info = rooms_info
        self.students_info = students_info

    def student_distribution(self):
        rooms_dict = {}
        rooms_list = []
        for room in self.rooms_info:
            students_list = []
            for student in self.students_info:
                if student['room'] == room['id']:
                    students_list.append(student['name'])
                rooms_dict = {
                    'room': room['id'],
                    'population': students_list
                }
        rooms_list.append(rooms_dict)
        return rooms_list
