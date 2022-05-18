import matplotlib as plt
import numpy as np
from fitting import Fitting as ft
from extracting import Extract as et

class Plot:
    def __init__(self):
        self.X=et.get_IV()[0]
        self.Y=et.get_IV()[1]

    def IV_ref_plot(self):
        plt.plot(self.X, abs(self.Y), 'bo--', label='Raw data')
        plt.xlabel('Voltage [V]')
        plt.ylabel('Current [A]')
        plt.xticks(np.arange(-2, 1.25, 0.25))
        plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
        plt.yscale('log')
        plt.title('IV-analysis')
        plt.legend(loc='best')
        plt.show()

    def IV_ployfit_plot(self):
        plt.plot(self.X,abs(ft.normal_fit()),'r',label='fitting(ployfit)')
        plt.xlabel('Voltage [V]')
        plt.ylabel('Current [A]')
        plt.xticks(np.arange(-2, 1.25, 0.25))
        plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
        plt.yscale('log')
        plt.title('IV-analysis')
        plt.legend(loc='best')
        plt.show()

    def IV_lmfit_plot(self):
        plt.plot(self.X,abs(ft.non_linear_fit()),'r',label='fitting(lmfit)')
        plt.xlabel('Voltage [V]')
        plt.ylabel('Current [A]')
        plt.xticks(np.arange(-2, 1.25, 0.25))
        plt.yticks([10 ** -12, 10 ** -11, 10 ** -10, 10 ** -9, 10 ** -8, 10 ** -7, 10 ** -6, 10 ** -5, 10 ** -4, 10 ** -3,10 ** -2])
        plt.yscale('log')
        plt.title('IV-analysis')
        plt.legend(loc='best')
        plt.show()
