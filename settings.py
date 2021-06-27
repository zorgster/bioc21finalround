from collections import defaultdict

def init():
    global tol, cases, nD, nP, exonStops, exonStarts, intronStops, intronStarts, dispaths
    cases = 0
    nD = 0
    nP = 0
    dispaths = defaultdict()
    exonStarts = defaultdict(list)
    exonStops = defaultdict(list)
    intronStarts = defaultdict(list)
    intronStops = defaultdict(list)
    tol = 0