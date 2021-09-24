# EC601_Project2

## Like Tweet From Terminal
The first test case that I ran using Twitters API and my developer account was to see if there was a way I could like a specific tweet without ever having to go on Twitter. While this test case my only be used by a handful of individuals, it allowed me to see how the API worked, along with just how powerful this tool is. This involved using python code and I have attached the open source code that I used, named `LikeTweetFromTerminal.py` to this GitHub project for reference. I used an adaptation of code from Twitters Developers but had to trouble shoot many issues that I ran into. First, making sure that you have an authorized API key and API Secret Key is vital. Secondly, you must enter the userID of the account that you made your developer account. This is not your user name, this is the ID associated with your username, which can be found at the website I linked in the comments of the code. Next, in the payload variable you need to specific the tweets ID that you want to like. This can be located in your web address by locating the tweet and taking everything after `status\`. Now we can see that this code requests a token using your entered API key and API Secret Key. There will be web address that displays in the terminal that you must copy and past into your browser. You will be prompted by a display to allow your created app access. A pin number will then be displayed, which will need to be copied and pasted back into your terminal window to authenticate. You have then granted access and the request is made and then saved, ultimately liking the specified tweet. I have attached a screenshot below of the output of this code, showing that “liked” is now true. 

### Terminal Window After Sending Request
![Output of Liking a Tweet](https://user-images.githubusercontent.com/74614080/134572333-ed80b030-f011-48fe-84a1-9994596bf331.png)



## Tesla Recent Likes
The second test cast that I ran was through Twitters Postman tool. The first step was to load Twitter API v2 postman collection into my environment. I had to create an account in postman, which then loaded in this API for me. For this test case, I decided to pull liked Tweets from a specific user. I navigated to the likes folder and then `GET Liked Tweets`. After this tab was opened in my application, I had to make sure that when I made a GET request like this, it would be authenticated. This required me to go to the authentication tab and enter in my Bearer Token, which is located in the Developer Portal on Twitter. After this was done, I had to decide who I wanted to pull liked tweets from. For this example, I used Tesla. Under the Params tab, scroll down to the path variables and next to id, enter the userID, or value, for Tesla here. You can again get this ID through the website I mentioned in my previous test case. Scroll back up and decided what parameters you want to display in the output. I selected only the user fields for this example and set the max_results to 10. Now we can hit send and should see our results below our selected fields. It is listed in a JSON format and can be downloaded by going to Save Response and then Save to a file. This is a simple example of how this tool works but also displays the power of it. 


### Layout of Postman Web Application
![Example of Tesla Layout](https://user-images.githubusercontent.com/74614080/134568475-5da5fc0e-f304-4bcd-b5ac-be2c7dad7c5e.png)



## Panera Bread
The next application I thought of using was to see if I can see when a people tweet about a specific thing or place to determine popularity at time periods. I used Panera Bread as an example for this test. As you can see from the screenshot below in the query field I specified “Panera” as what I wanted Postman to search for in tweets. By default, my results come back in by the hour, with the count for that hour being displayed. After looking through the PaneraByHour.JSON file above. I determined that on September 17th, between 5pm and 6pm, Panera was tweeted about the most. I then filtered this down more by breaking up the data into minutes for that hour time period. I then sent that request and received back PaneraByMinute.JSON. From this file, we see that the tweets begin to pick up towards the second half of that hour. I can then make the assumption that between 5:30 and 6, Panera is starting to get busy, and customers are beginning to be vocal about this. This is right around when people get off work and are getting dinner, so this makes a lot of sense to me logically. This data can be used Panera, to help the company focus on specific periods of time, like this hour for example, and make sure that their social media channels are active and employee staffing is high. 

### Panera By Hour
![Panera By Hour](https://user-images.githubusercontent.com/74614080/134581926-d2da3b1b-892d-47ba-af49-e05e00fbc142.png)

### Panera By Minute
![Panera By Minute](https://user-images.githubusercontent.com/74614080/134581974-24e36101-f007-4dd1-8822-465c4c1680a9.png)


## Pull Tweets From Individual
Another application that we can use Twitters API for is to pull a list of tweets by and individual or company. This can be useful for many applications including companies using it for job screening. I have included the link of where this code was originally from in the .py file above. In this code, the bearer token is required to authenticate access for use of Twitters API. Secondly, we need to specific the user_id of the account that we want to pull tweets from. This is the same process that we used before and need to get the user id from the Twitter username. Next, in `get_params()`, this is where we specific what exactly we want from the tweets that we pull. Do we want the attachments or the author id, or do we want to metrics on the tweet or what time it was created. Next, we are going to authenticate our bearer token and send our request. If successful, we are going to get the data we are looking for. I have changed the code around in `main()` to create a JSON file and write our data to it, close the file and put it in our working directory. This is a much more readable and transferable method than printing out on our terminal window, which is what the previous code did.Lets for example pull the tweets of Jeff Bezos to see what he has been voicing publicly lately. I can get the userId of his twitter account and put it into my code. I have attached a screenshot of the output in the terminal and then also changed the code so it outputs into JobScreen.json and attached that file above. 


![Terminal Output for Jeff Bezos](https://user-images.githubusercontent.com/74614080/134730627-31a05dc8-ba6e-44e2-9261-dfc8d3dbbcd4.png)
