import requests

# Replace with your actual Render URL
url = "https://cartoonify-api.onrender.com/cartoonify"

# Upload your image
with open("myphoto.jpg","rb") as f:  # Make sure this image exists locally
    files = {"image": f}
    response = requests.post(url, files=files)

# Save the cartoonified result
if response.status_code == 200:
    with open("cartoonified.png","wb") as out:
        out.write(response.content)
    print("Cartoonified image saved as cartoonified.png")
else:
    print("Error:", response.status_code, response.text)
