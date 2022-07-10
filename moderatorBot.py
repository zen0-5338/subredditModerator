import praw
import pdb
import re
from dotenv import load_dotenv
from os import getenv

load_dotenv()
botClientID = getenv("botClientID")
botClientSecret = getenv("botClientSecret")
botUsername = getenv("botUsername")
botPassword = getenv("botPassword")
botUserAgent = getenv("botUserAgent")

#Subreddit Name (without r/, case sensitive)
subredditName = "" 

# words and Phrases to be banned, case insensitive.
bannedWords = ["hello"]


#Auto Reply Format
botReplyFormat = """Sorry u/{} , your comment contained words which are not allowed in this subreddit and got deleted. I am a bot and this action was performed automatically.
Please contact [moderators of the subreddit](/message/compose/?to=/r/{}) for assistance/complaints."""


botInstance = praw.Reddit(
    client_id=botClientID,
    client_secret=botClientSecret,
    username=botUsername,
    password=botPassword,
    user_agent=botUserAgent
)


botSubreddit = botInstance.subreddit(subredditName)


def moderateComments(botInstance, botSubreddit):
    """
    if isinstance(botInstance,None):
        raise TypeError("None Type in Bot Reddit Instance.")
    elif isinstance(botSubreddit,None):
        raise TypeError("None Type in Bot Subreddit Instance")
    """
    try:
        for submission in botSubreddit.new(limit=5):
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                for bannedWord in bannedWords:
                    if re.search(bannedWord,comment.body, re.IGNORECASE):
                        comment.reply(botReplyFormat.format(comment.author,subredditName))
                        comment.delete()
    except Exception as moderationException:
        print("{}".format(moderationException))


if __name__ == "__main__":
    moderateComments(botInstance,botSubreddit)



            


