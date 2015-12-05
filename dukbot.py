from slackbot.bot import respond_to
from slackbot.bot import Bot
from pprint import pprint

@respond_to('topreddit$')
@respond_to('topreddit (.*)')
def topreddit(message, sub='all'):
    import praw
    reddit = praw.Reddit('dukslack')
    submissions = reddit.get_subreddit(sub).get_hot(limit=5)
    res = ""
    for submission in submissions:
	    res += submission.title + ":\n" +  submission.url + "\n"
    message.reply(res)

@respond_to('talk')
def talk(message):
    message.reply("Beep boop");

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
