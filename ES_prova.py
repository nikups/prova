# G(s) = (s+1) / s^2+5s+7 #
# Provo a implementarla e poi provo a migliorare la dinamica col PID

import pylab

class PIDController:
    def __init__(self,kp,ki,kd):
        self.__kp = kp
        self.__ki = ki
        self.__kd = kd
        self.__prev_error = 0
        self.__integral_term = 0

    def evaluate(self,target,measure,delta_t):
        self.__error = target -measure
        derivative = (self.__error - self.__prev_error) / delta_t
        self.__prev_error = self.__error
        self.__integral_term = self.__integral_term + self.__error*delta_t
        output = self.__kp*self.__error + self.__ki*self.__integral_term + self.__kd *derivative
        return output

class G :
    def __init__ (self):
        self.__x1 = 0
        self.__x2 = 0

    def evaluate(self,u,delta_t):
        x1 = self.__x1 + delta_t*self.__x2
        x2 = -7*delta_t*self.__x1 + (1-(5*delta_t))*self.__x2 + u*delta_t
        y = self.__x1 + self.__x2
        self.__x1 = x1
        self.__x2 = x2
        return y

if __name__ == "__main__":

    t = []
    out = []
    u=1
    outpid = []
    y1=0
    y =0
    yinf = 1./7.

# Per determinare il t.c. considero la durata del transitorio
# I poli sono c.c. con Re = -2.5 -> 3/-(-2.5) -> 1.2
# considero 3s e delta_t 10000 volte piu piccolo -> 0.0003 
# Per il numero di punti : points = int(3/delta_t)

# Apro i file per scrivere i dati su gnuplot

    f = open('/home/nikups/Scrivania/Uni/PROGRAMMAZIONE_SIST_ROBOTICI/ESERCITAZIONI/ES_PROVA/dati', 'w')
    f2 = open('/home/nikups/Scrivania/Uni/PROGRAMMAZIONE_SIST_ROBOTICI/ESERCITAZIONI/ES_PROVA/dati_pid', 'w')
    
    delta_t = 0.0003
    points = int(3/delta_t)

    sistema1 = G()
    sistema2 = G()
    PID = PIDController(250,0,0.5)

    for i in range(0,points):
        pid_out = PID.evaluate(u,y1,delta_t)
        y1 = sistema2.evaluate(pid_out,delta_t)
        y = sistema1.evaluate(u,delta_t)
        t.append(i*delta_t)
        outpid.append(y1)
        out.append(y)
        f.write (str(t[i])+' '+str(out[i])+'\n')
        f2.write (str(t[i])+' '+str(outpid[i])+'\n')

    # PER PLOTTARE: spostarsi nella cartella dove vi e il file da plottare
    # DA TERMINALE: gnuplot
    # POI SCRIVERE DA GNUPLOT:
    # plot "nome_file" using 1:2 with lines

    ##### CALCOLO TEMPO DI ASSESTAMENTO SENZA PID #####

    t_as = 0.

    for i in range (0, points):
         if (float(out[i]) > ((yinf*95)/100)) and (float(out[i]) < ((yinf*105)/100)):
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
    pylab.plot(t,out)
    pylab.figure(2)
    pylab.plot(t,outpid)
    pylab.show()