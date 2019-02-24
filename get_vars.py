import csv

# FILE_NAME = 'Y-03_SART_201902131053.csv'
FILE_NAME = 'Y-04_SART_201902211715.csv'

INPUT_FILE = 'behavior/' + FILE_NAME
OUTPUT_FILE = 'result/pilot.csv'
SUBJECT_ID = FILE_NAME.split('_')[0]

target_num = 0
nontarget_num = 0
err_of_commission_cnt = 0	# FAIL to withhold keypress while TARGET 3 presented
omission_cnt = 0			# FAIL to perform keypress while NONTARGET presented
anticipation_cnt = 0		# non-target RTs less than 100ms
nontarget_rt_cnt = 0
nontarget_rt_sum = 0

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
				if rt < 100: anticipation_cnt += 1
				nontarget_rt_cnt += 1
				nontarget_rt_sum += rt

trial_num = target_num + nontarget_num
err_of_commission = err_of_commission_cnt / target_num * 100
omission = omission_cnt / nontarget_num * 100
anticipation = anticipation_cnt / nontarget_num * 100
nontarget_rt_mean = nontarget_rt_sum / nontarget_rt_cnt

with open(OUTPUT_FILE, 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	# writer.writerow(['subj','trial_num','target_num','nontarget_num','err_of_commission','omission','anticipation','nontarget_rt_mean'])
	writer.writerow([
		SUBJECT_ID, trial_num, target_num, nontarget_num,
		"{0:.3f}".format(err_of_commission),
		"{0:.3f}".format(omission),
		"{0:.3f}".format(anticipation),
		"{0:.3f}".format(nontarget_rt_mean)
	])



