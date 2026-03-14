import requests

url = "https://<your-render-app-url>/cartoonify"

with open("myphoto.jpg","rb") as f:
    files = {"image": f}
    response = requests.post(url, files=files)

with open("cartoonified.png","wb") as out:
    out.write(response.content)

print("Cartoonified image saved as cartoonified.png")
