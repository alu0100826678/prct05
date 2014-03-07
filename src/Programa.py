 #!/usr/bin/python
n = int(raw_input('Cantidad de intervalos: '))
pi = 3.14159265358979323846264338327950288
suma = 0
for i in range (1,n+1):
        x_i = (i - 0.5)/n
        fx_i = 4.0/(1+x_i*x_i)
        suma = suma+fx_i
        a = float (i-1)/n
        b = float (i)/n
        print 'subintervalos: [%f,%f] xi : %f f_xi:%f' % (a, b, x_i , fx_i)
        pi2 = float(suma)/n
print 'El valor real de pi es: %36.35f ', pi 
print 'El valor aproximado de pi que resulta de la formula dada es : %36.35f' %pi2

  
   
  
 
  
