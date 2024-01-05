def solution(players, callings):
    answer = []
    players_dict = {players[i]:i for i in range(len(players))}
    for call in callings:
        back_index = players_dict[call]
        front_index = back_index - 1
        players_dict[call] = front_index
        players_dict[players[front_index]] = back_index
        players[back_index], players[front_index] = players[front_index], players[back_index]
    answer = players
    return answer