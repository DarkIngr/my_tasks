team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 10717.6
name1 = 'Мастера кода'
name2 = 'Волшебники Данных'
challenge_result = ''

print('В команде %s участников: %s !' % (name1, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда {} решила задач: {}!'.format(name2, score_2))
print('{} решили задачи за {} c !'.format(name2, team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Результат битвы: победа команды {name2}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Результат битвы: победа команды {name1}!'
else:
    challenge_result = 'Ничья!'

print(challenge_result)

print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по '
      f'{round((team1_time + team2_time)/(score_1 + score_2), 1)} секунды на задачу!')