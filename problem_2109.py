def addSpaces(s, spaces):
        leftPointer = 0
        result = []
        for i in spaces:
            rightPointer = i
            result.append(s[leftPointer:rightPointer])
            leftPointer = rightPointer
        result.append(s[rightPointer:])
        return " ".join(result)