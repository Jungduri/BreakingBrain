def solution(players, callings):
    players_dict = {players:i for i, players in enumerate(players)}
    
    for call in callings:
        overtake_idx = players_dict[call]
        overtaken_name = players[overtake_idx-1]
        overtaken_idx = players_dict[overtaken_name]
        
        players_dict[call] = overtaken_idx
        players_dict[overtaken_name] = overtake_idx
        
        players[overtaken_idx], players[overtake_idx] = players[overtake_idx], players[overtaken_idx]
    
    answer = players
    
    return answer