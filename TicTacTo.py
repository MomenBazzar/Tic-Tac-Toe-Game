import datetime
import sys
from random import randint
from PyQt5 import QtTest
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.turn = 'X'
        self.show()
        self.oldPos = 0
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_newGame.clicked.connect(self.newGame)
        self.ui.label_result.setText("CHOOSING PLAYERS")
        # ==============================================
        self.ui.p0.clicked.connect(lambda x: self.human(0, 0))
        self.ui.p1.clicked.connect(lambda x: self.human(0, 1))
        self.ui.p2.clicked.connect(lambda x: self.human(0, 2))
        self.ui.p3.clicked.connect(lambda x: self.human(1, 0))
        self.ui.p4.clicked.connect(lambda x: self.human(1, 1))
        self.ui.p5.clicked.connect(lambda x: self.human(1, 2))
        self.ui.p6.clicked.connect(lambda x: self.human(2, 0))
        self.ui.p7.clicked.connect(lambda x: self.human(2, 1))
        self.ui.p8.clicked.connect(lambda x: self.human(2, 2))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def newGame(self):
        for row in range(3):
            for col in range(3):
                self.ui.gridLayout.itemAtPosition(row, col).widget().setText("?")
                self.ui.gridLayout.itemAtPosition(row, col).widget().setStyleSheet(
                    "background-color: rgb(142, 176, 174);\n"
                    "color: rgb(230, 230, 230);\n")
        self.turn = 'X'
        self.ui.label_result.setText(f"[{self.turn}] TURN")
        QtTest.QTest.qWait(5)
        if self.ui.comboBox_x.currentIndex() == 1:
            self.easyAI()
        elif self.ui.comboBox_x.currentIndex() == 2:
            QtTest.QTest.qWait(1000)
            self.ui.gridLayout.itemAtPosition(0, 0).widget().setText("X")
            self.turn = 'O'
            self.ui.label_result.setText(f"[{self.turn}] TURN")
            self.nextTurn()

    def isFinished(self):
        # check rows
        for row in range(3):
            if self.ui.gridLayout.itemAtPosition(row, 0).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(row, 1).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(row, 2).widget().text() != '?':
                for col in range(3):
                    self.ui.gridLayout.itemAtPosition(row, col).widget().setStyleSheet(
                        "background-color: rgb(142, 176, 174);\n"
                        "color: rgb(100, 220, 100);\n")
                self.ui.label_result.setText(f"PLAYER [{self.turn}] WON")
                if self.ui.gridLayout.itemAtPosition(row, 0).widget().text() == 'X':
                    return 'X'
                else:
                    return 'O'

        # check columns
        for col in range(3):
            if self.ui.gridLayout.itemAtPosition(0, col).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(1, col).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(2, col).widget().text() != '?':
                for row in range(3):
                    self.ui.gridLayout.itemAtPosition(row, col).widget().setStyleSheet(
                        "background-color: rgb(142, 176, 174);\n"
                        "color: rgb(100, 220, 100);\n")
                self.ui.label_result.setText(f"PLAYER [{self.turn}] WON")
                if self.ui.gridLayout.itemAtPosition(0, col).widget().text() == 'X':

                    return 'X'
                else:
                    return 'O'

        # check first diagonal
        if self.ui.gridLayout.itemAtPosition(0, 0).widget().text() == \
                self.ui.gridLayout.itemAtPosition(1, 1).widget().text() == \
                self.ui.gridLayout.itemAtPosition(2, 2).widget().text() != '?':
            for row in range(3):
                self.ui.gridLayout.itemAtPosition(row, row).widget().setStyleSheet(
                    "background-color: rgb(142, 176, 174);\n"
                    "color: rgb(100, 220, 100);\n")
            self.ui.label_result.setText(f"PLAYER [{self.turn}] WON")
            if self.ui.gridLayout.itemAtPosition(0, 0).widget().text() == 'X':
                return 'X'
            else:
                return 'O'

        # check second diagonal
        if self.ui.gridLayout.itemAtPosition(0, 2).widget().text() == \
                self.ui.gridLayout.itemAtPosition(1, 1).widget().text() == \
                self.ui.gridLayout.itemAtPosition(2, 0).widget().text() != '?':
            for row in range(3):
                self.ui.gridLayout.itemAtPosition(row, 2 - row).widget().setStyleSheet(
                    "background-color: rgb(142, 176, 174);\n"
                    "color: rgb(100, 220, 100);\n")
            self.ui.label_result.setText(f"PLAYER [{self.turn}] WON")
            if self.ui.gridLayout.itemAtPosition(0, 2).widget().text() == 'X':
                return 'X'
            else:
                return 'O'

        for row in range(3):
            for col in range(3):
                if self.ui.gridLayout.itemAtPosition(row, col).widget().text() == '?':
                    break
            else:
                continue
            break
        else:
            self.ui.label_result.setText(f"NO WINNER")
            return 'T'
        self.turn = 'X' if self.turn == 'O' else 'O'
        self.ui.label_result.setText(f"[{self.turn}] TURN")
        return None

    def nextTurn(self):
        QtTest.QTest.qWait(5)
        if self.turn == 'X':
            if self.ui.comboBox_x.currentIndex() == 0: return
            elif self.ui.comboBox_x.currentIndex() == 1: self.easyAI()
            else: self.hardAI()
        else:
            if self.ui.comboBox_o.currentIndex() == 0: return
            elif self.ui.comboBox_o.currentIndex() == 1: self.easyAI()
            else: self.hardAI()

    def human(self, row, col):
        if self.ui.gridLayout.itemAtPosition(row, col).widget().text() != '?':
            return
        if self.turn == 'X' and self.ui.comboBox_x.currentIndex() != 0:
            return
        if self.turn == 'O' and self.ui.comboBox_o.currentIndex() != 0:
            return
        self.ui.gridLayout.itemAtPosition(row, col).widget().setText(self.turn)
        if self.isFinished() is None:
            self.nextTurn()

    def easyAI(self):
        choices = []
        for row in range(3):
            for col in range(3):
                if self.ui.gridLayout.itemAtPosition(row, col).widget().text() == '?':
                    choices.append((row, col))

        row, col = choices[randint(0, len(choices) - 1)]
        QtTest.QTest.qWait(1000)
        self.ui.gridLayout.itemAtPosition(row, col).widget().setText(self.turn)
        if self.isFinished() is None:
            self.nextTurn()

    def hardAI(self):
        dt_started = datetime.datetime.utcnow()
        self.player = self.turn
        self.opponent = 'O' if self.player == 'X' else 'X'

        bestVal = -1000
        bestMove = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for row in range(3):
            for col in range(3):

                # Check if cell is empty
                if self.ui.gridLayout.itemAtPosition(row, col).widget().text() == '?':

                    # Make the move
                    self.ui.gridLayout.itemAtPosition(row, col).widget().setText(self.player)

                    # compute evaluation function for this
                    # move.
                    moveVal = self.minimax(0, False)

                    # Undo the move
                    self.ui.gridLayout.itemAtPosition(row, col).widget().setText('?')

                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if moveVal > bestVal:
                        bestMove = (row, col)
                        bestVal = moveVal

        while (datetime.datetime.utcnow()-dt_started).total_seconds() < 1:
            QtTest.QTest.qWait(1000)
        self.ui.gridLayout.itemAtPosition(bestMove[0], bestMove[1]).widget().setText(self.player)
        if self.isFinished() is None:
            self.nextTurn()

    def isMovesLeft(self):
        for row in range(3):
            for col in range(3):
                if self.ui.gridLayout.itemAtPosition(row, col).widget().text() == '?':
                    return True
        return False

    def evaluate(self):
        # Checking for Rows for X or O victory.
        for row in range(3):
            if self.ui.gridLayout.itemAtPosition(row, 0).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(row, 1).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(row, 2).widget().text() != '?':

                if self.ui.gridLayout.itemAtPosition(row, 0).widget().text() == self.player:
                    return 10
                else:
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(3):
            if self.ui.gridLayout.itemAtPosition(0, col).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(1, col).widget().text() == \
                    self.ui.gridLayout.itemAtPosition(2, col).widget().text() != '?':

                if self.ui.gridLayout.itemAtPosition(0, col).widget().text() == self.player:
                    return 10
                else:
                    return -10

        # Checking for Diagonals for X or O victory.
        if self.ui.gridLayout.itemAtPosition(0, 0).widget().text() == \
                self.ui.gridLayout.itemAtPosition(1, 1).widget().text() == \
                self.ui.gridLayout.itemAtPosition(2, 2).widget().text() != '?':

            if self.ui.gridLayout.itemAtPosition(0, 0).widget().text() == self.player:
                return 10
            else:
                return -10

        if self.ui.gridLayout.itemAtPosition(0, 2).widget().text() == \
                self.ui.gridLayout.itemAtPosition(1, 1).widget().text() == \
                self.ui.gridLayout.itemAtPosition(2, 0).widget().text() != '?':

            if self.ui.gridLayout.itemAtPosition(0, 2).widget().text() == self.player:
                return 10
            else:
                return -10

        # Else if none of them have won then return 0
        return 0

    def minimax(self, depth, isMax):
        score = self.evaluate()

        # If Maximizer has won the game return his/her
        # evaluated score
        if score == 10:
            return score - depth

        # If Minimizer has won the game return his/her
        # evaluated score
        if score == -10:
            return score + depth

        # If there are no more moves and no winner then
        # it is a tie
        if not self.isMovesLeft():
            return 0

        # If this maximizer's move
        if isMax:
            best = -1000

            # Traverse all cells
            for row in range(3):
                for col in range(3):

                    # Check if cell is empty
                    if self.ui.gridLayout.itemAtPosition(row, col).widget().text() == '?':
                        # Make the move
                        self.ui.gridLayout.itemAtPosition(row, col).widget().setText(self.player)

                        # Call minimax recursively and choose
                        # the maximum value
                        best = max(best, self.minimax(depth + 1, not isMax))

                        # Undo the move
                        self.ui.gridLayout.itemAtPosition(row, col).widget().setText('?')
            return best

        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for row in range(3):
                for col in range(3):

                    # Check if cell is empty
                    if self.ui.gridLayout.itemAtPosition(row, col).widget().text() == '?':
                        # Make the move
                        self.ui.gridLayout.itemAtPosition(row, col).widget().setText(self.opponent)

                        # Call minimax recursively and choose
                        # the maximum value
                        best = min(best, self.minimax(depth + 1, not isMax))

                        # Undo the move
                        self.ui.gridLayout.itemAtPosition(row, col).widget().setText('?')
            return best


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
