# Joshua Phillips
# 10/29/24
# Generating Grade Reports

import time
# I
# Lists
robbins_grades = [87, 93, 79, 71, 96]
haas_grades = [96, 80, 75, 83, 90]

# Ask for latest grade
appendage_rob = int(input('We seem to be missing the latest quiz score for Robbin, please enter it here: '))
time.sleep(1)
appendage_has = int(input('We seem to be missing the latest quiz score for Haas, please enter it here: '))
time.sleep(1)
# Relevant information
robbin = 'ROBBINS, Carli'
haas = 'HAAS, Randall'
school = 'Career Tech Center'
course = 'Web & App Development'

# P
# Fix list with latest scores
robbins_grades.append(appendage_rob)
haas_grades.append(appendage_has)

# Find number of scores for both
num_robbin = len(robbins_grades)
num_haas = len(haas_grades)

# Find the sum of each list
sum_robbin = sum(robbins_grades)
sum_haas = sum(haas_grades)

# Average the two lists
average_robbin = sum_robbin / num_robbin
average_haas = sum_haas / num_haas
average_robbin = round(average_robbin, 2)
average_haas = round(average_haas, 2)

# O
print(f'''
      Semester 1 Grade Report
      -------------
      Student: {robbin}
      School: {school}
      Course: {course}
      Average Score: {average_robbin}

      Student: {haas}
      School: {school}
      Course: {course}
      Average Score: {average_haas}''')