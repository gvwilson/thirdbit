import requests

response = requests.get("http://third-bit.com/test.html")
print("status code:", response.status_code)
print("content length:", response.headers["content-length"])
print(response.text)
