import re
file = open("movieData.txt").read()
text = file.split("\n")[:-1]

all_movies = [] #a "list of lists" of all movies in the data;
all_actors = [] #a list of all actors in the data;


dictionary_one = {} #key: actors, value: set of movies;
for i in range(len(text)): #for every string i of the list data;
    text[i] = text[i].replace("&", "and")
    first_comma = text[i].find(",") #find the index of the first comma in each string i;
    actor = text[i][0:first_comma] #all the characters before the first comma is the actor;
    movie = [movie.strip() for movie in text[i][first_comma + 1:].split(", ")] #the rest are movies;
    
    all_movies.append(movie) #append the list "movie" to the list all_movies;
    all_actors.append(actor) #append the string "actor" to the list all_actors;
    
    dictionary_one[actor] = set(movie) #key: actors, value: set of movies;

def actors(dictionary = dictionary_one.items()): #given dictionary_one;
    result = set()
    for actor, set_of_movies in dictionary: #for every key (actor) and value (movies) of the dictionary;
        if movie in set_of_movies: #if a movie (declared in the next loop outside the function) is in the value;
            result.add(actor) #add the movie's key to the set result;
    return result 

dictionary_two = {} #key: movies, value: set of actors;
for i in range(len(all_movies)): #for every list i of the "list of lists" all_movies;
    for movie in all_movies[i]: #for every movie in list i;
        if movie not in dictionary_two.keys(): #if the movie is not a key in dictionary_two;
            dictionary_two[movie] = actors() #add the movie as a key with the value given by actors();
        else: #if the movie is already a key in dictionary_two;
            for actor in actors(): #for all actors in the set given by actors();
                dictionary_two[movie].add(actor) #simply add the actors to the existing value
                 
def actors_or_movies(Command, operator):
    input = Command.split(operator)
    
    if input[0] in all_actors and input[1] in all_actors:
        return "both are actors"
    elif any(input[0] in i for i in all_movies) and any(input[1] in i for i in all_movies):
        return "both are movies"
    else: 
        return "invalid"

def set_operations(Command, operator):
    input = Command.split(operator) 
    
    set_1 = set()
    set_2 = set()
    if actors_or_movies(Command, operator) == "both are actors": #if the input is two actors;
        set_1.update(dictionary_one[input[0]]) #let set_1 be the set of movies by the first actor;
        set_2.update(dictionary_one[input[1]]) #let set_2 be the set of movies by the second actor;
    elif actors_or_movies(Command, operator) == "both are movies": #if the input is two movies;
        set_1.update(dictionary_two[input[0]]) #let set_1 be the set of actors in the first movie;
        set_2.update(dictionary_two[input[1]]) #let set_2 be the set of actors in the second movie;
        
    result = set()
    if operator.strip() == "|": #if the operator is |, 
        result.update(set_1.union(set_2)) #let result be the union of the sets
    elif operator.strip() == "&": #if the operator is &,
        result.update(set_1.intersection(set_2)) #let result be the intersection of sets
    elif operator.strip() == "^": #if the operator is ^,
        result.update(set_1.symmetric_difference(set_2)) #let result be the symmetric difference of the sets
    
    if len(result) > 0:
        return result
    else:
        return "The set operation between the two actors or two movies yields an empty set."

def costars(Command):
    set_of_movies = set()
    for i, j in dictionary_two.items():
        if Command in j: 
            set_of_movies.add(i) 
            
    set_of_actors = set()
    for i in set_of_movies: 
        for j, k in dictionary_one.items(): 
            if i in k: 
                set_of_actors.add(j)
                
    set_of_actors.remove(Command) 

    result = {}
    for i, j in dictionary_one.items(): 
        if i in set_of_actors: 
            result[i] = set_of_movies.intersection(j) 
    
    if len(result) > 0:
        return result
    else:
        return Command + " does not have any costars in the data."

print("Please ensure that the text file is in the same directory as this program. To perform set operations, there must be")
print("one or more spaces before and after the operator (&, ^, |). Please input \"end the program\" when you are finished.")
print("Note that the commands don't capture partial matches of actors or movies; they are also case-sensitive. A message will")
print("appear accordingly when an actor has no costar(s); a set operation is not defined; or an actor/movie does not exist in")
print("the data. The program automatically removes leading/trailing spaces and trims extra white spaces in your commands ")
print("with the exception of \"end the program.\" Although the movie Mr & Mrs Smith contains a set operator, you can still")
print("input the movie as a command to perform set operations; an \"and\" can also take the place of \"&\" in the title.")

pattern_one = ".+(\s[\^\|\&]\s).+" #commands 1 - 3;
pattern_two = "[A-Za-z\s]+" #command 4;

stopping_condition = 0
while stopping_condition == 0: #as long as the stopping_condition equals 0;
    Command_untrimmed = input("Command: ")
    
    
    if Command_untrimmed != "end the program": #if the command doesn't end the program;
        Command = re.sub("\s+", " ", Command_untrimmed).strip()
        
        if "Mr & Mrs Smith" in Command: #a special case where a movie contains a set operator
            Command = Command.replace("Mr & Mrs Smith", "Mr and Mrs Smith")
            
        #check if the command matches pattern_one;
        if re.match(pattern_one, Command):
            operator = re.match(pattern_one, Command).group(1) 
            if actors_or_movies(Command, operator) != "invalid": #if the two actors or two movies exist in the data;
                print(set_operations(Command, operator)) #perform the set operation;
            else: #if at least one of the two actors or two movies does not exist in the data;
                print("At least one of the two actors or two movies does not exist in the data.")
                
        #check if the command matches pattern_two and whether it's an actor that exists in the data;
        elif re.match(pattern_two, Command) and Command in all_actors:
            print(Command + "\'s costars in the data include:")
            if len(costars(Command)) > 0: #if the actor indeed has costars;
                for actor, movie in costars(Command).items(): 
                    print(actor + ": " + str(movie))
            else: #if the actor has no costars;
                print(costars(Command))
                   
        #otherwise,
        else: 
            print("The command is not valid or the actor does not exist in the data.")
            
    else: 
        stopping_condition-=1
        print("You have ended the program.")
        
        