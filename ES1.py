import pylab

class PIDController:
    def __init__(self,kp,ki,kd):
        self.__kp = kp
        self.__ki = ki
        self.__kd = kd
        self.__integral_term = 0
        self.__previous_error = 0
    
    def evaluate (self,target,measure,delta_t):
        self.__error = target - measure
        derivative = (self.__error-self.__previous_error) / delta_t
        self.__previous_error = self.__error
        self.__integral_term = self.__integral_term + self.__error * delta_t
        output = self.__error*self.__kp + self.__integral_term * self.__ki + derivative * self.__kd
        return output

class G :
    def __init__ (self):
        self.__x1 = 0
        self.__x2 = 0
    
    def evaluate (self,u,delta_t):
        x1 = self.__x1 + delta_t*self.__x2
        x2 = -3*delta_t*self.__x1 + (-0.5*delta_t +1)*self.__x2 + delta_t*u
        y = self.__x1
        self.__x1 = x1
        self.__x2 = x2
        return y

out = []
t = []
yinf = 1. # valore all infinito -> METTERE IL PUNTO ALTRIMENTI NON FUNZIONA!!!

# i poli sono cc con parte reale pari a -0.25 (0.5 /2). Quindi il transitorio dura :
# 3/-Re[p] = circa 12s -> considero 20s e un tempo di campionamento 10000 volte
# piu piccolo -> 0.0020 con numero di punti pari a 20/delta_t

delta_t = 0.0020
points = int(20 / delta_t)
u=1
y=0

# apro il file per salvarmi i dati:

f= open('/home/nikups/Scrivania/Uni/PROGRAMMAZIONE_SIST_ROBOTICI/ESERCITAZIONI/ES1/dati1','w')


sistema1 = G()
PID = PIDController(10,10,10)

for i in range (0,points):
    pid_out = PID.evaluate(u,y,delta_t)
    y = sistema1.evaluate(pid_out,delta_t)
    out.append(y)
    t.append(i*delta_t)
    # Plottare con GNUPLOT -> salvo sul file
    f.write(str(t[i])+' '+str((out[i]))+'\n')

# PER PLOTTARE: spostarsi nella cartella dove vi e il file da plottare
# DA TERMINALE: gnuplot
# POI SCRIVERE DA GNUPLOT:
# plot "nome_file" using 1:2 with lines

##### CALCOLO TEMPO DI ASSESTAMENTO #####

t_as = 0
i=0

for i in range (0, points):
     if (float(out[i]) > ((yinf*95)/100)) and (float(out[i]) < ((yinf*105)/100)):
         t_as = t[i] # prendo il tempo al tempo i 
         break
    # mi metto in una banda del 5 percento 


print("il tempo di assestamento e: "+str(t_as))

########################################## 

pylab.figure()
pylab.plot(t,out)
pylab.show()






