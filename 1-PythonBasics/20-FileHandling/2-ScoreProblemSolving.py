# you have scores.csv file
# cal the min , max, total and avg scores of each player
player_scores={}

with open("scores.csv",'r') as f:
    for line in f:
        player, matchID, score = line.split(',')
        score = int(score.strip())
        print(player,matchID,score)

        if player not in player_scores:
            player_scores[player] = [score]
        else:
            player_scores[player].append(score)

print(player_scores)
for player, scores in player_scores.items():
    min_score = min(scores)
    max_score = max(scores)
    total_score = sum(scores)
    avg_score = total_score/len(scores)
    print(f"{player} : min score is {min_score} , max score is {max_score}, total runs are {total_score}, average run score is {avg_score}")


