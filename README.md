# A.I. Rowling

### About
This is a recurrent neural network model (LSTM) for generating new Harry Potter content. I trained the model on the entire Harry Potter series and it can now produce completely new text in the style of J.K. Rowling. While the model is probably not good enough to fool an attentive reader, it has managed to capture a lot of the writing style and vocabulary of these famous books.

The model was trained by taking every consecutive 50-word sequence in Harry Potter and trying to predict the next word. It was implemented in Keras with the following structure:
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
### Usage
All of my results can be reproduced by running the notebooks in this repository. The txt_generator.ipynb notebook can be used to try out my pre-trained model and generate new text. If you would like to train the model again from scratch you can use the train_model.ipynb notebook.

### Models
There are a number of different pre-trained models included in this repository. The 070520 model is used by default in the txt_generator notebook as I believe it produces the best results. Feel free to try any of the other models. Unfortunately I didn't keep track of all the hyperparameter settings other than number of training epochs:
* 030520: 28 epochs (early stopping on validation loss was used)
* 070520: 178 epochs (intentionally overfit)
* 080520: 250 epochs (intentionally overfit)