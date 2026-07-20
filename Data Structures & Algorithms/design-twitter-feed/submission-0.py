class Twitter:

    def __init__(self):
        self.friendsList = {} #user: set of followees
        self.posts = {} #user: [(time, tweetId)], chronological
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.setdefault(userId, []).append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for friend in self.friendsList.get(userId, set()) | {userId}:
            tweets = self.posts.get(friend, [])
            if tweets:
                ind = len(tweets) - 1 #latest tweet
                time, tweetId = tweets[ind]
                minHeap.append((-time, tweetId, friend, ind - 1))

        heapq.heapify(minHeap)
        out = []
        while minHeap and len(out) < 10:
            negTime, tweetId, friend, ind = heapq.heappop(minHeap)
            out.append(tweetId)
            if ind >= 0:
                time, nextId = self.posts[friend][ind]
                heapq.heappush(minHeap, (-time, nextId, friend, ind - 1))
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.friendsList.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        friends = self.friendsList.get(followerId, None)
        if friends:
            friends.discard(followeeId)