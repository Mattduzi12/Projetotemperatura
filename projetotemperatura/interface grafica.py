from calculo import *
import PySimpleGUI as psg

layou_frame = [
    [psg.Radio('Celsius', 'btnRadio1', key='Celsius')],
    [psg.Radio('Fahrenheit', 'btnRadio1', key='Fahrenheit', default=True)],
]

layout = [
    [psg.Text('Informe um número: '), psg.InputText(key='numero'), psg.Frame('Opções: ', layou_frame)],
    [psg.Text("", key='resultado')],
    [psg.Output(size=(12,6), key='resultado2')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
]

window = psg.Window('Sistema Matemático do Senai', layout)

while True:
    evento, valor = window.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        # psg.popup('Limpar a tela!')
        window['Fahrenheit'].update(True) # Radio
        window['resultado'].update('') # Text
        window['numero'].update('') # InputText
        window['resultado2'].update('') # Output
    else:
        if valor['Fahrenheit']:
            num = fahr(int(valor['numero']))
            window['resultado'].update(f'{valor["numero"]}! = {num}')
        else:
            window['resultado2'].update(cels(int(valor['numero'])))



window.close()