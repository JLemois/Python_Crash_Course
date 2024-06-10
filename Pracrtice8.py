seperator = '\r\n' + '_' * 60 + '\r\n'

# Header
print('\r\n' + '=' * 60 + '\r\n\nPython Crash Course practice work By: Joseph Lemois')
print(seperator)


# expanded class practice
class DoctorVisit:
    def __init__(self, doctor_name, visit_type):
        self.doctor_name = doctor_name
        self.visit_type = visit_type
        self.copay_amount = 0

    def set_copay_amount(self, copay_amount):
        self.copay_amount = copay_amount

    def describe_visit(self):
        if self.copay_amount == 0:
            print(f'Doctors appointment with {self.doctor_name} to go over {self.visit_type}.\nThere is no copay'
                  f' for this visit.\n')
        else:
            print(f'Doctors appointment with {self.doctor_name} to go over {self.visit_type}.\nThe copay for this visit'
                  f' costs: {self.copay_amount}.\n')


medVisit1 = DoctorVisit('Priscilla', 'Consultation')
medVisit1.set_copay_amount(50)
medVisit1.describe_visit()

medVisit2 = DoctorVisit('Chowdurry', 'Infusion')
medVisit2.describe_visit()

print(seperator)


class SpecialVisit(DoctorVisit):
    def __init__(self, doctor_name, visit_type):
        super().__init__(doctor_name, visit_type)
        self.location = ""

    def set_location(self, location):
        self.location = location

    def describe_location(self):
        print(f'The appointment scheduled will be at {self.location}.')


medVisit3 = SpecialVisit('Priscilla', 'T-Cell Treatment')
medVisit3.set_location('Main Hospital')
medVisit3.describe_visit()
medVisit3.describe_location()
