import logging
import pathlib

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
fn = pathlib.Path(__file__).parent / 'state.txt'

def getState():
    file = open(fn, "r")
    readLine = file.readline()
    file.close()
    return readLine

def setState(state):
    logging.debug("Editing file.")
    file = open(fn, "w")
    file.write(state)
    file.close()
