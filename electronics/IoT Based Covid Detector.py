########################
# Python script to receive and record the data
# by Raunak Singh
########################

## requires pySerial to be installed 
import serial
import datetime
import pandas as pd

# change the serial port to the one of your arduino
serial_port1 = '/dev/cu.usbmodem1422201'
serial_port2 = '/dev/cu.usbserial-D3070P02'
baud_rate = 9600 # set as serial monitor baud rate
# data will be written to this csv file
write_to_file_path = "record_sheet.csv"

# define serial with port and baud rate
ser1 = serial.Serial(serial_port1, baud_rate)
ser2 = serial.Serial(serial_port2, baud_rate)
# define a new dataframe with one column
df =pd.DataFrame(["default"],columns=["name,temp"])

i=0 # counter
# while input is coming
while True: 
    line1 = ser1.readline() # read the line from the serial port
    line2 = ser2.readline()

    line1 = line1.decode("utf-8") #ser.readline returns a binary, convert to string
    line2 = line2.decode("utf-8") #ser.readline returns a binary, convert to string
    line = line1+','+line2+''
    pos =repr(line).find(",") # find comma in the line and mark it's position
    line = repr(line).replace("'","").replace(r"\r","").replace(r"\n","") # clean the string of unwanted characters
    print(line) # debugging code
    nametemp = line[:pos-1] # select the name of user
    df.loc[i] = nametemp # insert name in name,temp column
    i+=1 # increase counter by 1
    
    # show the code after every 3 lines
    if (i%3==0):
        # record the time when input recieved
        df["DateTime"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # write all of this data to record_sheet.csv
        df.to_csv(write_to_file_path)

ser1.close() # close serial1
ser2.close() # close serial2
#____DONE_____#