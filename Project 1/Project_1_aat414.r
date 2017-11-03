
library(ggplot2);
library(dplyr);
library(maps);
library(ggmap);
library(mongolite);
library(lubridate);
library(gridExtra);
library("data.table");

#Working with twitter data, importing the csv file to a dataframe in r
tweet_data <- data.table::fread("demonetization-tweets 2.csv")

#see what fields this dataframe has
colnames(tweet_data)

head(tweet_data,3)

#Since I am only working with dates, I strip the time factor from the "created" field, 
#and convert the datatype of the field to data format.
tweet_data$created <- as.Date(tweet_data$created, "%m/%d/%y")
head(tweet_data,3)

#estabish connection,create db and a collection named tweets inside
tweet_collection = mongo(collection = "tweets", db = "Twit_Sentiment_Analysis")

#just making sure the tweet_collection instance of tweets collection is empty before inserting
tweet_collection$remove('{}')
#insert tweet_data inside the collection
tweet_collection$insert(tweet_data)

#equivalent in SQL to select * from tweet_collection where ROWNUM=1
tweet_collection$iterate()$one()

# equivalent SQL query -> select text,created from tweet_collection LIMIT 5;
tweet_collection$find(fields='{"_id":false,"text":true,"created":true}',limit=5)

tweet_collection$aggregate('[{"$group": {"_id": "$created","count": {"$sum": 1}}}]')%>%
ggplot(aes(x=`_id`,y=count))+geom_bar(stat="identity",color='skyblue',fill='#b35900')+
geom_text(aes(label = count), color = "blue")+coord_flip()+xlab("Date")+ylab("Number of Tweets")

#getting the tweets from the mongo database into a dataframe and sorting them as per date using R's order() function
tweets_dates <- tweet_collection$find(fields='{"text":true,"created":true}')
tweets_dates<-tweets_dates[order(tweets_dates$created),]

head(tweets_dates,3)

#required packages
library('tm');

cleanText <- function(txt){
    txt.tweets <- VCorpus(VectorSource(txt))
    #lowercase
    txt.tweets <- tm_map(txt.tweets, content_transformer(tolower))
    # Remove numbers
    txt.tweets <- tm_map(txt.tweets, removeNumbers)
    #Remove english common words
    txt.tweets <- tm_map(txt.tweets, removeWords, stopwords("english"))
    #Remove punctuations
    txt.tweets <- tm_map(txt.tweets, removePunctuation)
    #Remove whitespaces
    txt.tweets<- tm_map(txt.tweets, stripWhitespace)
    
    #remove the word rt(retweet)
    txt.tweets<- tm_map(txt.tweets,content_transformer(function(x){return (gsub("rt","",x))}))

    
    return(txt.tweets)
}

tweet.txt_data <- cleanText(tweets_dates$text)
head(tweet.txt_data)

library('wordcloud');

#create a TermDocumentMatrix in order to generate the wordcloud
dtm <- TermDocumentMatrix(tweet.txt_data)
m <- as.matrix(dtm)
d <- data.frame(as.table(m))
head(d)

#Generating a word cloud
wordcloud(d$Terms,d$Freq,min.freq = 1,
          max.words=50, col=terrain.colors(length(d$Terms), alpha=0.9))

library("syuzhet");

sentiments <- get_sentiment(as.character(tweets_dates$text))

tweets_dates$sentiments <- sentiments

head(tweets_dates,2)

tweet_sentiments = mongo(collection = "tweets_sentiments", db = "Twit_Sentiment_Analysis")

tweet_sentiments$remove('{}')
tweet_sentiments$insert(tweets_dates)

tweet_sentiments$find('{"created":"2017-04-19"}','{"sentiments":true}',limit=5)

#group by each day and calculate the avg sentiment of tweets that day
tweet_sentiments$aggregate('[{"$group":{"_id":"$created","sentiments":{"$avg":"$sentiments"}}}]')

tweet_sentiments$aggregate('[{"$group":{"_id":"$created","sentiments":{"$avg":"$sentiments"}}}]')%>%
ggplot(aes(x=`_id`,y=sentiments,fill=sentiments))+scale_fill_gradient(low = "red", high = "green")+
geom_bar(stat="identity")+coord_flip()+xlab("Date")+ylab("Overall public Sentiment")
