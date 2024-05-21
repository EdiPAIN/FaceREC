from PIL import Image, ImageDraw
import face_recognition


img_path = "test_data/British-and-Irish-actors-009.jpg"
count = 5
faces = face_recognition.load_image_file(img_path)
faces_locations = face_recognition.face_locations(faces)

for face_location in faces_locations:
    top, right, bottom, left = face_location

    face_img = faces[top:bottom, left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.save(f"test_data/face_{count}.jpg")
    count += 1

print(f"Found {count} face(s) in this photo")