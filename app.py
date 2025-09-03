from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# 🔹 Informações do contrato
TOKEN_INFO = {
    "name": "USDT/TRX",
    "symbol": "USDT",
    "decimals": 6,
    "supply": 1000000000,  # 1 bilhão
    "network": "Tron",
    "standard": "TRC20",
    "contract_address": "TKKt9vhwV961ZR92FPF3MJ3xzWeBmt9qUX"  # cole o contrato real aqui
}

# 🔹 Preço fixo inicial (você pode ajustar quando quiser)
PRICE_DATA = {
    "TRX": 0.05,     # 1 USDT = 0.01 TRX
    "USDT": 0.006    # 1 USDT = 0.0012 USDT (exemplo simbólico)
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "token": TOKEN_INFO,
        "message": "USDT/TRX Price API is running!"
    })

@app.route("/info", methods=["GET"])
def get_info():
    return jsonify({
        "name": TOKEN_INFO["name"],
        "symbol": TOKEN_INFO["symbol"],
        "decimals": TOKEN_INFO["decimals"],
        "supply": TOKEN_INFO["supply"],
        "contract_address": TOKEN_INFO["contract_address"],
        "network": TOKEN_INFO["network"],
        "standard": TOKEN_INFO["standard"]
    })

@app.route("/price", methods=["GET"])
def get_price():
    return jsonify({
        "symbol": TOKEN_INFO["symbol"],
        "name": TOKEN_INFO["name"],
        "price": PRICE_DATA,
        "last_update": datetime.datetime.utcnow().isoformat() + "Z"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
