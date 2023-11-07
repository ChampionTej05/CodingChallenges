'''
Problem : https://lowleveldesign.io/LLD/GameDesign/Scoreboard

Design a Leaderboard class, which has the following features:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.

top(K): Return the score sum of the top K players.

reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
'''

#basic solution from data structure point of view

import collections


class Leaderboard(object):
    def __init__(self):
        self.leaderboard = {}
        self.leaderboard_counter = collections.Counter()

    #o(1)
    def addScore(self, playerId, score):
        if playerId in self.leaderboard:
            self.leaderboard[playerId] += score
        else:
            self.leaderboard[playerId] = score

    def addScoreCounterMethod(self, playerId, score):
        self.leaderboard_counter[playerId] += score

    def resetCounterMethod(self, playerId):
        self.leaderboard_counter[playerId] = 0

    def topCounterMethod(self, k):
        k_most_common = self.leaderboard_counter.most_common(k)
        return k_most_common

    #o(1)
    def reset(self, playerId):
        if playerId in self.leaderboard:
            self.leaderboard[playerId] = 0

    #o(nlogN) because of sorting the elements everytime
    def top(self, k):

        sortedDict = dict(
            sorted(self.leaderboard.items(),
                   key=lambda item: item[1],
                   reverse=True))
        print("Sorted Dict", sortedDict)
        sortedDict = list(sortedDict.keys())
        return sortedDict[:k] if len(sortedDict) > k else sortedDict

    # if we can maintain the sorted dict or map of objects then then it would easier to find the top(k) queries though add and remove won't be O(1)
    # we could use heap to do this  or we could use balary binary tree like Red-black tree to do this

    #O(NlogN + K)
    def topHeap(self, k):

        import heapq
        leaderboardHeap = []
        #O(nlogN) operation anyways
        for playerId, score in self.leaderboard.items():
            #maxHeap
            #O(logN)
            heapq.heappush(leaderboardHeap, [score * (-1), playerId])

        print("MaxHeap", leaderboardHeap)
        top_k_players = [[
            playerId, score * (-1)
        ] for score, playerId in heapq.nsmallest(k, leaderboardHeap)]
        print("top_k_players")
        return top_k_players


if __name__ == "__main__":

    leaderboard = Leaderboard()

    leaderboard.addScore("player1", 10)
    leaderboard.addScore("player2", 15)
    leaderboard.addScore("player1", 8)
    leaderboard.addScore("player2", 2)
    leaderboard.addScore("player3", 1)
    leaderboard.addScore("player4", 9)
    leaderboard.addScore("player5", 23)
    leaderboard.addScore("player1", 13)
    leaderboard.addScore("player3", 11)
    leaderboard.addScore("player4", 1)

    print(leaderboard.leaderboard)

    top_2 = leaderboard.topHeap(3)
    print("Top 2", top_2)