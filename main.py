#Criado por Rafael Martins
#01/02/2019
#Jogo da Velha 1.0
from os import system
from time import sleep
import sqlite3


class Game(object):
    """classe do jogo da velha"""

    def __init__(self):
        """metodo construtor da classe"""

        #Variaveis globais da classe Game que atuarão na função board
        self.a1, self.b1, self.c1 = "   ", "   ", "   "
        self.a2, self.b2, self.c2 = "   ", "   ", "   "
        self.a3, self.b3, self.c3 = "   ", "   ", "   "
        #Quantidade de jogadas
        self.plays = 0
        #Variaveis dos jogadores.
        self.player1, self.player2 = 0,0
        self.name_p1x, self.name_p2o = "", ""
        #lista que armazena as jogadas ja feitas
        self.list_try = []
        self.valid_list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
        self.wins = False

    def board(self):
        """Gera o board do game"""

        system("clear")
        d = "  1   2   3"
        a = "A {}|{}|{}".format(self.a1, self.a2, self.a3)
        b = "B {}|{}|{}".format(self.b1, self.b2, self.b3)
        c = "C {}|{}|{}".format(self.c1, self.c2, self.c3)
        t = "  -----------"
        print("=" * 65)
        print("||{:^61}||".format("Joguinho da velha v1.0"))
        print("=" * 65)
        print()
        print("{:^65}".format(d))
        print("{:^65}".format(a))
        print("{:^65}".format(t))
        print("{:^65}".format(b))
        print("{:^65}".format(t))
        print("{:^65}".format(c))
        print()

    def names(self):
        """função responsavel por pegar o nome dos jogadores"""

        self.name_p1x = input("Informe o nome do player 1: ")
        self.name_p2o = input("Informe o nome do player 2: ")

    def validator(self, play):
        """Verifica se a jogada é valida e não repetida"""

        name = play[0]
        p = play[1]
        #verifica se a jogada ja foi realizada
        if p not in self.list_try and p in self.valid_list:
            self.list_try.append(p)
            self.includes(play)

        else:
            print("Tente novamente")
            self.validator(self.game_play(play[0]))



    def includes(self,player):
        """Inclui a jogada na tabela"""

        self.plays += 1
        name = player[0]
        p = player[1]

        #player1
        if name == self.name_p1x:
            if p == "A1":
                self.a1 = " X "
            elif p == "A2":
                self.a2 = " X "
            elif p == "A3":
                self.a3 = " X "
            elif p == "B1":
                self.b1 = " X "
            elif p == "B2":
                self.b2 = " X "
            elif p == "B3":
                self.b3 = " X "
            elif p == "C1":
                self.c1 = " X "
            elif p == "C2":
                self.c2 = " X "
            elif p == "C3":
                self.c3 = " X "

        #player2
        elif name == self.name_p2o:
            if p == "A1":
                self.a1 = " O "
            elif p == "A2":
                self.a2 = " O "
            elif p == "A3":
                self.a3 = " O "
            elif p == "B1":
                self.b1 = " O "
            elif p == "B2":
                self.b2 = " O "
            elif p == "B3":
                self.b3 = " O "
            elif p == "C1":
                self.c1 = " O "
            elif p == "C2":
                self.c2 = " O "
            elif p == "C3":
                self.c3 = " O "


    def verify_wins(self):
        """Verifica se alguem venceu"""

        #listas para facilitar a verificação
        self.a_list = [self.a1,self.a2,self.a3]
        self.b_list = [self.b1,self.b2,self.b3]
        self.c_list = [self.c1,self.c2,self.c3]
        self.d_list = [self.a1,self.b2,self.c3]
        self.e_list = [self.a1,self.b1,self.c1]
        self.f_list = [self.a2,self.b2,self.c2]
        self.g_list = [self.a3,self.b3,self.c3]
        self.h_list = [self.a3,self.b2,self.c1]

        #Condicional que verifica se o X ganhou na horizontal e diagonal.
        if self.a_list.count(" X ") == 3 or self.b_list.count(" X ") == 3 or self.c_list.count(" X ") == 3 or self.d_list.count(" X ") == 3:
            print("{} venceu".format(self.name_p1x))
            input()
            self.end_game = True
            self.wins = True

        #Condicional que verifica se o X ganhou na vertical.
        elif self.e_list.count(" X ") == 3 or self.f_list.count(" X ") == 3 or self.g_list.count(" X ") == 3 or self.h_list.count(" X ") == 3:
            print("{} venceu".format(self.name_p1x))
            input()
            self.end_game = True
            self.wins = True

        #Condicional que verifica se o O ganhou.
        elif self.a_list.count(" O ") == 3 or self.b_list.count(" O ") == 3 or self.c_list.count(" O ") == 3 or self.d_list.count(" O ") == 3:
            print("{} venceu".format(self.name_p2o))
            input()
            self.end_game = True
            self.wins = True

        elif self.e_list.count(" O ") == 3 or self.f_list.count(" O ") == 3 or self.g_list.count(" O ") == 3 or self.h_list.count(" O ") == 3:
            print("{} venceu".format(self.name_p2o))
            input()
            self.end_game = True
            self.wins = True

        return self.end_game

    def end(self):
        """verifica se plays == 9"""

        if self.plays == 9 and self.wins == False:
            print("fim de jogo sem vencedores")
            self.end_game = True
        return self.end_game
    def game_play(self, name):
        play = input("{}, informe a LETRA e o NÚMERO da sua jogada: ".format(name)).upper()
        return name, play

    def start(self):
        """função que inicia o jogo"""

        self.names()
        self.end_game = False
        while not self.end_game:
            self.board()
            self.validator(self.game_play(self.name_p1x))
            self.board()
            self.end_game = self.verify_wins()
            self.end_game = self.end()

            if self.end_game == False:
                self.validator(self.game_play(self.name_p2o))
                self.board()
                self.end_game = self.verify_wins()
                self.end_game = self.end()
                if self.plays == 9 and self.wins == False:
                    print("fim do jogo sem vencedores")
                    input()


            self.board()

game = Game()
game.start()
"""
0 - PEDE OS NOMES DOS PLAYERS = FUNÇÃO NAME
1 - EXIBE O BOARD = FUNÇÃO BOARD
2 - N° 1 FAZ JOGADA = FUNÇÃO game_play1
3 - VERIFICA SE A JOGADA É VALIDA E NÃO REPETIDA. = FUNÇÃO VALIDATOR
3.1 - SE FOR VALIDA RETORNA A JOGADA
4 - INCLUI A JOGADA VALIDA NO BOARD, SOMA + 1 A PLAYS. = FUNC INCLUDES
1 - EXIBE O BOARD
5 - VERIFICA SE N° 1 VENCEU. = FUNC VERIFY_WINS
5.1 - VERIFICA SE PLAYS == 9. = FUNC END
5.2 - SE N°1 NÃO TIVER VENCIDO ENTÃO N° 2 FAZ JOGADA = FUNÇÃO game_play2
3 - VERIFICA SE A JOGADA É VALIDA E NÃO REPETIDA.
3.1 - SE FOR VALIDA RETORNA A JOGADA
4 - INCLUI A JOGADA VALIDA NO BOARD, SOMA + 1 A PLAYS.
1 - EXIBE O BOARD
5 - VERIFICA SE N° 2 VENCEU.
5.1 - VERIFICA SE PLAYS == 9.
5.2 - SE N°2 NÃO TIVER VENCIDO RETORNA FALSE E N° 1 FAZ JOGADA
"""
