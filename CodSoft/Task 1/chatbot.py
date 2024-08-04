import re
import pandas as pd
import random
import datetime
date = datetime.datetime.now()
time = date.hour
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if time >= 6 and time < 12:
    period = "morning"
elif time >= 12 and time < 17:
    period = "afternoon"
elif time >= 17 and time < 19:
    period = "evening"
else:
    period = "night"
if time > 12:
    meridian = "PM"
    time -= 12
else:
    meridian = "AM"
todaydate = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
currenttime = str(time) + ":" + str(date.minute) + ":" + str(date.second) + " " + meridian
day = days[date.today().weekday()]
def typeofSentence(sent):
    sent = sent.lower()
    sentwords = sent.split()
    types = ["Greetings", "Declarative", "Interrogative", "Imperative", "Computational"]
    scores = [0, 0, 0, 0, 0]
    greetingwords = ["hi","hey","hello","how are you?","good morning","good afternoon","good evening","good night"]
    interrogativewords = ["how","what","where","why","when","which","who"]
    imperativewords = ["do","let","please","perform"]
    computationalwords = ["solve","compute","find","+","-","*","/"]
    verbs_dataset = pd.read_csv('verbs.csv')
    verbs = list(verbs_dataset[verbs_dataset.columns[0]].values)
    if sent[-1] == '?':
        scores[2] += 1
    elif sent[-1] == '.':
        scores[1] += 1
    scores[0] = sum([0.5 for words in greetingwords if words in sent])
    scores[4] = sum([0.75 for words in sentwords if words in computationalwords])
    if sentwords[0] in verbs or sentwords[0] in imperativewords:
        scores[3] += 1.25
    if sentwords[0] in interrogativewords:
        scores[2] += 0.5
    #print("Scores on the types of queries : ", scores)
    maxscore = max(scores)
    ind = scores.index(maxscore)
    return types[ind]
def greetings(sent):
    resp = ["Hi there, how can I help you? ", "Hello. What can I do for you? ", "Hey, hope you're doing well ",
            "Hi, good " + period + " ", "Hey, good " + period + " ", "Hello, good " + period + " "]
    return random.choice(resp)
def declarative(sent):
    sentiment_dataset = pd.read_csv('Positive and Negative Word List.csv')
    neg_words = list(sentiment_dataset[sentiment_dataset.columns[1]].values)
    pos_words = list(sentiment_dataset[sentiment_dataset.columns[2]].values)
    neg_response = ["Oh, that's concerning. ", "Unfortunate! ", "Uh oh! ", "Oh! ", "That\'s bad! ", "Damn!! ", "Hmm "]
    pos_response = ["Glad to know. ", "Great! ", "Amazing! ", "Affirmative one. ", "That\'s nice. ", "Nice! "]
    sent = sent.lower()
    sentwords = sent.split()
    neg_score = sum([0.75 for words in sentwords if words in neg_words])
    pos_score = sum([0.5 for words in sentwords if words in pos_words])
    if neg_score > pos_score:
        resp = random.choice(neg_response)
    else:
        resp = random.choice(pos_response)
    return resp
def interrogative(sent):
    sent = sent[:-1].lower()
    sentwords = sent.split()
    if "you" in sentwords:
        if sentwords[0] == "who":
            if "are" in sentwords:
                resp = "I am Chatbot AI that is programmed to respond to simple queries given by user. "
            elif "designed" in sentwords or "made" in sentwords:
                resp = "I am designed by Renganathan M to handle simple queries and respond to the user appropriately. "
        else:
            if "designed" in sentwords and sentwords[0] == "how":
                resp = "I am designed by Renganathan M to handle simple queries and respond to the user appropriately. "
            else:
                resp = "I am just a bot designed to answer queries. So I don\'t have feelings. "
    elif sentwords[0] == "what" or sentwords[0] == "which":
        if "today" in sentwords or "today\'s" in sentwords:
            if "date" in sentwords:
                resp = "Today\'s date is " + todaydate + ". "
            elif "day" in sentwords:
                resp = "Today\'s day is " + day + ". "
        elif "time" in sentwords and "now" in sentwords:
            resp = "Now the time is " + currenttime + ". "
        else:
            resp = "Sorry, I am not programmed for the question. "
    else:
        resp = "Unfortunately, I am programmed only for basic questions. "
    return resp
def imperative(sent):
    sent = sent.lower()
    sentwords = sent.split()
    for i in range(len(sentwords)):
        if sentwords[i] == "me":
            sentwords[i] = "you"
        elif sentwords[i] == "my":
            sentwords[i] = "your"
        elif sentwords[i] == "you":
            sentwords[i] = "me"
    newsent = " ".join(sentwords)
    imperativeresponses = ["I can understand that you are commanding me to do a task. But I cannot " + newsent + ". ",
                           "I do not know how to " + newsent + ". ", "Sorry, I cannot " + newsent + ". ",
                           "I am unable to " + newsent + ". "]
    return random.choice(imperativeresponses)

def isnumeric(n):
    try:
        int(n) or float(n)
    except ValueError:
        return False
    return True

def computational(sent):
    operations = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y,
                  '^': lambda x, y: x ** y}
    for i in range(len(sent)):
        if isnumeric(sent[i]) or sent[i] == '(':
            expr = sent[i:]
            break
    expr = expr.split()
    print(expr)
    stack = []
    opstack = ""
    for ch in expr:
        if ch == '(':
            opstack += ch
        elif ch == ')':
            j = -1
            while opstack[j] != '(':
                stack += opstack[j]
                opstack = opstack[:j]
            opstack = opstack[:j]
        elif ch == '^':
            opstack += ch
        elif ch == '*' or ch == '/':
            j = -1
            while opstack != "" and opstack[j] != '+' and opstack[j] != '-' and opstack[j] != '(':
                stack += opstack[j]
                opstack = opstack[:j]
            opstack += ch
        elif ch == '+' or ch == '-':
            j = -1
            while opstack != "" and opstack[j] != '(':
                stack += opstack[j]
                opstack = opstack[:j]
            opstack += ch
        else:
            stack.append(ch)
    for i in range(len(opstack)):
        stack += opstack[-i-1]
    print(stack)
    i = 0
    while i < len(stack) :
        if stack[i] in list(operations.keys()):
            res = float(operations[stack[i]](float(stack[i-2]), float(stack[i-1])))
            stack[i] = res
            del(stack[i-2:i])
            print(stack)
            i = 0
        i += 1
    return "The answer is " + str(stack[0])

print("\nWelcome! This is a Chatbot AI. You can interact with the bot and get desired responses\nIf you want to end the conversation, enter \'Exit\'\n")
while True:
    inp = input("User : ")
    if inp == "Exit" or inp == "exit":
        print("Thank you!!")
        break
    delimiters = r'(\?|\!|\. )'
    inp = re.sub(delimiters, '\\1[eol]', inp)
    text = inp.split('[eol]')
    response = ""
    for sentence in text:
        if len(sentence) > 1:
            tos = typeofSentence(sentence)
            #print("Type of query is : ", tos)
            if tos == "Greetings":
                response += greetings(sentence)
            elif tos == "Declarative":
                response += declarative(sentence)
            elif tos == "Interrogative":
                response += interrogative(sentence)
            elif tos == "Imperative":
                response += imperative(sentence)
            elif tos == "Computational":
                response += computational(sentence)
    print("Chatbot : ", response)