def are_valid_groups(student_numbers, groups ):
      
  for group in groups:
    for student_number in group:
        for student in student_numbers:
          if (student == student_number):
              student_numbers.remove(student)

  if student_numbers:
    return False
  else:
    return True

print(are_valid_groups([1234, 3920, 3402, 2390], [[0000, 9303, 3920 ], [7383, 2303, 3402, 1234 ], [2390]]))
