import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'  # Enable all logs
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Force GPU 0 visibility
import tensorflow as tf
print("TensorFlow Version:", tf.__version__)
print("Num GPUs Available:", len(tf.config.list_physical_devices('GPU')))
try:
    with tf.device('/GPU:0'):
        a = tf.random.normal([100, 100])
        b = tf.random.normal([100, 100])
        c = tf.matmul(a, b)
    print("GPU operation successful")
except Exception as e:
    print("Error during GPU operation:", e)