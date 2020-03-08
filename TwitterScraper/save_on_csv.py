#twitter scraper
import GetOldTweets3 as got
import pandas as pd


def username_tweets_to_csv(username, count):
    # Creation of query object
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                            .setMaxTweets(count)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    # Creating list of chosen tweet data
    user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    tweets_df = pd.DataFrame(user_tweets, columns = ['Datetime', 'Text'])

    # Converting dataframe to CSV
    tweets_df.to_csv('./{}-{}k-tweets.csv'.format(username, int(count/1000)), sep=',')

if __name__ == '__main__':
       user_name = input('Please write the twitter user name and press enter:')
       count = input('how many twitts do you want to get scraped? write only numbers and press enter:')
       username_tweets_to_csv(user_name,count)
       print('CSV file is saved.')