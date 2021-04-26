from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setBaseSize(500,500)
window.setFixedWidth(900)
window.setFixedHeight(600)
table = QtWidgets.QTableWidget(10,7)
table.setHorizontalHeaderLabels(['Nabavka', 'Kod', 'Mesto', 'Narucilac', 'Rok', 'Vrednost','Tip'])
exq = QtWidgets.QRadioButton('ekskurzije')
radovi = QtWidgets.QRadioButton('radovi')
ostalo = QtWidgets.QRadioButton('ostalo')
layout = QtWidgets.QHBoxLayout()
levo = QtWidgets.QVBoxLayout()
dugmad = QtWidgets.QHBoxLayout()
desno = QtWidgets.QVBoxLayout()
ime = QtWidgets.QLabel('Nabavka: ')
vrednost = QtWidgets.QLabel('Vrednost: ')
mesto = QtWidgets.QLabel('Mesto:')
desno.addWidget(ime)
desno.addWidget(vrednost)
desno.addWidget(mesto)
levo.addLayout(dugmad)
levo.addWidget(table)
layout.addLayout(levo)
layout.addLayout(desno)
dugmad.addWidget(exq)
dugmad.addWidget(radovi)
dugmad.addWidget(ostalo)
window.setLayout(layout)
window.show()
app.exec_()

