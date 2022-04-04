from gui_base_class import BaseWindow   


layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

def new_func(layout):
    window = sg.Window('Window Title', layout)
    return window


event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)