def are_valid_groups(studentNums, groups):
    #All students are by default not in a group
    isStudentInGroup = []
    for x in range(len(studentNums)):
        isStudentInGroup.append([False])
        print("false\n")
    #If students are in a group, set their respective index to true
        for group in groups:
            if studentNums[x] in group:
                isStudentInGroup[x] = True
                break
    #If every student is in a group, return true, else return false
    for student in isStudentInGroup:
        if student is False:
            return False
    return True

print(are_valid_groups(["1234", "3920", "3402", "2390"], [["0000", "9303", "3920" ], ["7383", "2303", "3402", "1234" ], ["2390"]]))