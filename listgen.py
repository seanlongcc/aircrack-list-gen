import itertools

output = open("Lab4WordList.txt", "w")

def gmuMason():
	num_list = ['20']
	num_list2 = ['21']
	gmu = ['GMU', 'GMu', 'GmU', 'Gmu', 'gMU', 'gMu', 'gmU', 'gmu']
	cyse = ['CYSE', 'CYSe', 'CYsE', 'CYse', 'CySE', 'CySe', 'CysE', 'Cyse', 'cYSE', 'cYSe', 'cYsE', 'cYse', 'cySE', 'cySe', 'cysE', 'cyse']
	mason = ['MASON', 'MASOn', 'MASoN', 'MASon', 'MAsON', 'MAsOn', 'MAsoN', 'MAson', 'MaSON', 'MaSOn', 'MaSoN', 'MaSon', 'MasON', 'MasOn', 'MasoN', 
			'Mason', 'mASON', 'mASOn', 'mASoN', 'mASon', 'mAsON', 'mAsOn', 'mAsoN', 'mAson', 'maSON', 'maSOn', 'maSoN', 'maSon', 'masON', 'masOn', 'masoN', 'mason']

	for n in range(len(num_list)): #loop for numbers
		for m in range(len(num_list2)):
			for a in range(len(gmu)): #loop for gmu
				for c in range(len(mason)): #loop for cyse
					for d in itertools.permutations([num_list[n], num_list2[m], gmu[a], mason[c]], 4):
						output.write("".join(d)+"\n")
def gmuCyse():
	num_list = ['20']
	num_list2 = ['21']
	gmu = ['GMU', 'GMu', 'GmU', 'Gmu', 'gMU', 'gMu', 'gmU', 'gmu']
	cyse = ['CYSE', 'CYSe', 'CYsE', 'CYse', 'CySE', 'CySe', 'CysE', 'Cyse', 'cYSE', 'cYSe', 'cYsE', 'cYse', 'cySE', 'cySe', 'cysE', 'cyse']
	mason = ['MASON', 'MASOn', 'MASoN', 'MASon', 'MAsON', 'MAsOn', 'MAsoN', 'MAson', 'MaSON', 'MaSOn', 'MaSoN', 'MaSon', 'MasON', 'MasOn', 'MasoN', 
			'Mason', 'mASON', 'mASOn', 'mASoN', 'mASon', 'mAsON', 'mAsOn', 'mAsoN', 'mAson', 'maSON', 'maSOn', 'maSoN', 'maSon', 'masON', 'masOn', 'masoN', 'mason']

	for n in range(0,1): #loop for numbers
		for m in range(len(num_list2)):
			for a in range(len(gmu)): #loop for gmu
				for b in range(len(cyse)): #loop for cyse
					for d in itertools.permutations([num_list[n], num_list2[m], gmu[a], cyse[b]], 4):
						output.write("".join(d)+"\n")
def masonCyse():
	num_list = ['20']
	num_list2 = ['21']
	gmu = ['GMU', 'GMu', 'GmU', 'Gmu', 'gMU', 'gMu', 'gmU', 'gmu']
	cyse = ['CYSE', 'CYSe', 'CYsE', 'CYse', 'CySE', 'CySe', 'CysE', 'Cyse', 'cYSE', 'cYSe', 'cYsE', 'cYse', 'cySE', 'cySe', 'cysE', 'cyse']
	mason = ['MASON', 'MASOn', 'MASoN', 'MASon', 'MAsON', 'MAsOn', 'MAsoN', 'MAson', 'MaSON', 'MaSOn', 'MaSoN', 'MaSon', 'MasON', 'MasOn', 'MasoN', 
			'Mason', 'mASON', 'mASOn', 'mASoN', 'mASon', 'mAsON', 'mAsOn', 'mAsoN', 'mAson', 'maSON', 'maSOn', 'maSoN', 'maSon', 'masON', 'masOn', 'masoN', 'mason']

	for n in range(0,1): #loop for numbers
		for m in range(len(num_list2)):
			for b in range(len(cyse)): #loop for cyse
				for c in range(len(mason)): #loop for mason
					for d in itertools.permutations([num_list[n], num_list2[m], cyse[b], mason[c]], 4):
						output.write("".join(d)+"\n")	

def main():
	gmuMason()
	gmuCyse()
	masonCyse()
	print("Wordlist Generated")
	output.close();

if __name__ == "__main__":
	main()