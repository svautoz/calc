import ui
import complex_calc
import float_calc
import login


def calc_complex():
    number_1, number_2, oper = ui.input(type(complex))
    result = complex_calc.calc(number_1, number_2, oper)
    login.log_in_file(number_1, number_2, oper, result)
    ui.output(result)




def calc_fractional():
    number_1, number_2, oper = ui.input(type(float)) #Семен
    result = float_calc.calc(number_1, number_2, oper) #Ренат
    login.log_in_file(number_1, number_2, oper, result)
    ui.output(result)