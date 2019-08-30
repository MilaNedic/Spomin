import bottle
import model
import ast
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
	#spomin = model.Memory(tezavnost)
	#plosca = spomin.plosca
	bottle.redirect('/skrita?tezavnost=' + str(tezavnost) + '&kliknjena=')		# v get tabelo shranimo izbrano težavnost


@bottle.get('/skrita')  #želimo, da nam pokaže skrito ploščo
def pokazi_skrito_plosco():

	#get ='/skrita?tezavnost=' + str(tezavnost) + '&kliknjena='
	#get = request.query[]
	#<td> <a href = "/skrita?tezavnost=' + str(tezavnost) + '&kliknjena=[' + str(i) + ',' + str(j) + ']">' 

	tezavnost = int(request.query['tezavnost'])		#iz get tabele preberemo težavnost
	spomin = model.Memory(tezavnost)
	skrita_plosca = spomin.skrita
	plosca = spomin.plosca
	id_igre = spomin.id_igre 

	output_1 = '<style> table { border-collapse: collapse; }'
	output_1 += 'table, td, th { border: 1px solid black; }'
	output_1 += 'td { width: 30; }'
	output_1 += 'td { align: center; }</style>'
	output_1 += '<h1>Spomin</h1> <table>'		# generiramo html tabelo na podlagi težavnosti
	output_2 = '<h1>Izbira polj</h1> <table>'   #generiramo tabelo za ugibanje polje, mesta v tej tabeli sovpadajo s polji v tabeli za skrto ploco

	if tezavnost in [2, 3, 4]:

		niz = request.query['kliknjena']
		originalNiz = request.query_string

		polja = niz.count('[') #prestejemo st [, da dobimo stevilo polj, ki smo jih ugibali
		niz = niz.rstrip(',')
		#niz = niz.split(',')


		if niz != '':
			if polja == tezavnost:
				niz = ast.literal_eval(niz)
				for element in niz:
					element =  [ int(x) for x in element]
				if spomin.ugibaj(niz) == 1:
					output_1 += 'uganu si'
				else:
					output_1 += 'zajebu si'
				originalNiz = 'tezavnost=' + str(tezavnost) + '&kliknjena='     # spraznimo original niz get tabe


		i = 0
		while i < 4:
			j = 0
			output_1 += '<tr>'
			output_2 += '<tr>'
			while j < 6:
				output_1 += '<td> <a href = /skrita?' + originalNiz + '[' + str(i) + ',' + str(j) + '],>'
				output_2 += '<td>' 
				output_1 += plosca[i][j] 	
				output_2 += '<input type="button" value=' + str(i) + ',' + str(j) + '>'		#tukaj želimo gumbek za izbiro polja, želimo, da sta i,j pripadajoča indeksa skrite plošče, torej predstavljata
				output_1 += '</td>'									#polje, ki ga želimo izbrati
				output_2 += '</td>'									#inpu type=raido, to je krozec za označevanje, pusti samo eno možnost, mi pa rabimo izbrati toliko polj, kot je težavnost
				j += 1
			output_1 += '</tr>'
			output_2 += '</tr>'
			i += 1
	output_1 += '</table>'
	output_2 += '</table>'
	return output_1, output_2

#@bottle.post('/skrita')
#def ugibaj_polja():
#	pass


bottle.run(debug=True, reloader=True)

