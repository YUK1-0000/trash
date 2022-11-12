# インストールした discord.py を読み込む
import discord
import random

HAND_TYPES = ("グー","チョキ","パー")
my_hand = ""


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'MTAzNjIxNDYxODgwMjEwNjQ0OA.GZk6IX.N6HUjRC7cQCTSLf_PiP8KIcEluR9ci6icuxTSs'

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())


# 起動時に動作する処理
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
client.event(on_ready)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content.startswith("/janken"):
        my_hand = int(message.content.replace("/janken ",""))-1
        cpu_hand = random.randint(0,2)

        if my_hand in (0,1,2):
            await message.channel.send(f"YOU: {HAND_TYPES[my_hand]}\nCPU: {HAND_TYPES[cpu_hand]}")
            if my_hand == cpu_hand:
                await message.channel.send("あいこ！")
            elif my_hand == cpu_hand-1:
                await message.channel.send("勝ち！")
            else:
                await message.channel.send("負け！")
        else:
            await message.channel.send("入力が無効です。")

    if message.content.startswith("/osero"):
        turn = 0


        grid = [["　" for _ in range(8)] for _ in range(8)]

        grid[3][3] = "○"
        grid[3][4] = "●"
        grid[4][3] = "●"
        grid[4][4] = "○"

        await message.channel.send("０１２３４５６７８")
        for i in range(8):
            await message.channel.send(f'{i+1}  {"".join(grid[i])}')


        while any("　" in grid[i] for i in range(8)) and any("○" in grid[i] for i in range(8)) and any("●" in grid[i] for i in range(8)):

            turn += 1
            X = 9
            Y = 9

            if turn % 2 == 0:
                piece = "●"
            else:
                piece = "○"
            await message.channel.send("You :", piece)

            while not 0 <= X <= 7:
                X = int(float(input("X=")))-1
            while not 0 <= Y <= 7:
                Y = int(float(input("Y=")))-1

            grid[Y][X] = piece

            await message.channel.send("０１２３４５６７８")
            for i in range(8):
                await message.channel.send(i + 1, "  ", "".join(grid[i]))
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)