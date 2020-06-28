import requests
#FUNCIÓN PARA PODER APLICAR LA FUNCIÓN NATIONS_RANK Y RECOGER LOS 50 MEJORES RANKINGS ANTES DEL MUNDIAL RESPECTIVO

def best_fifty(x):
    return x.find("tbody").find_all("tr")[0:50]


def nations_rank(nation):
    celdas = nation.find_all("td")
    country = celdas[1].find("a").text.strip().split('\n')
    print(country)
    return {
        "Year" : 1994,
        "Position": int(celdas[0].text),
        "Country": country[0],
        "Image": celdas[1].find("img")["src"]
    }

def checkerror(x,y):
    try:
        if 1993<int(x)<2015:
            pass
    except Exception:
        raise ValueError("You have to enter a number between 1994-2014")
        
    try:
        if 0<int(y)<51:
            pass
    except Exception:
        raise ValueError("You have to enter a number between 1-50")

def filter_data(w,x,y):
    z=w[w.Year == x]
    z=z[(z.Position_x == y) | (z.Position_y == y)]
    return z

def dropcol(x):
    y = x.drop(['Datetime', 'Stage', 'Stadium', 'City', 'Attendance', 'Half-time Home Goals',
       'Half-time Away Goals', 'Referee', 'Assistant 1', 'Assistant 2',
       'RoundID', 'MatchID', 'Home Team Initials', 'Away Team Initials'],axis=1)
    return y



def plot(x,y):
    return plt.bar(wc_matches_clean.x, wc_matches_clean.y)

#Esta era para sacar las imágenes de la columna con la url que tengo en el dataset

def imagerequest(x,y):
    for x in y:
        z = requests.get(str(x))
    
        return z