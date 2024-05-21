import face_recognition
import pickle


train_data_file = "train_data.pkl" #база данных
with open(train_data_file, 'rb') as f:
    train_data = pickle.load(f)

known_faces = train_data['faces']
known_names = train_data['names']


new_image = face_recognition.load_image_file("feb1e7a7-5ec8-402c-86be-1a792e3a9caa.jpeg") #фото который надо распознать
new_face_encodings = face_recognition.face_encodings(new_image)


for new_face_encoding in new_face_encodings:
    distances = face_recognition.face_distance(known_faces, new_face_encoding)
    min_distance_index = distances.argmin()

    if distances[min_distance_index] < 0.48:
        recognized_name = known_names[min_distance_index]
        print("Распознано лицо:", recognized_name)
    else:
        print("Не удалось распознать лицо")
