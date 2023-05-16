# The plan is to create an interface to allow making a workout plan, adding/removing exercises from said plan and
# add times to set durations such as time per set or rep, an optional resting timer, an optional 'get ready' timer and
# an optional display/sound countdown to eliminate holding a phone/watch/counting in head
import csv

# TODO:

"""
-create template for weight exercises, name, set, reps, rest between sets, slow-rep-mode with duration(?), ??
- implement visual/acoustic notification when rest is about to expire, optional too for duration to hold
- be able to create plans and save/load/remove exercises
- tracker how long a workout takes
- ??
"""

class Exercise:

    all = []

    def __init__(self, name, sets=0, reps=0, duration=0, rest=0):
        assert sets >= 0 and reps >= 0 and duration >= 0 and rest >= 0, \
            "Must be a whole number greater than or equal to 0"

        self.name = name
        self.sets = sets
        self.reps = reps
        self.duration = duration
        self.rest = rest

        Exercise.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open('exercises.csv', 'r') as file:
            reader = csv.DictReader(file)
            exercises = list(reader)

        for item in exercises:
            Exercise(
                name=item.get('name'),
                sets=int(item.get('sets')),
                reps=int(item.get('reps')),
                duration=int(item.get('duration')),
                rest=int(item.get('rest'))
            )


def save_exercise(name, sets, reps, duration, rest):
    with open('exercises.csv', 'a', newline="") as file:
        save = csv.writer(file)
        exercise = name, sets, reps, duration, rest
        save.writerow(exercise)


    # def __repr__(self):
    #     return f"{self.__class__.__init__}('{self.name}', {self.sets}, {self.reps}, {self.duration}, {self.rest})"

save_exercise("Squat", 2, 20, 0, 25)
Exercise.instantiate_from_csv()

