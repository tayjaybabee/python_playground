import argparse
import os
from appJar import gui

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


def press():
    filepath = app.getEntry('Files')
    with open(filepath) as path:
        line = path.readline()
        cnt = 1
        while line:
            app.addLabel(cnt.__str__(), line.strip())
            app.setLabelBg(cnt.__str__(), "red")
            line = path.readline()
            cnt += 1


app.addOpenEntry('Files')
app.addButton('Begin', press)

app.go()