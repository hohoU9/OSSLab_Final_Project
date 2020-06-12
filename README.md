## This is the final project of OSS Lab(HGU, 2020-1)
**Project name: Stock price teller bot**


**Video Link: [Project presentation video](https://youtu.be/GYCX6G9wAZw)**

## What does this project do?

**Stock price teller bot** is an automatic tool for keep tracking the stock price that a user want to watch in a real time.
When a user want to keep watching some stock price with the expected price(target price), just use this bot and take some notifications using your email.


## Why is this project useful?
In these days, there are many platforms and applications providing stock makret information. 
However, it is very complicated for the beginners to use the functions in that application. 

As a result, the beginners get tired of using the applications.
In that case, this project might be helpful. You just type the stock lists that you are interested in. 
Then, the bot start to keep watching the stock list in a real time and send an email to an user when the stock is price is over the expected value.


## Tools
I develop this project using python web crawler and the open soruce named IFTTT for handling the event and sending a notification.
The information is crawled from the naver web server.


## Getting Started!

0. Clone this git repository.

1. Go to the link [iffft](https://ifttt.com/) and sing up or sign in.

2. Make the service for taking some notifications from our stock bot.
  1. Click the 'This' and find and make the 'webhooks' (The event name is used in the third process)
  
  2. Click the 'That' and find and make the email servie as below. (You have to confirm you email address in the process)
     <center><img src="/img/email.png" width="600" height="600"></center>
  
  3. Go to the link [webhook](https://ifttt.com/maker_webhooks) and click the documentation
  
  4. Type your event name and copy and paste the url address into target_url of 'config.py'
    <center><img src="/img/url.png" width="500" height="500"></center>
   
   
  5. Execute the program with the stock name and the target price so the bot gives you notification when the current price is over the        target price.(You have to sell or buy the stock)
  
     Our project provides only korea stock market information and the stock name must be matched with the KRX's offical stock name.
     (three arguments are needed: stock name, target price, time interval of watching stock)
    
      ```
      python3 stock.py 삼성전자 52000 2
      ```
  
  

## You need get some help?

Please email me hgu.thinker@gmail.com when you need some help. Or give some comments on issues


## References
https://sonsofaureus.wordpress.com/2014/05/29/ifttt-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC/

https://wendys.tistory.com/173
