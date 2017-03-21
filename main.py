
#	Visual Computing Project#1
#	20113337 Choi Young_keun
#	Iris Classify
#
#
import numpy
import numpy as np
import math

def calCovariance(Iris, mean):
	sepal_length = 0
	sepal_width = 0
	petal_length = 0
	petal_width = 0

	IrisCovarianceMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

	# covariance of sepal_length
	for i in range(0, len(Iris)):
		if i%4 == 0:
			sepal_length = sepal_length + ((Iris[i] - mean[0])*(Iris[i] - mean[0]))
		elif i%4 == 1:
			sepal_width = sepal_width + ((Iris[i-1] - mean[0])*(Iris[i] - mean[1]))
		elif i%4 == 2:
			petal_length = petal_length + ((Iris[i-2] - mean[0])*(Iris[i] - mean[2]))
		elif i%4 == 3:
			petal_width = petal_width + ((Iris[i-3] - mean[0])*(Iris[i] - mean[3]))

	sepal_length = sepal_length/((len(Iris)/4)-1)
	sepal_width = sepal_width/((len(Iris)/4)-1)
	petal_length = petal_length/((len(Iris)/4)-1)
	petal_width = petal_width/((len(Iris)/4)-1)

	IrisCovarianceMatrix[0][0] = sepal_length
	IrisCovarianceMatrix[0][1] = sepal_width
	IrisCovarianceMatrix[0][2] = petal_length
	IrisCovarianceMatrix[0][3] = petal_width

	sepal_length = 0
	sepal_width = 0
	petal_length = 0
	petal_width = 0

	# covariance of sepal_width
	for i in range(0, len(Iris)):
		if i%4 == 0:
			sepal_length = sepal_length + ((Iris[i+1] - mean[1])*(Iris[i] - mean[0]))
		elif i%4 == 1:
			sepal_width = sepal_width + ((Iris[i] - mean[1])*(Iris[i] - mean[1]))
		elif i%4 == 2:
			petal_length = petal_length + ((Iris[i-1] - mean[1])*(Iris[i] - mean[2]))
		elif i%4 == 3:
			petal_width = petal_width + ((Iris[i-2] - mean[1])*(Iris[i] - mean[3]))

	sepal_length = sepal_length/((len(Iris)/4)-1)
	sepal_width = sepal_width/((len(Iris)/4)-1)
	petal_length = petal_length/((len(Iris)/4)-1)
	petal_width = petal_width/((len(Iris)/4)-1)

	IrisCovarianceMatrix[1][0] = sepal_length
	IrisCovarianceMatrix[1][1] = sepal_width
	IrisCovarianceMatrix[1][2] = petal_length
	IrisCovarianceMatrix[1][3] = petal_width

	sepal_length = 0
	sepal_width = 0
	petal_length = 0
	petal_width = 0
	
	# covariance of petal_length
	for i in range(0, len(Iris)):
		if i%4 == 0:
			sepal_length = sepal_length + ((Iris[i+2] - mean[2])*(Iris[i] - mean[0]))
		elif i%4 == 1:
			sepal_width = sepal_width + ((Iris[i+1] - mean[2])*(Iris[i] - mean[1]))
		elif i%4 == 2:
			petal_length = petal_length + ((Iris[i] - mean[2])*(Iris[i] - mean[2]))
		elif i%4 == 3:
			petal_width = petal_width + ((Iris[i-1] - mean[2])*(Iris[i] - mean[3]))

	sepal_length = sepal_length/((len(Iris)/4)-1)
	sepal_width = sepal_width/((len(Iris)/4)-1)
	petal_length = petal_length/((len(Iris)/4)-1)
	petal_width = petal_width/((len(Iris)/4)-1)

	IrisCovarianceMatrix[2][0] = sepal_length
	IrisCovarianceMatrix[2][1] = sepal_width
	IrisCovarianceMatrix[2][2] = petal_length
	IrisCovarianceMatrix[2][3] = petal_width

	sepal_length = 0
	sepal_width = 0
	petal_length = 0
	petal_width = 0
	
	# covariance of petal_width
	for i in range(0, len(Iris)):
		if i%4 == 0:
			sepal_length = sepal_length + ((Iris[i+3] - mean[3])*(Iris[i] - mean[0]))
		elif i%4 == 1:
			sepal_width = sepal_width + ((Iris[i+2] - mean[3])*(Iris[i] - mean[1]))
		elif i%4 == 2:
			petal_length = petal_length + ((Iris[i+1] - mean[3])*(Iris[i] - mean[2]))
		elif i%4 == 3:
			petal_width = petal_width + ((Iris[i] - mean[3])*(Iris[i] - mean[3]))

	sepal_length = sepal_length/((len(Iris)/4)-1)
	sepal_width = sepal_width/((len(Iris)/4)-1)
	petal_length = petal_length/((len(Iris)/4)-1)
	petal_width = petal_width/((len(Iris)/4)-1)

	IrisCovarianceMatrix[3][0] = sepal_length
	IrisCovarianceMatrix[3][1] = sepal_width
	IrisCovarianceMatrix[3][2] = petal_length
	IrisCovarianceMatrix[3][3] = petal_width

	IrisCovarianceMatrix = np.array(IrisCovarianceMatrix)

	print(IrisCovarianceMatrix)
	print ""

	return IrisCovarianceMatrix


def cal_mean(Iris):

	sepal_length_mean = 0
	sepal_width_mean = 0
	petal_length_mean = 0
	petal_width_mean = 0

	Iris_mean = [0, 0, 0, 0]

	for i in range(0, len(Iris)):
		if i%4 == 0:
			sepal_length_mean = sepal_length_mean + Iris[i]
		elif i%4 == 1:
			sepal_width_mean = sepal_width_mean + Iris[i]
		elif i%4 == 2:
			petal_length_mean = petal_length_mean + Iris[i]
		elif i%4 == 3:
			petal_width_mean = petal_width_mean + Iris[i]

	sepal_length_mean = sepal_length_mean/(len(Iris)/4) 
	sepal_width_mean = sepal_width_mean/(len(Iris)/4)
	petal_length_mean = petal_length_mean/(len(Iris)/4)
	petal_width_mean = petal_width_mean/(len(Iris)/4)

	Iris_mean[0] = sepal_length_mean
	Iris_mean[1] = sepal_width_mean
	Iris_mean[2] = petal_length_mean
	Iris_mean[3] = petal_width_mean

	Iris_mean = np.array(Iris_mean)

	print(Iris_mean)
	print ""

	return Iris_mean

#------calculate for discriminant function 
def discriminantFunctions(IrisTestData, meanMatrix, covarianceMatrix, vi0):
	
	cal1 = np.dot(np.dot(np.transpose(IrisTestData), -0.5*np.linalg.inv(covarianceMatrix)), IrisTestData)
	cal2 = np.dot(np.transpose(np.dot(np.linalg.inv(covarianceMatrix), meanMatrix)), IrisTestData)

	result = cal1 + cal2 + vi0
	return result

#------calculate for vi0 of discriminant function
def calVi0(meanMatrix, covarianceMatrix):

	vi0 = -0.5*np.dot(np.dot(np.transpose(meanMatrix), np.linalg.inv(covarianceMatrix)), meanMatrix) - 0.5*np.log2(numpy.linalg.det(covarianceMatrix))
	#print(vi0)

	return vi0

#-------read file, init variables, calculate confusion matrix
if __name__ == "__main__":
	File = open("Iris_train.dat.txt",'r')
	lines = File.readlines()
	features = []
	
	#variable of Iris Info 
	setosa = []
	versicolor = []
	virginica = []

	#mean of Iris Info
	setosaMeanVector = []
	versicolorMeanVector = []
	virginicaMeanVector = []

	#covariance matrix of Iris Info
	setosaCovarianceMatrix = []
	versicolorCovarianceMatrix = []
	virginicaCovarianceMatrix = []


	for line in lines:
		word = line.split(" ")
		features.append(word)

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

	print("----setosa Mean----")
	setosaMeanVector = cal_mean(setosa)
	print("----versicolor Mean----")
	versicolorMeanVector = cal_mean(versicolor)
	print("----virginica Mean----")
	virginicaMeanVector = cal_mean(virginica)

	print("----setosa Covariance Matrix----")
	setosaCovarianceMatrix = calCovariance(setosa, setosaMeanVector)
	print("----versicolor Covariance Matrix----")
	versicolorCovarianceMatrix = calCovariance(versicolor, setosaMeanVector)
	print("----virginica Covariance Matrix----")
	virginicaCovarianceMatrix = calCovariance(virginica, virginicaMeanVector)

	#--------------------Iris_test.dat.txt read------------------
	File = open("Iris_test.dat.txt",'r')
	lines = File.readlines()

	#each value of test data set
	setosaTestData = np.zeros((10,4))
	versicolorTestData = np.zeros((10,4))
	virginicaTestData = np.zeros((10,4))
	
	featuresTestData = []
	
	confusionMatrix = np.zeros((3,3))

	for line in lines:
		word = line.split(" ")
		featuresTestData.append(word)

	File.close()

	#save 
	for i in range(0, len(featuresTestData)) : 
		if featuresTestData[i][4] == "1" or featuresTestData[i][4] == "1\r\n":
			for j in range(0, 4) :
				setosaTestData[i][j] = (float(featuresTestData[i][j]))
		elif featuresTestData[i][4] == "2" or featuresTestData[i][4] == "2\r\n":
			for j in range(0, 4) :
				versicolorTestData[i-10][j] = (float(featuresTestData[i][j]))
		elif featuresTestData[i][4] == "3" or featuresTestData[i][4] == "3\r\n":
			for j in range(0, 4) :
				virginicaTestData[i-20][j] = (float(featuresTestData[i][j]))

	#calculate vi0
	setosaVi0 = calVi0(setosaMeanVector, setosaCovarianceMatrix)
	versicolorVi0 = calVi0(versicolorMeanVector, versicolorCovarianceMatrix)
	virginicaVi0 = calVi0(virginicaMeanVector, virginicaCovarianceMatrix)

	#calculate confusion matrix
	for i in range(0, len(setosaTestData)):
		gx1 = discriminantFunctions(setosaTestData[0], setosaMeanVector, setosaCovarianceMatrix, setosaVi0)
		gx2 = discriminantFunctions(setosaTestData[0], versicolorMeanVector, versicolorCovarianceMatrix, versicolorVi0)
		gx3 = discriminantFunctions(setosaTestData[0], virginicaMeanVector, virginicaCovarianceMatrix, virginicaVi0)
		
		if max([gx1, gx2, gx3]) == gx1:
			confusionMatrix[0][0] += 1
		elif max([gx1, gx2, gx3]) == gx2:
			confusionMatrix[0][1] += 1
		elif max([gx1, gx2, gx3]) == gx3:
			confusionMatrix[0][2] += 1

	for i in range(0, len(versicolorTestData)):
		gx1 = discriminantFunctions(versicolorTestData[0], setosaMeanVector, setosaCovarianceMatrix, setosaVi0)
		gx2 = discriminantFunctions(versicolorTestData[0], versicolorMeanVector, versicolorCovarianceMatrix, versicolorVi0)
		gx3 = discriminantFunctions(versicolorTestData[0], virginicaMeanVector, virginicaCovarianceMatrix, virginicaVi0)
		
		if max([gx1, gx2, gx3]) == gx1:
			confusionMatrix[1][0] += 1
		elif max([gx1, gx2, gx3]) == gx2:
			confusionMatrix[1][1] += 1
		elif max([gx1, gx2, gx3]) == gx3:
			confusionMatrix[1][2] += 1

	for i in range(0, len(virginicaTestData)):
		gx1 = discriminantFunctions(virginicaTestData[0], setosaMeanVector, setosaCovarianceMatrix, setosaVi0)
		gx2 = discriminantFunctions(virginicaTestData[0], versicolorMeanVector, versicolorCovarianceMatrix, versicolorVi0)
		gx3 = discriminantFunctions(virginicaTestData[0], virginicaMeanVector, virginicaCovarianceMatrix, virginicaVi0)
		
		if max([gx1, gx2, gx3]) == gx1:
			confusionMatrix[2][0] += 1
		elif max([gx1, gx2, gx3]) == gx2:
			confusionMatrix[2][1] += 1
		elif max([gx1, gx2, gx3]) == gx3:
			confusionMatrix[2][2] += 1

	print("----confusion Matrix----")
	print(confusionMatrix)



