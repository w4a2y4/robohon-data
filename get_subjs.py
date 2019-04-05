import csv
import numpy as np

FILE_LIST = [
	'Y14.csv', 'Y15.csv'
	# 'Y01.csv', 'Y02.csv', 'Y03.csv', 'Y04.csv', 'Y05.csv', 'Y06.csv', 'Y07.csv',
	# 'Y10.csv', 'Y11.csv', 'Y12.csv'
]

OUTPUT_FILE = 'result/formal.csv'

of = open(OUTPUT_FILE, 'a', newline='')
writer = csv.writer(of)
writer.writerow(['subj','eoc','omission','anticipation','RT','RTCV'])

for FILE_NAME in FILE_LIST:

	INPUT_FILE = 'behavior/' + FILE_NAME
	SUBJECT_ID = FILE_NAME[:3]

	target_num = 0
	nontarget_num = 0
	err_of_commission_cnt = 0	# FAIL to withhold keypress while TARGET 3 presented
	omission_cnt = 0			# FAIL to perform keypress while NONTARGET presented
	anticipation_cnt = 0		# non-target RTs less than 100ms
	nontarget_rt = []

	with open(INPUT_FILE, newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for index, row in enumerate(rows):
			# skip practice session
			if index < 10: continue
			# count err_of_commission & omission
			if row['isTarget'] == 'true' :
				target_num += 1
				if row['correct'] == 'false':
					err_of_commission_cnt += 1
			else:
				nontarget_num += 1 
				if row['correct'] == 'false':
					omission_cnt += 1
			# count anticipation
			if row['rt'] == 'null':
				pass
			else:
				rt = int(row['rt'])
				if row['isTarget'] == 'false':
					if rt < 100: 
						anticipation_cnt += 1
					nontarget_rt.append(rt)


	trial_num = target_num + nontarget_num
	err_of_commission = err_of_commission_cnt / target_num * 100
	omission = omission_cnt / nontarget_num * 100
	anticipation = anticipation_cnt / nontarget_num * 100

	writer.writerow([
		SUBJECT_ID,
		"{0:.3f}".format(err_of_commission),
		"{0:.3f}".format(omission),
		"{0:.3f}".format(anticipation),
		"{0:.3f}".format(np.mean(nontarget_rt)),
		"{0:.3f}".format(np.std(nontarget_rt) / np.mean(nontarget_rt))
	])

of.close()

