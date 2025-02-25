

# datos de entrenamiento
train_data = pd.read_csv("./static/assets/data_files/tweet_emotions.csv")    
training_sentences = []


# cargar modelo

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"



# asignar emoticones para diferentes emociones
emo_code_url = {
    "empty": [0, "./static/assets/emoticons/Empty.png"],
    "sadness": [1,"./static/assets/emoticons/Sadness.png" ],
    "enthusiasm": [2, "./static/assets/emoticons/Enthusiasm.png"],
    "neutral": [3, "./static/assets/emoticons/Neutral.png"],
    "worry": [4, "./static/assets/emoticons/Worry.png"],
    "surprise": [5, "./static/assets/emoticons/Surprise.png"],
    "love": [6, "./static/assets/emoticons/Love.png"],
    "fun": [7, "./static/assets/emoticons/fun.png"],
    "hate": [8, "./static/assets/emoticons/hate.png"],
    "happiness": [9, "./static/assets/emoticons/happiness.png"],
    "boredom": [10, "./static/assets/emoticons/boredom.png"],
    "relief": [11, "./static/assets/emoticons/relief.png"],
    "anger": [12, "./static/assets/emoticons/anger.png"]
    
    }
# escribir la función para predecir la emoción

        
