import PySimpleGUI as sg
import multiprocessing
import botHiLink

sg.theme("Black")
checkbot = sg.Check("", False, key="a1", text_color="WHITE",checkbox_color="WHITE")
textstatusbot = sg.Text("BOT ONLINE", auto_size_text=True)
buttonupbot = sg.Button("Start Bot", key="upbot")
buttondownbot = sg.Button("Stop Bot", key="downbot")
consolelog = sg.Text("CONSOLE LOG", background_color="WHITE", text_color="BLACK", size=[100,20], auto_size_text=True,key="LOG")
layout =[[sg.Column([[sg.Text("", size=[6, 2])]]), sg.Column([[checkbot, textstatusbot]]), sg.Column([[sg.Text("")]])],
         [sg.Column([[sg.Text("", size=[9, 2])]]), sg.Column([[buttonupbot]]), sg.Column([[sg.Text("")]])],
         [sg.Column([[sg.Text("", size=[9, 2])]]), sg.Column([[buttondownbot]]), sg.Column([[sg.Text("")]])],
         [consolelog]
         ]

window = sg.Window('Pick a color', layout, size=(300, 200))
saida = ''
def gui():
    global bot,saida
    while True:
        event, values = window.read()
        #print(event)
        #print(values)
        consolelog.update(value=saida)
        print(saida)

        try:
            if event == sg.WIN_CLOSED:
                exit()
                break

            if event == "upbot":
                print("Inicializando o BOT")
                textstatusbot.update("BOT ONLINE")
                checkbot.update(True, text_color="GREEN", checkbox_color="GREEN")
                bot = multiprocessing.Process(target=botHiLink.runBot, name="boot")
                bot.start()


            if event == "downbot":
                print("Finalizando o BOT")
                textstatusbot.update("BOT OFFLINE")
                checkbot.update(True)
                checkbot.update(True, text_color="RED", checkbox_color="RED")
                bot.kill()
        except :
            saida = "Tem nada de errado"


if __name__ == '__main__':
    bot = multiprocessing.Process(target=botHiLink.runBot, name="boot")
    bot.start()
    gui()

