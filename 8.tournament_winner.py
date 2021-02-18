def tournamentWinner(competitions, results):
    # Write your code here.
    record = {}
    max_score = 0
    for i in range(len(competitions)):
        team_1 = competitions[i][0]
        team_2 = competitions[i][1]

        if results[i] == 1:
            tmp_winner = team_1
        else:
            tmp_winner = team_2

        if tmp_winner in record:
            his_score = record[tmp_winner]
        else:
            his_score = 0

        if his_score + 3 > max_score:
            max_score = his_score + 3
            winner = tmp_winner

        record[tmp_winner] = his_score + 3

    return winner
