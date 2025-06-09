class Game:
    class Pary:
        __slots__ = ('first', 'second', 'pick')
        def __init__(self, first=0, second=0, pick=0):
            self.first = first
            self.second = second
            self.pick = pick

        def __str__(self):
            return f"{self.first} {self.second} {self.pick}"

    def find_moves(self, pots):
        n = len(pots)
        moves = [[self.Pary() for _ in range(n)] for _ in range(n)] 
        
        for i in range(n):
            moves[i][i].first = pots[i]
            moves[i][i].pick = i
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                left_pick = pots[i] + moves[i+1][j].second
                right_pick = pots[j] + moves[i][j-1].second
                
                if left_pick > right_pick:
                    moves[i][j].first = left_pick
                    moves[i][j].second = moves[i+1][j].first
                    moves[i][j].pick = i
                else:
                    moves[i][j].first = right_pick
                    moves[i][j].second = moves[i][j-1].first
                    moves[i][j].pick = j
        return moves

    def print_sequence(self, pots, moves):
        i = 0
        j = len(pots) - 1
        first_moves = []
        second_moves = []
        turn = 0
        
        for _ in range(len(pots)):
            step = moves[i][j].pick
            value = pots[step]
            if turn == 0:
                first_moves.append(value)
            else:
                second_moves.append(value)
            turn = 1 - turn
            
            if step == i:
                i += 1
            else:
                j -= 1
        
        first_str = ", ".join(map(str, first_moves))
        second_str = ", ".join(map(str, second_moves))
        total_first = sum(first_moves)
        total_second = sum(second_moves)
        
        print(f"First player: {first_str} | Sum: {total_first}")
        print(f"Second player: {second_str} | Sum: {total_second}")
        return total_first, first_str, second_str


if __name__ == "__main__":
    npg = Game()
    # pots = [3, 9, 1, 2]
    # pots = [3, 9, 1, 2,4,6,11,44,21,8]
    pots = [2,33,11,1]
    moves = npg.find_moves(pots)
    

    total_first, first_moves, second_moves = npg.print_sequence(pots, moves)
    print(f"\nFinal result: {first_moves} / {second_moves}")
    print(f"Maximum amount won by first player: {total_first}")
    