import csv
import numpy as np

# FILE_LIST = [
# 	'Y01.csv', 'Y02.csv', 'Y03.csv', 'Y04.csv', 'Y05.csv',
# 	'Y06.csv', 'Y07.csv', 'Y08.csv', 'Y09.csv', 'Y10.csv',
# 	'Y11.csv', 'Y12.csv', 'Y13.csv', 'Y14.csv', 'Y15.csv',
# 	'Y16.csv', 'Y17.csv', 'Y18.csv', 'Y19.csv', 'Y20.csv',
# 	'Y21.csv', 'Y22.csv', 'Y23.csv'
# ]

FILE_LIST = [
	'O02.csv', 'O03.csv', 'O04.csv', 'O05.csv',
	'O06.csv', 'O07.csv', 'O08.csv', 'O09.csv', 'O10.csv',
	'O11.csv', 'O12.csv', 'O13.csv'
]

OUTPUT_FILE = 'result/formal.csv'

of = open(OUTPUT_FILE, 'a', newline='')
writer = csv.writer(of)
writer.writerow(['subj','eoc','omission','anticipation','RT','RTCV', 'focus', 'distracted', 'mw', 'self_perform'])

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


	PROBE_FILE = 'questionaire/' + FILE_NAME

	probe_cnt = 0
	focus = 0
	mw = 0
	distracted = 0
	self_perform = 0

	with open(PROBE_FILE, newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for index, row in enumerate(rows):
			if index % 2 == 0:
				probe_cnt += 1
				probe1 = row['responses'][0]
				if probe1 == '1': focus +=1
				elif probe1 == '2': distracted += 1
				else: mw += 1
			else:
				probe2 = row['responses'][0]
				self_perform += int(probe2) + 1


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
		"{0:.3f}".format(np.std(nontarget_rt) / np.mean(nontarget_rt)),
		"{0:.3f}".format(focus / probe_cnt),
		"{0:.3f}".format(distracted / probe_cnt),
		"{0:.3f}".format(mw / probe_cnt),
		"{0:.3f}".format(self_perform / probe_cnt)
	])

of.close()

