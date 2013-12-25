playerCount = 0
players = []
scores = {}

def newGame():
    global playerCount
    global players
    global scores
    playerCount = int(input("Enter the number of players: "))
    for i in range(playerCount):
        players.append(input("Enter the name for player " + str(1+i) + ": "))
    for player in players:
        scores[player] = 0

def showScores():
    for i,player in enumerate(players):
        print(i+1, player, scores[player])

def startRound():
    showScores()
    firstPlayer = int(input("Enter the number of the first player"))-1
    currentPlayer = firstPlayer
    scores[players[firstPlayer]] += 10
    winner = False
    while not winner:
        newscore = input("Enter the score for " + players[currentPlayer] + ": ")
        if newscore[-1] == "w":
            winner = True
            newscore = newscore[:-1] + 25
        scores[players[currentPlayer]] += int(newscore)
        showScores()
        if not winner:
            currentPlayer = (currentPlayer + 1) % playerCount
    while winner:
        newscore = int(input("Enter a subtotal or 0 to finish"))
        scores[players[currentPlayer]] += newscore
        if newscore == 0:
            showScores()
            return

def setScore(player, score):
    global scores
    scores[player] = score

