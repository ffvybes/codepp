from flask import Flask, jsonify, request
import redis
import os

app = Flask(_name_)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def home():
    return jsonify(message="Flask + Redis API is running 🚀")

@app.route('/set', methods=['POST'])
def set_value():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    if not key or not value:
        return jsonify(error="Key and value required"), 400
    r.set(key, value)
    return jsonify(message=f"Stored {key} = {value}")

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    value = r.get(key)
    if value:
        return jsonify(key=key, value=value)
    return jsonify(error="Key not found"), 404

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)