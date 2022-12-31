from tkinter import *
from random import choice
from playsound import playsound
from tkinter import ttk
from liste_mot import mot
global fenetre1, fenetre2,fenetre3,liste_mots
class jeu():
        def passage(self):
            global fenetre1, fenetre2,fenetre3
            self.fenetre1.destroy()
            self.joueur1
        def passage2(self):
            global fenetre1, fenetre2,fenetre3
            self.fenetre2.destroy()
            self.joueur2
        def fenetre(self):
            global fenetre1,pendu
            self.fenetre1 = Tk()
            self.fenetre1.title("JEUX DE PENDU")
            self.fenetre1.geometry("550x400")
            self.fenetre1.resizable(0, 0)
            self.bg = PhotoImage(file = "pen.gif")
            label1 = Label(self.fenetre1, image = self.bg) 
            label1.place(x = 30, y = 50)
            self.bouton = Button(self.fenetre1,text="JOUER", command=self.passage,height = 3, width = 23, bg = "yellow")
            self.bouton.pack()
            self.bouton.place(x = 200, y = 320)
            self.fenetre1.mainloop()
        def joueur1(self):
            global fenetre2,entree,liste_mots
            self.fenetre2 = Tk()           
            def OnValidate():
                for j in self.entries : 
                   if len(j.get())<=3 or len(j.get())>=10:
                        t =Toplevel(self.fenetre2)
                        lab=Label(t, text=" reentrer votre mot ").pack(padx=5, pady=5)
                        btn=Button(t, text="Ok", command=t.destroy).pack(padx=5, pady=5)
                   else :
                        mot.append(j.get()) 
            self.cadre = Frame(self.fenetre2)
            self.cadre.pack(padx=5, pady=5)
            self.fenetre2.title("JOUEUR 1")
            self.fenetre2.resizable(0, 0)
            self.etiquette = Label(self.cadre, text='mot choisi :')
            self.etiquette.pack(padx=5, pady=5, side=LEFT)
            self.entries=[]
            
            self.entree = Entry(self.cadre, width=50, show="*")
            self.entree.pack(padx=5, pady=5, side=LEFT)
            self.entree.focus_force()
            self.entries.append(self.entree)
            self.btnAffiche = Button(self.fenetre2, text='ENREGISTRER', command=OnValidate)
            self.btnAffiche.pack(padx=5, pady=5)
            self.btnPass = Button(self.fenetre2, text='JOUEUR 2', command=self.passage2)
            self.btnPass.pack(padx=5, pady=5)
            self.fenetre2.mainloop()
        def joueur2(self):
            global fenetre3,liste_mots,partie_en_cours, mot_partiel, mot_choisi, echecs, pendu,lettres,liste_mots,lettres
            liste_mots=mot
            self.fenetre = Tk()
            def combineFunc(*funcs):
                def combinedFunc(*args, **kwargs):
                    for f in funcs:
                            f(*args, **kwargs)
                return combinedFunc
            def lettre_existe(lettre) :
                global partie_en_cours, mot_partiel, mot_choisi, echecs, pendu
                
                if partie_en_cours : 
                    nouveau_mot = ""
                    lettre_existe = False
                    i=0
                    while i<len(mot_choisi):
                        if mot_choisi[i]==lettre:
                            nouveau_mot = nouveau_mot + lettre
                            lettre_existe = True 
                        else:
                            nouveau_mot = nouveau_mot + mot_partiel[i]
                        i+=1   
                    mot_partiel = nouveau_mot
                    afficher(mot_partiel)
                    if not lettre_existe :        
                        echecs += 1
                        print("il vous reste ",11-echecs," essaies !! ")
                        nomFichier = "pendu_"+str(echecs)+".gif"
                        photo=PhotoImage(file=nomFichier)
                        self.pendu.config(image=photo)
                        self.pendu.image=photo
                        if echecs == 11:  
                            partie_en_cours = False
                            afficher2(mot_choisi)
                            playsound('gameover.mp3')
                            print("perdu !!! : ",mot_choisi)                          
                    elif mot_partiel == mot_choisi:  
                        partie_en_cours = False
                        nomFichier = "pendu_12.gif"
                        photo=PhotoImage(file=nomFichier)
                        self.pendu.config(image=photo)
                        self.pendu.image=photo
                        afficher3(mot_choisi)
                        playsound('victory.mp3')
                        print("bravo gagner !! : ",mot_choisi)
            def etata():
                if (btna['state'] == NORMAL):
                    btna['state'] = DISABLED
                else:
                    btna['state'] == NORMAL
            def etatb():
                if (btnb['state'] == NORMAL):
                    btnb['state'] = DISABLED
                else:
                    btnb['state'] == NORMAL
            def etatc():
                if (btnc['state'] == NORMAL):
                    btnc['state'] = DISABLED
                else:
                    btnc['state'] == NORMAL
            def etatd():
                if (btnd['state'] == NORMAL):
                    btnd['state'] = DISABLED
                else:
                    btnd['state'] == NORMAL
            def etate():
                if (btne['state'] == NORMAL):
                    btne['state'] = DISABLED
                else:
                    btne['state'] == NORMAL
            def etatf():
                if (btnf['state'] == NORMAL):
                    btnf['state'] = DISABLED
                else:
                    btnf['state'] == NORMAL
            def etatg():
                if (btng['state'] == NORMAL):
                    btng['state'] = DISABLED
                else:
                    btng['state'] == NORMAL
            def etath():
                if (btnh['state'] == NORMAL):
                    btnh['state'] = DISABLED
                else:
                    btnh['state'] == NORMAL
            def etati():
                if (btni['state'] == NORMAL):
                    btni['state'] = DISABLED
                else :
                    btni['state'] == NORMAL
            def etatj():
                if (btnj['state'] == NORMAL):
                    btnj['state'] = DISABLED
                else :
                    btnj['state'] == NORMAL
            def etatk():
                if (btnk['state'] == NORMAL):
                    btnk['state'] = DISABLED
                else :
                    btnk['state'] == NORMAL
            def etatl():
                if (btnl['state'] == NORMAL):
                    btnl['state'] = DISABLED
                else:
                    btnl['state'] == NORMAL
            def etatm():
                if (btnm['state'] == NORMAL):
                    btnm['state'] = DISABLED
                else:
                    btnm['state'] == NORMAL
            def etatn():
                if (btnn['state'] == NORMAL):
                    btnn['state'] = DISABLED
                else:
                    btnn['state'] == NORMAL
            def etato():
                if (btno['state'] == NORMAL):
                    btno['state'] = DISABLED
                else:
                    btno['state'] == NORMAL
            def etatp():
                if (btnp['state'] == NORMAL):
                    btnp['state'] = DISABLED
                else:
                    btnp['state'] == NORMAL
            def etatq():
                if (btnq['state'] == NORMAL):
                    btnq['state'] = DISABLED
                else :
                    btnq['state'] == NORMAL
            def etatr():
                if (btnr['state'] == NORMAL):
                    btnr['state'] = DISABLED
                else:
                    btnr['state'] == NORMAL
            def etats():
                if (btns['state'] == NORMAL):
                    btns['state'] = DISABLED
                else:
                    btns['state'] == NORMAL
            def etatt():
                if (btnt['state'] == NORMAL):
                    btnt['state'] = DISABLED
                else:
                    btnt['state'] == NORMAL
            def etatu():
                if (btnu['state'] == NORMAL):
                    btnu['state'] = DISABLED
                else:
                    btnu['state'] == NORMAL
            def etatv():
                if (btnv['state'] == NORMAL):
                    btnv['state'] = DISABLED
                else:
                    btnv['state'] == NORMAL
            def etatw():
                if (btnw['state'] == NORMAL):
                    btnw['state'] = DISABLED
                else:
                    btnw['state'] == NORMAL
            def etatx():
                if (btnx['state'] == NORMAL):
                    btnx['state'] = DISABLED
                else:
                    btnx['state'] == NORMAL
            def etaty():
                if (btny['state'] == NORMAL):
                    btny['state'] = DISABLED
                else:
                    btny['state'] == NORMAL
            def etatz():
                if (btnz['state'] == NORMAL):
                    btnz['state'] = DISABLED
                else:
                    btnz['state'] == NORMAL
            def afficher(m):
                global lettres
                mot_large = ""
                i=0
                while i<len(m):  
                    mot_large = mot_large + m[i] + " "
                    i+=1
                    self.canevas.delete(self.lettres)
                    self.lettres = self.canevas.create_text(320,60,text=mot_large,fill='black',font='Courrier 30')
            def afficher2(m):
                global lettres
                mot_large = ""
                i=0
                while i<len(m):  
                    mot_large = mot_large + m[i] + " "
                    i+=1
                    self.canevas.delete(self.lettres)
                    lettres = self.canevas.create_text(320,60,text=mot_large,fill='red',font='Courrier 30')
            def afficher3(m):
                global lettres
                mot_large = ""
                i=0
                while i<len(m):  
                    mot_large = mot_large + m[i] + " "
                    i+=1
                    self.canevas.delete(self.lettres)
                    self.lettres = self.canevas.create_text(320,60,text=mot_large,fill='green',font='Courrier 30')

            def init_jeu():
                global mot_choisi, mot_partiel, pendu, lettres, liste_mots
                global echecs, partie_en_cours
                echecs = 0
                partie_en_cours = True
                mot_choisi = choice(mot).rstrip()
                mot_choisi = mot_choisi.upper()
                mot_partiel = "-" * len(mot_choisi)
                afficher(mot_partiel)
                photo=PhotoImage(file="pendu_0.gif")
                self.pendu.config(image=photo)
                self.pendu.image=photo
                btna['state'] == NORMAL
                btnb['state'] == NORMAL
                btnc['state'] == NORMAL
                btnd['state'] == NORMAL
                btne['state'] == NORMAL
                btnf['state'] == NORMAL
                btng['state'] == NORMAL
                btnh['state'] == NORMAL
                btni['state'] == NORMAL
                btnj['state'] == NORMAL
                btnk['state'] == NORMAL
                btnl['state'] == NORMAL
                btnm['state'] == NORMAL
                btnn['state'] == NORMAL
                btno['state'] == NORMAL
                btnp['state'] == NORMAL
                btnq['state'] == NORMAL
                btnr['state'] == NORMAL
                btns['state'] == NORMAL
                btnt['state'] == NORMAL
                btnu['state'] == NORMAL
                btnv['state'] == NORMAL
                btnw['state'] == NORMAL
                btnx['state'] == NORMAL
                btny['state'] == NORMAL
                btnz['state'] == NORMAL
                
            def aide():
                global mot_choisi, mot_partiel,lettres
                mot_choisi = mot_choisi.upper()
                afficher(mot_choisi[0]+"-" * (len(mot_choisi)-2)+mot_choisi[-1])
            self.fenetre.title("JOUEUR 2")
            self.fenetre.resizable(0, 0)
            self.canevas = Canvas(self.fenetre, bg='white', height=550, width=620)
            self.canevas.pack(side=BOTTOM)
            i=0
            btna=Button(self.fenetre,text='A',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etata),state = NORMAL)
            btna.pack(side=LEFT)
            i+=1
            btnb=Button(self.fenetre,text='B',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatb),state = NORMAL)
            btnb.pack(side=LEFT)
            
            i+=1
            btnc=Button(self.fenetre,text='C',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatc),state = NORMAL)
            btnc.pack(side=LEFT)
            i+=1
            btnd=Button(self.fenetre,text='D',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatd),state = NORMAL)
            btnd.pack(side=LEFT)
            i+=1
            
            btne=Button(self.fenetre,text='E',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etate),state = NORMAL)
            btne.pack(side=LEFT)
            i+=1
            btnf=Button(self.fenetre,text='F',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatf),state = NORMAL)
            btnf.pack(side=LEFT)
            i+=1
            btng=Button(self.fenetre,text='G',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatg),state = NORMAL)
            btng.pack(side=LEFT)
            i+=1
            btnh=Button(self.fenetre,text='H',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etath),state = NORMAL)
            btnh.pack(side=LEFT)
            i+=1
            btni=Button(self.fenetre,text='I',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etati),state = NORMAL)
            btni.pack(side=LEFT)
            i+=1
            btnj=Button(self.fenetre,text='J',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatj),state = NORMAL)
            btnj.pack(side=LEFT)
            i+=1
            btnk=Button(self.fenetre,text='K',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatk),state = NORMAL)
            btnk.pack(side=LEFT)
            i+=1
            btnl=Button(self.fenetre,text='L',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatl),state = NORMAL)
            btnl.pack(side=LEFT)
            i+=1
            btnm=Button(self.fenetre,text='M',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatm),state = NORMAL)
            btnm.pack(side=LEFT)
            i+=1
            btnn=Button(self.fenetre,text='N',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatn),state = NORMAL)
            btnn.pack(side=LEFT)
            i+=1
            btno=Button(self.fenetre,text='O',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etato),state = NORMAL)
            btno.pack(side=LEFT)
            i+=1
            btnp=Button(self.fenetre,text='P',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatp),state = NORMAL)
            btnp.pack(side=LEFT)
            i+=1
            btnq=Button(self.fenetre,text='Q',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatq),state = NORMAL)
            btnq.pack(side=LEFT)
            i+=1
            btnr=Button(self.fenetre,text='R',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatr),state = NORMAL)
            btnr.pack(side=LEFT)
            i+=1
            btns=Button(self.fenetre,text='S',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etats),state = NORMAL)
            btns.pack(side=LEFT)
            i+=1
            btnt=Button(self.fenetre,text='T',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatt),state = NORMAL)
            btnt.pack(side=LEFT)
            i+=1
            btnu=Button(self.fenetre,text='U',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatu),state = NORMAL)
            btnu.pack(side=LEFT)
            i+=1
            btnv=Button(self.fenetre,text='V',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatv),state = NORMAL)
            btnv.pack(side=LEFT)
            i+=1
            btnw=Button(self.fenetre,text='W',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatw),state = NORMAL)
            btnw.pack(side=LEFT)
            i+=1
            btnx=Button(self.fenetre,text='X',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatx),state = NORMAL)
            btnx.pack(side=LEFT)
            i+=1
            btny=Button(self.fenetre,text='Y',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etaty),state = NORMAL)
            btny.pack(side=LEFT)
            i+=1
            btnz=Button(self.fenetre,text='Z',command=combineFunc((lambda x=i+65:lettre_existe(chr(x))),etatz),state = NORMAL)
            btnz.pack(side=LEFT)

            btn2=Button(self.fenetre,background = "red",foreground = "black",text='Quitter',command=self.fenetre.quit)
            btn2.pack(side=RIGHT)
            i+=1
            btn1 = Button(self.fenetre,background = "green",foreground = "black",text='Recommencer',command=init_jeu)
            btn1.pack(side=RIGHT)
            i+=1
            btn3 = Button(self.fenetre,background = "yellow",foreground = "black",text='Aide',command=aide)
            btn3.pack(side=RIGHT)
            self.photo=PhotoImage(file="pendu_0.gif")
            self.pendu = Label(self.canevas, image=self.photo, border=0)
            self.pendu.place(x=120, y=140)
            self.lettres = self.canevas.create_text(320,60,text="",fill='black',font='Courrier 30') 
            init_jeu()
            self.fenetre.mainloop()

if __name__ == '__main__':
    fen=jeu()
    fen.fenetre()
    fen.joueur1()
    fen.joueur2()










