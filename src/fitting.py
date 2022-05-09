# fittin the differents type of curves

import numpy as np
from lmfit import Model
from src import handler

class Fitting:
    
    def __init__(self,X,Y):

        self.X = X
        self.Y = Y


    def reference_fit(self):
        """
        fit linear curve which can be fitted by polynomials

        Returns:
            list: list of the differents coefficients for the fitting
        """

        polynome = []
        for i in range (1,7):
            step = np.polyfit(self.X, self.Y,i)
            polynome.append(np.poly1d(step))
        return polynome

    def normal_fit(self, order:int):
        """
        fit a linear curve

        Args:
            order (int): the order of the polynomials 

        Returns:
            list: list containing the coefficient for the fitting
        """

        step = np.polyfit(self.X,abs(self.Y),order)
        coef = np.poly1d(step)

        return coef

    def non_linear_fit(self):

        gmodel = Model(handler.func)
        result = gmodel.fit(self.Y,x=self.X_3,a=1,b=1,c=1,d=1)
        
        return result.best_fit


    def 
    