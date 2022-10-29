import os
import paho.mqtt.client as mqtt
import logging

def on_connect(client, userdata, flags, rc):
  logging.debug(f"Connected with result code {rc}")
  client.subscribe("$PRINT/#")

def on_message(client, userdata, msg):
  try:
    # Get bytes & create a file from them & convert to pdf with ghostpdl
    data = str(msg.payload)
    with open("tempfile.PRN", "wb") as binary_file:
      binary_file.write(bytes.fromhex(data))
    os.system('./ghostpdl-10.0.0/bin/gpcl6 -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=output.pdf tempfile.PRN')
    # TODO: print pdf to usb connected printer
    # TODO: push pdf somewhere where it can be downloaded.
  except Exception as e:
    logging.error("Error parsing message")
    logging.exception(e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()