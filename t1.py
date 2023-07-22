import paho.mqtt.client as mqtt
import subprocess
import requests
import json

# Callback function to handle connection established
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    # Subscribe to the desired topic(s) upon successful connection
    client.subscribe("test/mytopic7")

# Callback function to handle received messages

def on_message(client, userdata, msg):
    x = ("Received message: " + msg.payload.decode())
    string = msg.payload.decode()
    d = json.loads(string)
    f = json.dumps(d)
    
    if f.startswith('{"ED"'):
        del d['deviceId']
        del d['ts']

        keys_list = list(d.keys())
        deviceName = keys_list[0]
    
        if (float(d["ED"][3])+float(d["ED"][4])+ float(d["ED"][5])) ==0:
            statement = 'off'
           
        else :
            
             statement = 'on'

 
        nested_dict ={
            "RY_Voltage": int(d["ED"][0]),
            "YB_Voltage": int(d["ED"][1]),
            "BR_Voltage": int(d["ED"][2]),
            "R_Phase_line_Current": float(d["ED"][3]),
            "Y_Phase_line_Current": float(d["ED"][4]),
            "B_Phase_line_Current": float(d["ED"][5]),
            "Rph_power_Factor": float(d["ED"][6]),
            "Yph_power_Factor": float(d["ED"][7]),
            "Bph_power_Factor":float(d["ED"][8]),
            "Frequency":d["ED"][9] ,
            "Total_KW_wrt_line": d["ED"][10],
            "Total_KWh_wrt_line": d["ED"][11],
            "Under_Voltage": d["ED"][12],
            "Over_Voltage": d["ED"][13],
            "Under_Current": d["ED"][14],
            "Over_Current": d["ED"][15],
            "RN_Voltage": d["ED"][16],
            "YN_Voltage": d["ED"][17],
            "BN_Voltage": d["ED"][18],
            "status" : statement,
          

        }



        host_address = "http://localhost:8080"

        token = "antar"
        payload = json.dumps(nested_dict)

        url = f'{host_address}/api/v1/{token}/telemetry'

# Send POST request to ThingsBoard
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print('voltage!')
            else:
                print('Failed to send data. Status code:', response.status_code)
        except requests.exceptions.RequestException as e:
            print('An error occurred:', str(e))
    else:
            print("hi")


    
# Create an MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set("antariot", "admin@1234")

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Set up connection parameters (replace with your broker's IP address)
broker_ip = "192.168.68.116"
broker_port = 1883

# Connect to the MQTT broker
client.connect(broker_ip, broker_port, 60)

# Start the MQTT network loop to handle incoming messages
client.loop_start()



# Callback function to handle connection established
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    # Subscribe to the desired topic(s) upon successful connection
    client.subscribe("test/TV1")

# Callback function to handle received messages
def on_message(client, userdata, msg):
    x = ("Received message: " + msg.payload.decode())
    string = msg.payload.decode()
    d = json.loads(string)
    f = json.dumps(d)
    
    if f.startswith('{"devID"'):
        keys_list = list(d.keys())
        deviceName = keys_list[0]
        if int((d["data"][1])/1000)>40:
            abnormality="abnormal"
        else:
            abnormality="normal"
        if int((d["data"][2])/1000)>40:
            abnormalit="abnormal"
        else:
            abnormalit="normal"
        nested_dict ={
            "temperature": (d["data"][0])/100,
            "x axis rms velocity": int((d["data"][1])/1000),
            "z axis rms velocity": (d["data"][2])/1000,
            "x axis peak velocity": (d["data"][3])/1000,
            "z axis peak velocity": (d["data"][4])/1000,
            "abnormality(x)":abnormality,
            "abnormality(z)":abnormalit

        }


        host_address = "http://localhost:8080"

        token = "antar"
        payload = json.dumps(nested_dict)
        

        url = f'{host_address}/api/v1/{token}/telemetry'

# Send POST request to ThingsBoard
        try:
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print('temp!')
            else:
                print('Failed to send data. Status code:', response.status_code)
        except requests.exceptions.RequestException as e:
            print('An error occurred:', str(e))
    else:
            print("hi")
    
# Create an MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set("antariot", "admin@1234")

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Set up connection parameters (replace with your broker's IP address)
broker_ip = "192.168.68.116"
broker_port = 1883

# Connect to the MQTT broker
client.connect(broker_ip, broker_port, 60)

# Start the MQTT network loop to handle incoming messages
client.loop_start()

# Keep the script running to continue receiving messages
while True:
    pass

