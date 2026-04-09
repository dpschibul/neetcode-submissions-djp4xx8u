class Twitter:

    def __init__(self):
        self.tweetCount = 0
        self.tweets = {}
        self.follows = {}
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append([self.tweetCount, tweetId])
        else:
            self.tweets[userId] = [[self.tweetCount, tweetId]]
        self.tweetCount += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.follows.get(userId, set())
        following.add(userId)

        tweetList = []

        for follow in following:
            if follow in self.tweets:
                for tweet in self.tweets[follow]:
                    tweetList.append(tweet)
        
        tweetList.sort(key=lambda x: x[0])

        return [t[1] for t in tweetList[-1:-11:-1]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

        
