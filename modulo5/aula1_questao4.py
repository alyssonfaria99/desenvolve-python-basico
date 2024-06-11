import datetime

data = datetime.datetime.now()
dataFormatada = f'Data: {data.day:02}/{data.month:02}/{data.year}\nHora: {data.hour:02}:{data.minute:02}'
print (dataFormatada)
