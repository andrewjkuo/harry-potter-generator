from flask import Flask, request
from flask_cors import CORS
import json
import tensorflow as tf
import gpt_2_simple as gpt2

class GptModel:
  def __init__(self):
    self.sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(self.sess, run_name='run1')
    self.graph = tf.get_default_graph()

  def predict(self, prefix):
    print('pred working')
    with self.graph.as_default():
      txt = gpt2.generate(self.sess, run_name='run1', length=200, prefix=prefix, return_as_list=True)[0]
    return txt

gptmodel = GptModel()
app = Flask(__name__)
CORS(app)

@app.route('/v1/gpt2', methods=['POST'])
def gpt2_model():
  print('req received')
  data = json.loads(request.data.decode("utf-8"))
  txt = gptmodel.predict(data['text'])
  return txt

if __name__ == "__main__":
  app.debug = True
  app.run(threaded=False)
