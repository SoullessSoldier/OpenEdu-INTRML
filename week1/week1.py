import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('math_students.csv', delimiter=',')

# функция .head(n) выводит первые n строк таблицы (по умолчанию n=5)
print(data.head())
#Какая причина выбора школы была самой частой? В качестве ответа приведите соответствующее значение признака.
print(data['reason'].value_counts())
#Найдите количество студентов, у родителей которых нет никакого образования.
print(data[(data['Medu'] == 0) & (data['Fedu'] == 0)].shape)
#Найдите минимальный возраст учащегося школы Mousinho da Silveira
print(data[(data['school'] == 'MS')]['age'].min())
#Найдите количество студентов, имеющих нечетное число пропусков.
print(data[(data['absences']%2 != 0)].shape)
'''
 Найдите разность между средними итоговыми оценками студентов, состоящих и не состоящих в романтических отношениях. 
 В качестве ответа приведите число, округленное до двух значащих цифр после запятой. Ответ вводите с точкой.
'''
print(data[data['romantic']=='yes']['G3'].mean()-data[data['romantic']=='no']['G3'].mean())
'''
Сколько занятий пропустило большинство студентов с самым частым значением наличия внеклассных активностей?
'''
print(data[data['activities']=='yes']['absences'].value_counts())
'''
plt.figure(figsize=(10,7))
plt.title('Absences distribution')
data['activities'].hist()
plt.xlabel('absences')
plt.ylabel('number of students')
plt.show()
'''