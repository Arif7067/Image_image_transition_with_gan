from flask import Flask, send_from_directory, request, jsonify, render_template
# from flask_cors import CORS

app = Flask(__name__, template_folder='template')
# CORS(app) 

# MAX_X = 8
# MAX_Y = 894

 # Render the map.html template

@app.route('/map')
def index():
    # return 'Welcome to the Image API!'
    return render_template('map.html') 


@app.get('/images/18/<int:x>/<int:y>')
def get_image(x, y):
    # print(f"{x},{y}")
    # Check if the provided x and y values are within the valid range
    # if 0 <= x <= MAX_X and 0 <= y <= MAX_Y:
    #     # Construct the path to the image based on x and y
    #     image_path = f'images/18/{x}/{y}.jpg'
    #     # print(image_path)

    #     try:
    #         # Serve the image file
    #         return send_from_directory('.', image_path)
    #     except FileNotFoundError:
    #         return 'Image not found', 404
    # else:
    #     return 'Invalid x or y value', 400
    try:
        # Check if the provided x and y values are within the valid range
        # if 0 <= x  and 0 <= y <= MAX_Y:
            # Construct the path to the image based on x and y
        image_path = f'images/predicted_jpg_image/{x}/{y}.jpg'

        # image_path = f'images/alternate_image_name/{x}/{y}.jpg'

        # image_path = f'images/alternate_image_name_satellite/{x}/{y}.jpg'



        # satellite images 'images/alternate_image_name_satellite/{x}/{y}.jpg'
        # open street original map style 'images/alternate_image_name/{x}/{y}.jpg'


        # images/18/{x}/{y}.jpg

            # Serve the image file
        return send_from_directory('.', image_path)
        # else:
        #     return send_from_directory('.','images/abcd/invalid.jpg')
        # 'Invalid x or y value', 400
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {str(e)}")
        return send_from_directory('.','images/invalid.jpg')
    # 'Internal Server Error', 500



# @app.route('/')
# def index():
#     return 'Welcome to the Image API!'

# @app.get('/images/18/<x>/<y>')
# def get_image(x,y):
#     # print(f"{x},{y}")
#     for y in range(98559, 98570):
#         return send_from_directory('images',x,y)




# @app.route('/images/<int:zoom>/<int:x>/<int:y>')
# def get_image(zoom, x, y):
#     # Check if the provided x and y values are within the valid range
#     if 0 <= x <= MAX_X and 0 <= y <= MAX_Y:
#         # Construct the path to the image based on zoom, x, and y
#         image_path = f'images/{zoom}/{x}/{y}.jpg'

#         try:
#             # Serve the image file
#             return send_from_directory('.', image_path)
#         except FileNotFoundError:
#             return jsonify(error="Image not found"), 404
#     else:
#         return jsonify(error="Invalid x or y value"), 400





if __name__ == '__main__':
    app.run(debug=True)
