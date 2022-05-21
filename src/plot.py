import matplotlib as plt
import numpy as np
from sklearn.metrics import r2_score

def IV_ref_plot(X,Y):
    plt.plot(X, abs(Y), 'bo--', label='Raw data')
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')
    plt.xticks(np.arange(-2, 1.25, 0.25))
    plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
    plt.yscale('log')
    plt.title('IV-analysis')
    plt.legend(loc='best')

def IV_ployfit_plot(X,Y):
    plt.plot(X,abs(Y),'r',label='fitting(ployfit)')
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')
    plt.xticks(np.arange(-2, 1.25, 0.25))
    plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
    plt.yscale('log')
    plt.title('IV-analysis')
    plt.legend(loc='best')

def IV_lmfit_plot(X,Y):
    plt.plot(X,abs(Y),'r',label='fitting(lmfit)')
    plt.xlabel('Voltage [V]')
    plt.ylabel('Current [A]')
    plt.xticks(np.arange(-2, 1.25, 0.25))
    plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
    plt.yscale('log')
    plt.title('IV-analysis')
    plt.legend(loc='best')

def raw_data(X,Y):
    plt.plot(X[0],Y[0],'r')
    plt.plot(X[1],Y[1],'g')
    plt.plot(X[2],Y[2],color='limegreen')
    plt.plot(X[3],Y[3],color='turquoise')
    plt.plot(X[4],Y[4],color='b')
    plt.plot(X[5],Y[5],color='darkorchid')
    plt.plot(X[6],Y[6],color='black',label='Raw data')
    plt.xlabel('wavelenght [nm]')
    plt.ylabel('Measured transmission[dB]')
    plt.title('Transmission spectra - As mesured')
    plt.axis([1527, 1583, -65, 0])
    plt.legend(loc='best')

def ref_fit_plot(X,Y,ref_fit):
    x_line = np.arange(min(X[6]), max(X[6]), 0.01)
    plt.plot(x_line,ref_fit[0](x_line),'b-',label='1st order')
    plt.plot(x_line,ref_fit[1](x_line),'r-',label='2nd order')
    plt.plot(x_line,ref_fit[2](x_line),'g-',label='3rd order')
    plt.plot(x_line,ref_fit[3](x_line),'y-',label='4th order')
    plt.plot(x_line,ref_fit[4](x_line),'c-',label='5th order')
    plt.plot(x_line,ref_fit[5](x_line),'b--',label='6th order')
    plt.plot(X,Y,'k--',label='Raw data')
    plt.xlabel('wavelenght [nm]')
    plt.ylabel('Measured transmission[dB]')
    plt.title('Transmission spectra - As mesured')
    plt.axis([1527, 1583, -65, 0])
    plt.legend(loc='best')

def flatten_data(X,Y):
    for i in range(0, 7):
        z = np.polyfit(X[6],Y[6],3)
        p = np.poly1d(z)
        plt.plot(X[i][:6065],Y[i][:6065] - p(X[6]))
    plt.xlabel('wavelenght [nm]')
    plt.ylabel('Measured transmission[dB]')
    plt.title('flatten Transmission spectra - as measured')
    plt.axis([1527, 1583, -65, 0])

def RSQ(X,fit):
    rsq = r2_score(X,fit)
    return rsq