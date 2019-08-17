import bottle
import model
from bottle import request	# rabimo uvozit da lahko delamo z get tabelo

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
	bottle.redirect('/skrita?tezavnost=' + str(tezavnost))		# v get tabelo shranimo izbrano težavnost


@bottle.get('/skrita')  #želimo, da nam pokaže skrito ploščo
def pokazi_skrito_plosco():

	tezavnost = request.query['tezavnost']		#iz get tabele preberemo težavnost

	tezavnost = int(tezavnost)

	output = '<h1>Spomin</h1> <table>'		# generiramo html tabelo na podlagi težavnosti

	if tezavnost == 2:
		i = 0
		while i < 4:
			j = 0
			output += '<tr>'
			while j < 6:
				output += '<td> <img src="img/slika.jpg" alt="Slika" height="50" width="50">	</td>'		# treba zgruntat kje bottle išče slike ker ne delajo
				j += 1
			output += '</tr>'
			i += 1
	output += '</table>'
	return output


bottle.run(debug=True, reloader=True)

