
#	Visual Computing Project#1
#	20113337 Choi Young_keun
#	Iris Classify
#
#

def cal_covariance(Iris):
	

def cal_mean(Iris):

	sepal_length = 0
	sepal_width = 0
	petal_length = 0
	petal_width = 0

	Iris_mean = []

	for i in range(0, len(Iris)):
		if i%4 == 0:
			sepal_length = sepal_length + Iris[i]
		elif i%4 == 1:
			sepal_width = sepal_width + Iris[i]
		elif i%4 == 2:
			petal_length = petal_length + Iris[i]
		elif i%4 == 3:
			petal_width = petal_width + Iris[i]

	sepal_length = sepal_length/(len(Iris)/4) 
	sepal_width = sepal_width/(len(Iris)/4)
	petal_length = petal_length/(len(Iris)/4)
	petal_width = petal_width/(len(Iris)/4)

	Iris_mean.append(sepal_length)
	Iris_mean.append(sepal_width)
	Iris_mean.append(petal_length)
	Iris_mean.append(petal_width)

	print(sepal_length, sepal_width, petal_length, petal_width)

	return Iris_mean

if __name__ == "__main__":
	File = open("Iris_train.dat.txt",'r')
	lines = File.readlines()
	features = []
	#variable of Iris Info 
	setosa = []
	versicolor = []
	virginica = []

	setosa_features = []
	versicolor_features = []
	virginica_features = []

	for line in lines:
		word = line.split(" ")
		features.append(word)

	#print(features[0][4])
	#print(len(features))

	File.close()

	for i in range(0, len(features)) : 
		if features[i][4] == "1" or features[i][4] == "1\n":
			for j in range(0, 4) :
				setosa.append(float(features[i][j]))
		elif features[i][4] == "2" or features[i][4] == "2\n":
			for j in range(0, 4) :
				versicolor.append(float(features[i][j]))
		elif features[i][4] == "3" or features[i][4] == "3\n":
			for j in range(0, 4) :
				virginica.append(float(features[i][j]))

	setosa_features = cal_mean(setosa)
	versicolor_features = cal_mean(versicolor)
	virginica_features = cal_mean(virginica)

#def cal_covariance(Iris):

