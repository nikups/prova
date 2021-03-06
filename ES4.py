import pylab

class PIDController:
    def __init__(self,kp,ki,kd):
        self.__kp = kp
        self.__ki = ki
        self.__kd = kd
        self.__integral_term = 0
        self.__previous_error = 0
    
    def evaluate (self, target, measure, delta_t):
        self.__error = target - measure
        derivative = (self.__error - self.__previous_error) / delta_t
        self.__previous_error = self.__error
        self.__integral_term = self.__integral_term + self.__error * delta_t
        output = self.__error * self.__kp + self.__integral_term*self.__ki + derivative*self.__kd
        return output

class G : 
    def __init__ (self):
        self.__x1 = 0
        self.__x2 = 0
    
    def evaluate (self,u,delta_t):
        x1 = self.__x1 + delta_t*self.__x2
        x2 = -4*delta_t*self.__x1 + ((-5*delta_t) +1)*self.__x2 + delta_t*u
        y = 8*self.__x1
        self.__x1 = x1
        self.__x2 = x2
        return y

yinf = 8./4. # METTERE COSI ALTRIMENTI NON FUNZIONA!!!

t=[]
out1 = []
# Per fare il confronto con il sistema originario mi salvo sia l uscita senza che con PID
outpid = []

u = 1
y2 = 0
y=0.
y1 = 0
i=0

f = open('/home/nikups/Scrivania/Uni/PROGRAMMAZIONE_SIST_ROBOTICI/ESERCITAZIONI/ES4/dati4', 'w')
f2 = open('/home/nikups/Scrivania/Uni/PROGRAMMAZIONE_SIST_ROBOTICI/ESERCITAZIONI/ES4/dati4_pid', 'w')

# Scelta del tempo di campionamento
# I poli sono reali a parte reale negativa
# Il polo dominante e -1 poiche piu vicino all asse reale
# La durata del transitorio e 3/-Re(p) -> 3s
# Scelgo 5s e t.c. 10000 volte piu piccolo -> 0.0005
# Numero di punti -> points = int(5/delta_t)

delta_t = 0.0005
points = int(5/delta_t)

sistema1 = G()
sistema2 = G()
PID = PIDController(15,10,0.5)

# AL PID METTERE L USCITA GIUSTA CIOE QUELLA DEL SISTEMA 2 CON PID

for i in range(0, points):
    pid_output = PID.evaluate(u,y2,delta_t)
    y2 = sistema2.evaluate(pid_output,delta_t)
    y1 = sistema1.evaluate(u,delta_t)
    out1.append(y1)
    outpid.append(y2)
    t.append(i*delta_t)
    f.write(str(t[i])+' '+str(out1[i])+'\n')
    f2.write(str(t[i])+' '+str(outpid[i])+'\n')

# PER PLOTTARE: spostarsi nella cartella dove vi e il file da plottare
# DA TERMINALE: gnuplot
# POI SCRIVERE DA GNUPLOT:
# plot "nome_file" using 1:2 with lines

##### CALCOLO TEMPO DI ASSESTAMENTO SENZA PID #####

t_as = 0.

for i in range (0, points):
     if (float(out1[i]) > ((yinf*95)/100)) and (float(out1[i]) < ((yinf*105)/100)):
         t_as = t[i] # prendo il tempo al tempo i 
         break
    # mi metto in una banda del 5 percento 


print("il tempo di assestamento senza pid e: "+str(t_as))

##################################################

##### CALCOLO TEMPO DI ASSESTAMENTO CON PID #####

t_as2 = 0.

for i in range (0, points):
     if (float(outpid[i]) > ((u*95)/100)) and (float(outpid[i]) < ((u*105)/100)):
         t_as2 = t[i] # prendo il tempo al tempo i 
         break
    # mi metto in una banda del 5 percento 


print("il tempo di assestamento con PID e: "+str(t_as2))

##################################################


pylab.figure(1)
pylab.plot(t,out1)
pylab.figure(2)
pylab.plot(t,outpid)
pylab.show()