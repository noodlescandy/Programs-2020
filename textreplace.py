with open('vocablist.txt', 'r') as vocabFileIn, open('vocablistout.txt', 'w') as vocabFileOut:
    #count = 0
    while(True):
        #count += 1
        line = vocabFileIn.readline()
        if not line:
            break
        # line is the current string line
        """line.replace("1", " ")
        line.replace("2", " ")
        line.replace("3", " ")
        line.replace("4", " ")
        line.replace("5", " ")
        line.replace("6", " ")
        line.replace("7", " ")
        line.replace("8", " ")
        line.replace("9", " ")
        line.replace("0", " ")
        line.replace(".", " ")"""
        newLine = line[3:]
        newLine = newLine.strip()
        print(newLine)
        vocabFileOut.write(newLine + "\n")
