# インストールした discord.py を読み込む
import discord

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
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃん')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)