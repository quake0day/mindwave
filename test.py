import mindwave
import time

headset = mindwave.Headset('/dev/tty.MindWave','625f')
time.sleep(2)
headset.autoconnect()

#headset.connect()
print "Connecting.."

while (headset.status) != 'connected':
    print headset.status
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.autoconnect()
        print "Retrying connect..."

print "Connected."

while True:
    print "Attention: %s, Meditation: %s" % (headset.attention, headset.meditation)
    time.sleep(2)
