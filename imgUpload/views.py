from django.shortcuts import render
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

def handle_uploaded_file(f):
    with open('img.jpg', 'wb+') as destino:
        for trozo in f.chunks():
            destino.write(trozo)


# Create your views here.
def home(request):
    return render(request, 'home.html')

def procesarimagen(request):
    handle_uploaded_file(request.FILES['imagen'])
    model = ResNet50(weights='imagenet')
    img_path = 'img.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)

    print('Predicción:', decode_predictions(preds, top=3)[0])

    html = decode_predictions(preds, top=3)[0]
    res = []
    for e in html:
        res.append((e[1], np.round(e[2]*100, 2)))

    return render(request, 'resultado.html', {'res':res})