import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

def getState():
    file = open("D:\\Documents\\Mining\\sunmine\\state.txt", "r")
    readLine = file.readline()
    file.close()
    return readLine

def setState(state):
    logging.debug("Editing file.")
    file = open("D:\\Documents\\Mining\\sunmine\\state.txt", "w")
    file.write(state)
    file.close()
