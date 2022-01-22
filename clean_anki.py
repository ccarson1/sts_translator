f = open('data_sets/rus.txt', encoding = 'utf-8', mode = 'r')
new = open('data_sets/rus-eng.txt', encoding = 'utf-8', mode = 'a')

to_clean = f.read()

to_clean = to_clean.split("\n")

print(to_clean[0])
finish_clean = []
counter = 0



for x in to_clean:
	y = x.split("\t")
	try:
		new.write(y[0] + " " + y[1] + "\n")
	except OSError:
		print("could not write file")
	counter = counter + 1


	if counter == 10:
		
		print(finish_clean)
		exit()
