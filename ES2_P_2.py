from profeta.main import *
from profeta.lib import *

class ora(Belief):
    pass

class mezzora(Belief):
    pass

class reset(Goal):
    pass

class tariffa (Belief):
    pass

class aggiorna_tariffa(Goal):
    pass

class due (Belief):
    pass

class uno (Belief):
    pass

class cinquanta(Belief):
    pass

class venti(Belief):
    pass

class dieci(Belief):
    pass

PROFETA.start()

+ora() >> \
[
    +tariffa(0),
    show_line("hai inserito un ora"),
    aggiorna_tariffa(),
    -tariffa(0)
] 

+mezzora() >> \
[
    +tariffa(0),
     show_line("hai inserito mezzora"),
    aggiorna_tariffa(),
    -tariffa(0)
]

aggiorna_tariffa () / (ora() & tariffa("T")) >> \
[
    -ora(),
    -tariffa("T"),
    "T= 1+T",
    show_line("la tariffa corrente e", "T"),
    +tariffa("T")
]

aggiorna_tariffa () / (mezzora() & tariffa("T")) >> \
[
    -mezzora(),
    -tariffa("T"),
    "T= 0.5+T",
    show_line("la tariffa corrente e", "T"),
    +tariffa("T")
]

reset() / tariffa("T") >> \
[
    -tariffa("T"),
    +tariffa(0)
]

+due() / (tariffa("T") & (lambda: T>0) & (lambda: T>2)) >> \
[
    show_line("hai inserito due euro"),
    -due(),
    -tariffa("T"),
    "T = T-2",
    show_line("ti mancano","T","euro"),
    +tariffa("T")
]

+due() / (tariffa("T") & (lambda: T<=2)) >> \
[
    show_line("emissione biglietto in corso..."),
    -due(),
    -tariffa("T"),
    "T = T-2",
    "Resto = -T",
    +tariffa(0),
    show_line("ti torno il resto di","Resto","euro"),
    reset()
]

+due() >> \
[
    show_line("devi scegliere prima la durata del parcheggio!")
]


+uno() / (tariffa("T") & (lambda: T>0) & (lambda: T>1)) >> \
[
    show_line("hai inserito un euro"),
    -uno(),
    -tariffa("T"),
    "T = T-1",
    show_line("ti mancano","T","euro"),
    +tariffa("T")
]

+uno() / (tariffa("T") & (lambda: T<=1)) >> \
[
    show_line("emissione biglietto in corso..."),
    -uno(),
    -tariffa("T"),
    "T = T-1",
    "Resto = -T",
    +tariffa(0),
    show_line("ti torno il resto di","Resto","euro"),
    reset()
]

+uno() >> \
[
    show_line("devi scegliere prima la durata del parcheggio!")
]

+cinquanta() / (tariffa("T") & (lambda: T>0) & (lambda: T>0.50)) >> \
[
    show_line("hai inserito cinqaunta centesimi"),
    -cinquanta(),
    -tariffa("T"),
    "T = T-0.50",
    show_line("ti mancano","T","euro"),
    +tariffa("T")
]

+cinquanta() / (tariffa("T") & (lambda: T<=0.50)) >> \
[
    show_line("emissione biglietto in corso..."),
    -cinquanta(),
    -tariffa("T"),
    "T = T-0.50",
    "Resto = -T",
    +tariffa(0),
    show_line("ti torno il resto di","Resto","euro"),
    reset()
]

+cinquanta() >> \
[
    show_line("devi scegliere prima la durata del parcheggio!")
]

+venti() / (tariffa("T") & (lambda: T>0) & (lambda: T>0.20)) >> \
[
    show_line("hai inserito venti centesimi"),
    -venti(),
    -tariffa("T"),
    "T = T-0.20",
    show_line("ti mancano","T","euro"),
    +tariffa("T")
]

+venti() / (tariffa("T") & (lambda: T<=0.20)) >> \
[
    show_line("emissione biglietto in corso..."),
    -venti(),
    -tariffa("T"),
    "T = T-0.20",
    "Resto = -T",
    +tariffa(0),
    show_line("ti torno il resto di","Resto","euro"),
    reset()
]

+venti() >> \
[
    show_line("devi scegliere prima la durata del parcheggio!")
]

+dieci() / (tariffa("T") & (lambda: T>0) & (lambda: T>0.10)) >> \
[
    show_line("hai inserito dieci centesimi"),
    -dieci(),
    -tariffa("T"),
    "T = T-0.10",
    show_line("ti mancano","T","euro"),
    +tariffa("T")
]

+dieci() / (tariffa("T") & (lambda: T<=0.10)) >> \
[
    show_line("emissione biglietto in corso..."),
    -dieci(),
    -tariffa("T"),
    "T = T-0.10",
    "Resto = -T",
    +tariffa(0),
    show_line("ti torno il resto di","Resto","euro"),
    reset()
]

+dieci() >> \
[
    show_line("devi scegliere prima la durata del parcheggio!")
]



PROFETA.run_shell(globals())