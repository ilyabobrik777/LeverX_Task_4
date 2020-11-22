import File_reader from file_reader
import Distribution from distribution


rooms = File_reader.file_reader("rooms.json")
students = File_reader.file_reader("students.json")
print(Distribution.student_distribution(rooms, students))