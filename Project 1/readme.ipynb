{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project in R and MongoDB\n",
    "### Name: Ajay Anil Thorve\n",
    "### Net ID: aat414\n",
    "### N number: N13008057\n",
    "### Course: Big Data Analytics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Project Description\n",
    "\n",
    "During the Demonetization phase in India November 2016- April 2017, I subscribe tweets from various days and analyze the top most topics trending during that time. I also compute sentiment analysis of overall tweets each day for 8 different days during this time period and observe if there was any shift in emotions towards the decision"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Technology Used\n",
    "\n",
    "1. R langauge for scripting.\n",
    "2. Mongodb for the backend.\n",
    "3. R's Mongolite package for connection of R to mongo\n",
    "4. SQL on ibm cloud\n",
    "5. RMySQL package\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Using the Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": false
   },
   "source": [
    "#### 1) Importing the required libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "library(ggplot2);\n",
    "library(dplyr);\n",
    "library(maps);\n",
    "library(ggmap);\n",
    "library(mongolite);\n",
    "library(lubridate);\n",
    "library(gridExtra);\n",
    "library(\"data.table\");"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The dataset:\n",
    "\n",
    "#### I decided to work on the tweets related to demonetization. Since the topic was trending on twitter for a lot of time when prime minister of India, Narendra Modi, announced the decision in November 2016, I decided to pull tweets during that period and do some week wise analysis on the reaction to this decision.\n",
    "\n",
    "<i>Since twitter does not allow to pull tweets which are more than 2 weeks old anymore(its a paid fearture). I tried researching on the internet if there are any tweets scrapped already. I found a dataset which consisted of some of the tweets during the November 2016 period, on this link: https://www.kaggle.com/arathee2/demonetization-in-india-twitter-data/downloads/demonetization-tweets.csv</i>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Working with twitter data, importing the csv file to a dataframe in r\n",
    "tweet_data <- data.table::fread(\"demonetization-tweets 2.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'V1'</li>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'text'</li>\n",
       "\t<li>'favorited'</li>\n",
       "\t<li>'favoriteCount'</li>\n",
       "\t<li>'replyToSN'</li>\n",
       "\t<li>'created'</li>\n",
       "\t<li>'truncated'</li>\n",
       "\t<li>'replyToSID'</li>\n",
       "\t<li>'id'</li>\n",
       "\t<li>'replyToUID'</li>\n",
       "\t<li>'statusSource'</li>\n",
       "\t<li>'screenName'</li>\n",
       "\t<li>'retweetCount'</li>\n",
       "\t<li>'isRetweet'</li>\n",
       "\t<li>'retweeted'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'V1'\n",
       "\\item 'X'\n",
       "\\item 'text'\n",
       "\\item 'favorited'\n",
       "\\item 'favoriteCount'\n",
       "\\item 'replyToSN'\n",
       "\\item 'created'\n",
       "\\item 'truncated'\n",
       "\\item 'replyToSID'\n",
       "\\item 'id'\n",
       "\\item 'replyToUID'\n",
       "\\item 'statusSource'\n",
       "\\item 'screenName'\n",
       "\\item 'retweetCount'\n",
       "\\item 'isRetweet'\n",
       "\\item 'retweeted'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'V1'\n",
       "2. 'X'\n",
       "3. 'text'\n",
       "4. 'favorited'\n",
       "5. 'favoriteCount'\n",
       "6. 'replyToSN'\n",
       "7. 'created'\n",
       "8. 'truncated'\n",
       "9. 'replyToSID'\n",
       "10. 'id'\n",
       "11. 'replyToUID'\n",
       "12. 'statusSource'\n",
       "13. 'screenName'\n",
       "14. 'retweetCount'\n",
       "15. 'isRetweet'\n",
       "16. 'retweeted'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       " [1] \"V1\"            \"X\"             \"text\"          \"favorited\"    \n",
       " [5] \"favoriteCount\" \"replyToSN\"     \"created\"       \"truncated\"    \n",
       " [9] \"replyToSID\"    \"id\"            \"replyToUID\"    \"statusSource\" \n",
       "[13] \"screenName\"    \"retweetCount\"  \"isRetweet\"     \"retweeted\"    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#see what fields this dataframe has\n",
    "colnames(tweet_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>V1</th><th scope=col>X</th><th scope=col>text</th><th scope=col>favorited</th><th scope=col>favoriteCount</th><th scope=col>replyToSN</th><th scope=col>created</th><th scope=col>truncated</th><th scope=col>replyToSID</th><th scope=col>id</th><th scope=col>replyToUID</th><th scope=col>statusSource</th><th scope=col>screenName</th><th scope=col>retweetCount</th><th scope=col>isRetweet</th><th scope=col>retweeted</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1                                                                                                                                                                                             </td><td>1                                                                                                                                                                                             </td><td><span style=white-space:pre-wrap>RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;amp;…  </span></td><td>FALSE                                                                                                                                                                                         </td><td>0                                                                                                                                                                                             </td><td>NA                                                                                                                                                                                            </td><td>11/23/16 18:40                                                                                                                                                                                </td><td>FALSE                                                                                                                                                                                         </td><td>NA                                                                                                                                                                                            </td><td>8.01496e+17                                                                                                                                                                                   </td><td>NA                                                                                                                                                                                            </td><td>&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;                                                                                          </td><td>HASHTAGFARZIWAL                                                                                                                                                                               </td><td>331                                                                                                                                                                                           </td><td>TRUE                                                                                                                                                                                          </td><td>FALSE                                                                                                                                                                                         </td></tr>\n",
       "\t<tr><td>2                                                                                                                                                                                         </td><td>2                                                                                                                                                                                         </td><td><span style=white-space:pre-wrap>RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                </span></td><td>FALSE                                                                                                                                                                                     </td><td>0                                                                                                                                                                                         </td><td>NA                                                                                                                                                                                        </td><td>11/23/16 18:40                                                                                                                                                                            </td><td>FALSE                                                                                                                                                                                     </td><td>NA                                                                                                                                                                                        </td><td>8.01496e+17                                                                                                                                                                               </td><td>NA                                                                                                                                                                                        </td><td>&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;                                                                                      </td><td>PRAMODKAUSHIK9                                                                                                                                                                            </td><td> 66                                                                                                                                                                                       </td><td>TRUE                                                                                                                                                                                      </td><td>FALSE                                                                                                                                                                                     </td></tr>\n",
       "\t<tr><td>3                                                                                                                                                 </td><td>3                                                                                                                                                 </td><td>RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th…</td><td>FALSE                                                                                                                                             </td><td>0                                                                                                                                                 </td><td>NA                                                                                                                                                </td><td>11/23/16 18:40                                                                                                                                    </td><td>FALSE                                                                                                                                             </td><td>NA                                                                                                                                                </td><td>8.01496e+17                                                                                                                                       </td><td>NA                                                                                                                                                </td><td>&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;                                              </td><td>rahulja13034944                                                                                                                                   </td><td> 12                                                                                                                                               </td><td>TRUE                                                                                                                                              </td><td>FALSE                                                                                                                                             </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|llllllllllllllll}\n",
       " V1 & X & text & favorited & favoriteCount & replyToSN & created & truncated & replyToSID & id & replyToUID & statusSource & screenName & retweetCount & isRetweet & retweeted\\\\\n",
       "\\hline\n",
       "\t 1                                                                                                                                                      & 1                                                                                                                                                      & RT @rssurjewala: Critical question: Was PayTM informed about \\#Demonetization edict by PM? It's clearly fishy and requires full disclosure \\&amp;…   & FALSE                                                                                                                                                  & 0                                                                                                                                                      & NA                                                                                                                                                     & 11/23/16 18:40                                                                                                                                         & FALSE                                                                                                                                                  & NA                                                                                                                                                     & 8.01496e+17                                                                                                                                            & NA                                                                                                                                                     & <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                               & HASHTAGFARZIWAL                                                                                                                                        & 331                                                                                                                                                    & TRUE                                                                                                                                                   & FALSE                                                                                                                                                 \\\\\n",
       "\t 2                                                                                                                                                      & 2                                                                                                                                                      & RT @Hemant\\_80: Did you vote on \\#Demonetization on Modi survey app?                                                                                 & FALSE                                                                                                                                                  & 0                                                                                                                                                      & NA                                                                                                                                                     & 11/23/16 18:40                                                                                                                                         & FALSE                                                                                                                                                  & NA                                                                                                                                                     & 8.01496e+17                                                                                                                                            & NA                                                                                                                                                     & <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                               & PRAMODKAUSHIK9                                                                                                                                         &  66                                                                                                                                                    & TRUE                                                                                                                                                   & FALSE                                                                                                                                                 \\\\\n",
       "\t 3                                                                                                                                                    & 3                                                                                                                                                    & RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste \\#Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th… & FALSE                                                                                                                                                & 0                                                                                                                                                    & NA                                                                                                                                                   & 11/23/16 18:40                                                                                                                                       & FALSE                                                                                                                                                & NA                                                                                                                                                   & 8.01496e+17                                                                                                                                          & NA                                                                                                                                                   & <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                             & rahulja13034944                                                                                                                                      &  12                                                                                                                                                  & TRUE                                                                                                                                                 & FALSE                                                                                                                                               \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "V1 | X | text | favorited | favoriteCount | replyToSN | created | truncated | replyToSID | id | replyToUID | statusSource | screenName | retweetCount | isRetweet | retweeted | \n",
       "|---|---|---|\n",
       "| 1                                                                                                                                                  | 1                                                                                                                                                  | RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…   | FALSE                                                                                                                                              | 0                                                                                                                                                  | NA                                                                                                                                                 | 11/23/16 18:40                                                                                                                                     | FALSE                                                                                                                                              | NA                                                                                                                                                 | 8.01496e+17                                                                                                                                        | NA                                                                                                                                                 | <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                           | HASHTAGFARZIWAL                                                                                                                                    | 331                                                                                                                                                | TRUE                                                                                                                                               | FALSE                                                                                                                                              | \n",
       "| 2                                                                                                                                                  | 2                                                                                                                                                  | RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                 | FALSE                                                                                                                                              | 0                                                                                                                                                  | NA                                                                                                                                                 | 11/23/16 18:40                                                                                                                                     | FALSE                                                                                                                                              | NA                                                                                                                                                 | 8.01496e+17                                                                                                                                        | NA                                                                                                                                                 | <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                           | PRAMODKAUSHIK9                                                                                                                                     |  66                                                                                                                                                | TRUE                                                                                                                                               | FALSE                                                                                                                                              | \n",
       "| 3                                                                                                                                                  | 3                                                                                                                                                  | RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th… | FALSE                                                                                                                                              | 0                                                                                                                                                  | NA                                                                                                                                                 | 11/23/16 18:40                                                                                                                                     | FALSE                                                                                                                                              | NA                                                                                                                                                 | 8.01496e+17                                                                                                                                        | NA                                                                                                                                                 | <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                           | rahulja13034944                                                                                                                                    |  12                                                                                                                                                | TRUE                                                                                                                                               | FALSE                                                                                                                                              | \n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "  V1 X\n",
       "1 1  1\n",
       "2 2  2\n",
       "3 3  3\n",
       "  text                                                                                                                                              \n",
       "1 RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…  \n",
       "2 RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                \n",
       "3 RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\\r\\r\\r\\rIf not for Aam Aadmi, listen to th…\n",
       "  favorited favoriteCount replyToSN created        truncated replyToSID\n",
       "1 FALSE     0             NA        11/23/16 18:40 FALSE     NA        \n",
       "2 FALSE     0             NA        11/23/16 18:40 FALSE     NA        \n",
       "3 FALSE     0             NA        11/23/16 18:40 FALSE     NA        \n",
       "  id          replyToUID\n",
       "1 8.01496e+17 NA        \n",
       "2 8.01496e+17 NA        \n",
       "3 8.01496e+17 NA        \n",
       "  statusSource                                                                            \n",
       "1 <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>\n",
       "2 <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>\n",
       "3 <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>\n",
       "  screenName      retweetCount isRetweet retweeted\n",
       "1 HASHTAGFARZIWAL 331          TRUE      FALSE    \n",
       "2 PRAMODKAUSHIK9   66          TRUE      FALSE    \n",
       "3 rahulja13034944  12          TRUE      FALSE    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(tweet_data,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>V1</th><th scope=col>X</th><th scope=col>text</th><th scope=col>favorited</th><th scope=col>favoriteCount</th><th scope=col>replyToSN</th><th scope=col>created</th><th scope=col>truncated</th><th scope=col>replyToSID</th><th scope=col>id</th><th scope=col>replyToUID</th><th scope=col>statusSource</th><th scope=col>screenName</th><th scope=col>retweetCount</th><th scope=col>isRetweet</th><th scope=col>retweeted</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1                                                                                                                                                                                             </td><td>1                                                                                                                                                                                             </td><td><span style=white-space:pre-wrap>RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;amp;…  </span></td><td>FALSE                                                                                                                                                                                         </td><td>0                                                                                                                                                                                             </td><td>NA                                                                                                                                                                                            </td><td>2016-11-23                                                                                                                                                                                    </td><td>FALSE                                                                                                                                                                                         </td><td>NA                                                                                                                                                                                            </td><td>8.01496e+17                                                                                                                                                                                   </td><td>NA                                                                                                                                                                                            </td><td>&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;                                                                                          </td><td>HASHTAGFARZIWAL                                                                                                                                                                               </td><td>331                                                                                                                                                                                           </td><td>TRUE                                                                                                                                                                                          </td><td>FALSE                                                                                                                                                                                         </td></tr>\n",
       "\t<tr><td>2                                                                                                                                                                                         </td><td>2                                                                                                                                                                                         </td><td><span style=white-space:pre-wrap>RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                </span></td><td>FALSE                                                                                                                                                                                     </td><td>0                                                                                                                                                                                         </td><td>NA                                                                                                                                                                                        </td><td>2016-11-23                                                                                                                                                                                </td><td>FALSE                                                                                                                                                                                     </td><td>NA                                                                                                                                                                                        </td><td>8.01496e+17                                                                                                                                                                               </td><td>NA                                                                                                                                                                                        </td><td>&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;                                                                                      </td><td>PRAMODKAUSHIK9                                                                                                                                                                            </td><td> 66                                                                                                                                                                                       </td><td>TRUE                                                                                                                                                                                      </td><td>FALSE                                                                                                                                                                                     </td></tr>\n",
       "\t<tr><td>3                                                                                                                                                 </td><td>3                                                                                                                                                 </td><td>RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th…</td><td>FALSE                                                                                                                                             </td><td>0                                                                                                                                                 </td><td>NA                                                                                                                                                </td><td>2016-11-23                                                                                                                                        </td><td>FALSE                                                                                                                                             </td><td>NA                                                                                                                                                </td><td>8.01496e+17                                                                                                                                       </td><td>NA                                                                                                                                                </td><td>&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;                                              </td><td>rahulja13034944                                                                                                                                   </td><td> 12                                                                                                                                               </td><td>TRUE                                                                                                                                              </td><td>FALSE                                                                                                                                             </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|llllllllllllllll}\n",
       " V1 & X & text & favorited & favoriteCount & replyToSN & created & truncated & replyToSID & id & replyToUID & statusSource & screenName & retweetCount & isRetweet & retweeted\\\\\n",
       "\\hline\n",
       "\t 1                                                                                                                                                      & 1                                                                                                                                                      & RT @rssurjewala: Critical question: Was PayTM informed about \\#Demonetization edict by PM? It's clearly fishy and requires full disclosure \\&amp;…   & FALSE                                                                                                                                                  & 0                                                                                                                                                      & NA                                                                                                                                                     & 2016-11-23                                                                                                                                             & FALSE                                                                                                                                                  & NA                                                                                                                                                     & 8.01496e+17                                                                                                                                            & NA                                                                                                                                                     & <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                               & HASHTAGFARZIWAL                                                                                                                                        & 331                                                                                                                                                    & TRUE                                                                                                                                                   & FALSE                                                                                                                                                 \\\\\n",
       "\t 2                                                                                                                                                      & 2                                                                                                                                                      & RT @Hemant\\_80: Did you vote on \\#Demonetization on Modi survey app?                                                                                 & FALSE                                                                                                                                                  & 0                                                                                                                                                      & NA                                                                                                                                                     & 2016-11-23                                                                                                                                             & FALSE                                                                                                                                                  & NA                                                                                                                                                     & 8.01496e+17                                                                                                                                            & NA                                                                                                                                                     & <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                               & PRAMODKAUSHIK9                                                                                                                                         &  66                                                                                                                                                    & TRUE                                                                                                                                                   & FALSE                                                                                                                                                 \\\\\n",
       "\t 3                                                                                                                                                    & 3                                                                                                                                                    & RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste \\#Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th… & FALSE                                                                                                                                                & 0                                                                                                                                                    & NA                                                                                                                                                   & 2016-11-23                                                                                                                                           & FALSE                                                                                                                                                & NA                                                                                                                                                   & 8.01496e+17                                                                                                                                          & NA                                                                                                                                                   & <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                             & rahulja13034944                                                                                                                                      &  12                                                                                                                                                  & TRUE                                                                                                                                                 & FALSE                                                                                                                                               \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "V1 | X | text | favorited | favoriteCount | replyToSN | created | truncated | replyToSID | id | replyToUID | statusSource | screenName | retweetCount | isRetweet | retweeted | \n",
       "|---|---|---|\n",
       "| 1                                                                                                                                                  | 1                                                                                                                                                  | RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…   | FALSE                                                                                                                                              | 0                                                                                                                                                  | NA                                                                                                                                                 | 2016-11-23                                                                                                                                         | FALSE                                                                                                                                              | NA                                                                                                                                                 | 8.01496e+17                                                                                                                                        | NA                                                                                                                                                 | <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                           | HASHTAGFARZIWAL                                                                                                                                    | 331                                                                                                                                                | TRUE                                                                                                                                               | FALSE                                                                                                                                              | \n",
       "| 2                                                                                                                                                  | 2                                                                                                                                                  | RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                 | FALSE                                                                                                                                              | 0                                                                                                                                                  | NA                                                                                                                                                 | 2016-11-23                                                                                                                                         | FALSE                                                                                                                                              | NA                                                                                                                                                 | 8.01496e+17                                                                                                                                        | NA                                                                                                                                                 | <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                           | PRAMODKAUSHIK9                                                                                                                                     |  66                                                                                                                                                | TRUE                                                                                                                                               | FALSE                                                                                                                                              | \n",
       "| 3                                                                                                                                                  | 3                                                                                                                                                  | RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th… | FALSE                                                                                                                                              | 0                                                                                                                                                  | NA                                                                                                                                                 | 2016-11-23                                                                                                                                         | FALSE                                                                                                                                              | NA                                                                                                                                                 | 8.01496e+17                                                                                                                                        | NA                                                                                                                                                 | <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>                                                           | rahulja13034944                                                                                                                                    |  12                                                                                                                                                | TRUE                                                                                                                                               | FALSE                                                                                                                                              | \n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "  V1 X\n",
       "1 1  1\n",
       "2 2  2\n",
       "3 3  3\n",
       "  text                                                                                                                                              \n",
       "1 RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…  \n",
       "2 RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                \n",
       "3 RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\\r\\r\\r\\rIf not for Aam Aadmi, listen to th…\n",
       "  favorited favoriteCount replyToSN created    truncated replyToSID id         \n",
       "1 FALSE     0             NA        2016-11-23 FALSE     NA         8.01496e+17\n",
       "2 FALSE     0             NA        2016-11-23 FALSE     NA         8.01496e+17\n",
       "3 FALSE     0             NA        2016-11-23 FALSE     NA         8.01496e+17\n",
       "  replyToUID\n",
       "1 NA        \n",
       "2 NA        \n",
       "3 NA        \n",
       "  statusSource                                                                            \n",
       "1 <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>\n",
       "2 <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>\n",
       "3 <a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>\n",
       "  screenName      retweetCount isRetweet retweeted\n",
       "1 HASHTAGFARZIWAL 331          TRUE      FALSE    \n",
       "2 PRAMODKAUSHIK9   66          TRUE      FALSE    \n",
       "3 rahulja13034944  12          TRUE      FALSE    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Since I am only working with dates, I strip the time factor from the \"created\" field, \n",
    "#and convert the datatype of the field to data format.\n",
    "tweet_data$created <- as.Date(tweet_data$created, \"%m/%d/%y\")\n",
    "head(tweet_data,3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Making a connection with mongodb database"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<i>I am using the R package \"mongolite\"</i>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#estabish connection,create db and a collection named tweets inside\n",
    "tweet_collection = mongo(collection = \"tweets\", db = \"Twit_Sentiment_Analysis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "List of 5\n",
       " $ nInserted  : num 14940\n",
       " $ nMatched   : num 0\n",
       " $ nRemoved   : num 0\n",
       " $ nUpserted  : num 0\n",
       " $ writeErrors: list()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#just making sure the tweet_collection instance of tweets collection is empty before inserting\n",
    "tweet_collection$remove('{}')\n",
    "#insert tweet_data inside the collection\n",
    "tweet_collection$insert(tweet_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Making a connection with SQL database on ibm cloud"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>conn <- dbConnect(dbDriver('MySQL'),host='localhost',user='aat414',password='aat414123',dbname='aat414')</b>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<i>#create a table demontization</i> <br>\n",
    "<b>loadDataQuery <- \"LOAD DATA LOCAL INFILE \n",
    "'/home/2017/fall/nyu/cs9223/aat414/R- midterm/1.csv' \n",
    "INTO TABLE tweet_collection FIELDS TERMINATED BY ',' ENCLOSED BY '\\\"' LINES TERMINATED BY '\\\\n' IGNORE 1 ROWS”</b>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Performing a query and retrieving data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<dl>\n",
       "\t<dt>$V1</dt>\n",
       "\t\t<dd>1</dd>\n",
       "\t<dt>$X</dt>\n",
       "\t\t<dd>1</dd>\n",
       "\t<dt>$text</dt>\n",
       "\t\t<dd>'RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It\\'s clearly fishy and requires full disclosure &amp;amp;…'</dd>\n",
       "\t<dt>$favorited</dt>\n",
       "\t\t<dd>FALSE</dd>\n",
       "\t<dt>$favoriteCount</dt>\n",
       "\t\t<dd>0</dd>\n",
       "\t<dt>$created</dt>\n",
       "\t\t<dd>'2016-11-23'</dd>\n",
       "\t<dt>$truncated</dt>\n",
       "\t\t<dd>FALSE</dd>\n",
       "\t<dt>$id</dt>\n",
       "\t\t<dd>8.01496e+17</dd>\n",
       "\t<dt>$statusSource</dt>\n",
       "\t\t<dd>'&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;'</dd>\n",
       "\t<dt>$screenName</dt>\n",
       "\t\t<dd>'HASHTAGFARZIWAL'</dd>\n",
       "\t<dt>$retweetCount</dt>\n",
       "\t\t<dd>331</dd>\n",
       "\t<dt>$isRetweet</dt>\n",
       "\t\t<dd>TRUE</dd>\n",
       "\t<dt>$retweeted</dt>\n",
       "\t\t<dd>FALSE</dd>\n",
       "</dl>\n"
      ],
      "text/latex": [
       "\\begin{description}\n",
       "\\item[\\$V1] 1\n",
       "\\item[\\$X] 1\n",
       "\\item[\\$text] 'RT @rssurjewala: Critical question: Was PayTM informed about \\#Demonetization edict by PM? It\\textbackslash{}'s clearly fishy and requires full disclosure \\&amp;…'\n",
       "\\item[\\$favorited] FALSE\n",
       "\\item[\\$favoriteCount] 0\n",
       "\\item[\\$created] '2016-11-23'\n",
       "\\item[\\$truncated] FALSE\n",
       "\\item[\\$id] 8.01496e+17\n",
       "\\item[\\$statusSource] '<a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\">Twitter for Android</a>'\n",
       "\\item[\\$screenName] 'HASHTAGFARZIWAL'\n",
       "\\item[\\$retweetCount] 331\n",
       "\\item[\\$isRetweet] TRUE\n",
       "\\item[\\$retweeted] FALSE\n",
       "\\end{description}\n"
      ],
      "text/markdown": [
       "$V1\n",
       ":   1\n",
       "$X\n",
       ":   1\n",
       "$text\n",
       ":   'RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It\\'s clearly fishy and requires full disclosure &amp;amp;…'\n",
       "$favorited\n",
       ":   FALSE\n",
       "$favoriteCount\n",
       ":   0\n",
       "$created\n",
       ":   '2016-11-23'\n",
       "$truncated\n",
       ":   FALSE\n",
       "$id\n",
       ":   8.01496e+17\n",
       "$statusSource\n",
       ":   '&lt;a href=\"\"http://twitter.com/download/android\"\" rel=\"\"nofollow\"\"&gt;Twitter for Android&lt;/a&gt;'\n",
       "$screenName\n",
       ":   'HASHTAGFARZIWAL'\n",
       "$retweetCount\n",
       ":   331\n",
       "$isRetweet\n",
       ":   TRUE\n",
       "$retweeted\n",
       ":   FALSE\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "$V1\n",
       "[1] 1\n",
       "\n",
       "$X\n",
       "[1] 1\n",
       "\n",
       "$text\n",
       "[1] \"RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…\"\n",
       "\n",
       "$favorited\n",
       "[1] FALSE\n",
       "\n",
       "$favoriteCount\n",
       "[1] 0\n",
       "\n",
       "$created\n",
       "[1] \"2016-11-23\"\n",
       "\n",
       "$truncated\n",
       "[1] FALSE\n",
       "\n",
       "$id\n",
       "[1] 8.01496e+17\n",
       "\n",
       "$statusSource\n",
       "[1] \"<a href=\\\"\\\"http://twitter.com/download/android\\\"\\\" rel=\\\"\\\"nofollow\\\"\\\">Twitter for Android</a>\"\n",
       "\n",
       "$screenName\n",
       "[1] \"HASHTAGFARZIWAL\"\n",
       "\n",
       "$retweetCount\n",
       "[1] 331\n",
       "\n",
       "$isRetweet\n",
       "[1] TRUE\n",
       "\n",
       "$retweeted\n",
       "[1] FALSE\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#equivalent in SQL to select * from tweet_collection where ROWNUM=1\n",
    "tweet_collection$iterate()$one()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>text</th><th scope=col>created</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td><span style=white-space:pre-wrap>RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;amp;…  </span></td><td>2016-11-23                                                                                                                                                                                    </td></tr>\n",
       "\t<tr><td>RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                </td><td>2016-11-23                                                                                                                                        </td></tr>\n",
       "\t<tr><td>RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th…</td><td>2016-11-23                                                                                                                                        </td></tr>\n",
       "\t<tr><td>RT @ANI_news: Gurugram (Haryana): Post office employees provide cash exchange to patients in hospitals #demonetization https://t.co/uGMxUP9…      </td><td>2016-11-23                                                                                                                                        </td></tr>\n",
       "\t<tr><td>RT @satishacharya: Reddy Wedding! @mail_today cartoon #demonetization #ReddyWedding https://t.co/u7gLNrq31F                                       </td><td>2016-11-23                                                                                                                                        </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|ll}\n",
       " text & created\\\\\n",
       "\\hline\n",
       "\t RT @rssurjewala: Critical question: Was PayTM informed about \\#Demonetization edict by PM? It's clearly fishy and requires full disclosure \\&amp;…   & 2016-11-23                                                                                                                                            \\\\\n",
       "\t RT @Hemant\\_80: Did you vote on \\#Demonetization on Modi survey app?                                                                                 & 2016-11-23                                                                                                                                            \\\\\n",
       "\t RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste \\#Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th… & 2016-11-23                                                                                                                                          \\\\\n",
       "\t RT @ANI\\_news: Gurugram (Haryana): Post office employees provide cash exchange to patients in hospitals \\#demonetization https://t.co/uGMxUP9…       & 2016-11-23                                                                                                                                            \\\\\n",
       "\t RT @satishacharya: Reddy Wedding! @mail\\_today cartoon \\#demonetization \\#ReddyWedding https://t.co/u7gLNrq31F                                        & 2016-11-23                                                                                                                                              \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "text | created | \n",
       "|---|---|---|---|---|\n",
       "| RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…   | 2016-11-23                                                                                                                                         | \n",
       "| RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                 | 2016-11-23                                                                                                                                         | \n",
       "| RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\r",
       "\r",
       "\r",
       "\r",
       "If not for Aam Aadmi, listen to th… | 2016-11-23                                                                                                                                         | \n",
       "| RT @ANI_news: Gurugram (Haryana): Post office employees provide cash exchange to patients in hospitals #demonetization https://t.co/uGMxUP9…       | 2016-11-23                                                                                                                                         | \n",
       "| RT @satishacharya: Reddy Wedding! @mail_today cartoon #demonetization #ReddyWedding https://t.co/u7gLNrq31F                                        | 2016-11-23                                                                                                                                         | \n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "  text                                                                                                                                              \n",
       "1 RT @rssurjewala: Critical question: Was PayTM informed about #Demonetization edict by PM? It's clearly fishy and requires full disclosure &amp;…  \n",
       "2 RT @Hemant_80: Did you vote on #Demonetization on Modi survey app?                                                                                \n",
       "3 RT @roshankar: Former FinSec, RBI Dy Governor, CBDT Chair + Harvard Professor lambaste #Demonetization.\\r\\r\\r\\rIf not for Aam Aadmi, listen to th…\n",
       "4 RT @ANI_news: Gurugram (Haryana): Post office employees provide cash exchange to patients in hospitals #demonetization https://t.co/uGMxUP9…      \n",
       "5 RT @satishacharya: Reddy Wedding! @mail_today cartoon #demonetization #ReddyWedding https://t.co/u7gLNrq31F                                       \n",
       "  created   \n",
       "1 2016-11-23\n",
       "2 2016-11-23\n",
       "3 2016-11-23\n",
       "4 2016-11-23\n",
       "5 2016-11-23"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# equivalent SQL query -> select text,created from tweet_collection LIMIT 5;\n",
    "tweet_collection$find(fields='{\"_id\":false,\"text\":true,\"created\":true}',limit=5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### I want to group the tweets as per day; aggregate in mongo (similar to groupby in sql) may help achieve that!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Using monoglite helps process big amounts of data directly from the datastore, without the need to load it in a dataframe in R, which might slow down the process. Below, I process a query and direclty plot it, without storing it in a dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAYAAAD958/bAAAEDWlDQ1BJQ0MgUHJvZmlsZQAA\nOI2NVV1oHFUUPrtzZyMkzlNsNIV0qD8NJQ2TVjShtLp/3d02bpZJNtoi6GT27s6Yyc44M7v9\noU9FUHwx6psUxL+3gCAo9Q/bPrQvlQol2tQgKD60+INQ6Ium65k7M5lpurHeZe58853vnnvu\nuWfvBei5qliWkRQBFpquLRcy4nOHj4g9K5CEh6AXBqFXUR0rXalMAjZPC3e1W99Dwntf2dXd\n/p+tt0YdFSBxH2Kz5qgLiI8B8KdVy3YBevqRHz/qWh72Yui3MUDEL3q44WPXw3M+fo1pZuQs\n4tOIBVVTaoiXEI/MxfhGDPsxsNZfoE1q66ro5aJim3XdoLFw72H+n23BaIXzbcOnz5mfPoTv\nYVz7KzUl5+FRxEuqkp9G/Ajia219thzg25abkRE/BpDc3pqvphHvRFys2weqvp+krbWKIX7n\nhDbzLOItiM8358pTwdirqpPFnMF2xLc1WvLyOwTAibpbmvHHcvttU57y5+XqNZrLe3lE/Pq8\neUj2fXKfOe3pfOjzhJYtB/yll5SDFcSDiH+hRkH25+L+sdxKEAMZahrlSX8ukqMOWy/jXW2m\n6M9LDBc31B9LFuv6gVKg/0Szi3KAr1kGq1GMjU/aLbnq6/lRxc4XfJ98hTargX++DbMJBSiY\nMIe9Ck1YAxFkKEAG3xbYaKmDDgYyFK0UGYpfoWYXG+fAPPI6tJnNwb7ClP7IyF+D+bjOtCpk\nhz6CFrIa/I6sFtNl8auFXGMTP34sNwI/JhkgEtmDz14ySfaRcTIBInmKPE32kxyyE2Tv+thK\nbEVePDfW/byMM1Kmm0XdObS7oGD/MypMXFPXrCwOtoYjyyn7BV29/MZfsVzpLDdRtuIZnbpX\nzvlf+ev8MvYr/Gqk4H/kV/G3csdazLuyTMPsbFhzd1UabQbjFvDRmcWJxR3zcfHkVw9GfpbJ\nmeev9F08WW8uDkaslwX6avlWGU6NRKz0g/SHtCy9J30o/ca9zX3Kfc19zn3BXQKRO8ud477h\nLnAfc1/G9mrzGlrfexZ5GLdn6ZZrrEohI2wVHhZywjbhUWEy8icMCGNCUdiBlq3r+xafL549\nHQ5jH+an+1y+LlYBifuxAvRN/lVVVOlwlCkdVm9NOL5BE4wkQ2SMlDZU97hX86EilU/lUmkQ\nUztTE6mx1EEPh7OmdqBtAvv8HdWpbrJS6tJj3n0CWdM6busNzRV3S9KTYhqvNiqWmuroiKgY\nhshMjmhTh9ptWhsF7970j/SbMrsPE1suR5z7DMC+P/Hs+y7ijrQAlhyAgccjbhjPygfeBTjz\nhNqy28EdkUh8C+DU9+z2v/oyeH791OncxHOs5y2AtTc7nb/f73TWPkD/qwBnjX8BoJ98VVBg\n/m8AAEAASURBVHgB7N0HmFRVmvDxt3PTiaabnCQpIEoQkCSDukYEdQQMMwZGdMdZdXHcb3ZR\nR0ZHBAYF1HFwEAdEVleCCQcV0F0GBhREQSWIIklybDqH6u7vvqe5Zd1ONE11V7j/8zzVVTee\nc363qrreOqEiSq0kJAQQQAABBBBAAAEEEEAAAYnEAAEEEEAAAQQQQAABBBBAoEyAAIlnAgII\nIIAAAggggAACCCBwSoAAiacCAggggAACCCCAAAIIIHBKgACJpwICCCCAAAIIIIAAAgggcEqA\nAImnAgIIIIAAAggggAACCCBwSoAAiacCAggggAACCCCAAAIIIHBKgACJpwICCCCAAAIIIIAA\nAgggcEqAAImnAgIIIIAAAggggAACCCBwSiAaifAROHz4cMAqExsbKwkJCZKTkyNFRUUBK0cg\nMm7QoIF4PB5X1jsuLk6ysrKkuLg4EPQByzMpKUlyc3OlpKQkYGUIRMZa7+joaMnIyAhE9gHN\nMyUlRTIzMwNahkBk3rBhQ/M819e5m1JERITo892N9dZrrv/H9f+5m5K+t+lnGX1vd1PSeutz\nPT8/39zCve5RUVGSnp5+2moSIJ2WKHR2COSHVP1nYr+xBLIcgbhaWndNbqt3ZGSkueYaJLit\n7voG68Z62x8g3Ha99fUdExPjuue5XW83Ptf1fV2f7257rtvv61pvt9Vd39f15sZ66+e3goIC\n19Vd3+OqSnSxq0qG9QgggAACCCCAAAIIIOA6AQIk111yKowAAggggAACCCCAAAJVCRAgVSXD\negQQQAABBBBAAAEEEHCdAAGS6y45FUYAAQQQQAABBBBAAIGqBAiQqpJhPQIIIIAAAggggAAC\nCLhOgADJdZecCiOAAAIIIIAAAggggEBVAkzzXZUM689IYH9usfz1+8NS5CmW0tIzOjTodtZZ\nuy9tLNIxMeiKRoEQQAABBBBAAAEE6liAAKmOgd1y+gN5JXI8v1gi8zIksigvZKtdGhUrxYnp\nss+qAgFSyF5GCo4AAggggAACCNRagACp1nQcWJlAy4/+IKnfvFPZppBYl9Omr+z81VshUVYK\niQACCCCAAAIIIOB/AcYg+d+UMyKAAAIIIIAAAggggECIChAgheiFo9gIIIAAAggggAACCCDg\nfwECJP+bckYEEEAAAQQQQAABBBAIUQECpBC9cBQbAQQQQAABBBBAAAEE/C9AgOR/U86IAAII\nIIAAAggggAACISpAgBSiF45iI4AAAggggAACCCCAgP8FCJD8b8oZEUAAAQQQQAABBBBAIEQF\nCJBC9MJRbAQQQAABBBBAAAEEEPC/AAGS/005IwIIIIAAAggggAACCISoAAFSiF44io0AAggg\ngAACCCCAAAL+FyBA8r8pZ0QAAQQQQAABBBBAAIEQFSBACtELR7ERQAABBBBAAAEEEEDA/wIE\nSP435YwIIIAAAggggAACCCAQogIESCF64Sg2AggggAACCCCAAAII+F+AAMn/ppwRAQQQQAAB\nBBBAAAEEQlSAAClELxzFRgABBBBAAAEEEEAAAf8LECD535QzIoAAAggggAACCCCAQIgKECCF\n6IWj2AgggAACCCCAAAIIIOB/AQIk/5tyxiAWOJTbQTIKmlVbwuN7oqSwoNpdJDMzQjZvjpYj\nR3gJVS/FVgQQQAABBBBAILQEooOluPv375dVq1ZJVFSUDBw4UFq2bOko2p49e2TNmjWSlpZm\nticlJTm22wsrV66U5ORk6dWrl1l1+PBh2bBhg73Zcd+pUyfp2LGjY53vQlZWlqxevVr0vl+/\nftK2bVvfzY7HCxcuNHnqOatLJSUl8s0338jGjRulWbNmctlll0lcXFyFQ/bt22fqO2rUqArb\nWFE7gW0nLpGJ6z+RK9u+KLd3/g/HSUpKI2TB9xPl0zW3y4nZTWVOdKlcNzRfpk/PkAYNftp1\nx44oefTRhrJy5U/XrHPnEpk6NUcuuuin/XiEAAIIIIAAAgggEJoCQfH19+OPPy6jR4+W7777\nTj744AO544475NNPP/WKzps3z6zbsmWLLFiwQH7zm9/IiRMnvNvtBxp0jB8/XnQ/O2lgNWvW\nLMftpZdekgkTJsj69evt3Src79y5U2644QZZtGiRbNq0Se6++2757LPPKuynK95//3154YUX\nZPv27ZVut1cePXpUbrrpJpk4caJoAPSXv/zF1DszM9PexdxnZ2fLuHHjZOnSpY71LNReIM+T\n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\nMwQQQAABBBBAAAEEEAhmgehgLhxlCz2B7A6DpTg+JfQKfhYlLm7Q6CyO5lAEEEAAAQQQQACB\nYBIgQAqmqxHCZYmOiDClz+gxUvTmxhRdRuDGqlNnBBBAAAEEEEAgbAQIkMLmUga2IhekRklq\ncqpkZudIUWFRYAtTz7nHx8dLSXGxNI92V73rmZnsEEAAAQQQQACBehEgQKoX5vDPJCoyQro3\naiAZ0QWSl+euQCE5OUaKrCrn57ur3uH/rKaGCCCAAAIIIOBGASZpcONVp84IIIAAAggggAAC\nCCBQqQABUqUsrEQAAQQQQAABBBBAAAE3CtDFzo1XvQ7qnFdcKut/zJKc3CIp8tRBBkF8yrjs\nAikuKRbPGdZb53TonCSSFhvElaNoCCCAAAIIIICAywQIkFx2weuqut+eLJZl+/Lq6vRBft7C\nWpcvywqqrmpa68M5EAEEEEAAAQQQQMDPAgRIfgZ16+lKSktN1RuvniFJO/7pVoYa17sopYXs\nu2GqnGKr8XHsiAACCCCAAAIIIFC3AgRIdevrurPHH94mSTsJkE534QvS2p1uF7YjgAACCCCA\nAAIIBECASRoCgE6WCCCAAAIIIIAAAgggEJwCBEjBeV0oFQIIIIAAAggggAACCARAgAApAOhk\niQACCCCAAAIIIIAAAsEpQIAUnNeFUiGAAAIIIIAAAggggEAABAiQAoBOlggggAACCCCAAAII\nIBCcAgRIwXldKBUCCCCAAAIIIIAAAggEQIAAKQDoZIkAAggggAACCCCAAALBKUCAFJzXhVIh\ngAACCCCAAAIIIIBAAAQIkAKATpYIIIAAAggggAACCCAQnAIESMF5XSgVAggggAACCCCAAAII\nBECAACkA6GSJAAIIIIAAAggggAACwSlAgBSc14VSIYAAAggggAACCCCAQAAECJACgE6WCCCA\nAAIIIIAAAgggEJwCBEjBeV0oFQIIIIAAAggggAACCARAgAApAOhkiQACCCCAAAIIIIAAAsEp\nQIAUnNeFUiGAAAIIIIAAAggggEAABAiQAoBOlggggAACCCCAAAIIIBCcAgRIwXldKFWICuR7\nEmVP1oWSW5RSoxrs3R4tx45FnHbfb7+t2X6nPRE7IIAAAggggAACCFQrQIBULQ8bEaiZwPH8\nVjJx/cfy6/87Lr//7Eu5b8VRmbV5lnhKoqs8wY7P4mT8zY3lH/+Iq3If3fC//xsn//Ivp9+v\n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\nYmJkwIABdqhw72W0VmrFihWSnp5u56ekpHjP9rxevny5pKamyimnnGKn7du3T7TWy1/q0qWL\ndO7c2d8sO+3IkSPy8ccfiz7369ev0pvjauY333zTblPXGUjauXOnLU95K91edna2zypOPPFE\nadeunc803vw8gdyiVPnHuplSKhVbme442l1e/Xqq9Gy6WPoN2S77uo6Qb+amyFVXNTEjNR6U\nXr3KgqTs7Ci59tp0OXw4Rv7whzw577yjsnJlA5kxI8mM6pguixfvly5din/ejrI0AggggAAC\nCCCAQL0KBBQgad+iBx980O5Yt27d7I1i//KXv9Tajo4dO1Y+++wzGThwoHz//ffy/PPPy/jx\n4+0w4rqR1157zZx0zpAzzzxTNJDS91OnTq1QS7V69WoZN26c3HTTTZ4ASQOrF1980Wdfi4qK\n5ODBg3L77bdXGiDpftx444124Ik2bdrICy+8YPepf//+PuvSN++++67dn4ceesicEFcfIB09\netSOAhgfH+8TTBYXF9v91wBPg00n/e53vyNAcjBq6XnWxmektLRicKSrn/vteEmIPSK//8XV\ncqTL9ZL2q3y5tGexXDe0mQmQEjwB0sKFCebzGmtqkPLlrrtyTbPSQvO5K5SOprbpuuvS5dVX\nk+Wvf82qpT1mNQgggAACCCCAAAL1IXDsLDzArV155ZVV5iwtLZX//ve/NtipMuOPMzdt2iRa\n66M1MM2bN7dT9WazGgDpfZY0wNEmfk8//bRo0z0Nbm655RZ7ryV91qTTNGjSR1RUlJ3m/Nen\nTx956623nLf2+cknnxQdlnzYsGE+073fTJw4US6++GIZM2aMXeesWbPkqaeektmzZ/tsY8eO\nHXZo80BH79NAcNKkSZKRkWFOpDt6b1J++OEH29frpZdekiZNmvjM403tCXy6Z4R8smek3PPL\nITLpy8U+KzYfXzmn3T/sI9EESUd+nNuhS5EZhKRU9u2L8eSPjS2Vc8/Nk5EjfWuJzjgj39SE\nlprP7rG8noV4gQACCCCAAAIIIBDSAv4voVezyy+//LL07t3b1mq0bNlS9NGiRQt7Uq+1Ir/6\n1a+qWcOx2YcPH7Y1NU5wpHO0edyePXvMFf5SOyBE69atbXCk87Rm5fzzz5clS5boW5t0YIgF\nCxbIY489Vm1NiwZGWuOjNU0JCQnOKnyetXZp48aNNoByAq6LLrrI1l5t2LDBk1cDs0cffdTU\nFlxnB6Rw8noylHuhTfW0Jk5H/bvqqqvKzRU7ZHrTpk0JjirI1N6EQ3ltZObGZ2VYp8ekc6PP\nK6xY4+tepmmdPpxUUiTyxoxkKSyMMp+9PGeyXHppnqklOmyaXpqoyistXpwgxcVR0q2bWZCE\nAAIIIIAAAgggEFYCNa5B0n5Cv/3tb21fIe2Xo31mNFjSUev0nkjR0dG2iVygCtpkrXyztaVL\nl4r2u9GAY/fu3aJN3LyTBkx67yW9Sa1u7/TTT5chQ4bY4Om5557zzurzOj8/Xx5//HFzxX+k\nOXnt5jPP+40GZ5p0O07SGp0GDRqYGoR90r17dztZa5WSkpLksssus7VcTt7KnhMTE2Xu3Lk2\nANKb7JZPmzdvtv2ntIZLXbU/16hRo/wGnIsWLbJNHZ11aLCngVqwUmyhBgNlfXOCtQ/VbVdr\nh14w/Y5aJH0nwzpOkIKSxOoWkdn/N1K++lsLKciOliefzDN9i/Q+X773+tLPhfad01rEnByR\nf/wjUZKTS+V3v4uyx7PajYRpBi23puTkZM8No8O0KDXebT3eWm69iOOmpOXWpM2A3Zb075Fb\ny61/Z91YdjeW27nQq3/P3HbM9XjrRXi3ldv5XdcKDuf4R/Lvu8YOgaQaB0j//ve/bVCifXR0\nJDsNFq644gp7byQ9wT/nnHPsyWIgG/eXZ86cObJmzRrb50fna7DSsGFDn6z64dUCZmZm2iAi\n0OZoy5Yts4HV5Zdf7rO+8m80KNMPij68k25Xa7w0rVu3zt7zSWvTAv1A6Revqn395ptv5NCh\nQ3LCCSfYgSg0CNJ+TdokT5sbeicdLOPtt9/2TFKj2267zfO+vl/EHdGBJXLre7M12t6ibX+U\nzZn9ZHz/PhITbZrFVfMd0XPfgsIG0vKEQtm+qoEJbhPk7LNNDVMv/5vNNcUfPVrkq6/E3EhZ\nzHcj2X/GCJuqFwncmLz7Cbqt/JUNkhPpDm4tt/6Nc2vZ3Vpu/X1za9kD7TIRab93etHTufAZ\naWXzLo9z2yLvaf5e1zhA+u677+zJujPMtzaH+/TTT+26dYCCv/3tb7bfjg6UUNOkwcbrr78u\nEyZMsDee1eX1g6pN2byT876mJ2batE4HevAOUjQY0+Z0TtLaMH/b1Pk6iIJuM8dUE2jTOu2f\n1KxZM2dRz7MGOe+//77nvTYfPFvPrKtJDz/8sA38nCHStWZNg04NGssHSDfffLOtuXJWqT9m\n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\nChAg1RCMzRFAAAEEEEAAAQQQQCB+BQiQ4rduKRkCCCCAAAIIIIAAAgjUUIAAqYZgbI4AAggg\ngAACCCCAAALxK0CAFL91S8kQQAABBBBAAAEEEECghgIESDUEY3MEEEAAAQQQQAABBBCIXwEC\npPitW0qGAAIIIIAAAggggAACNRRIruH2bI5AtQIlObtJUavu1W7DSgQQQACB2guUpeXUfmf2\nRAABBBBwFSBAciVig3AEEn7faP2w60RvJAQQQACB+hVw3nfr9yjkjgACCHhPgADJe3VeLyXu\n3iRJtpanSEHRTikrK6uXY8RqpikpKVJeXu7JcienJEtRYZH4fL5YrZ56Oa/UtFQpKS7xXLnT\n0tIkMSlRCgsK68U1ljNNT0+XoqKimDnFLPPpncMneMzUByeCAALxJcDba3zVZ9RKk5OSKCfv\n2VS2bt0qhYXe+vKUk5MuJSUl5suTtwLDJk0yJCsrS3Jzc6W0tDRqr71oHLhFi2zZtm2b54Li\nli2zJTU1Vdau9db/uL7G2rRpIhs2xE6AFI3XPcdEAAEEvCLAJA1eqWnKiQACCCCAAAIIIIAA\nAq4CBEiuRGyAAAIIIIAAAggggAACXhEgQPJKTVNOBBBAAAEEEEAAAQQQcBUgQHIlYgMEEEAA\nAQQQQAABBBDwigABkldqmnIigAACCCCAAAIIIICAqwABkisRGyCAAAIIIIAAAggggIBXBBLM\n9Uu8dQGTOK5ZnXY4WmnZsmUyf/58+dOf/iQdO3aM1mlE5biJiYn2ejhe+1f6/vvvZenSpXLo\noYdKs2bNomIfrYMmJSV5bopvtf70009l06ZNcuKJJ0pCgrcuU5qcnOy56ey1zt955x3R618d\nfvjh+tRTyYt1rtf6mjVrlrRr104OOOAAT9W3vqfp57nXruW4YcMGmTNnjvTq1Ut69uwZ93Wu\ndZyTk+NaTq6D5ErUeDZo2rRp1E72hx9+kNtuu03uvvtu6du3b9TOgwM3nMDs2bPlxRdftB+i\nnTp1argDc6SoCUyfPl2+/vprOfPMM0W/PJLiX+C+++6Tli1byogRI+K/sJTQXgxZP8uPPPJI\nGTZsGCIeEFiwYIH9/jZ+/Hg58MADPVDi8IpIF7vwnNgKAQQQQAABBBBAAAEEPCBAgOSBSqaI\nCCCAAAIIIIAAAgggEJ4AAVJ4TmyFAAIIIIAAAggggAACHhBgkgYPVHJDFHH79u2Sm5srbdu2\n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\nQAABBKIh8P/Sx/tpf8xOMgAAAABJRU5ErkJggg==",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# equivalent to SQL query: select count(*) from tweet_collection group by created;\n",
    "\n",
    "tweet_collection$aggregate('[{\"$group\": {\"_id\": \"$created\",\"count\": {\"$sum\": 1}}}]')%>%\n",
    "ggplot(aes(x=`_id`,y=count))+geom_bar(stat=\"identity\",color='skyblue',fill='#b35900')+\n",
    "geom_text(aes(label = count), color = \"blue\")+coord_flip()+xlab(\"Date\")+ylab(\"Number of Tweets\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that I have tweets group by each day, I can perform sentiment analysis for each day and see how it changed over the days"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "But before that, lets see what the top terms used in tweets were. We will generate a wordcloud to show the top 50 words.\n",
    "\n",
    "<br>\n",
    "\n",
    "Let us clean the text first"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#getting the tweets from the mongo database into a dataframe and sorting them as per date using R's order() function\n",
    "tweets_dates <- tweet_collection$find(fields='{\"text\":true,\"created\":true}')\n",
    "tweets_dates<-tweets_dates[order(tweets_dates$created),]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th></th><th scope=col>_id</th><th scope=col>text</th><th scope=col>created</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>5215</th><td>59e8dda1c553ce84b80a6792                                                                                                                                                                                                                                                                                                                                                                                                                                                       </td><td>RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.&lt;U+092D&gt;&lt;U+093E&gt;&lt;U+0935&gt;&lt;U+0941&gt;&lt;U+0915&gt;\"\" &lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00A9&gt;&lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00A5&gt;&lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00A2&gt;&lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00AD&gt;#demonetization https://t.co/ObQrhlNSL6</td><td>2016-11-22                                                                                                                                                                                                                                                                                                                                                                                                                                                                     </td></tr>\n",
       "\t<tr><th scope=row>5216</th><td>59e8dda1c553ce84b80a6793                                                                                                                                                                                                                                                                         </td><td>RT @ippatel: Retaining all seats of LS and state in Byelection by BJP has proved the people's support on #DeMonetization. It should be abov…                                                                                                                                                     </td><td>2016-11-22                                                                                                                                                                                                                                                                                       </td></tr>\n",
       "\t<tr><th scope=row>5217</th><td>59e8dda1c553ce84b80a6794                                                                                                                                                                                                                                                                                                                                                                                                                                                       </td><td>RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.&lt;U+092D&gt;&lt;U+093E&gt;&lt;U+0935&gt;&lt;U+0941&gt;&lt;U+0915&gt;\"\" &lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00A9&gt;&lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00A5&gt;&lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00A2&gt;&lt;ed&gt;&lt;U+00A0&gt;&lt;U+00BD&gt;&lt;ed&gt;&lt;U+00B8&gt;&lt;U+00AD&gt;#demonetization https://t.co/ObQrhlNSL6</td><td>2016-11-22                                                                                                                                                                                                                                                                                                                                                                                                                                                                     </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lll}\n",
       "  & \\_id & text & created\\\\\n",
       "\\hline\n",
       "\t5215 & 59e8dda1c553ce84b80a6792                                                                                                                                                                                                                                                                            & RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.<U+092D><U+093E><U+0935><U+0941><U+0915>\"\" <ed><U+00A0><U+00BD><ed><U+00B8><U+00A9><ed><U+00A0><U+00BD><ed><U+00B8><U+00A5><ed><U+00A0><U+00BD><ed><U+00B8><U+00A2><ed><U+00A0><U+00BD><ed><U+00B8><U+00AD>\\#demonetization https://t.co/ObQrhlNSL6 & 2016-11-22                                                                                                                                                                                                                                                                                         \\\\\n",
       "\t5216 & 59e8dda1c553ce84b80a6793                                                                                                                                                                                                                                                                            & RT @ippatel: Retaining all seats of LS and state in Byelection by BJP has proved the people's support on \\#DeMonetization. It should be abov…                                                                                                                                                      & 2016-11-22                                                                                                                                                                                                                                                                                         \\\\\n",
       "\t5217 & 59e8dda1c553ce84b80a6794                                                                                                                                                                                                                                                                            & RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.<U+092D><U+093E><U+0935><U+0941><U+0915>\"\" <ed><U+00A0><U+00BD><ed><U+00B8><U+00A9><ed><U+00A0><U+00BD><ed><U+00B8><U+00A5><ed><U+00A0><U+00BD><ed><U+00B8><U+00A2><ed><U+00A0><U+00BD><ed><U+00B8><U+00AD>\\#demonetization https://t.co/ObQrhlNSL6 & 2016-11-22                                                                                                                                                                                                                                                                                         \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| <!--/--> | _id | text | created | \n",
       "|---|---|---|\n",
       "| 5215 | 59e8dda1c553ce84b80a6792                                                                                                                                                                                                                                                                          | RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.<U+092D><U+093E><U+0935><U+0941><U+0915>\"\" <ed><U+00A0><U+00BD><ed><U+00B8><U+00A9><ed><U+00A0><U+00BD><ed><U+00B8><U+00A5><ed><U+00A0><U+00BD><ed><U+00B8><U+00A2><ed><U+00A0><U+00BD><ed><U+00B8><U+00AD>#demonetization https://t.co/ObQrhlNSL6 | 2016-11-22                                                                                                                                                                                                                                                                                        | \n",
       "| 5216 | 59e8dda1c553ce84b80a6793                                                                                                                                                                                                                                                                          | RT @ippatel: Retaining all seats of LS and state in Byelection by BJP has proved the people's support on #DeMonetization. It should be abov…                                                                                                                                                      | 2016-11-22                                                                                                                                                                                                                                                                                        | \n",
       "| 5217 | 59e8dda1c553ce84b80a6794                                                                                                                                                                                                                                                                          | RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.<U+092D><U+093E><U+0935><U+0941><U+0915>\"\" <ed><U+00A0><U+00BD><ed><U+00B8><U+00A9><ed><U+00A0><U+00BD><ed><U+00B8><U+00A5><ed><U+00A0><U+00BD><ed><U+00B8><U+00A2><ed><U+00A0><U+00BD><ed><U+00B8><U+00AD>#demonetization https://t.co/ObQrhlNSL6 | 2016-11-22                                                                                                                                                                                                                                                                                        | \n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "     _id                     \n",
       "5215 59e8dda1c553ce84b80a6792\n",
       "5216 59e8dda1c553ce84b80a6793\n",
       "5217 59e8dda1c553ce84b80a6794\n",
       "     text                                                                                                                                                                                                                                                                                             \n",
       "5215 RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.<U+092D><U+093E><U+0935><U+0941><U+0915>\"\" <ed><U+00A0><U+00BD><ed><U+00B8><U+00A9><ed><U+00A0><U+00BD><ed><U+00B8><U+00A5><ed><U+00A0><U+00BD><ed><U+00B8><U+00A2><ed><U+00A0><U+00BD><ed><U+00B8><U+00AD>#demonetization https://t.co/ObQrhlNSL6\n",
       "5216 RT @ippatel: Retaining all seats of LS and state in Byelection by BJP has proved the people's support on #DeMonetization. It should be abov…                                                                                                                                                     \n",
       "5217 RT @DrKumarVishwas: And the Oscar goes to \"\"Mr.<U+092D><U+093E><U+0935><U+0941><U+0915>\"\" <ed><U+00A0><U+00BD><ed><U+00B8><U+00A9><ed><U+00A0><U+00BD><ed><U+00B8><U+00A5><ed><U+00A0><U+00BD><ed><U+00B8><U+00A2><ed><U+00A0><U+00BD><ed><U+00B8><U+00AD>#demonetization https://t.co/ObQrhlNSL6\n",
       "     created   \n",
       "5215 2016-11-22\n",
       "5216 2016-11-22\n",
       "5217 2016-11-22"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(tweets_dates,3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Cleaning the text content of the tweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Loading required package: NLP\n",
      "\n",
      "Attaching package: ‘NLP’\n",
      "\n",
      "The following object is masked from ‘package:ggplot2’:\n",
      "\n",
      "    annotate\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#required packages\n",
    "library('tm');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "cleanText <- function(txt){\n",
    "    txt.tweets <- VCorpus(VectorSource(txt))\n",
    "    #lowercase\n",
    "    txt.tweets <- tm_map(txt.tweets, content_transformer(tolower))\n",
    "    # Remove numbers\n",
    "    txt.tweets <- tm_map(txt.tweets, removeNumbers)\n",
    "    #Remove english common words\n",
    "    txt.tweets <- tm_map(txt.tweets, removeWords, stopwords(\"english\"))\n",
    "    #Remove punctuations\n",
    "    txt.tweets <- tm_map(txt.tweets, removePunctuation)\n",
    "    #Remove whitespaces\n",
    "    txt.tweets<- tm_map(txt.tweets, stripWhitespace)\n",
    "    \n",
    "    #remove the word rt(retweet)\n",
    "    txt.tweets<- tm_map(txt.tweets,content_transformer(function(x){return (gsub(\"rt\",\"\",x))}))\n",
    "\n",
    "    \n",
    "    return(txt.tweets)\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<<VCorpus>>\n",
       "Metadata:  corpus specific: 0, document level (indexed): 0\n",
       "Content:  documents: 6"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "tweet.txt_data <- cleanText(tweets_dates$text)\n",
    "head(tweet.txt_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Generate wordcloud"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Loading required package: RColorBrewer\n"
     ]
    }
   ],
   "source": [
    "library('wordcloud');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#create a TermDocumentMatrix in order to generate the wordcloud\n",
    "dtm <- TermDocumentMatrix(tweet.txt_data)\n",
    "m <- as.matrix(dtm)\n",
    "d <- data.frame(as.table(m))\n",
    "head(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#Generating a word cloud\n",
    "wordcloud(d$Terms,d$Freq,min.freq = 1,\n",
    "          max.words=50, col=terrain.colors(length(d$Terms), alpha=0.9))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sentiment Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "library(\"syuzhet\");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sentiments <- get_sentiment(as.character(tweets_dates$text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "tweets_dates$sentiments <- sentiments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "head(tweets_dates,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "tweet_sentiments = mongo(collection = \"tweets_sentiments\", db = \"Twit_Sentiment_Analysis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "tweet_sentiments$remove('{}')\n",
    "tweet_sentiments$insert(tweets_dates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "tweet_sentiments$find('{\"created\":\"2017-04-19\"}','{\"sentiments\":true}',limit=5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#group by each day and calculate the avg sentiment of tweets that day\n",
    "tweet_sentiments$aggregate('[{\"$group\":{\"_id\":\"$created\",\"sentiments\":{\"$avg\":\"$sentiments\"}}}]')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating a Sentiment Analysis bar chart which displays the varying sentiments over the days during the demonetization phase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "tweet_sentiments$aggregate('[{\"$group\":{\"_id\":\"$created\",\"sentiments\":{\"$avg\":\"$sentiments\"}}}]')%>%\n",
    "ggplot(aes(x=`_id`,y=sentiments,fill=sentiments))+scale_fill_gradient(low = \"red\", high = \"green\")+\n",
    "geom_bar(stat=\"identity\")+coord_flip()+xlab(\"Date\")+ylab(\"Overall public Sentiment\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Results and Discoveries"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<i>\n",
    "1. Initially when the decision was made in the month of november to stop the notes of 500 and 1000 in a very short amount of time, people were slightly happy or neutral. \n",
    "2.  On 11th April, as can be seen, there were a lot of hate tweets, this mostly summarizes the angst of people during that time, as people were facing a lot of inconvenience. \n",
    "3. However in the next few days, when people realized there were more pros to the decision than cons, they whole heartedly supported the decision, and hence a flurry of positive tweets followed in the next few days</i>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### References\n",
    "<i>\n",
    "1. https://www.r-bloggers.com/\n",
    "2. https://www.kaggle.com/arathee2/demonetization-in-india-twitter-data/downloads/demonetization-tweets.csv\n",
    "3. https://github.com/jeroen/mongolite\n",
    "</i>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.4.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
