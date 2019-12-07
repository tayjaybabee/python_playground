import argparse
import os
from appJar import gui
from sense_emu import SenseHat
import statistics
import psutil

process = psutil.Process(os.getpid())

sense = SenseHat()
temps = []
counter = 0

app = gui("Test App", '400x200', useTtk=True, handleArgs=False)
app.info('Created GUI!')
app.info('Showing splash!')

pwd = os.getcwd()

parser = argparse.ArgumentParser(description='Get a pretty version of your common songs!', epilog="And that's how you wubbalubbadub a simple dub")
parser.add_argument("-a", "--action", default=pwd, help="This is the 'a' variable")
parser.add_argument('-v', '--verbose', default=False, help='Run verbosely')

args = parser.parse_args()
a = args
print(a)


def flushBuffer():
    global temps
    global counter
    print('Received flush command')
    print('Appending stat data')
    temps.append('avg: %s' % app.getLabel('avg'))
    temps.append('min: %s' % app.getLabel('min'))
    temps.append('max: %s' % app.getLabel('max'))
    with open('temps.txt', 'w') as f:
        for temp in temps:
            f.write("%s\n" % temp)

    temps = []
    counter = 0


def press():
    flushBuffer()

def getTemp():
    global sense
    global temps
    global counter
    global process
    app.setLabel('temp', sense.temp)
    temps.append(sense.temp)
    counter += 1
    print('Counter is now %s' % counter)
    process_mem = process.memory_info().rss / 1000000
    app.setLabel('mem', process_mem )
    print(process_mem)
    #print(temps)
    if counter >= 10000:
        print('Triggering flush')
        flushBuffer()
        return
    app.setLabel('avg', statistics.median(temps))
    app.setLabel('min', min(temps))
    app.setLabel('max', max(temps))
    app.setLabel('iter', counter)


app.addOpenEntry('Files')
app.addLabel('temp', sense.temp)
app.addLabel('avg', sense.temp)
app.addLabel('min', sense.temp)
app.addLabel('max', sense.temp)
app.addLabel('mem', 0)
app.addLabel('iter', 0)
app.addButton('clear', press)
app.registerEvent(getTemp)

app.go()