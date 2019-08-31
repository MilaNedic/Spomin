import bottle
import model
import ast
from bottle import request	

trenutne_igre = []

@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    tezavnost = int(bottle.request.forms['tezavnost'])
    if tezavnost not in [2, 3, 4]:
        return 'Neveljaven vnos! Vnesi 2, 3 ali 4!'
    id_igre = len(trenutne_igre)              #ig_igre je pripadajoc indeks igre v seznamu trenutnih iger
    spomin = model.Memory(tezavnost)
    trenutne_igre.append(spomin)     
    bottle.redirect('/skrita?tezavnost=' + str(tezavnost) + '&id_igre=' + str(id_igre) + '&kliknjena=')	


@bottle.get('/skrita') 
def pokazi_skrito_plosco():

    tezavnost = int(request.query['tezavnost'])		#iz get tabele preberemo tezavnost
    id_igre = int(request.query['id_igre'])         #iz get tabele preberemo id_igre
    
    spomin = trenutne_igre[id_igre]       #trenutno igra je definirana z id-jem, torej pozicija v seznamu trenutnih igre
    skrita_plosca = spomin.skrita         #generiramo skrito plosco
    plosca = spomin.plosca                #generiramo plosco, ki jo ugibamo
    
    output_1 = '<style> table { border-collapse: separate; background-color: lavender; }'
    output_1 += 'table, td, th { border: 2px solid black; border-color: purple;}'
    output_1 += 'td { width: 30; height: 30; padding: 20; }'
    output_1 += 'a {text-decoration: none;}'
    output_1 += 'a {visited-color: blue;}'
    output_1 += 'td, th { text-align: center; font-size: 25;}</style>'
    output_1 += '<h1 style="font-size:50px;"><i>Spomin</i></h1> <table>'	
    output_2 = '<tr>''<td>''<p>''<h3>'

    niz = request.query['kliknjena']
    originalNiz = request.query_string
    polja = niz.count('[') #prestejemo st [, da dobimo stevilo polj, ki smo jih ugibali
    niz = niz.rstrip(',')
    if niz != '':
        niz = ast.literal_eval('[' + niz + ']')
        if polja == tezavnost:
            for element in niz:
                element =  [ int(x) for x in element]
            if spomin.ugibaj(niz) == 1:
                output_2 += 'Uganil si! :)'
                output_2 += '</p>''</td>''</tr>'
                if spomin.zmaga() == True:
                    return bottle.template('zmaga.tpl')     #ko zmagamo, zelimo, da nas bottle preusmeri na novo stran, ki am pove, da smo zmagali in ima moznost izbire nove igre
            else:
                output_2 += 'Nisi uganil. :( '
                output_2 += '</h3>''</p>''</td>''</tr>'
            originalNiz = 'tezavnost=' + str(tezavnost) + '&id_igre=' + str(id_igre) + '&kliknjena='    
    else:
        niz = []
    i = 0
    while i < 4:                                           #generiramo tabelo ustrezne velikosti, torej s 4 vrsticami in 6 stolpci
        j = 0
        output_1 += '<tr>'
        while j < 6: 
            output_1 += '<td>'
            if skrita_plosca[i][j] != '*':
                output_1 += skrita_plosca[i][j]             #elementi tabele so skrita polja, ki jih ugibamo
            elif [i, j] in niz:
                output_1 += '<span>' + plosca[i][j] + '</span>'     #ce je polje v nizu, zelimo, da se nam dano polje odpre, torej vidimo element polja
            else:    
                output_1 += '<a href = /skrita?' + originalNiz + '[' + str(i) + ',' + str(j) + '],>*</a>' 	
            
            output_1 += '</td>'									
            j += 1
        output_1 += '</tr>'
        i += 1
    output_1 += '</table>'
    return output_1, output_2

bottle.run(debug=True, reloader=True)

