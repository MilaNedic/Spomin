import bottle
import model

@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    # naredi novo igro
    tezavnost = int(bottle.request.forms['tezavnost'])
    if tezavnost not in [2, 3, 4]:
        return 'Neveljaven vnos! Vnesi 2, 3 ali 4!'
    spomin = model.Memory(tezavnost)
    bottle.redirect('/skrita/')


@bottle.post('/skrita/')  #želimo, da nam pokaže skrito ploščo
def pokazi_skrito_plosco():
    return 'Tukaj bi se morala pokazati skrita plosca ampak stvar ocitno se ne dela'


bottle.run(debug=True, reloader=True)