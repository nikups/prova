from profeta.lib import *
from profeta.main import *

class free(Belief):
    pass

class free_all_A(Goal):
    pass

class free_all_B(Goal):
    pass

class alloca_sopra(Goal):
    pass

class alloca_sotto(Goal):
    pass

class occupati(Belief):
    pass

class alloca(Goal):
    pass

class current_shift(Belief):
    pass

class isFree(Goal):
    pass




PROFETA.start()

+free("Numero","Posto") / (lambda: 2<=Numero<=34) >> \
[
    show_line("inserisco posto libero")
]

+free("Numero","Posto") >> \
[
    -free("Numero","Posto"),
    show_line("non hai inserito un posto possibile")
]

free_all_A("Numero", "Posto") / (free("Numero","Posto") & (lambda: Posto =='a') & (lambda: Numero<=34)) >> \
[
    "Posto='b'",
    +free("Numero","Posto"),
    free_all_B("Numero","Posto") 
]

free_all_B("Numero","Posto") / (free("Numero","Posto") & (lambda: Posto =='b') & (lambda: Numero<=34)) >> \
[
    "Posto='a'",
    "Numero=Numero+1",
    +free("Numero","Posto"),
    free_all_A("Numero","Posto")
]

free_all_A() >> \
[
    show_line("libero tutti i posti"),
    +free(2,'a'),
    free_all_A(2,'a')
]

isFree("Numero","Posto","N") / (free("Numero","Posto") & current_shift("processed","X")) >> \
[
    show_line("il numero va bene"),
    alloca_sopra("N","Numero","Posto","X"),
    -current_shift("processed","X")
]

isFree("Numero","Posto","N") / occupati("Numero","Posto") >> \
[
    "Numero = Numero -1 ",
    isFree("Numero")
]

alloca_sopra("N","Numero","Posto","X") / (free("Numero","Posto") & (lambda: Numero <= 17) & (lambda: N>0)) >> \
[
    -free("Numero","Posto"),
    +occupati("Numero","Posto"),
    show_line("ho allocato il posto", "Numero", "Posto"),
    "Posto = 'b'",
    alloca_sopra("N","Numero","Posto","X"),
    "N=N-2",
    "X=X+1",
    "Numero= Numero + X",
    "Posto='a'",
    alloca_sotto("N","Numero","Posto","X"),
] 

alloca_sopra("N","Numero","Posto","X") / (free("Numero","Posto") & (lambda: N>=0)) >> \
[
    show_line("posti allocati"),
    -current_shift("X"),
    +current_shift("processed","X")
] 

alloca_sotto("N","Numero","Posto","X") / (free("Numero","Posto") & (lambda: Numero > 17) & (lambda: N>0)) >> \
[
    -free("Numero","Posto"),
    +occupati("Numero","Posto"),
    show_line("ho allocato il posto", "Numero", "Posto"),
    "Posto = 'b'",
    alloca_sotto("N","Numero","Posto","X"),
    "N=N-2",
    "X=X+1",
    "Numero= Numero - X",
    "Posto='a'",
    alloca_sopra("N","Numero","Posto","X"),
] 

alloca_sotto("N","Numero","Posto","X") / (free("Numero","Posto") & (lambda: N>=0)) >> \
[
    show_line("posti allocati"),
    -current_shift("X"),
    +current_shift("processed","X")

] 

alloca("N") / (free("Numero","Posto") & current_shift("processed","X")) >> \
[
    show_line("alloco","N","posti"),
    "Numero = 17 - X + 1",
    isFree("Numero","Posto","N")
]

alloca("N") / free("Numero","Posto") >> \
[
    show_line("alloco","N","posti"),
    "Numero = 17",
    "X=0",
    +current_shift("X"),
    "Posto= 'a'",
    alloca_sopra("N","Numero","Posto","X")
]

alloca("N") >> \
[
    show_line("non ci sono posti liberi, mi dispiace")
]











PROFETA.run_shell(globals())