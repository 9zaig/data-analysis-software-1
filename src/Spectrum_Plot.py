import numpy as np
import matplotlib as plt
from fitting import Fitting as ft
from extracting import Extract as et

class Ref_Plot:
    def __init__(self):
        self.X=et.get_Spectrum()[0]
        self.Y=et.get_Spectrum()[1]

    def raw_data(self):
        plt.plot(self.X[0],self.Y[0],'r')
        plt.plot(self.X[1],self.Y[1],'g')
        plt.plot(self.X[2],self.Y[2],color='limegreen')
        plt.plot(self.X[3],self.Y[3],color='turquoise')
        plt.plot(self.X[4],self.Y[4],color='b')
        plt.plot(self.X[5],self.Y[5],color='darkorchid')
        plt.plot(self.X[6],self.Y[6],color='black',label='Raw data')
        plt.xlabel('wavelenght [nm]')
        plt.ylabel('Measured transmission[dB]')
        plt.title('Transmission spectra - As mesured')
        plt.axis([1527, 1583, -65, 0])
        plt.legend(loc='best')
        plt.show()

    def ref_fit_plot(self):
        x_line = np.arange(min(self.X[6]), max(self.X[6]), 0.01)
        plt.plot(x_line,ft.reference_fit()[0](x_line),'b-',label='1st order')
        plt.plot(x_line,ft.reference_fit()[1](x_line),'r-',label='2nd order')
        plt.plot(x_line,ft.reference_fit()[2](x_line),'g-',label='3rd order')
        plt.plot(x_line,ft.reference_fit()[3](x_line),'y-',label='4th order')
        plt.plot(x_line,ft.reference_fit()[4](x_line),'c-',label='5th order')
        plt.plot(x_line,ft.reference_fit()[5](x_line),'b--',label='6th order')
        plt.plot(self.X,self.Y,'k--',label='Raw data')
        plt.xlabel('wavelenght [nm]')
        plt.ylabel('Measured transmission[dB]')
        plt.title('Transmission spectra - As mesured')
        plt.axis([1527, 1583, -65, 0])
        plt.legend(loc='best')
        plt.show()

    def flatten_data(self):
        for i in range(0, 7):
            z = np.polyfit(self.X[6],self.Y[6], 3)
            p = np.poly1d(z)

            plt.plot(self.X[i][:6065],self.Y[i][:6065] - p(self.X[6]))
        plt.xlabel('wavelenght [nm]')
        plt.ylabel('Measured transmission[dB]')
        plt.title('flatten Transmission spectra - as measured')
        plt.axis([1527, 1583, -65, 0])
        plt.show()
