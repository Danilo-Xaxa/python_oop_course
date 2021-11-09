class TODO:
    def __init__(self, description, classification, date, priority, status):
        self.description = description
        self.classification = classification
        self.date = date
        self.priority = priority
        self.status = status
 
    def mark_done(self):
        self.status = 'done'
 
class Class:
    def __init__(self, code, count, professor, start, end, classroom):
        self.code = code
        self.count = count
        self.professor = professor
        self.start = start
        self.end = end
        self.classroom = classroom