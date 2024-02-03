import time
import RPi.GPIO as GPIO
import sys
import urllib2

#from LED_display import display_number
def getSensorData():
    GPIO.setmode(GPIO.BOARD)

    trig = 14  # sends the signal
    echo = 40  # listens for the signal

    GPIO.setwarnings(False)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)



        

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0: pass

    start = time.time()  # reached when echo listens

    while GPIO.input(echo) == 1:  pass

    end = time.time() # reached when signal arrived

    distance = ((end - start) * 34300) / 2

    return (int (distance))
def main():
    if len(sys.argv) < 2:
        print('Usage: python tstest.py PRIVATE_KEY')
        exit(0)
    print 'starting...'
    
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % sys.argv[1]
       
    while True:
        try:

            distance = getSensorData()
            f = urllib2.urlopen(baseURL + "&field1=%s" % int(distance/5))
            print f.read()
            f.close()
            sleep(15)
        except:
            print 'exiting.'
            break

         

       
            
# call main
if __name__ == '__main__':
    main()            
