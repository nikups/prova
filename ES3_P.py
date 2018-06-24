from profeta.lib import *
from profeta.main import *

class cube(Belief):
    pass

class follows(Belief):
    pass

class move(Goal):
    pass

class pick(Goal):
    pass

class owned(Belief):
    pass

class upon(Goal):
    pass

class toPick(Belief):
    pass

# TRA VIRGOLETTA SIGNIFICA STRINGA!!! NUMERI SENZA VIRGOLETTE!!!!

PROFETA.start()

+cube("X","Y","Color") >> \
[
    show_line("hai inserito un nuovo cubo o hai spostato correttamente il cubo")
]

+cube("X","Y") >> \
[
    -cube("X","Y"),
     show_line("devi specificare il colore o entrambe le coordinate")
]

+cube("X") >> \
[
    -cube("X"),
    show_line("devi specificare anche l altra coordinata e il colore")
]

+cube("Color") >> \
[
    -cube("Color"),
    show_line("devi specificare anche le coordinate x,y")
]

+follows("Color1","Color2") / (cube("X","Y","Color1") & cube("Z","G","Color2"))  >> \
[
    show_line("hai inserito un nuovo ordine per i cubi"),
    move()
    
] 

+follows("Color1","Color2") / cube("X","Y","Color1")  >> \
[
    -follows("Color1","Color2"),
    show_line("inserisci almeno un altro cubo")
] 

+follows("Color1","Color2") >> \
[
    -follows("Color1","Color2"),
    show_line("inserisci un cubo prima oppure cubi non trovati!")
]

move() / (owned("Color1") & cube("Z","G","Color2") & follows("Color1","Color2")) >> \
[
    show_line("mi muovo verso le coordinate del cubo 2","Z","G", "Color2"),
    upon()
]

move() / (follows("Color1","Color2") & cube("X","Y","Color1")) >> \
[
    +toPick("Color1"),
    show_line ("mi muovo verso le coordinate","X","Y","del primo cubo","Color1"),
    pick()
]

move() >> [show_line("specificare prima un ordine di cattura")]

pick() / (toPick("Color1") & cube("X","Y","Color1")) >> \
[
    -toPick("Color1"),
    +owned("Color1"),
    show_line("ho preso il cubo di colore","Color1"),
    move()
]

pick() >> [show_line("specificare prima il cubo da catturare o l ordine di cattura")]

upon() / (cube("Z","G","Color2") & cube("X","Y","Color1") & owned("Color1") & follows("Color1","Color2")) >> \
[
    -cube("X","Y","Color1"),
    "Y=G+Y",
    "X=Z",
    show_line("X","Y"),
    +cube("X","Y","Color1"),
    -owned("Color1"),
    -follows("Color1","Color2")
]

upon() >> [show_line("prendi il cubo prima e muoviti verso l altro")]

#### MI RACCOMANDO PASSARE I NUMERI SENZA VIRGOLETTE!!! ALLORA NON FUNZIONA ####

PROFETA.assert_belief(cube(10,1,"red"))
PROFETA.assert_belief(cube(1,1,"blue"))
PROFETA.assert_belief(cube(5,1,"yellow"))
PROFETA.assert_belief(cube(15,1,"green"))
PROFETA.assert_belief(follows("red","blue"))
PROFETA.assert_belief(follows("green","red"))
PROFETA.assert_belief(follows("yellow","green"))




PROFETA.run_shell(globals())