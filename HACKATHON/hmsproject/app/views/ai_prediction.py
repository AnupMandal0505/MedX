from django.shortcuts import render,redirect,HttpResponse
import tensorflow as tf

# from app.ML import saved_trained_model

from PIL import Image
        

		
	


def prediction(request):

    def run_predict(myfile):
	
        img = Image.open(myfile.file)
        img = img.convert('RGB')
        
        return img

    if request.method == 'POST':
        image1=request.FILES['img1']
        image2=request.FILES['img2']
        image3=request.FILES['img3']
        image4=request.FILES['img4']
        image5=request.FILES['img5']

        

        
        # Load in a model and evaluate it
        loaded_model_1 = tf.keras.models.load_model("D:/HACKATHON/hmsproject/app/ML/saved_trained_model")

        # Create a function to import an image and resize it to be able to be used with our model
        def load_and_prep_image(filename, img_shape=[450, 600]):
            # """
            # Reads an image from filename, turns it into a tensor
            # and reshapes it to (img_shape, img_shape, colour_channel).
            # """
            # Read in target file (an image)
            img = run_predict(filename)

            # Decode the read file into a tensor & ensure 3 colour channels
            # (our model is trained on images with 3 colour channels and sometimes images have 4 colour channels)
            # img = tf.image.decode_image(img, channels=3)

            # Resize the image (to the same size our model was trained on)
            img = tf.image.resize(img, size = img_shape)

            # Rescale the image (get all values between 0 and 1)
            img = img/255.
            return img

        # Function to work with multi-class
        def pred(model, filename, class_names, img_shape=[450, 600]):
        
            # Imports an image located at filename, makes a prediction on it with
            # a trained model and plots the image with the predicted class as the title.
        
            # Import the target image and preprocess it
            img = load_and_prep_image(filename, img_shape)

            # Make a prediction
            pred = model.predict(tf.expand_dims(img, axis=0))
            #print(pred)

            # Get the predicted class
            pred_class = class_names[pred.argmax()] # if more than one output, take the max

            return pred_class

        class_names = ['actinic keratosis', 'basal cell carcinoma', 'dermatofibroma', 'melanoma',
                        'nevus', 'pigmented benign keratosis', 'squamous cell carcinoma', 'vascular lesion']

        
        
        
        prediction = []
        prediction.append(pred(loaded_model_1, image1, class_names))
        prediction.append(pred(loaded_model_1, image2, class_names))
        prediction.append(pred(loaded_model_1, image3, class_names))
        prediction.append(pred(loaded_model_1, image4, class_names))
        prediction.append(pred(loaded_model_1, image5, class_names))

        pred_dict = {}

        for i in class_names:
            pred_dict[i] = prediction.count(i)

        max_name = ""
        max = 0
        for i in class_names:
            if pred_dict[i] > max:
                max_name = i
                max = pred_dict[i]



        print(max_name)
        # prediction.append(pred(loaded_model_1,"D:/HACKATHON/project/app/static/image/WhatsApp Image 2023-09-14 at 23.52.24 (5).jpeg", class_names))
        # prediction.append(pred(loaded_model_1,image1, class_names))

        # print(prediction)
        # import pandas as pd

        # preiction_Ser = pd.Series(data = prediction).to_csv("/content/drive/MyDrive/SIH/Prediction.csv")
        
        return redirect("home")
    
    # return render(request,"home/aboutus.html")
