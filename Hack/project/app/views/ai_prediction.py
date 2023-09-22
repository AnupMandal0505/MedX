from django.shortcuts import render
import datetime
import tensorflow as tf

# from app.ML import saved_trained_model

from PIL import Image
        

		
	


def prediction(request):


    def run_predict(myfile):
	
        img = Image.open(myfile.file)
        img = img.convert('RGB')
        
        return img

    if request.method == 'POST':
        image1=request.FILES['diagnosis_image_1']
        image2=request.FILES['diagnosis_image_2']
        image3=request.FILES['diagnosis_image_3']
        image4=request.FILES['diagnosis_image_4']
        image5=request.FILES['diagnosis_image_5']

        

        
        # Load in a model and evaluate it
        loaded_model_1 = tf.keras.models.load_model("D:/Hack/project/app/ML/saved_efficientnet")

        # Create a function to import an image and resize it to be able to be used with our model
        def load_and_prep_image(filename, img_shape=[224, 224]):
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
        def pred(model, filename, class_names, img_shape=[224, 224]):
        
            # Imports an image located at filename, makes a prediction on it with
            # a trained model and plots the image with the predicted class as the title.
        
            # Import the target image and preprocess it
            img = load_and_prep_image(filename, img_shape)

            # Make a prediction
            pred = model.predict(tf.expand_dims(img, axis=0))
            #print(pred)

            # Get the predicted class
            pred_class = class_names[pred.argmax()] # if more than one output, take the max

            return (pred_class,pred.max())

       
        class_names = ["Actinic Keratosis", "Basal Cell Carcinoma", "Dermatofibroma", "Melanoma",
               "Nevus", "Pigmented Benign Keratosis", "Seborrheic Keratosis", "Solar Lentigo", "Squamous Cell Carcinoma", "Vascular Lesion"]

        
        # prediction = []
        # prediction.append(pred(loaded_model_1, image1, class_names))
        # prediction.append(pred(loaded_model_1, image2, class_names))
        # prediction.append(pred(loaded_model_1, image3, class_names))
        # prediction.append(pred(loaded_model_1, image4, class_names))
        # prediction.append(pred(loaded_model_1, image5, class_names))


        T1 = pred(loaded_model_1, image1, class_names)
        T2 = pred(loaded_model_1, image2, class_names)
        T3 = pred(loaded_model_1, image3, class_names)
        T4 = pred(loaded_model_1, image4, class_names)
        T5 = pred(loaded_model_1, image5, class_names)

        prediction = [T1[0], T2[0], T3[0], T4[0], T5[0]]
        pred_prob = [T1[1], T2[1], T3[1], T4[1], T5[1]]


        name_desc = {"Nevus": "Nevi are very common, most people have between 10 and 40. Common nevi are harmless collections of colored cells. They typically appear as small brown, tan, or pink spots. Nothing to worry about !!",
                    "Basal Cell Carcinoma": "Basal cell carcinoma is a type of skin cancer that most often develops on areas of skin exposed to the sun, such as the face. It often looks like a bump that's skin-colored or pink.",
                    "Squamous Cell Carcinoma": "Squamous cell carcinoma is a common type of skin cancer which is usually not life-threatening. But if not treated, it can grow large or spread to other parts of the body.  ",
                    "Actinic Keratosis": "Actinic keratosis may appear as irregular, red, scaly papules or plaques on sun-exposed regions of the body. It can potentially progress into invasive squamous cell carcinoma.",
                    "Pigmented Benign Keratosis": "Pigmented Benign Keratosis is a common noncancerous waxy or scaly and slightly raised skin growth, which develops on the face, neck, chest or back with age.",
                    "Dermatofibroma": "A dermatofibroma is a common benign fibrous nodule usually found on the skin of the lower legs. Sometimes attributed to minor trauma including insect bites, injections, or a rose thorn injury, but not consistently.",
                    "Melanoma": "Melanoma, the most serious type of skin cancer. While the exact cause isn't clear, but exposure to ultraviolet (UV) radiation from sunlight or tanning lamps and beds increases your risk of developing melanoma.",
                    "Vascular Lesion": "Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks.",
                    "Solar Lentigo": "Solar Lentigo is a harmless patch of darkened skin. It results from exposure to UV radiation, which causes local proliferation of melanocytes and accumulation of melanin within the skin cells",
                    "Seborrheic Keratosis": "Seborrheic keratoses are epidermal skin tumors that commonly present in adult and elderly patients. They are benign skin lesions and often do not require treatment"}

        def mode_pred(prediction, pred_prob, class_names, name_desc):
            pred_dict = {}

            for i in class_names:
                pred_dict[i] = prediction.count(i)

            max_name = ""
            max = 0
            for i in range(len(class_names)):
                if pred_dict[class_names[i]] > max:
                    max_name = class_names[i]
                    max = pred_dict[class_names[i]]
                    max_ind = prediction.index(class_names[i])

            return(max_name, pred_prob[max_ind], name_desc[max_name])

        prediction_data=mode_pred(prediction, pred_prob, class_names, name_desc)
            # print(max_name, name_desc[max_name])

        


        date= datetime.datetime.now()
        print(date)
        context={

            'diagnosis':prediction_data[0],
            'probability':prediction_data[1],
            'description':prediction_data[2],
            'prediction_date':date,
           

        }
        
        return render(request,"dasboard/user/prediction_report.html",context)
     
    
    # return render(request,"home/aboutus.html")
