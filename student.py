class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_average_mark(self):
        if not self.marks:
            return None
        return sum(self.marks) / len(self.marks)

    def is_eligible(self):
        average_mark = self.calculate_average_mark()
        return average_mark is not None and average_mark >= 60

    def is_adult(self):
        return self.age >= 18

    def get_first_three_characters(self):
        if len(self.name) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        return self.name[:3]
