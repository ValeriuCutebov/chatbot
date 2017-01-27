import sl4a
droid = sl4a.Android()


data1 = open("questions.txt", 'r+')
data2 = open("answers.txt",'r+')

droid.ttsSpeak('Enter your name please >>')
username = droid.recognizeSpeech()
droid.setClipboard(username.result)
uname = username.result

droid.ttsSpeak("Hello" uname)

def call():
    inputer = droid.recognizeSpeech()
    droid.setClipboard(inputer.result)
    inputer1 = inputer.result    
    for i in predic:
        if inputer1+'\n'== i:
            index = predic.index(i)
            droid.ttsSpeak(answers [index])
            kot = raw_input("Press anything to ask again >> ")
            call()
    call()
    
    
al = 0
i = 0
predic = []
answers = []
if al == 0:
    for u in data1:
        predic.append(u)
    for n in data2:
        answers.append(n)
    call()

data1.close()
data2.close()

