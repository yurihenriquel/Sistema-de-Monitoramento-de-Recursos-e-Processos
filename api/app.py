@app.route("/metrics", methods=["POST"])
def receive_metrics():
    data = request.json
    save_metrics(data)
    return {"status": "ok"}, 201