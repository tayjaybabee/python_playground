from appJar import gui

winFindDupesTitle = 'Find Duplicate Titles'
winCreateStatsTitle = 'Plot Statistics'
winCommonTitle = 'Find Common'
winParseCommonTitle = 'Parse previous session output'


class Error(Exception):
    """
    Base error class for this module
    """
    pass


class ButtonError(Error):
    """
    Exception raised for button errors
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class FDNotImplementedError(Error):
    """
    Exception raised for pressing a button that's not implemented
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message



def winFindDupe():
    app.startSubWindow('Find Duplicates:', modal=True, transient=True)
    app.setSize(200, 200)
    app.addOpenEntry('Playlist File')
    app.stopSubWindow()
    app.showSubWindow('Find Duplicates:')


def winCreateStats():
    app.startSubWindow('Plot Statistics:', modal=True, transient=True)
    app.setSize(100, 100)
    app.addOpenEntry('Playlist file')
    app.addButton('Parse', press)
    app.stopSubWindow()
    app.showSubWindow('Plot Statistics:')


def not_imp():
    raise FDNotImplementedError


def press(btn):
    global winFindDupesTitle
    global winCreateStatsTitle
    global winCommonTitle
    global winParseCommonTitle

    if btn == 'Find Duplicates':
        winFindDupe()
    elif btn == 'Create Statistics':
        winCreateStats()
    elif btn == 'Find Common Among Playlists':
        app.info('Not implemented, buddy')
    elif btn == 'Parse common.txt':
        app.info('Not implemented, buddy')
    else:
        raise ButtonError

    app.info('Button was pressed: %s' % btn)


app = gui("Test App", '400x200', useTtk=True)
app.info('Created GUI!')
app.info('Showing splash!')
app.showSplash('the test app')

app.info('Setting theme...')
app.setTtkTheme('black')
app.info("Set theme to '%s'" % app.getTtkTheme())

app.addButton('Find Duplicates', press)
app.addButton('Create Statistics', press)
app.addButton('Find Common Among Playlists', press)
app.addButton('Parse common.txt', press)

app.go()
