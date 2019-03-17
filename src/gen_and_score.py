import generate_string
import score_string

def gen_and_score():
    """a function that will repeatedly call generate and score, then if 100% of
    the letters are correct we are done. If the letters are not correct
    then we will generate a whole new string.To make it easier to follow
    your program’s progress this third function should print out the best
    string generated so far and its score every 1000 tries.

    Improve upon the program in the self check by keeping letters that are
    correct and only modifying one character in the best string so far. This
    is a type of algorithm in the class of ‘hill climbing’ algorithms,
    that is we only keep the result if it is better than the previous one."""
    bestStrSoFar = ''
    bestScoreSoFar = 0.00
    thePhrase = 'methinks it is like a weasel'
    correctphrase = False
    i = 0
    correctChars = 0
    while not correctphrase:
        strToCheck = generate_string.generate_string()
        if strToCheck[correctChars] == thePhrase[correctChars]:
            bestStrSoFar += strToCheck[correctChars]
            correctChars += 1
        score = score_string.score_string(bestStrSoFar)
        if score == 1:
            correctphrase = True
            bestScoreSoFar = score
        elif score > bestScoreSoFar:
            bestScoreSoFar = score
        i += 1
        if not i%1000:
            print("Best string and score so far: " + bestStrSoFar + " -- " + str(bestScoreSoFar))
            bestScoreSoFar = 0.00

    #print("Generated correct phrase!: " + bestStrSoFar + " -- " + str(bestScoreSoFar))
    return bestStrSoFar, str(bestScoreSoFar)

def main():
    genStr, genScore = gen_and_score()
    print("Generated correct phrase!: " + genStr + " -- " + genScore)

if __name__ == '__main__':
    main()
