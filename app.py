from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Cartoonify API running!"

@app.route('/cartoonify', methods=['POST'])
def cartoonify():
    try:
        file = request.files['image']
        img = Image.open(file).convert('RGB')

        # Edge detection
        edges = img.convert('L').filter(ImageFilter.FIND_EDGES)

        # Reduce colors
        cartoon = ImageOps.posterize(img, bits=3)

        # Overlay edges
        cartoon_np = np.array(cartoon)
        edges_np = np.array(edges)
        edges_mask = edges_np > 50
        cartoon_np[edges_mask] = 0

        cartoon_final = Image.fromarray(cartoon_np)

        # Save temporarily
        out_path = "cartoonified.png"
        cartoon_final.save(out_path)
        return send_file(out_path, mimetype='image/png')
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
