class CustomCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8080"
        response["Access-Control-Allow-Headers"] = "Content-Type,X-CSRFToken"
        response["Access-Control-Allow-Methods"] = 'DELETE, PUT, POST, GET, OPTIONS'
        response["Access-Control-Allow-Credentials"] = "true"
        return response