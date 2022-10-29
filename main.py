import os
import paho.mqtt.client as mqtt
import logging

def on_connect(client, userdata, flags, rc):
  logging.log(f"Connected with result code {rc}")
  client.subscribe("$PRINT/#")

def on_message(client, userdata, msg):
  try:
    print(msg.topic+" "+str(msg.payload))
    # Get bytes & create a file from them & convert to pdf with ghostpdl & print job
  except Exception as e:
    logging.error("Error parsing message")
    logging.exception(e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()


# bytes = bytes.fromhex('0000000000000000000200620000000000000200002000000000000000000000301B0000000000000008020080080004800000200200620000000000000200002000000000000000000000301B000C')

# with open("testfile.PRN", "wb") as binary_file:
#   binary_file.write(bytes)

# os.system('./ghostpdl-10.0.0/bin/gpcl6 -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=output.pdf testfile.PRN')