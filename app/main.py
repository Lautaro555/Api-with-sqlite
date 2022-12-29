from fastapi import FastAPI
import sqlite3

app=FastAPI()

#Conection to the database and cursor creation
conn = sqlite3.connect('app/database.db',check_same_thread=False)
cur = conn.cursor()

#Function to obtain maximum duration in minutes or seasons, of the specified platform and year
@app.get("/get-max-duration/{year-platform-duration}")
async def get_max_duration(año:int, plataforma:str, duration_type:str):
    if duration_type=="min":
        cur.execute(f"SELECT title FROM {plataforma} WHERE release_year={año} AND type='Movie' ORDER BY duration DESC LIMIT 1")
    elif duration_type=="season":
        cur.execute(f"SELECT title FROM {plataforma} WHERE release_year={año} AND type='TV Show' ORDER BY duration DESC LIMIT 1")
    return cur.fetchone()[0]

#Function to obtain the number of movies and series of the specified platform
@app.get("/get-count-plataform/{plataforma}")
async def get_count_plataform(plataforma):
    cur.execute(f"SELECT COUNT(*) FROM {plataforma} WHERE type == 'Movie'")
    movies = cur.fetchone()[0]
    cur.execute(f"SELECT COUNT(*) FROM {plataforma} WHERE type == 'TV Show'")
    series = cur.fetchone()[0]
    dict={"Number of series":int(series),"Number of movies":int(movies)}
    return dict

#Function to obtain the platform in which the specified genre is most repeated
@app.get("/get-listedin/{genero}")
async def get_listedin(genero:str):
    amazon_count = 0
    hulu_count = 0
    disney_count = 0
    netflix_count = 0
    
    cur.execute("SELECT * FROM amazon")
    for row in cur.fetchall():
        if genero in row[9].split(","):
            amazon_count += 1
    cur.execute("SELECT * FROM netflix")
    for row in cur.fetchall():
        if genero in row[9].split(","):
            netflix_count += 1
    cur.execute("SELECT * FROM hulu")
    for row in cur.fetchall():
        if genero in row[9].split(","):
            hulu_count += 1
    cur.execute("SELECT * FROM disney")
    for row in cur.fetchall():
        if genero in row[9].split(","):
            disney_count += 1
    
    dict_count = {"Amazon": amazon_count, "netflix": netflix_count, "hulu": hulu_count, "disney": disney_count}
    max_value = max(dict_count.values())
    max_platform = key = [key for key, val in dict_count.items() if val == max_value][0]
    return max_platform, max_value

#Function to obtain the number of times an actor or actress is repeated and their name, on the specified platform and year
@app.get("/get_actor/{platform-year}")
async def get_actor(plataforma:str, año:int):
    cur.execute(f"SELECT {plataforma}.cast FROM {plataforma} WHERE release_year={año}")
    actors=cur.fetchall()
    list=[]
    for i in actors:
        if i != 0:
            s=i[0].split(",")
            for a in range(len(s)):
                if s[a] not in list and s[a] != "0":
                    list.append(s[a])
    dict={}
    for i in list:
        cur.execute(f"SELECT {plataforma}.cast FROM {plataforma} WHERE release_year={año}")
        actors=cur.fetchall()
        c=0
        for n in actors:
            if i in n[0].split(","):
                c+=1
        dict[i]=c
    max_value=max(dict.values())
    max_actor= [key for key, val in dict.items() if val == max_value][0]
    return max_actor , max_value

