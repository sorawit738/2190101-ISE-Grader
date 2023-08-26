x = str(input())
num_faculty = ['01', '02', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '51', '53', '55', '58']
name_faculty = ['The Sirindhorn Thai Language Institute', 'General Education Center', 'Graduate School', 'Faculty of Engineering', 'Faculty of Arts', 'Faculty of Science', 'Faculty of Political Science', 'Faculty of Architecture', 'Faculty of Commerce and Accountancy', 'Faculty of Education', 'Faculty of Communication Arts', 'Faculty of Economics', 'Faculty of Medicine', 'Faculty of Veterinary Science', 'Faculty of Dentistry', 'Faculty of Pharmaceutical Sciences', 'Faculty of Law', 'Faculty of Fine and Applied Arts', 'Faculty of Nursing', 'Faculty of Allied Health Sciences', 'Faculty of Psychology', 'Faculty of Sports Science', 'School of Agricultural', 'College of Population Studies', 'College of Public Health Sciences', 'Language Institute', 'Sasin Graduate Institute of Business Administration of Chulalongkorn University']

count = 0
if x in (num_faculty or name_faculty):
    count += 1

if count > 0:
  print('OK')
else:
  print('Error')