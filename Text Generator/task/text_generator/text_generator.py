from nltk.tokenize import WhitespaceTokenizer
import random
import re


filename = input()
f = open(filename, "r", encoding="utf-8")

tk = WhitespaceTokenizer()
text = f.read()
tokens = tk.tokenize(text)
res = [(tokens[i] + ' ' + tokens[i + 1], tokens[i + 2]) for i in range(len(tokens) - 2)]
f.close()

chain = {}

# example_final = {"Night": {"King": 17, "gathers": 9, "King's": 4, "is": 2}}
# example_bigram = [('Night', 'King'), ('Night', 'gathers')]

for bigram in res:
    if bigram[0] in chain.keys():
        if bigram[1] not in chain[bigram[0]].keys():
            chain[bigram[0]] = chain[bigram[0]] | {bigram[1]: 1}
        else:
            chain[bigram[0]] = chain[bigram[0]] | {bigram[1]: (chain[bigram[0]][bigram[1]] + 1)}
    else:
        chain.update({bigram[0]:{bigram[1]: 1}})


for i in range(10):
    line = ''
    next_list = []
    dots = True
    while dots:
        if i == 0 and len(next_list) == 0:
            found = True
            while found:
                temp = random.choice(list(chain.keys()))
                if bool(re.match(r'[A-Z]', temp[0])) and not bool(re.match(r'[\?!\.]', temp.split()[0][-1])):

                    word = temp
                    found = False
                    next_list += word.split()

            line += word + ' '

        elif len(next_list) == 0:
            found = True
            while found:
                temp = random.choice(list(chain.keys()))
                if bool(re.match(r'[A-Z]', temp[0])) and not bool(re.match(r'[\?!\.]', temp.split()[0][-1])):
                    # print(temp)
                    word = temp
                    found = False
                    next_list += word.split()

            line += word + ' '

        else:
            word = random.choice(list(chain[next_list[-2] + ' ' + next_list[-1]].keys()))
            next_list += word.split()

            line += word + ' '

        if len(next_list) >= 5 and bool(re.match(r'[\?!\.]', next_list[-1][-1])):

            next_list = []
            dots = False
    print(line)
