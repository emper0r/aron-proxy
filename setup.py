#!/usr/bin/env python
# encoding: utf-8

import npyscreen, curses

class AronSetup(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.TitleText,
                 name="Computer Time S.r.l",
                 value="Aron Web Manager Setup",
                 max_height=10,
                 editable=False,
                 )
        self.add(npyscreen.MultiLineEdit,
                 value="""\n\n\n\nUn prodotto semplice e veloce per\nla impostazione della rete del server\ncon rapido accesso intuitivo\ne facil da utilizzare.""",
                 max_height=15,
                 editable=False)
        self.add(npyscreen.TitleText,
                 name="Impostazione Aron",
                 value="Per accedere al Menu premi il tasto Ctrl + X",
                 max_height=2,
                 editable=False,
                 )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE] = self.exit_application

        # The menus are created here.
        self.m1 = self.add_menu(name="Opzioni")
        self.m1.addItemsFromList([
            ("1- Impostazioni Rete", self.network),
            ("2- Licenza Aron", self.network),
            ("3- Status servizi", self.network),
            ("4- Riavvio server", self.network),
            ("5- Spegni server", self.network),
            ("6- Exit Application", self.exit_application),
        ])

    def whenDisplayText(self, argument):
       npyscreen.notify_confirm(argument)

    def network(self):
        curses.beep()

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

def main():
    App = AronSetup()
    App.run()

if __name__ == '__main__':
    main()
