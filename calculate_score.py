from sys import argv

#script, inputf1, inputf2, outputf1 = argv
script, inputf1, inputf2 = argv

file1 = open(inputf1, "r")	#output/predicted file
file2 = open(inputf2, "r")	#labelled/real file
#file3 = open(outputf1, "w") #results

pred_results = []
line1 = file1.readline()
while line1:
	pred_results.append(line1.strip())
	line1 = file1.readline()

real_results = []
line2 = file2.readline()
while line2:
	line2 = line2.strip()
	r_class = line2.split(" ")
	real_results.append(r_class[0])
	line2 = file2.readline()

no_correctly_classified_positive = 0
no_correctly_classified_negative = 0
no_belong_positive = 0
no_belong_negative = 0
no_classified_positive = 0
no_classified_negative = 0

#print(pred_results)

for i in range(0, len(pred_results)):
	if(pred_results[i] == "POSITIVE"):
		no_classified_positive += 1
		if(pred_results[i] == real_results[i]):
			no_correctly_classified_positive += 1

	if(pred_results[i] == "NEGATIVE"):
		no_classified_negative += 1
		if(pred_results[i] == real_results[i]):
			no_correctly_classified_negative += 1

	if(real_results[i] == "POSITIVE"):
		no_belong_positive += 1

	if(real_results[i] == "NEGATIVE"):
		no_belong_negative += 1

precision_positive = no_correctly_classified_positive/ no_classified_positive
recall_positive = no_correctly_classified_positive/ no_belong_positive
f1score_positive = (2 * precision_positive * recall_positive)/ (precision_positive + recall_positive)

precision_negative = no_correctly_classified_negative/ no_classified_negative
recall_negative = no_correctly_classified_negative/ no_belong_negative
f1score_negative = (2 * precision_negative * recall_negative)/ (precision_negative + recall_negative)

print("no_correctly_classified_positive = " +str(no_correctly_classified_positive))
print("no_classified_positive = " +str(no_classified_positive))
print("no_belong_positive = " +str(no_belong_positive))

print("no_correctly_classified_negative = " +str(no_correctly_classified_negative))
print("no_classified_negative = " +str(no_classified_negative))
print("no_belong_negative = " +str(no_belong_negative))

print("precision_positive = " +str(precision_positive))
print("recall_positive = " +str(recall_positive))
print("f1score_positive = " +str(f1score_positive))

print("precision_negative = " +str(precision_negative))
print("recall_negative = " +str(recall_negative))
print("f1score_negative = " +str(f1score_negative))

print("Finished processing!")



