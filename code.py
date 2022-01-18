def are_valid_groups(studentNums, groups):
    #All students are by default not in a group
    isStudentInGroup = []
    for x in range(len(studentNums)):
        isStudentInGroup.append(0)
    #If students are in a group, set their respective index to true
        for group in groups:
            if len(group)<2 or len(group)>3:
                return False
            if  group.count(studentNums[x])==1:
                isStudentInGroup[x]=isStudentInGroup[x]+1
            elif group.count(studentNums[x])>1:
                return False
    #If every student is in a group, return true, else return false
    for student in isStudentInGroup:
        if student == 0 or student > 1:
            return False
    return True

#New testing code
print(are_valid_groups(["1234", "3920", "3402", "2390"], [["9303" ], ["9999"], ["1111"]]))

