# Import packages
import cv2
import numpy as np
import os
import time
 

image_path = "E:/Internship/TechVariable/code/website_handle/images/predicted_broken_images"
save_path = "predicted_jpg_image"

for x in range(77149, 77273):
    # image path
    image_local_x= os.path.join(image_path,str(x))
    # saved path
    newfolder = str(x)
    sub_folder = os.path.join(save_path,newfolder)
    os.makedirs(sub_folder,exist_ok=True)

    for y in range(98530,99638):
        image_name = image_local_x +"/"+ str(y)+".png"
        img = cv2.imread(image_name)  
        if img is None :
            break      
        print(img.shape) # Print image shape

        # cv2.imshow("original", img)
        
        # # Cropping an image
        cropped_image = img[:,:]
        
        # # Display cropped image
        # cv2.imshow("cropped", cropped_image)
        
        # # Save the cropped image
        path_image = os.path.join(sub_folder,f"{y}.jpg")
        cv2.imwrite(path_image, cropped_image)
        
        # time.sleep(0.1)
        # continue
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import os
# import time

# image_path = "down_18"
# save_path = "18_open"

# for x in range(77149, 77273):
#     # Create a sub-folder for each 'x'
#     sub_folder = os.path.join(save_path, str(x))
#     os.makedirs(sub_folder, exist_ok=True)

#     for y in range(98530, 99638):
#         image_name = os.path.join(image_path, str(x), f"{y}.png")

#         if os.path.isfile(image_name):
#             img = cv2.imread(image_name)

#             if img is not None:
#                 # Cropping an image
#                 cropped_image = img[172:428, 272:528]

#                 # Save the cropped image
#                 path_image = os.path.join(sub_folder, f"{y}.jpg")
#                 cv2.imwrite(path_image, cropped_image)

#                 print(f"Saved {path_image}")
#             else:
#                 print(f"Could not read image: {image_name}")
#         else:
#             print(f"Image not found: {image_name}")

#         time.sleep(0.1)


# import cv2
# import numpy as np
# import os
# import time
# import shutil

# image_path = "down_18"
# save_path = "18_open"

# for x in range(77149, 77273):
#     # Create a sub-folder for each 'x'
#     sub_folder = os.path.join(save_path, str(x))
#     os.makedirs(sub_folder, exist_ok=True)

#     for y in range(98530, 99638):
#         image_name = os.path.join(image_path, str(x), f"{y}.png")

#         if os.path.isfile(image_name):
#             img = cv2.imread(image_name)

#             if img is not None:
#                 # Cropping an image
#                 cropped_image = img[172:428, 272:528]

#                 # Save the cropped image
#                 path_image = os.path.join(sub_folder, f"{y}.jpg")
#                 cv2.imwrite(path_image, cropped_image)

#                 print(f"Saved {path_image}")
#             else:
#                 print(f"Could not read image: {image_name}")
#         else:
#             break

#         time.sleep(0.1)

    # Move to the next folder after cropping
    # next_x = x + 1
    # next_folder = os.path.join(save_path, str(next_x))
    # if os.path.exists(sub_folder) and not os.path.exists(next_folder):
    #     shutil.move(sub_folder, next_folder)
    #     print(f"Moved folder {sub_folder} to {next_folder}")

