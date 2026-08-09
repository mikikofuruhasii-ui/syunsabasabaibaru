from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# サーバー情報の定数
SERVER_IP = "atoms-jail.tun.ply.gg"
DISCORD_URL = "https://discord.gg/MQsMCftBpx"

@app.route('/')
def index():
    # HTMLへIPとDiscordのURLを渡す
    return render_template('index.html', server_ip=SERVER_IP, discord_url=DISCORD_URL)

# 【機能3】Javaサーバーのリアルタイムステータス取得API
@app.route('/api/status')
def get_status():
    try:
        # Minecraft Java Edition専用のステータスAPI
        response = requests.get(f"https://api.mcsrvstat.us/2/{SERVER_IP}", timeout=5)
        data = response.json()
        return jsonify({
            "online": data.get("online", False),
            "players_online": data.get("players", {}).get("online", 0),
            "players_max": data.get("players", {}).get("max", 0),
            "version": data.get("version", "不明"),
            "motd": " ".join(data.get("motd", {}).get("clean", ["サバイバルサーバーへようこそ！"])),
            "player_list": data.get("players", {}).get("list", [])
        })
    except Exception as e:
        return jsonify({"online": False, "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
