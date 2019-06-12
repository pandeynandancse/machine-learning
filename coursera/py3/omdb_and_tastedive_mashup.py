import requests

def get_movies_from_tastedive(movieName, key="327878-course3p-I4ZNBN4A"):
    baseurl="https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"]= movieName
    params_d["k"]= key
    params_d["type"]= "movies"
    params_d["limit"] = "5"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic 

def extract_movie_titles(movieName):
    result=[]
    for listRes in movieName['Similar']['Results']:
        result.append(listRes['Name'])
    return result
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
def get_related_titles(listMovieName):
    if listMovieName != []:
        auxList=[]
        relatedList=[]
        for movieName in listMovieName:
            auxList = extract_movie_titles(get_movies_from_tastedive(movieName))
            for movieNameAux in auxList:
                if movieNameAux not in relatedList:
                    relatedList.append(movieNameAux)
        
        return relatedList
    return listMovieName

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


def get_movie_data(movieName, key="546c6742"):
    baseurl= "http://www.omdbapi.com/"
    params_d = {}
    params_d["t"]= movieName
    params_d["apikey"]= key
    params_d["r"]= "json"
    resp = requests.get(baseurl, params=params_d)
    print(resp.url)
    respDic = resp.json()
    return respDic
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

def get_movie_rating(movieNameJson):
    strRanting=""
    for typeRantingList in movieNameJson["Ratings"]:
        if typeRantingList["Source"]== "Rotten Tomatoes":
            strRanting = typeRantingList["Value"]
    if strRanting != "":
        ranting = int(strRanting[:2])
    else: ranting = 0
    return ranting

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))


def get_sorted_recommendations(listMovieTitle):
    listMovie= get_related_titles(listMovieTitle)
    listMovie= sorted(listMovie, key = lambda movieName: (get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)
    
    return listMovie

print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

