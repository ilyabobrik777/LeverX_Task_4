class Distribution:
    def __init__(self, room, students):
        self.room = room
        self.students = students

    def student_distribution(self):
        rooms_dict = {}
        rooms_list = []
        for room_info in self.room:
            students_list = []
            for student_info in self.students:
                if student_info['room'] == room_info['id']:
                    students_list.append(student_info['name'])
                rooms_dict = {
                    'room': room_info['id'],
                    'population': students_list
                }
        rooms_list.append(rooms_dict)
        return rooms_list
