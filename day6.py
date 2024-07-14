class Player:
    """ A single player in the game
    """
    def __init__(self, name: str, points: int = 0):
        self.name = name
        self.points = points



class Game():
    def __init__(self):
        self.scoreboard = {}

    
    def add_player(self, name, points) -> type[Player] | None:
        player = Player(name, points)
        if name in self.scoreboard:
            print("Este jogador já está cadastrado.")
            return None
        else:
            self.scoreboard[name] = points
            print(f"Jogador adicionado: {name}")
            return player
        
    
    def remove_player(self, name):
        if name in self.scoreboard:
            del self.scoreboard[name]
            print(f"Jogador removido: {name}")
        else:
            print("Jogador não encontrado.")

    
    def update_points(self, name, new_points):
        if name in self.scoreboard:
            self.scoreboard[name] = new_points
            print("Pontuação atualizada.")
        else:
            print("Jogador não encontrado.")


    def sort_players_by_points(self) -> dict:
        if self.scoreboard:
            filtered_list = sorted(self.scoreboard.items(), key = lambda item: item[1], reverse = True)
            filtered_dict = dict(filtered_list)
            return filtered_dict
        else:
            return {}
        

    def tie(self):
        if self.scoreboard:
            sorted_dict = self.sort_players_by_points().items()
            iterable_sorted_dict = iter(sorted_dict)
            possible_winner_points = next(iter(sorted_dict))[1]
            tied_winners = {}
            for key, value in iterable_sorted_dict:
                if value == possible_winner_points:
                    tied_winners[key] = value
            return tied_winners


    def winner(self):
        if self.scoreboard:
            if len(self.tie()) <= 1:
                winner = next(iter(self.sort_players_by_points().items()))
                print("E o vencedor do jogo é...")
                print(f"{winner[0]}, com {winner[1]} pontos!")
            else:
                print("Houve um empate!")
                print("E os vencedores são...")
                for player, points in self.tie().items():
                    print(f"{player}: {points} pontos")
            print("\n\n")
        else:
            print("Nenhum jogador na lista.")
            print("\n\n")


    def list_all_players(self):
        if self.scoreboard:
            print("Lista de jogadores:")
            players_list = self.sort_players_by_points()
            for key, value in players_list.items():
                print(f"{key} \t {value}")
        else:
            print("Nenhum jogador na lista.")
        print("\n")


def main():
    game = Game()
    game.list_all_players()
    # game.winner()

    game.add_player("Eduardo", 0)
    game.add_player("Vitor", 0)

    game.list_all_players()
    game.winner()

    game.add_player("Lucato", 0)

    game.list_all_players()
    game.winner()

    game.update_points("Eduardo", 10)
    game.update_points("Vitor", 5)

    game.list_all_players()
    game.winner()

    game.add_player("Biner", 10)

    game.list_all_players()
    game.winner()

    game.add_player("Suspiquill", 5)

    game.list_all_players()
    game.winner()


main()
    