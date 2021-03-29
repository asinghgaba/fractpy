
import sympy as sym



class Function:
    """A class for caclulating derivative and relative difference.

    
    """
    #default variable
    #x = sym.Symbol('x')

    # TODO: Check for single variable function
           # expr.free_symbols (sympy expression)
    #TODO: Check for other potential errors

    
    def __init__(self, function, variable):
        self.f = function
        self.variable = variable
    
    def calculate_roots(self):
        return list(sym.solveset(self.f, self.variable))

    def differentiate(self):
        return sym.diff(self.f, self.variable)

    def relative_difference(self):
        return self.f / self.differentiate()

    def make_pfunction(self, function, variable):
        "Converts sympy functions to python functions."
        return sym.lambdify(variable, function)

    def rd_pfunction(self):
        rd = self.relative_difference()
        return self.make_pfunction(rd, self.variable)

    
