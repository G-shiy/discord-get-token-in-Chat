import discord
import os, re, os.path
import json
import getToken

bot = discord.Client()
@bot.event
async def on_ready() -> bool:
    print('iniciando . . .')
    logfolder = "./trashlog"
    token= "./token"
    if not os.path.exists(logfolder) and not os.path.exists(token):
        os.mkdir(logfolder)
        print("Pasta {0} criada".format(logfolder))
        os.mkdir(token)
        print("Pasta {0} criada".format(token))
    print("carregando dados da pasta {0} e da pasta {1}".format(logfolder, token))
    

@bot.event
async def on_message(message: str):
    mensagem = message.content
    if message.channel.id != config["channel_id"]:
        pass
    else:
        if not os.path.exists("token/token.txt"):              
            open("token/token.txt", "a+") 
        if not os.path.exists("trashlog/trashlog.txt"):
            open("trashlog/trashlog.txt", "a+")
        with open("trashlog/trashlog.txt", "a", encoding='utf8' ) as file:
            file.write(mensagem+"\n")
        getToken.findToken()


try:
    with open('config.json') as f:
        config = json.load(f)

    bot.run(config["token"], bot=False)

except Exception as e:
    print(f"Erro ao logar - // - Erro: {e}")