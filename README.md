# A.I. Rowling

### About
This is a Transformer neural network model for generating new Harry Potter content. I trained the model on the entire book series and it can now produce completely new text in the style of J.K. Rowling. It probably isn’t quite good enough to fool an attentive reader but it has captured a lot of the writing style and vocabulary of these famous books.

### Demo
TBC

### Transformer Model
This model was trained using Max Woolf's fantastic gpt2_simple python package. It uses the pre-trained 124M GPT-2 model as a starting point and is then finetuned on text from the Harry Potter books. The model itself is large and so not stored in this repository but it can be re-trained using the "2-transformer-model/train_transformer_model.ipynb" notebook. The gpt2_simple package currently doesn't work with tensorflow 2.0 and so you should probably use a virtual environment (with dependencies in requirements.txt installed) to run this notebook.

### Flask Inference API
I have included a dockerfile that can be used to spin up a flask inference API. To use this you first need to repeat the fine-tuning steps in "2-transformer-model/train_transformer_model.ipynb" and then copy the model into the ai_api folder.

### LSTM Model
This was the original model that I trained from scratch. The model was trained by taking every consecutive 50-word sequence in Harry Potter and trying to predict the next word. It was implemented in Keras with the following structure:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_1 (Embedding)      (None, 50, 64)            528832    
_________________________________________________________________
lstm_1 (LSTM)                (None, 50, 128)           98816     
_________________________________________________________________
lstm_2 (LSTM)                (None, 128)               131584    
_________________________________________________________________
dense_1 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_2 (Dense)              (None, 8263)              1065927   
=================================================================
Total params: 1,841,671
Trainable params: 1,841,671
Non-trainable params: 0
_________________________________________________________________
```

There are a number of different pre-trained models included in this repository. The 070520 model is used by default in the txt_generator notebook as I believe it produces the best results. Feel free to try any of the other models. Unfortunately I didn't keep track of all the hyperparameter settings other than number of training epochs:
* 030520: 28 epochs (early stopping on validation loss was used)
* 070520: 178 epochs (intentionally overfit)
* 080520: 250 epochs (intentionally overfit)
