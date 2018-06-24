from profeta.lib import *
from profeta.main import *

class cinquanta(Belief):
    pass

class venti(Belief):
    pass

class dieci(Belief):
    pass

class cinque(Belief):
    pass

class restituisci(Goal):
    pass

class totale(Belief):
    pass

class aggiorna_totale(Goal):
    pass

PROFETA.start()


+cinquanta("C") >> \
[
    aggiorna_totale()
]


+venti("V") >> \
[
    aggiorna_totale()
]

+dieci("D") >> \
[
    aggiorna_totale()
]

+cinque("S") >> \
[
    aggiorna_totale()
]

aggiorna_totale() / (totale("T") & cinquanta("C") & venti("V") & dieci("D") & cinque("S")) >> \
[
    -totale("T"),
    "T= 50*C+20*V+10*D+5*S",
    +totale("T")
] 

# Svuoto prima il serbatoio piu grande, cioe quello da 50 cent e poi a scalare

restituisci("M") / (totale("T") & cinquanta("C") & (lambda: T!=0) & (lambda: M>=50) & (lambda: C>0) & (lambda: M>0)) >> \
[
    -cinquanta("C"),
    "M=M-50",
    "C=C-1",
    +cinquanta("C"),
    restituisci("M")
]

restituisci("M") / (totale("T") & venti("V")  & (lambda: T>0) & (lambda: M>=20) & (lambda: V>0) & (lambda: M>0)) >> \
[
    -venti("V"),
    "M=M-20",
    "V=V-1",
    +venti("V"),
    restituisci("M")
]

restituisci("M") / (totale("T") & dieci("D") & (lambda: T>0) & (lambda: M>=10) & (lambda: D>0) & (lambda: M>0)) >> \
[
    -dieci("D"),
    "M=M-10",
    "D=D-1",
    +dieci("D"),
    restituisci("M")
]

restituisci("M") / (totale("T") & cinque("S") & (lambda: T>0) & (lambda: M>=5) & (lambda: S>0) & (lambda: M>0)) >> \
[
    -cinque("S"),
    "M=M-5",
    "S=S-1",
    +cinque("S"),
    restituisci("M")
]

restituisci("M") / (lambda: M==0) >> \
[
    show_line("ti ho restituito il tuo resto!")
]


restituisci("M") / (lambda: M>0 & T==0) >> \
[
    show_line("non ho il resto da restituirti, ti ho mangiato","M","cent")
]


PROFETA.assert_belief((cinquanta(2)))
PROFETA.assert_belief((venti(3)))
PROFETA.assert_belief((dieci(1)))
PROFETA.assert_belief((cinque(2)))
PROFETA.assert_belief((totale(0)))

PROFETA.run_shell(globals())