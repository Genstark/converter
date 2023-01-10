import tensorflow as tf

model = tf.keras.models.load_model('.h5 model path')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflmodel = converter.convert()
file = open( '.tflite model path' , 'wb' ) 
file.write( tflmodel )
file.close()

def hex_to_c_array(hex_data, var_name):

    c_str = ''
    
    c_str += '#ifndef ' + var_name.upper() + '_H\n'
    c_str += '#define ' + var_name.upper() + '_H\n\n'

    c_str += '\nunsigned int ' + var_name + '_len = ' + str(len(hex_data)) + ';\n'

    c_str += 'unsigned char ' + var_name + '[] = {'
    hex_array = []
    for i, val in enumerate(hex_data) :

      hex_str = format(val, '#04x')

      if (i + 1) < len(hex_data):
          hex_str += ','
      if (i + 1) % 12 == 0:
          hex_str += '\n '
      hex_array.append(hex_str)

    c_str += '\n ' + format(' '.join(hex_array)) + '\n};\n\n'

    c_str += '#endif //' + var_name.upper() + '_H'

    return c_str

c_model_name = "esp32"

with open(c_model_name + '.h', 'w') as file:
  file.write(hex_to_c_array(tflmodel, c_model_name ))