import tri

tri.newGame()

while True:
    newround = tri.startRound()
    if newround == "exit":
        break
    prompt = input("Press ENTER to start a new round, or input 'q' to quit.")
    if prompt == "q":
        break
