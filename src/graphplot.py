import matplotlib as plt
import numpy as np

class Plot:

    def __init__(self,IV_X,IV_Y,SPC_X,SPC_Y,SPC_ref_fit):
        self.IV_X=IV_X
        self.IV_Y=IV_Y
        self.SPC_X=SPC_X
        self.SPC_Y=SPC_Y
        self.SPC_ref_fit=SPC_ref_fit

    def IV_ref_plot(self):
        plt.plot(self.IV_X, abs(self.IV_Y), 'bo--', label='Raw data')
        plt.xlabel('Voltage [V]')
        plt.ylabel('Current [A]')
        plt.xticks(np.arange(-2, 1.25, 0.25))
        plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
        plt.yscale('log')
        plt.title('IV-analysis')
        plt.legend(loc='best')

    def IV_ployfit_plot(self,X,Y):
        plt.plot(X,abs(Y),'r',label='fitting(ployfit)')
        plt.xlabel('Voltage [V]')
        plt.ylabel('Current [A]')
        plt.xticks(np.arange(-2, 1.25, 0.25))
        plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
        plt.yscale('log')
        plt.title('IV-analysis')
        plt.legend(loc='best')

    def IV_lmfit_plot(self,X,Y):
        plt.plot(X,abs(Y),'r',label='fitting(lmfit)')
        plt.xlabel('Voltage [V]')
        plt.ylabel('Current [A]')
        plt.xticks(np.arange(-2, 1.25, 0.25))
        plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
        plt.yscale('log')
        plt.title('IV-analysis')
        plt.legend(loc='best')

    def raw_data(self):
        plt.plot(self.SPC_X[0],self.SPC_Y[0],'r')
        plt.plot(self.SPC_X[1],self.SPC_Y[1],'g')
        plt.plot(self.SPC_X[2],self.SPC_Y[2],color='limegreen')
        plt.plot(self.SPC_X[3],self.SPC_Y[3],color='turquoise')
        plt.plot(self.SPC_X[4],self.SPC_Y[4],color='b')
        plt.plot(self.SPC_X[5],self.SPC_Y[5],color='darkorchid')
        plt.plot(self.SPC_X[6],self.SPC_Y[6],color='black',label='Raw data')
        plt.xlabel('wavelenght [nm]')
        plt.ylabel('Measured transmission[dB]')
        plt.title('Transmission spectra - As mesured')
        plt.axis([1527, 1583, -65, 0])
        plt.legend(loc='best')

    def ref_fit_plot(self):
        x_line = np.arange(min(self.SPC_X[6]), max(self.SPC_X[6]), 0.01)
        plt.plot(x_line,self.SPC_ref_fit[0](x_line),'b-',label='1st order')
        plt.plot(x_line,self.SPC_ref_fit[1](x_line),'r-',label='2nd order')
        plt.plot(x_line,self.SPC_ref_fit[2](x_line),'g-',label='3rd order')
        plt.plot(x_line,self.SPC_ref_fit[3](x_line),'y-',label='4th order')
        plt.plot(x_line,self.SPC_ref_fit[4](x_line),'c-',label='5th order')
        plt.plot(x_line,self.SPC_ref_fit[5](x_line),'b--',label='6th order')
        plt.plot(self.SPC_X,self.SPC_Y,'k--',label='Raw data')
        plt.xlabel('wavelenght [nm]')
        plt.ylabel('Measured transmission[dB]')
        plt.title('Transmission spectra - As mesured')
        plt.axis([1527, 1583, -65, 0])
        plt.legend(loc='best')

    def flatten_data(self):
        for i in range(0, 7):
            z = np.polyfit(self.SPC_X[6],self.SPC_Y[6],3)
            p = np.poly1d(z)
        plt.plot(self.SPC_X[i][:6065],self.SPC_Y[i][:6065] - p(self.SPC_X[6]))
        plt.xlabel('wavelenght [nm]')
        plt.ylabel('Measured transmission[dB]')
        plt.title('flatten Transmission spectra - as measured')
        plt.axis([1527, 1583, -65, 0])
