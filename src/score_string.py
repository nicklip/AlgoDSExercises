def score_string(strToScore):
    """a function that will score each generated string
    by comparing the randomly generated string to the goal"""
    goal = 'methinks it is like a weasel'
    numCharsCorrect = 0
    for i in range(len(strToScore)):
        if goal[i] == strToScore[i]:
            numCharsCorrect += 1
    # calculate percentage correct and return
    return numCharsCorrect/28.0