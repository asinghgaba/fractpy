


from fractpy.models.newton import NewtonFractal


function = 'x**3 - 1'

model = NewtonFractal(function)
model.plot(-2, 2, -2, 2, (50, 50))
