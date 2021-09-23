# EC601_Project2

## First Test Case
The first test case that I ran using Twitters API and my developer account was to see if there was a way I could like a specific tweet without ever having to go on Twitter. While this test case my only be used by a handful of individuals, it allowed me to see how the API worked, along with just how powerful this tool is. This involved using python code and I have attached the open source code that I used, named `LikeTweetFromTerminal.py` to this GitHub project for reference. I used an adaptation of code from Twitters Developers but had to trouble shoot many issues that I ran into. First, making sure that you have an authorized API key and API Secret Key is vital. Secondly, you must enter the userID of the account that you made your developer account. This is not your user name, this is the ID associated with your username, which can be found at the website I linked in the comments of the code. Next, in the payload variable you need to specific the tweets ID that you want to like. This can be located in your web address by locating the tweet and taking everything after `status\`. Now we can see that this code requests a token using your entered API key and API Secret Key. There will be web address that displays in the terminal that you must copy and past into your browser. You will be prompted by a display to allow your created app access. A pin number will then be displayed, which will need to be copied and pasted back into your terminal window to authenticate. You have then granted access and the request is made and then saved, ultimately liking the specified tweet. I have attached a screenshot below of the output of this code, showing that “liked” is now true. 

### Terminal Window After Sending Request
![Output of Liking a Tweet](https://user-images.githubusercontent.com/74614080/134572333-ed80b030-f011-48fe-84a1-9994596bf331.png)



## Second Test Case
The second test cast that I ran was through Twitters Postman tool. 


### Layout of Postman Web Application
![Example of Tesla Layout](https://user-images.githubusercontent.com/74614080/134568475-5da5fc0e-f304-4bcd-b5ac-be2c7dad7c5e.png)
