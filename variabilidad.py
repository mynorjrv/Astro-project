import numpy as np
import math

#skip_header=1,

markarian = '0_Mkn421_results.dat'
pks0 = '07_PKS0447-439_results.dat'
pks1 = '08_PKS1424+240_results.dat'

fuente = markarian

indata = np.genfromtxt( 
  fuente,               
  skip_header=1,       
  usecols=(0, 1, 2, 3),      
  dtype=[('x', float),       
         ('xerr', float),        
         ('y', float),       
         ('yerr', float),
        ],    
  comments='#'
)


data = np.array(
  [(0,0,0,0)], 
  dtype=[('x', float),
         ('xerr', float),
         ('y', float),
         ('yerr', float),
        ]
)

for i in range( len(indata) ):
    if( indata[i]['yerr'] == 0.0 ):
        continue
    else:
        data = np.append(data, [indata[i]], axis=0)

data = np.delete(data, 0)

#print(data)

#print( np.sum( data['yerr'] ) )
#print( data[1])
#print( np.average( data['yerr'] ) )
#print( len(data) )


flux = 'y'
fluxerr = 'yerr'

N = len(data)
Xaverage = np.average( data[flux] )

S_square = 0
for i in range( N ):
    S_square += ( data[i][flux] - Xaverage )**2
S_square = (1/(N-1))*S_square

sigma_err = 0
for i in range( N ):
    sigma_err += ( (data[i][fluxerr])**2 )
sigma_err = (1/N)*sigma_err

#error sistematico
#+ (0.03*data[i][flux])**2

F_var = math.sqrt( (S_square - sigma_err)/ Xaverage**2 )

F_var_err = math.sqrt( 
  ( math.sqrt(1/(2*N)) * ( sigma_err/(F_var*(Xaverage**2)) ) )**2 
  + ( math.sqrt(sigma_err/N) * (1/Xaverage) )**2 
)

#Dude de mi ecuacion pero way more ordenado
'''A = math.sqrt(1/(2*N))
B = sigma_err/( (Xaverage**2)*F_var  )

C = math.sqrt( sigma_err/N)
D = 1/Xaverage

F_err = math.sqrt( (A*B)**2 + (C*D)**2 )'''


print( "Fuente:")
print( fuente )
print( "Magnitud de variabilidad: ")
print( F_var )
print( "Error: ")
print( F_var_err )
print( "Flujo promedio: ")
print( Xaverage)
print( "Varianza: ")
print( math.sqrt(S_square) )
print()
