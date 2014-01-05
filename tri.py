playerCount = 0
players = []
scores = {}

def inputInt(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return int(x)
        else:
            print("Invalid Input!")

def inputScore(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return int(x), False
        elif x[-1] == "w" and x[:-1].isdigit():
            return int(x[:-1]), True
        else:
            print("Invalid Input!")

def newGame():
    global playerCount
    playerCount = inputInt("Enter the number of players: ")
    for i in range(playerCount):
        players.append(input("Enter the name for player " + str(1+i) + ": "))
    for player in players:
        scores[player] = 0

def showScores():
    for i,player in enumerate(players):
        print(i+1, player, scores[player])

def startRound():
    showScores()
    firstPlayer = inputInt("Enter the number of the first player: ")-1
    currentPlayer = firstPlayer
    scores[players[firstPlayer]] += 10
    winner = False
    winlist = []
    while not winner:
        newscore,winner = inputScore("Enter the score for " + players[currentPlayer] + ": ")
        scores[players[currentPlayer]] += newscore
        if winner:
            scores[players[currentPlayer]] += 25
        if scores[players[currentPlayer]] >= 400:
            winlist.append(players[currentPlayer])
        showScores()
        if not winner:
            currentPlayer = (currentPlayer + 1) % playerCount
    while winner:
        newscore = inputInt("Enter a subtotal or 0 to finish: ")
        scores[players[currentPlayer]] += newscore
        if newscore == 0:
            showScores()
            if max(scores.values()) >= 400:
                if players[currentPlayer] in winlist:
                    winplay = players[currentPlayer]
                else:
                    winplay = winlist[0] 
                print("WINNER! " + winplay)
                input()
                return "exit"
            return

def setScore(player, score):
    scores[player] = score

