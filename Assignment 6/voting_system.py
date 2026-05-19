"""Build a simple voting system using functions and global variables.

   create the following global variables:
   candidates---> a dictionary where keys are candidate names and values start at 0 votes.
   preload with 4 candidates of your choice.
   voted_voters-->an empty list to store names of people who have already voted.
   total _votes-->a global integer starting at 0

   Create the following functions:
   show_candidates()-->display all candidateswith their current vote count
   cast_vote(voter_name,candidate_name)-->validates:
   -voter name cannot be empty
   -voter has not already voted
   (check against voted voters)
   -candidate name must exist in the canidates dictionary
   -if all valid:add vote,record voter,update total_votes
   -print success or error message for each case
   Show_results()-->displays the current vote count for each candidate,total votes cast
                     and the leading candidate so far
   declare_winner()-->loops through candidates to find winner,handles a tie between two or more candidates,
                       print the final result

   run a loop presenting a menu:show candidates/caste vote/show results/declare winner/exit"""

candidates={"AAP":0,"BJP":0,"Congress":0,"DMK":0}
voted_voters=[]
t_v=0

def show_candidates():
    i=65
    for candidate in candidates:
        print(chr(i),". ",candidate)
        i=i+1

def caste_vote(voter_name,candidate_name):
    global t_v
    if(voter_name==" "):
        print("Error..!Voter name cannot be empty")
        return

    for voters in voted_voters:
        if voters==voter_name:
            print("Error..!Voter has already voted")
            return
        i=0
    for candidate in candidates:

        if(candidate_name==candidate):
            voted_voters.append(voter_name)
            t_v+=1
            candidates[candidate_name]+=1
            print(voter_name,"vote for ",candidate_name,"has been recorded!")
            break
        else:
            i+=1
            if(i==len(candidates)):
                print("Error!",candidate_name,"is not a valid  candidate")
            else:
                continue

def show_results():
    print("----Current Results---- ")
    for candidate in candidates:
        print(candidate,":",candidates[candidate],"vote(s)")
    print("Total Votes Cast: ",t_v)
    max=0
    for candidate in candidates:
        if(candidates[candidate]>=max):
            max=candidates[candidate]
    for candidate in candidates:
        if(candidates[candidate]==max):
            leading=candidate
            print("Currently Leading: ",leading)

def declare_winner():
    max=1
    for candidate in candidates:
        if(candidates[candidate]>=max):
            max=candidates[candidate]
    for candidate in candidates:
        if(candidates[candidate]==max):
            leading=candidate
            print("Winner: ",leading)

print("--- Voting Menu---")
print("1. Show Candidates")
print("2. Cast Vote")
print("3. Show Results")
print("4. Declare Winner")
print("5. Exit")

while (True):
    print("Choose your option:")
    choice=int(input())
    if(choice==1):
        show_candidates()
    elif(choice==2):
        print("Enter your name:")
        voter_name=input()
        print("Enter candidate name or code:")
        candidate_name=input()
        caste_vote(voter_name,candidate_name)
    elif(choice==3):
        show_results()
    elif(choice==4):
        declare_winner()
    elif(choice==5):
        break
