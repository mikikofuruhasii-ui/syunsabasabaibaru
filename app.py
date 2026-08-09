from mcstatus import JavaServer

IP = "atoms-jail.tun.ply.gg"

try:
    server = JavaServer.lookup(IP)
    status = server.status()

    print("🟢 ONLINE")
    print(f"👥 人数: {status.players.online}/{status.players.max}")
    print(f"📡 Ping: {status.latency:.0f}ms")
    print(f"🧱 バージョン: {status.version.name}")

except Exception as e:
    print("🔴 OFFLINE")
    print(f"エラー: {e}")
