import numpy
import os
import csv

#checks if votes.csv exists or not
if os.path.exists ('votes.csv'):

    #opens file containing details of vote
    with open('votes.csv') as vfile:
        votelines = vfile.readlines()

    number_of_options = len(votelines)
    Total = [0]* (number_of_options - 1) #5
    Party_votes = [0]* (number_of_options - 1) #5
    votedetails = [0]* (number_of_options) #6

    for i in range (0, number_of_options):
        votedetails[i] = [str(x) for x in votelines[i].rstrip('\n').split(', ')]

    for i in range (0, number_of_options - 1):
        Total[i] = int(votedetails[i][1]) #total party votes
        votedetails[i].remove(votedetails[i][1]);
        votedetails[i].remove(votedetails[i][0]);
        Party_votes[i] = votedetails[i] # vote1-15

    NOTA = int(votedetails[number_of_options - 1][1]) #nota votes

    for i in range (0, number_of_options - 1):
        for j in range (0, len(Party_votes[i])):
            Party_votes[i][j] = int(Party_votes[i][j])

#checks if candidate.csv exists or not
if os.path.exists ('candidates.csv'):

    #opens candidate detail file
    with open('candidates.csv') as pfile:
        partylines = pfile.readlines()

    number_of_parties = len(partylines)
    partydetails = [0]* number_of_parties
    Party = [0]* number_of_parties
    PartyName = [0]* number_of_parties
    max_seats = [0]* number_of_parties
    total_seats = [0]* number_of_parties
    Party_seats = [0]* number_of_parties
    zipped  = [0]* number_of_parties
    rzipped  = [0]* number_of_parties

    for i in range (0, number_of_parties):
        partydetails[i] = [str(x) for x in partylines[i].rstrip('\n').split(', ')]

    for i in range (0, number_of_parties):
        PartyName[i] = partydetails[i][0]
        partydetails[i].remove(partydetails[i][0]);
        Party[i] = partydetails[i]

    for i in range (0, number_of_parties):
        zipped[i] = zip(Party[i], Party_votes[i])
        rzipped[i] = sorted(zipped[i], key = lambda x: x[1], reverse = True)

    for i in range (0, number_of_parties):
        for j in range (0, len(partydetails[i])):
            max_seats[i] = max_seats[i] + 1

#change these to read from csv file
number_of_voters = 322 #number of users
number_of_seats = 15 #default number of seats
extra = 0 #check to see if any party gets more seats that what their max capacity is

#basic structure of variables
seats_left = number_of_seats
number_of_people_who_voted = NOTA
for i in range (0, number_of_parties):
    number_of_people_who_voted = number_of_people_who_voted + Total[i]
number_of_people_who_didnt_vote = number_of_voters - number_of_people_who_voted
election_quotient = number_of_voters / number_of_seats
currentEQ = election_quotient
percent_of_people_who_voted = ((number_of_people_who_voted * 1.0 / number_of_voters)) * 100
percent_of_people_who_didnt_vote = ((number_of_people_who_didnt_vote * 1.0 / number_of_voters)) * 100

#algorithm
while (seats_left != 0) and (currentEQ != 0):
    for i in range (0, number_of_parties):
        no_of_seats = Total[i] / currentEQ
        if no_of_seats > max_seats[i]:
            no_of_seats = max_seats[i]
            Total[i] = 0
        Total[i] = (Total[i] % currentEQ)
        Party_seats[i] = Party_seats[i] + no_of_seats
        if Party_seats[i] > max_seats[i]:
            extra = Party_seats[i] - max_seats[i]
            Party_seats[i] = Party_seats[i] - extra
            Total[i] = 0
        seats_left = seats_left - no_of_seats + extra
    currentEQ = currentEQ - 1
    extra = 0

#recursive algorithm
#takes in election quiotient
#calculates number of seats
#checks total seats
#calls itself with election quotient -1

print
print "Number of seats Won by each party:"
print
for i in range (0, number_of_parties):
    print PartyName[i]
    print Party_seats[i]
    print

print "Meet the HORs:"
for j in range (0, number_of_parties):
    for k in range (0, Party_seats[j]):
        print rzipped[j][k]
print
