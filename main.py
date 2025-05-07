def main(request):
    request_json = request.get_json(silent=True)
    print("PG&E Notification Received:", request_json)
    return "Notification received", 200
