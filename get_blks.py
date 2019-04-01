import csv
import numpy as np

FILE_LIST = [
	'Y01.csv', 'Y02.csv', 'Y03.csv', 'Y04.csv', 'Y05.csv', 'Y06.csv', 'Y07.csv',
	'Y10.csv', 'Y11.csv', 'Y12.csv'
]

of = open('result/blocks.csv', 'a', newline='')
writer = csv.writer(of)
writer.writerow(['subj','block','eoc','omission','anticipation','RT','RTCV'])

for FILE_NAME in FILE_LIST:

	INPUT_FILE = 'behavior/' + FILE_NAME
	SUBJECT_ID = FILE_NAME[:3]

	block = 1
	block_eoc = 0	# FAIL to withhold keypress while TARGET 3 presented
	block_oms = 0			# FAIL to perform keypress while NONTARGET presented
	block_anti = 0		# non-target RTs less than 100ms
	block_rt = []

	with open(INPUT_FILE, newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for index, row in enumerate(rows):
			# skip practice session
			if index < 10: continue
			# count err_of_commission & omission
			if row['isTarget'] == 'true' :
				if row['correct'] == 'false':
					block_eoc += 1
			else:
				if row['correct'] == 'false':
					block_oms += 1
			# count anticipation
			if row['rt'] == 'null':
				pass
			else:
				rt = int(row['rt'])
				if row['isTarget'] == 'false':
					if rt < 100: 
						block_anti += 1
					block_rt.append(rt)

			# a block
			if (index-9) % 20 == 0:
				writer.writerow([
					SUBJECT_ID,block,block_eoc,block_oms,block_anti,
					"{0:.3f}".format(np.mean(block_rt)),
					"{0:.3f}".format(np.std(block_rt) / np.mean(block_rt)),
				])
				block += 1
				block_eoc = 0	# FAIL to withhold keypress while TARGET 3 presented
				block_oms = 0			# FAIL to perform keypress while NONTARGET presented
				block_anti = 0		# non-target RTs less than 100ms
				block_rt = []
