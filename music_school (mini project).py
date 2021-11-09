class MusicSchool:
 
    students = {
        "Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
        "Talina": [28, "555-765-452", ["Cello"]],
        "Eric":   [12, "583-356-223", ["Singing"]]
    }
 
    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
 
    def print_students_data(self):
        for k, v in MusicSchool.students.items():
            print(f'Student: {k} who is {v[0]} years old and is taking {v[2]}')
 
    def print_student(self, student):
        print(f'Student: {student} who is {MusicSchool.students[student][0]} years old and is taking {MusicSchool.students[student][2]}')
 
    def add_student(self, name, data):
        MusicSchool.students[name] = data
 
 
m = MusicSchool(23, 51)
 
m.print_students_data()
m.print_student('Gino')
m.add_student("Jack", [60, "562-234-234", ["Piano"]])
 
with open("music_school.txt", "w") as file:
    for k, v in MusicSchool.students.items():
        file.write(f'Student: {k} who is {v[0]} years old and is taking {v[2]}\n')