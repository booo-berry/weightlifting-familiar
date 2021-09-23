import numpy as np
from tika import parser
from tabulate import tabulate


def main():
    workout_table = workout_pdf2table('Workout.pdf')

    print(tabulate(workout_table, headers='firstrow'))


    print('done')


def workout_pdf2table(file_path):
    raw = parser.from_file(file_path)
    #print(raw['content'])

    split_content = raw['content'].split("\n")

    exercises = ['snatch', 'clean', 'jerk', 'back squat']
    count = 0
    date_list = []
    exercise_list = []
    weight_list = []
    rep_list = []
    total_length = len(split_content)
    for index, line in enumerate(split_content):
        # Get the current date
        if '/' in line.lower():
            slash_index = line.find('/')
            # These can probably be while loops
            if line[slash_index - 1].isnumeric():
                month = line[slash_index - 1]
                if line[slash_index - 2].isnumeric():
                    day = line[slash_index - 2]+month
            if line[slash_index + 1].isnumeric():
                day = line[slash_index + 1]
                if line[slash_index + 2].isnumeric():
                    day = day+line[slash_index + 2]
            if 'month' in locals():  # should check if date exists as well
                date = month+'/'+day

        # Find exercises
        if any(exercise in line.lower() for exercise in exercises):
            # could try to use filter
            exercise_name = [exercise for exercise in exercises if exercise in line.lower()]
            # Find weight lifted and reps
            next_line = split_content[index+1].lower()
            if 'x' in next_line:
                # These can probably be while loops
                if next_line[0].isnumeric():
                    weight = next_line[0]
                    if next_line[1].isnumeric():
                        weight = weight+next_line[1]
                if next_line[-1].isnumeric():
                    reps = next_line[-1]
                    if next_line[-2].isnumeric():
                        reps = next_line[-2]+reps
                # Can this be combined into a single logical?
                if 'weight' in locals():
                    if 'reps' in locals():
                        date_list.append(date)
                        exercise_list.append(exercise_name)
                        weight_list.append(weight)
                        rep_list.append(reps)
                        ++count

    # Print table
    table = {'dates':  date_list, 'exercises': exercise_list, 'weight': weight_list, 'reps': rep_list}
    return table


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
