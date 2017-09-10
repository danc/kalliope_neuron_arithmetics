import pyowm

from kalliope.core.NeuronModule import NeuronModule, MissingParameterException
from random import randint
from math import sqrt, ceil

class Arithmetics(NeuronModule):
    def __init__(self, **kwargs):
        super(Arithmetics, self).__init__(**kwargs)

        self.maxresult = kwargs.get('maxresult', None)
        self.operator = kwargs.get('operator', None)
        self.result =  kwargs.get('result', None)

        # check if parameters have been provided
        if self._is_parameters_ok():
            
            operator_list = ["+", "-", "*", "/"]

            if self.operator in set(operator_list): 
	            operator = self.operator
            else: 
	    	    operator = operator_list[randint(0,3)]
	   
    	    if operator == "+": 
                n_1 = randint(0, int(self.maxresult))
                n_2 = randint(0, int(self.maxresult) - n_1)
                result = n_1 + n_2
            elif operator == "-":
                n_1 = randint(0, int(self.maxresult))
    	        n_2 = randint(0, int(self.maxresult))
                if n_1 < n_2:
            	    temp = n_2; n_2 = n_1; n_1 = temp
                result = n_1 - n_2
            elif operator == "*":
                n_1 = randint(0, ceil(sqrt(int(self.maxresult))))
                n_2 = randint(0, ceil(sqrt(int(self.maxresult))))
                result = n_1 * n_2
            elif operator == "/":
                a = randint(1, ceil(sqrt(int(self.maxresult))))
    	        b = randint(1, ceil(sqrt(int(self.maxresult))))
                n_1 = a * b; n_2 = a 
                result = b

            message = {
                "n_1": n_1,
                "n_2": n_2,
                "operator": operator,
                "result": result, 
            }

            self.say(message)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: NotImplementedError
        """
        if self.maxresult is None:
            raise MissingParameterException("Arithmetics neuron needs maxresult parameter.")

        return True
