#import libraries
from profeta.lib import *
from profeta.main import *

class ora(Belief):
    pass

class mezzora(Belief):
    pass

class reset(Goal):
    pass

class tariffa(Belief):
    pass

class uno(Belief):
    pass

class due(Belief):
    pass

class cinquanta(Belief):
    pass

class venti (Belief):
    pass

class dieci(Belief):
    pass

#instantiate the engine
PROFETA.start()

#define event plans

# LO SHOW_LINE DA ERRORE CON LE LETTERE MAIUSCOLE! SOLO LE VARIABILI MAIUSCOLE!

+ora() / tariffa("X") >> \
[
    -tariffa("X"), 
    -ora(), 
    "X=X+1", 
    +tariffa("X"), 
    show_line("hai inserito","X","ore")
]

+ora() >> \
[
    -ora(),
    +tariffa(1),
    show_line("hai inserito 1 ora")
]

+mezzora() / tariffa("X") >> \
[
    -tariffa("X"),
    -mezzora(), 
    "X=X+0.5",
    +tariffa("X"), 
    show_line("hai inserito","X","ore")
]

+mezzora() >> \
[
    -mezzora(),
    +tariffa(0.5),
    show_line("hai inserito mezz ora")
]

reset() / tariffa("X") >> \
[
    -tariffa("X"),
    reset(),
    show_line("durata resettata")
]

+due() / (tariffa("X") & (lambda: X>2)) >> \
[
    -due(),
    -tariffa("X"),
    "X=X-2",
    +tariffa("X"),
    show_line("devi ancora inserire","X","euro")
]

+due() / tariffa("X")>> \
[
    -due(),
    -tariffa("X"),
    "X=-X+2",   # valore assoluto e il resto 
    +tariffa("X"),
    show_line("emissione biglietto in corso.. ti torno il resto di","X","euro")
]

+due()  >> \
[   
    -due(),
    show_line("selezionare prima la durata, ti restituisco i soldi")
]

+uno() / (tariffa("X") & (lambda: X>1)) >> \
[
    -uno(),
    -tariffa("X"),
    "X=X-1",
    +tariffa("X"),
    show_line("devi ancora inserire","X","euro")
]

+uno() / tariffa("X")  >> \
[
    -uno(),
    -tariffa("X"),
    "X=-X+1", # valore assoluto e il resto
    +tariffa("X"),
    show_line("emissione biglietto in corso.. ti torno il resto di","X","euro")
]

+uno()  >> \
[   
    -uno(),
    show_line("selezionare prima la durata, ti restituisco i soldi")
]


+cinquanta() / (tariffa("X") & (lambda: X>0.5)) >> \
[
    -cinquanta(),
    -tariffa("X"),
    "X=X-0.50", # mi raccomando mettere due cifre decimali almeno altrimenti valori strani
    +tariffa("X"),
    show_line("devi ancora inserire","X","euro")
]

+cinquanta() / tariffa("X") >> \
[
    -cinquanta(),
    -tariffa("X"),
    "X=-X+0.50", # il resto e il valore assoluto
    +tariffa("X"),
    show_line("emissione biglietto in corso.. ti torno il resto di","X","euro")
]

+cinquanta()  >> \
[   
    -cinquanta(),
    show_line("selezionare prima la durata, ti restituisco i soldi")
]

+venti() / (tariffa("X") & (lambda: X>0.2)) >> \
[
    -venti(),
    -tariffa("X"),
    "X=X-0.20", # mi raccomando mettere due cifre decimali almeno altrimenti valori strani
    +tariffa("X"),
    show_line("devi ancora inserire","X","euro")
]

+venti() / tariffa("X") >> \
[
    -venti(),
    -tariffa("X"),
    "X=-X+0.20", # il resto e il valore assoluto
    +tariffa("X"),
    show_line("emissione biglietto in corso.. ti torno il resto di","X","euro")
]

+venti()  >> \
[   
    -venti(),
    show_line("selezionare prima la durata, ti restituisco i soldi")
]

+dieci() / (tariffa("X") & (lambda: X>0.1)) >> \
[
    -dieci(),
    -tariffa("X"),
    "X=X-0.10", # mi raccomando mettere due cifre decimali almeno altrimenti valori strani
    +tariffa("X"),
    show_line("devi ancora inserire","X","euro")
]

+dieci() / tariffa("X") >> \
[
    -dieci(),
    -tariffa("X"),
    "X=-X+0.10", # il valore assoluto e il resto
    +tariffa("X"),
    show_line("emissione biglietto in corso.. ti torno il resto di","X","euro")
]

+dieci()  >> \
[   
    -dieci(),
    show_line("selezionare prima la durata, ti restituisco i soldi")
]



#run the engine shell
PROFETA.run_shell(globals())