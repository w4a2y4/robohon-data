import csv
import numpy as np

FILE_LIST = [
	'Y01.csv', 'Y02.csv', 'Y03.csv', 'Y04.csv', 'Y05.csv', 'Y06.csv', 'Y07.csv',
	'Y08.csv', 'Y09.csv', 'Y10.csv', 'Y11.csv', 'Y12.csv', 'Y13.csv', 'Y14.csv',
	'Y15.csv', 'Y16.csv', 'Y17.csv', 'Y18.csv', 'Y19.csv', 'Y20.csv', 'Y21.csv', 
	'Y22.csv', 'Y23.csv'
]

of = open('result/trials.csv', 'a', newline='')
writer = csv.writer(of)
writer.writerow(['subj', 'block', 'target', 'correct', 'RT', 'anticipation', 'eoc'])

for FILE_NAME in FILE_LIST:

	INPUT_FILE = 'behavior/' + FILE_NAME
	SUBJECT_ID = FILE_NAME[:3]

	# PROBE_FILE = 'questionaire/' + FILE_NAME
	# pf = open(PROBE_FILE, newline='')
	# pfrows = csv.DictReader(pf)

	block = 1
	block_eoc = 0	# FAIL to withhold keypress while TARGET 3 presented
	probe1 = -1
	probe2 = -1

	block_buf = []

	with open(INPUT_FILE, newline='') as csvfile:
		rows = csv.DictReader(csvfile)
		for index, row in enumerate(rows):

			trial_buf = []
			trial_buf.append( 1 if ( row['isTarget'] == 'true' ) else 0 )
			trial_buf.append( 1 if ( row['correct']  == 'true' ) else 0 )
			trial_buf.append( "null" if ( row['rt'] == 'null' ) else int(row['rt']) )
			trial_buf.append( 0 )

			# skip practice session
			if index < 10: continue


			if row['isTarget'] == 'true' :
				if row['correct'] == 'false':
					block_eoc += 1

			# count anticipation
			if row['rt'] == 'null':
				pass
			else:
				rt = int(row['rt'])
				if row['isTarget'] == 'false':
					if rt < 100: 
						trial_buf[3] = 1

			block_buf.append(trial_buf)

			# a block
			if (index-9) % 20 == 0:

				# if block_eoc > 0 or block_oms > 0:
				# 	probe1 = next(pfrows)['responses'][0]
				# 	probe2 = next(pfrows)['responses'][0]

				for i in range(20):
					writer.writerow([
						SUBJECT_ID, block,
						block_buf[i][0], block_buf[i][1],
						block_buf[i][2], block_buf[i][3],
						block_eoc
					])

				block += 1
				block_eoc = 0	# FAIL to withhold keypress while TARGET 3 presented
				block_buf = []

	# pf.close()
