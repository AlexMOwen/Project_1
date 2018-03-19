import csv

# Sorts players into equal teams by experience level and writes sorted teams to a text file.
# Function takes the file path & delimiter as arguments and team names as kwargs with empty lists as values.
# Returns dict with team names as keys and lists of dicts containing player info as values. 
def experience_sorter(filepath, file_delimiter, **kwargs):
    
    # Kwargs become key names in teams dict with empty lists as values
    teams = kwargs

    # Opens csv file and reads it as a dict.
    with open(filepath) as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = file_delimiter)
 
        # Lists to hold experienced & inexperienced player dicts.
        experienced_players = []
        inexperienced_players = []
        
        # Sorts players into experienced and inexperienced lists based on data in csv file.
        for row in csvreader:
            if row['Soccer Experience'].upper() == 'YES':
                experienced_players.append(row)
            elif row['Soccer Experience'].upper() == 'NO':
                inexperienced_players.append(row)

        # Splits experienced & inexperienced players equally between teams.
        # If number of players cannot be split equally between teams (e.g. 9 players 2 teams, 19 players 3 teams etc) remaining players will not be added, keeping the teams even.
        # Once completed, 'teams' will be a dictionary with lists of dictionaries as values.
        while len(experienced_players) + len(inexperienced_players) >= len(teams) * 2:
            for team in teams:
                teams[team].append(experienced_players.pop())
                teams[team].append(inexperienced_players.pop())

    # writes sorted teams to a new text file
    with open('teams.txt', 'a') as text_file:
        for team in teams:
            text_file.write('\n' + team + '\n')
            for player_dict in teams[team]:
                text_file.write(player_dict['Name'] + ', ' + player_dict['Soccer Experience'] + ', ' + player_dict['Guardian Name(s)'] + ',' + '\n')

    return teams

# Writes welcome letters customised to each player in 'arg'.
# This code seemed more suited to its own function than being part of roster_builder().
def welcome_letters(arg):
    for team in arg:
        for player_dict in arg[team]:
            with open(player_dict['Name'].lower().replace(' ', '_') + '.txt', 'a') as welcome_letter:
                welcome_letter.write('Dear ' + player_dict['Guardian Name(s)'] + ',' + '\n\n')
                welcome_letter.write('I am writing to formally welcome your son/ daughter, ' + player_dict['Name'] + ', to the ' + team + ' soccer team. The first team practice is scheduled for Saturday the 24th of March at 10:30am, we look forward to seeing you there. \n\nCoach' )


if __name__ == '__main__':
    # Calls the functions with appropriate information.
    soccer_teams = experience_sorter('soccer_players.csv', ',', Dragons = [], Raptors = [], Sharks = [])
    welcome_letters(soccer_teams)



