import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.follows = {}
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        heap = []

        for user in self.follows[userId]:
            for tweet in self.tweets.get(user, []):
                if len(heap) < k:
                    heapq.heappush(heap, tweet)
                elif heap[0] < tweet:
                    heapq.heappushpop(heap, tweet)

        heap.sort(reverse=True)
        return heap

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
            self.follows[followerId].add(followerId)

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
