import logging
import pathlib

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
fn = pathlib.Path(__file__).parent / 'state.txt'

class MiningState:


    @staticmethod
    def get_state():
        file = open(fn, "r")
        read_line = file.readline()
        file.close()
        return read_line

    @staticmethod
    def set_state(state):
        logging.debug("Editing file.")
        file = open(fn, "w")
        file.write(state)
        file.close()
