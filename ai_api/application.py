from flask import Flask
from flask_cors import CORS
import tensorflow as tf
import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run2')
graph = tf.get_default_graph()

app = Flask(__name__)
CORS(app)

@app.route('/v1/gpt2', methods=['GET'])
def gpt2_model():
    with graph.as_default():
        txt = gpt2.generate(sess, run_name='run2', length=200, return_as_list=True)[0]
    return txt

if __name__ == "__main__":
    app.debug = True
    app.run()
