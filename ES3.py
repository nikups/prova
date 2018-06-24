import pylab
class PID_Controller:
    def __init__(self, kp, ki, kd):
        self.__kp = kp
        self.__ki = ki
        self.__kd = kd
        self.__intergral_term = 0
        self.__prev_error = 0
    
    def evaluate(self, target, measure, delta_t):
        self.__error = target - measure
        derivative = (self.__error - self.__prev_error) / delta_t
        self.__prev_error = self.__error
        self.__intergral_term = self.__intergral_term + self.__error * delta_t
        output = self.__error * self.__kp + self.__intergral_term * self.__ki + derivative * self.__kd
        return output

    def get_error(self):
        return self.__error


class G:
    def __init__(self):
        self.__x1 = 0
        self.__x2 = 0
        self.__x3 = 0
    def evaluate (self,u,delta_t):
        x1 = self.__x1 +delta_t*self.__x2
        x2 = self.__x2 +delta_t*self.__x3
        x3 = 5*delta_t*self.__x1+ 3*delta_t*self.__x2+((-3*delta_t)+1)*self.__x3+delta_t*u
        y = 4*self.__x1 + 17 * self.__x2 + 4 * self.__x3
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3
        return y  
 


t=[]
out=[]
out_1=[]
delta_t= 0.0005
points = int(5/delta_t)
# scelta del tempo di campionamento ?
# in questo caso il polo dominante e in -1 
# Allora per calcolare la durata di simulazione devo considerare 3/-Re[p.d.] -> 3/1 -> 3s
# Considero 5s -> il tempo di campionamento lo considero 10000 volte piu piccolo 
# Allora delta_t = 0.0005 e numero di punti points = int(5/delta_t) 


u = 1
y = 0
sistema_tot = G()
pid = PID_Controller(80,0,0)

# apro il file per salvarmi i dati:

f= open('/home/nikups/Scrivania/Uni/PROGRAMMAZIONE_SIST_ROBOTICI/ESERCITAZIONI/ES3/dati3','w')


for i in range(0, points):
    pid_output = pid.evaluate(u, y, delta_t)
    y = sistema_tot.evaluate (pid_output,delta_t)
    t.append(i*delta_t)
    out.append(y)
    # Plottare con GNUPLOT -> salvo sul file
    f.write(str(t[i])+' '+str((out[i]))+'\n')

# PER PLOTTARE: spostarsi nella cartella dove vi e il file da plottare
# DA TERMINALE: gnuplot
# POI SCRIVERE DA GNUPLOT:
# plot "nome_file" using 1:2 with lines


pylab.figure(1)
pylab.plot(t,out)
#pylab.figure(2)
#pylab.plot(t,out_1)
pylab.show()
