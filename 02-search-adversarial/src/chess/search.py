from abc import *
from state import State
import sys

MAX_FLOAT = sys.float_info.max
MIN_FLOAT = -MAX_FLOAT


class AdversarialSearch(object):
    """
    Apstraktna klasa za suparnicku/protivnicku pretragu.
    """

    def __init__(self, board, max_depth):
        """
        :param board: tabla koja predstavlja pocetno stanje.
        :param max_depth: maksimalna dubina pretrage (koliko poteza unapred).
        :return:
        """
        self.initial_state = State(board, parent=None)
        self.max_depth = max_depth

    @abstractmethod
    def perform_adversarial_search(self):
        """
        Apstraktna metoda koja vrsi pretragu i vraca sledece stanje.
        """
        pass


class Minimax(AdversarialSearch):
    def perform_adversarial_search(self):
        # TODO 1: Implementirati minimax algoritam
        pass


class AlphaBeta(AdversarialSearch):

    def perform_adversarial_search(self):
        # TODO 4: Implementirati alpha-beta algoritam
        pass
