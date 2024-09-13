s1,s2,s3,s4,s5 = map(int,input('Enter 5 subject marks : ').split())
total_subject_marks = int(input('Total Subject Marks : '))
total_marks =  s1 + s2 + s3 + s4 + s5
average_marks = total_marks // 5
percentage_of_marks = total_marks / total_subject_marks  * 100
print('Total Marks : ', total_marks)
print('Average Marks : ',average_marks)
print('Percentage of Marks : ',percentage_of_marks)