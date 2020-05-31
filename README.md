# TelegramQuestBot
Simple telegram quest-bot with declarative way of creating questions

### How to run:
0. install PyCharm (optional)
1. create virtual env for python3: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html?gclid=CjwKCAjwq832BRA5EiwACvCWsfFFf4IHs2UYAZaJiXpCIreHc_4vOejeeV465eZ071el5FbjcAlCfxoC6FoQAvD_BwE
2. install postgress db
3. create in postgress db with name: tlg_bot_db
4. clone this repo
5. run initial migrations - be in root of this repo: export PYTHONPATH=. && alembic upgrade head
6. create your own telegram bot in Bot Father: https://telegram.me/BotFather
7. paste your telegram bot token into config.py variable BOT_TOKEN
8. download ngrok: https://ngrok.com/download
9. run ./ngrok http 8080
10. copy ngrok created tunnel into config.py variable HOST
11. now your can run bot: python3 main.py
12. Open your bot in telegram and try it!


### How to use:

You should create the following commands in the FatherBot:

/info --- information about bot

/question --- show current question

/guess --- try to guess current question, should be use as "/quess ANSWER"

/start_new --- start game from the beginning for current chat

/help --- get help for current question


Then configure questions.py file following the example.