from urllib.request import urlretrieve


link = input('Enter Link : ')
Filename = input('Enter File Name : ')

urlretrieve(link , 'img/' + Filename + '.jpg')

