from scipy.optimize import curve_fit as cfit
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as PL


#data from textfile

# 0_Mkn421_results.dat
# 07_PKS0447-439_results.dat
# 08_PKS1424+240_results.dat

indata = np.genfromtxt(
  '08_PKS1424+240_results.dat',
  skip_header=1,
  usecols=(0, 1, 2, 3),
  dtype=[('x', float),                   
         ('xerr', float), 
         ('y', float),
         ('yerr', float),
        ],
  comments='#'
)

#elimino los elementos con error cero, creo una nueva lista
#mas dificil de lo que deberia
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
        print(indata[i])
        data = np.append(data, [indata[i]], axis=0)

data = np.delete(data, 0)

#* * * plotting * * * 
fig, ax = PL.subplots(1)

#Data plot with errors
PL.errorbar(
  data['x'], data['y'], 
  xerr=data['xerr'], yerr=data['yerr'], 
  fmt='none', color='black', label='Mkn421', capsize=2.0)
#fmt="+",


PL.title('Curva de luz de PKS1424+240')

ax.set_xlabel(r'MET ($s$)')
ax.set_ylabel(r'Flujo ($ph \cdot cm^{-2} \cdot s^{-1}$)')

#ax.grid(b=True, linestyle='--')

#PL.legend()
PL.show()
