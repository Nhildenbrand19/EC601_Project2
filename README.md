# EC601_Project2a

## Like Tweet From Terminal
The first test case that I ran using Twitters API and my developer account, was to see if there was a way I could like a specific tweet, without ever having to go on Twitter. While this test case may only be used by a handful of individuals, it allowed me to see how the API worked, along with just how powerful this tool is. This involved using python code and I have attached the open source code that I used, named `LikeTweetFromTerminal.py` to this GitHub project for reference. I used an adaptation of code from Twitters Developers but had to trouble shoot many issues that I ran into. First, making sure that you have an authorized API key and API Secret Key is vital. Secondly, you must enter the userID of the Twitter account that you made your developer account with. This is not your user name, this is the ID associated with your username, which can be found at the website I linked in the comments of the code. Next, in the payload variable you need to specific the tweets ID that you want to like. This can be located in your web address by locating the tweet and taking everything after `status\`. Now we can see that this code requests a token using your entered API key and API Secret Key. There will be web address that displays in the terminal that you must copy and past into your browser. You will be prompted by a display to allow your created app access. A pin number will then be displayed, which will need to be copied and pasted back into your terminal window to authenticate. You have then granted access and the request is made and then saved, ultimately liking the specified tweet. I have attached a screenshot below of the output of this code, showing that “liked” is now true. I tested this on a tweet from someone I know to ensure the right tweet was liked and in this case, it was.

### Terminal Window After Sending Request
![Output of Liking a Tweet](https://user-images.githubusercontent.com/74614080/134572333-ed80b030-f011-48fe-84a1-9994596bf331.png)


-----------
## Tesla Recent Likes
The second test cast that I ran was using Twitters Postman tool. The first step was to load Twitter API v2 Postman collection into my environment. I had to create an account in Postman, which then loaded in this API for me. For this test case, I decided to pull liked Tweets from a specific user. I navigated to the likes folder and then `GET Liked Tweets`. After this tab was opened in my application, I had to make sure that when I made a GET request like this, it would be authenticated. This required me to go to the authentication tab and enter in my Bearer Token, which is located in the Developer Portal on Twitter. After this was done, I had to decide who I wanted to pull liked tweets from. For this example, I used Tesla. Under the Params tab, scroll down to the path variables and next to id, enter the userID, or value, for Tesla here. You can again get this ID through the website I mentioned in my previous test case. Scroll back up and decided what parameters you want to display in the output. I selected only the user fields for this example and set the max_results to 10. Now we can hit send and should see our results below our selected fields. It is listed in a JSON format and can be downloaded by going to Save Response and then Save to a file. This file is saved in this repository under TeslaLast10Likes.JSON for further analysis and exploration. This is a simple example of how this tool works but also displays the power of it. 


### Layout of Postman Web Application
![Example of Tesla Layout](https://user-images.githubusercontent.com/74614080/134568475-5da5fc0e-f304-4bcd-b5ac-be2c7dad7c5e.png)


---------
## Panera Bread
The next application I thought of using was to see if I can see when people tweet about a specific thing or place to determine popularity at time periods. I used Panera Bread as an example for this test. As you can see from the screenshot below in the query field I specified “Panera” as what I wanted Postman to search for in tweets. By default, my results were broken down hourly, with the count for that hour being displayed. After looking through the PaneraByHour.JSON file above, I determined that on September 17th, between 5pm and 6pm, Panera was tweeted about the most for our case study. I then filtered this down further by breaking up the data into minutes for that hour long time period. I then sent that request and received back PaneraByMinute.JSON. From this file, we see that the tweets begin to pick up towards the second half of that hour. We can then make the assumption that between 5:30 and 6, Panera is starting to get busy, and customers are beginning to be vocal about this. This is right around when people get off work and are getting dinner, so this makes a lot of sense to me logically. This data can be used Panera, to help the company focus on specific periods of time, like this hour for example, and make sure that their social media channels are active and employee staffing is high. 

### Panera By Hour
![Panera By Hour](https://user-images.githubusercontent.com/74614080/134581926-d2da3b1b-892d-47ba-af49-e05e00fbc142.png)

### Panera By Minute
![Panera By Minute](https://user-images.githubusercontent.com/74614080/134581974-24e36101-f007-4dd1-8822-465c4c1680a9.png)

---------
## Pull Tweets From Individual
Another application that we can use Twitters API for is to pull a list of tweets by an individual or company. This can be useful for many applications including, for example, companies using it for job screening. I have included the link of where this code was originally from in the `ScreenForJob.py` file above. In this code, the bearer token is required to authenticate access for use of Twitters API. Secondly, we need to specific the user_id of the account that we want to pull tweets from. This is the same process that we used before and need to get the user id from the Twitter username. Next, in `get_params()`, this is where we specific what exactly we want from the tweets that we pull. Do we want the attachments or the author id, or do we want to metrics on the tweet or what time it was created. Next, we are going to authenticate our bearer token and send our request. If successful, we are going to get the data we are looking for. I have changed the code around in `main()` to create a JSON file and write our data to it, close the file and put it in our working directory. This is a much more readable and transferable method than printing out on our terminal window, which is what the previous code did. Lets for example pull the tweets of Jeff Bezos to see what he has been voicing publicly lately. I can get the userId of his twitter account and put it into my code. I have attached a screenshot of the output in the terminal and then also changed the code so it outputs into JobScreen.json and attached that file above. 


![Terminal Output for Jeff Bezos](https://user-images.githubusercontent.com/74614080/134730627-31a05dc8-ba6e-44e2-9261-dfc8d3dbbcd4.png)


# EC_601_Project2b

## Claritin Sentiment Analysis Model
To start I first needed to create a Google Cloud project and enable AutoML Natural Language. It is important to create this project as it is the place where I will be doing all of my training and testing for this project. Next I needed to enable the Cloud AutoML and Storage APIs that I am going to be using. Once this is done we can begin to test out a project. The first approach that I wanted to explore was sentiment analysis. I took an open source dataset from Kaggle with the plan of using it for a sentiment analysis of tweets about medicine, but more specifically, Claritin. Now that I have the dataset, I need to import it into the project to use for my model. The screenshot below shows the dataset after import **(1)** and we can see the number of items, how many of these items were scored, along with the number of items for training, validation and testing. We can also see the sentiment score that was assigned. I set the max sentiment score in this case to be 4, which is why we see scoring on the left side from 0-4. I then was able to train my model using this dataset and simply clicked the Train tab at the top of the window **(1)**. The model took several hours to train, but this was expected. Once training was complete, I was able to use this model to analyze either other documents, or just snippets of text and get a sentiment analysis score. In addition to this model, I received a precision percentage along with a confusion matrix **(2)**, that shows how often the trained model correctly classified each label (shown in blue) and which labels were confused (shown in grey). The first test I ran you can see in the screenshot below **(3)**, I tested this model by typing in “Claritin will help me feel better” as input text and clicked predict. As expected we got a high sentiment score of 3. I then ran another test saying that “Claritin does not help me at all” and received a score of 2. This is simply telling us that the trained model we are using is correctly predicting sentiment on our inputs. Looking back on this model, I would’ve liked the classification to be a bit more accurate and maybe even classify my second input as 1. As a whole, the model is accurate though and this test was a success.


I have also included above `predict.py`, `request_text.json` and `request_GCS.json` which give us the ability to use this custom model. To use this model in a REST API, `request_text.json` is available for text input, while `request_GCS.json` is available for a GCS file. On the other hand, `predict.py` gives us the ability to run a program in our terminal and predict the sentiment.



### Imported Dataset
- [Claritin Sentiment Scoring](https://www.kaggle.com/ranja7/nlp-sentiment-scoring-noheaderlabel)

### DataSet Upload (1)
![DataSet Upload](https://user-images.githubusercontent.com/74614080/135013905-c5ae4bc2-cae9-4225-8aba-c53b9b6139ae.png)

### After Training (2)
![Pie Chart](https://user-images.githubusercontent.com/74614080/135115100-ee994f70-7606-4540-b535-e71171cf09ee.png)
![Confusion Matrix](https://user-images.githubusercontent.com/74614080/135115102-3403c2f9-f0d8-4303-9376-a4c6a081454b.png)

### Input Sentiment Analysis (3)
![Given Text](https://user-images.githubusercontent.com/74614080/135115103-62c745eb-81fa-443e-84dd-565846568f30.png)

![Analysis Score](https://user-images.githubusercontent.com/74614080/135115104-e6d5996a-7063-4ac8-b814-bcf61dee4e97.png)

------
## IMDB Movie Review Sentiment Analysis Model
While still looking at sentiment analysis, I wanted to test something different this time. To do this, I again needed to create a Google Cloud Project and specify the type of model I wanted to create. For this test using Google NLP APIs, I picked a different dataset that contained movie reviews with all movie reviews being over 200 words each. Additionally, this dataset is roughly 10x the size of my first dataset used and only ranges from 0-1 on the sentiment scale. I was extremely curious to see how this analysis compared to my first and what kind of insights the NLP API could give me. The uploading of this dataset took much longer as well and the screenshot of the finished upload is below **(1)**. After the upload was complete, I again needed to train my model. When the training tab is selected we can see the breakdown of training, validation and testing for each sentiment score **(2)**. I then clicked start training and let my model begin to build. This took about 5 hours to complete but once finished, I could now use my custom model to predict the sentiment of any statement I made. We can see that after training **(3)**, we are getting a much better precision rate in this model compared to our first. Additionally we can see in the confusion matrix that we have a much higher percentage in blue compared to grey. This translates to a much better predictive model. Moving on to testing, I decided to pull a movie review from Rotten Tomatoes as our input text **(4)**. I took a quote from top approved critic Nicolas Delgadillo on the 2018 film Jurassic World, which received a 48% audience score. We can make the assumption that the sentiment is not great for this movie but let us test our trained model to see if that is the case. As we expected, the predicted score is 0, a great sign that our model is working **(5)**. Let’s now test a movie with a higher rating and see if we can get a correctly predicted score again. This time I chose Incredibles 2 and another review written by Nicolas Delgadillo. This movie received an 84% audience score and should give us a good sentiment score as well. We can see the quote I used **(6)** along with the correctly predicted sentiment score of 1, based on our input **(7)**. We can see based on just these two examples, just how accurate our custom model is in this case. 

Again we can use `predict.py` and `request.json` to use this custom model outside of the web browser. 


### Imported Dataset
- [IMDB Sentiment of Reviews](https://www.kaggle.com/columbine/imdb-dataset-sentiment-analysis-in-csv-format)

### DataSet Upload (1)
![Data Upload](https://user-images.githubusercontent.com/74614080/135138246-38850afa-5c9e-4347-8478-36e3e3473955.png)

### Training (2)
![Training Screen](https://user-images.githubusercontent.com/74614080/135138352-c482ec75-13c7-4199-9326-2ff8c0e5163d.png)


### After Training (3)
![Pie Chart](https://user-images.githubusercontent.com/74614080/135175600-3ac56378-17fd-4f12-a5c5-19a23acc411a.png)
![Confusion Matrix](https://user-images.githubusercontent.com/74614080/135175624-2233ecda-a71b-453f-b4fd-053dc361ee14.png)


### First Input Sentiment Analysis (4)
- [Jurassic World Film Review](https://discussingfilm.net/2018/06/22/jurassic-world-fallen-kingdom-plot-and-character-take-a-backseat-to-cheap-thrills/)

![Jurassic World Score](https://user-images.githubusercontent.com/74614080/135175760-f01c179e-adfd-417e-983a-0461e157c14f.png)


### Second Input Sentiment Analysis (5)
- [Incredibles 2 Film Review](https://discussingfilm.net/2018/06/15/incredibles-2-still-super-after-all-these-years/)

![Incredibles Score](https://user-images.githubusercontent.com/74614080/135175844-39fee7c6-18b9-467b-8a9b-30b95a2d00be.png)

# EC_601_Project2
## Product Definition
The goal of this project is too create both a simple sentiment analyzer regarding NFL games for each week using the Twitter API demonstrated in the first part of this project. This product will be able to be ran and output a text file that gives the favorites for each game based on power rankings each week. This can be used from both a fan perspective and a betting perspective. From a fan perspective, you can see if your team is favorited each and every week and from a betting perspective you can do the same, only using this information to decide what games to bet on. 

## User Stories
- As a better, I want to see the predicted outcome around a specific NFL game.
- As a fan, I want to see if my team is the favorite this week.
- As a better, I want to use this information to help better make a decision on each game.
- As a fan, I want to be able to see how my is stacking up against the rest of the league based on evolving power rankings.


## The Product

