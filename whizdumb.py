# zeke ash
# whiz-dumb of crowds
# based on wits and wagers

# questions taken from https://meebily.com/wits-wagers-questions-game-ideas

# getpass will hide people's answers in run in terminal
import csv
import getpass
import pwinput
import random

# replace this with whereever you are keeping these files:
# os.chdir("/Users/zekeash/Desktop/intro to comp sci")

inputsecret = input  # use this to run in IDLE
# inputsecret = getpass.getpass  # use this to run in terminal with no echo
# inputsecret = pwinput.pwinput  # use this to run in terminal with *'s instead of numbers

# create questions:
f = open("rules.txt", "r")
content = f.read()
f.close()


class Player:
    def __init__(self, playername, points=2):
        self.playername = playername
        self.points = points

    def __str__(self):
        return self.playername

    def placeBet(self, howMuch, guess, odds):
        self.points = self.points - howMuch
        bet = Bet(howMuch, guess, self, odds)
        return bet


def validLetters(tupleList):
    validLetters = []
    for tup in tupleList:
        validLetters.append(tup[0])
    return validLetters


negative_infinity = float('-inf')


class Question:
    def __init__(self, questionText, answerNumber):
        self.questionText = questionText
        self.answerNumber = answerNumber
        self.list_to_bet = []

    def __str__(self):
        return 'The question is {self.questionText} and the answer is {self.answerNumber}'.format(self=self)

    def getResponses(self, playerList):
        responses = []
        for player in playerList:
            guess = eval(inputsecret(player.playername + ", enter your guess: "))
            responses.append((player, guess))
        return (responses)

    def rankResponses(self, responses):
        responses = responses
        unique_responses = []
        for x in responses:
            if x[1] not in unique_responses:
                unique_responses.append(x[1])
                responders = []
                for z in responses:
                    if z[1] == x[1]:
                        responders.append(z[0].playername)
                self.list_to_bet.append((x[1], responders))
        self.list_to_bet.sort(key=lambda tup: tup[0])
        oddsList = []
        if len(self.list_to_bet) % 2 == 0:
            for j in range(1, int(len(self.list_to_bet) // 2) + 1):
                oddsList.insert(int(len(self.list_to_bet) / 2) + j, "{}:1"
                                .format(j + 2))
                oddsList.insert(int(len(self.list_to_bet) / 2) - j, "{}:1"
                                .format(j + 2))
        else:
            for j in range(1, int(len(self.list_to_bet) // 2) + 1):
                oddsList.insert(int(len(self.list_to_bet) / 2) + j, "{}:1"
                                .format(j + 2))
                oddsList.insert(int(len(self.list_to_bet) / 2) - j, "{}:1"
                                .format(j + 2))
            oddsList.insert((int(len(self.list_to_bet) // 2)), "2:1")
        bettingTable = []
        for j in range(len(oddsList)):
            bettingTable = bettingTable + [(chr(j + 98), oddsList[j], self.list_to_bet[j])]
        bettingTable.insert(0, ("a", "6:1", (negative_infinity, "all answers too high")))
        print("here are the available bets, identified by letter and odds: ")
        print(*bettingTable, sep="\n")
        return bettingTable

    def bettingRound(self, bettingTable, playerList):
        betList = []
        validBets = validLetters(bettingTable)
        for player in playerList:
            answer_to_bet = input(
                "{}, which of these answers would you like to bet on? (enter the corresponding letter) "
                .format(player.playername, player.points))
            while answer_to_bet not in validBets:
                answer_to_bet = input("sorry, please enter a valid letter: ")
            for tup in bettingTable:
                if answer_to_bet == tup[0]:
                    chosenAnswer = tup[-1]
            howMuch = eval(input("how much would you like to bet on answer {}? you have {} points. "
                                 .format(chosenAnswer, player.points)))
            while howMuch > player.points:
                howMuch = eval(input("sorry, you may not bet more than what you have. please enter your bet: "))
            # bet = player.placeBet(howMuch,chosenAnswer,int(tup[1][0]))
            bet = player.placeBet(howMuch, chosenAnswer, int(bettingTable[ord(answer_to_bet) - 97][1][0]))
            betList.append(bet)
            if player.points > 0:
                second_answer_to_bet = input(
                    "{}, you still have {} point. which of these answers would you like to bet on? (enter the corresponding letter or nothing to stop) "
                    .format(player.playername, player.points))
                if second_answer_to_bet == "":
                    pass
                else:
                    while second_answer_to_bet not in validBets:
                        second_answer_to_bet = input("sorry, please enter a valid letter: ")
                    for tup in bettingTable:
                        if second_answer_to_bet == tup[0]:
                            chosenAnswer = tup[-1]
                    second_howMuch = eval(input("you have {} points. how much would you like to bet on answer {}? "
                                                .format(player.points, chosenAnswer)))
                    while second_howMuch > player.points:
                        second_howMuch = eval(
                            input("sorry, you may not bet more than what you have. please enter your bet: "))
                    bet = player.placeBet(howMuch, chosenAnswer,
                                          int(bettingTable[ord(second_answer_to_bet) - 97][1][0]))
                    betList.append(bet)
        bestGuess = self.identifyCorrectResponse(self.list_to_bet)
        print(("the correct answer was {}! {} was the winning guess!")
              .format(self.answerNumber, bestGuess))
        for bet in betList:
            if bet.response == bestGuess:
                bet.cashout()
        input("press enter to continue to next round!")

    def identifyCorrectResponse(self, responses):
        self.list_to_bet.append((float(self.answerNumber), "correct answer"))
        self.list_to_bet.append((negative_infinity, "all answers too high"))
        self.list_to_bet.sort(key=lambda tup: tup[0])
        winningAnswerIndex = self.list_to_bet.index((float(self.answerNumber), "correct answer")) - 1
        return self.list_to_bet[winningAnswerIndex]


questions = []
with open('wits-and-wagers-questions.csv', newline='') as csvfile:
    questionReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in questionReader:
        questionText = row[0]
        answer = row[1]
        questions.append(Question(questionText, answer))


class Bet:
    def __init__(self, amount, response, player, odds):
        self.amount = amount
        self.odds = odds
        self.response = response
        self.player = player

    def cashout(self):
        self.player.points = self.player.points + (self.amount * self.odds)
        print("{} won {} points!".format(self.player.playername, self.amount * self.odds))


def main():
    # run program
    print("welcome to WHIZDUMB!")
    intro = input(
        "would you like to see the instructions on how to play? (enter y to see instructions, press enter to begin game) ")
    if intro == "yes" or intro == "y":
        print(content)
        o = input("press enter to start!")
    else:
        print("okay! loading game!")
    numPlayers = eval(input("how many players will be in this game (4 - 10 recommended)? "))
    playerList = []
    for c in range(numPlayers):
        name = input("what is player {}'s name? ".format(c + 1))
        player = Player(name)
        playerList.append(player)
    for r in range(7):
        for player in playerList:
            if player.points < 2:
                player.points = 2
        question = random.choice(questions)
        questions.remove(question)
        print(question.questionText)
        responses = question.getResponses(playerList)
        bettingTable = question.rankResponses(responses)
        print("ok, time to place bets!")
        question.bettingRound(bettingTable, playerList)
    print("game over! here are the scores: ")
    scoreboard = []
    for player in playerList:
        print("{}: {} points!".format(player.playername, player.points))
        scoreboard.append(player.points)
        if player.points == max(scoreboard):
            winner = "the winner is {} with {} points! thanks for playing!".format(player.playername, player.points)
    print(winner)

# comment this out if you do not want it to run automatically
if __name__=="__main__":
    main()

