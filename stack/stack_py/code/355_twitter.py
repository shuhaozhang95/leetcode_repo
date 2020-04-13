class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.fw = dict()
        self.tweet = dict()
        self.news = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """  
        self.news.append((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        for i in range(len(self.news)-1,-1,-1):
            if len(res)==10:
                return res
            uid,tid = self.news[i]
            if uid ==userId:
                res.append(tid)
            if userId in self.fw:
                if uid in self.fw[userId]:
                    res.append(tid)
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.fw:
                self.fw[followerId].add(followeeId)
            else:
                self.fw[followerId] = {followeeId}
            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.fw:
                if followeeId in self.fw[followerId]:
                    n = list(self.fw[followerId])
                    idx = n.index(followeeId)
                    n.pop(idx)
                    self.fw[followerId] = set(n)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)