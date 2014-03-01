import ioflo
from ioflo.base import aiding

from ioflo.base.consoling import getConsole
console = getConsole()

# These test should be redone with assert statements so that can get a boolean
# result that the test passed
def TestConsoleNB():
    """Class ConsoleNB self test"""
    try:
        print "Testing ConsoleNB"
        console = ConsoleNB()
        console.open()

        console.put("Testing nonblocking console\n")
        console.put("Enter characters and hit return: ")
        x = ''
        while not x:
            x = console.getLine()
        console.put("You typed: " + x)
    finally:
        console.close()

def TestSocketUdpNB():
    """Class SocketUdpNb self test """
    try:
        print "Testing SocketUdpNb"
        serverA = aiding.SocketUdpNb(port = 6101)
        serverA.reopen()
        serverB = aiding.SocketUdpNb(port = 6102)
        serverB.reopen()

        serverA.send("A sends to B",serverB.ha)
        print serverB.receive()
        serverA.send("A sends to A",serverA.ha)
        print serverA.receive()
        serverB.send("B sends to A",serverA.ha)
        print serverA.receive()
        serverB.send("B sends to B",serverB.ha)
        print serverB.receive()

    finally:
        serverA.close()
        serverB.close()

def TestSocketUxdNB():
    """Class SocketUxdNb self test """
    console.reinit(verbosity=console.Wordage.verbose)
    try:
        print "Testing SocketUxdNb"
        serverA = aiding.SocketUxdNb(ha = '/tmp/uxdA')
        serverA.reopen()
        serverB = aiding.SocketUxdNb(ha = '/tmp/usdB')
        serverB.reopen()
        serverC = aiding.SocketUxdNb(ha = '/tmp/usdC')
        serverC.reopen()

        serverA.send("A sends to B",serverB.ha)
        print serverB.receive()
        serverA.send("A sends to C",serverC.ha)
        print serverC.receive()
        serverA.send("A sends to A",serverA.ha)
        print serverA.receive()
        serverB.send("B sends to A",serverA.ha)
        print serverA.receive()
        serverC.send("C sends to A",serverA.ha)
        print serverA.receive()
        serverB.send("B sends to B",serverB.ha)
        print serverB.receive()
        serverC.send("C sends to C",serverC.ha)
        print serverC.receive()

        serverA.send("A sends to B again",serverB.ha)
        print serverB.receive()
        serverA.send("A sends to C again",serverC.ha)
        print serverC.receive()
        serverA.send("A sends to A again",serverA.ha)
        print serverA.receive()
        serverB.send("B sends to A again",serverA.ha)
        print serverA.receive()
        serverC.send("C sends to A again",serverA.ha)
        print serverA.receive()
        serverB.send("B sends to B again",serverB.ha)
        print serverB.receive()
        serverC.send("C sends to C again",serverC.ha)
        print serverC.receive()

        print serverA.receive()
        print serverB.receive()
        print serverC.receive()


    finally:
        serverA.close()
        serverB.close()

def TestBlend0(u = .25, s = .75, steps = 10):
    """Test the Blend0 function

    """
    u = abs(u)
    s = abs(s)
    steps = abs(steps)
    span = u + s
    ss = span / steps
    for x in xrange(-(steps + 1), steps + 2, 1):
        d = x * ss
        b = Blend0(d,u,s)
        print d, b

def Test():
    """Module self test



    """
    pass

if __name__ == "__main__":
    #Test()
    TestSocketUxdNB()
