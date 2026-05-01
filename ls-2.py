http_status_code = 404

if http_status_code == 200:
    print("200 OK")
elif http_status_code == 400:
    print("400 Bad Request")
elif http_status_code == 401:
    print("401 Unauthorized")
elif http_status_code == 403:
    print("403 Forbidden")
elif http_status_code == 404:
    print("404 Not Found")
elif http_status_code == 405:
    print("405 Method Not Allowed")
elif http_status_code == 406:
    print("406 Not Acceptable")
elif http_status_code == 407:
    print("407 Proxy Authentication Required")
elif http_status_code == 408:
    print("408 Request Timeout")
elif http_status_code == 500:
    print("500 Internal Server Error")
else:
    print(f"Unknown error code {http_status_code}")