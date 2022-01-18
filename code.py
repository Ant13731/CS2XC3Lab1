def are_valid_groups(studentNums, groups):
    #All students are by default not in a group
    isStudentInGroup = []
    for x in range(len(studentNums)):
        isStudentInGroup[x] = False
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
