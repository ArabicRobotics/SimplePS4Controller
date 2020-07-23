# you can Add your code In this File (Demo.py)
import os
import time
# import the related Classes :) 
from clsControllerData import ControllerData
from SimplePS4Controller import SimplePS4Controller
if __name__ == "__main__":
    ps4 = SimplePS4Controller()
    ps4.start() # Start the PlayStation Listen :) 
    i=100
    while(i>0):
       
        time.sleep(0.5)
        os.system('clear')
        if ControllerData.newData == True: # hmmm , I got a new data from the controller 
            print "Buttons Data"
            print ControllerData.button_data            
            x = ControllerData.axis_data[0]

            y = (ControllerData.axis_data[1]*-1) # flip the y data 
            angle =  ControllerData.getAngle360(0,0,ControllerData.L_Ball_H,ControllerData.L_Ball_V)
            print ("Angle : "+str(angle))
            print ("Simplified Data")
            ControllerData.printSimplifiedValues()
            # Set the New Data as Old data ( I got it , and used it )
            ControllerData.newData=False
        print(ps4.cTime)
        print ("timer"+str(i))
        i = i-1
    ps4.stop()
    time.sleep(0.1)# wait to stop the Playstation
    print ("terminated ")

    