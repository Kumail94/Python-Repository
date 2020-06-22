player_Scores = {}
with open ("Book.csv" ,"r") as f:
	for item in f:
		tokens = item.split(',')
		player = tokens[0]
		scores = int(tokens[1])
		if player in player_Scores:
			player_Scores[player].append(scores)
		else:
			player_Scores[player] = [scores]
print(player_Scores)
print('\n')			
for player , score_list  in player_Scores.items():
	min_score = min(score_list)
	max_score = max(score_list)
	avg_score = sum(score_list)/len(score_list)
	print(f"{player} ==> Min:{min_score} , Max:{max_score} , Average:{avg_score}")
		

