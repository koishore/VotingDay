from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q, F
from django.http import HttpResponseRedirect

#Displays index.html
def index(request):
    userlist = User.objects.all()
    template=loader.get_template('index.html')

    #manages the post request
    if request.method=='POST':
        keys = []
        for key, value in request.POST.iteritems():
            keys.append(key)
        keys.remove("csrfmiddlewaretoken")
        if len(keys) > 0:
            print keys
        else:
            print "Invalid Email/UserID!"

    context ={
        'userlist':userlist,
        }
    return HttpResponse(template.render(context,request))

#Displays main.html
def main(request):
    display = Candidate.objects.all()
    template=loader.get_template('main.html')
    context ={
        'display':display,
        }
    return HttpResponse(template.render(context,request))

#Displays register.html
def register(request):
    votebank = Vote.objects.all()
    template=loader.get_template('register.html')

    #manages the post request
    if request.method=='POST':
        keys = []
        #stores votes in t list named keys
        for key, value in request.POST.iteritems():
            keys.append(key)
        keys.remove("csrfmiddlewaretoken")
        if len(keys) > 0:

            #adds vote to NOTA
            if keys == ["group1"] or keys == ["group1", "NOTA+1"]:
                Vote.objects.filter(partyname="NOTA").update(totalvotes=F('totalvotes')+1)

            #saves party name in a variable
            else:
                if "group1" in keys:
                    keys.remove("group1")
                partyNameAndIndex = keys[0].split("+")
                index = []

                for i in keys:
                    x = i.split("+")
                    index.append(x[1])

                index.sort(key=int)
                party = partyNameAndIndex[0]

                #adds the vote to the respective fields
                if True:
                    Vote.objects.filter(partyname=party).update(totalvotes=F('totalvotes')+1)
                if "1" in index:
                    Vote.objects.filter(partyname=party).update(vote1=F('vote1')+1)
                if "2" in index:
                    Vote.objects.filter(partyname=party).update(vote2=F('vote2')+1)
                if "3" in index:
                    Vote.objects.filter(partyname=party).update(vote3=F('vote3')+1)
                if "4" in index:
                    Vote.objects.filter(partyname=party).update(vote4=F('vote4')+1)
                if "5" in index:
                    Vote.objects.filter(partyname=party).update(vote5=F('vote5')+1)
                if "6" in index:
                    Vote.objects.filter(partyname=party).update(vote6=F('vote6')+1)
                if "7" in index:
                    Vote.objects.filter(partyname=party).update(vote7=F('vote7')+1)
                if "8" in index:
                    Vote.objects.filter(partyname=party).update(vote8=F('vote8')+1)
                if "9" in index:
                    Vote.objects.filter(partyname=party).update(vote9=F('vote9')+1)
                if "10" in index:
                    Vote.objects.filter(partyname=party).update(vote10=F('vote10')+1)
                if "11" in index:
                    Vote.objects.filter(partyname=party).update(vote11=F('vote11')+1)
                if "12" in index:
                    Vote.objects.filter(partyname=party).update(vote12=F('vote12')+1)
                if "13" in index:
                    Vote.objects.filter(partyname=party).update(vote13=F('vote13')+1)
                if "14" in index:
                    Vote.objects.filter(partyname=party).update(vote14=F('vote14')+1)
                if "15" in index:
                    Vote.objects.filter(partyname=party).update(vote15=F('vote15')+1)
        else:
            print "NOTA voted"
            Vote.objects.filter(partyname="NOTA").update(totalvotes=F('totalvotes')+1)

    return HttpResponse(template.render(request))

#Displays result.html
def results(request):

    template=loader.get_template('results.html')

    #gets required details from the database
    PartyName = [e.party_name for e in Candidate.objects.exclude(party_name="NOTA")]
    number_of_parties = int(len(PartyName))
    NOTA = int([e.totalvotes for e in Vote.objects.filter(partyname="NOTA")][0])
    Total = [int(e.totalvotes) for e in Vote.objects.exclude(partyname="NOTA")]

    #initialising the lists for use in algorithm
    Party = [0]* number_of_parties
    Party_votes = [0]* number_of_parties
    max_seats = [0]* number_of_parties
    Party_seats = [0]* number_of_parties
    zipped  = [0]* number_of_parties
    rzipped  = [0]* number_of_parties

    #counter variable to run a loop simultaneously with 2 variable increment
    count = 0

    #initialises the party and sets the deletes the null values
    for e in Candidate.objects.exclude(party_name="NOTA"):
        Party[count] = [e.candidate1, e.candidate2, e.candidate3, e.candidate4, e.candidate5, e.candidate6, e.candidate7, e.candidate8, e.candidate9, e.candidate10, e.candidate11, e.candidate12, e.candidate13, e.candidate14, e.candidate15]
        Party[count] = [e for e in Party[count] if e != "NULL"]
        count+=1

    #reinitialises count to 0
    count = 0

    #initialises the list of votes and removes NOTA votes
    for e in Vote.objects.exclude(partyname="NOTA"):
        Party_votes[count] = [e.vote1, e.vote2, e.vote3, e.vote4, e.vote5, e.vote6, e.vote7, e.vote8, e.vote9, e.vote10, e.vote11, e.vote12, e.vote13, e.vote14, e.vote15]
        Party_votes[count] = [e for e in Party_votes[count] if e != '-1']
        count+=1

    #sorts party names w.r.t to number of votes
    for i in range (0, number_of_parties):
        zipped[i] = zip(Party[i], Party_votes[i])
        rzipped[i] = sorted(zipped[i], key = lambda k: k[1], reverse = True)

    #checks maximum seats for a given party
    for i in range (0, number_of_parties):
        max_seats[i] = len(Party[i])

    #total number of voters that cast their voter
    number_of_voters = 322

    #number of seats. Set to 15, since it is Ashoka convention
    number_of_seats = 15
    extra = 0

    #basic structure of variables
    seats_left = number_of_seats
    number_of_people_who_voted = NOTA
    number_of_people_who_voted = 0
    for i in Total:
        number_of_people_who_voted += i
    number_of_people_who_didnt_vote = number_of_voters - number_of_people_who_voted
    election_quotient = number_of_voters / number_of_seats
    currentEQ = election_quotient
    percent_of_people_who_voted = ((number_of_people_who_voted * 1.0 / number_of_voters)) * 100
    percent_of_people_who_didnt_vote = ((number_of_people_who_didnt_vote * 1.0 / number_of_voters)) * 100

    # algorithm (can be made recursive, but time complexity will increrase)
    while (seats_left != 0) and (currentEQ != 0):
        for i in range (0, number_of_parties):
            no_of_seats = Total[i] / currentEQ #number of seats won by party
            if no_of_seats > max_seats[i]: #check to see if party got more seats than their strength
                no_of_seats = max_seats[i] #revoke seats back to max_seats if there are extra(s)
                Total[i] = 0 #set the remaining seats to 0
            Total[i] = (Total[i] % currentEQ) #decrease the total seats if not first case deployed
            Party_seats[i] = Party_seats[i] + no_of_seats #add party seats
            if Party_seats[i] > max_seats[i]: #check if total party seats is greater than max_seats
                extra = Party_seats[i] - max_seats[i] #set extra to the extra number of seats
                Party_seats[i] = Party_seats[i] - extra #find actual number of seats by party
                Total[i] = 0 #set total to 0
            seats_left = seats_left - no_of_seats + extra #calculate number of seats left
        currentEQ = currentEQ - 1 #decrease election quotient by 1
        extra = 0 #reset extra to 0 for next interation of loop

    #recursive algorithm
    #takes in election quiotient
    #calculates number of seats
    #checks total seats
    #calls itself with election quotient -1

    #makes a list of people who got elected and saves them with the number of votes zipped
    result = []
    for i in range (0, number_of_parties):
        for j in range (0, Party_seats[i]):
            result.append(rzipped[i][j])

    #unzips zipped lists and creates a list of elected candidates
    temp = [list(t) for t in zip(*result)]
    Candlist = temp[0]

    context ={
        'PartyName':PartyName,
        'Party_seats':Party_seats,
        'Candlist':Candlist
        }

    return HttpResponse(template.render(context,request))
