import os, re, os.path

#u_tokens = unique tokens

def findToken():
    tokens = []
    for line in [x.strip() for x in open(f'trashlog/trashlog.txt',errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    for line in [x.strip() for x in open(f'token/token.txt',errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)

    tokens = list(set(tokens))
    with open("token/token.txt", "a") as file:
        file.truncate(0)
        for u_token in tokens:
            file.write(u_token+"\n")
