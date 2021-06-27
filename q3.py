import numpy as np
from collections import Counter, defaultdict
import settings
import random

def readfile(filename, randomseed=42):
    # open the file to read
    infile = open(filename, "r")
    random.seed(randomseed)

    # get the number of tests
    T = int(infile.readline().strip())
    # print("Number of tests: ", T)

    # results are returned as a list of people ids
    results = []
    for i in range(T):
        # settings.dispaths makes it accessible in a console
        settings.dispaths = defaultdict()

        # read in Vt people and D days
        line = infile.readline().split()
        Vt = int(line[0])
        D = int(line[1])
        # print("Number of people Vt =", Vt)
        # print("Period of",  D, "days")

        # for each day
        for j in range(D):
            # read number of contacts
            nC = int(infile.readline().strip())
            # print("Number of contacts on day", j+1, "=", nC)

            # for each contact
            for k in range(nC):
                # read a line and split to A->B with prob alpha
                contact = infile.readline().split()
                contactA = int(contact[0])
                contactB = int(contact[1])

                #
                # structure here is {'contactB': contactA}
                # Only set if PRNG is less than infection probability
                #
                if random.random() <= float(contact[2]):
                    #
                    # only set {'contactB': contactA}
                    # if contactB is not set
                    # does not handle all cases - what if?
                    # should set contactB = dispaths[contactA]
                    #
                    if contactB not in settings.dispaths.keys():
                        settings.dispaths[contactB] = contactA

        # print(settings.dispaths)

        # used to find the most used person in settings.dispaths 
        track = dict()
        for key, value in settings.dispaths.items():
            if value not in track:
                track[value] = 1
            else:
                track[value] += 1
        maxval = max(track, key=track.get)
        
        # add max value (person) to 
        results.append(maxval)
    infile.close()
    # used to return list of answers to run_many()
    return results

def run_many(filename, runs=5, people=10, randomseed=42):
    """
    runs readfile_1(filename) * 'runs'
    result added to numpy array
    median save to txt file outn.txt (set as parameter?)
    and returned by function
    """
    res = np.empty(shape=(runs, people), dtype='int')
    for i in range(runs):
        results = readfile(filename)
        # print(results)
        res[i] = results
        
    resmed = np.median(res, axis=0)
    np.savetxt("out-{}.txt".format(filename), resmed, delimiter=" ", fmt="%d")
    return resmed

