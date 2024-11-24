import pandas as pd
import re

with open('data/access_log','r') as file:
    logs = file.readlines()

log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>.*?) HTTP/.*" (?P<status>\d+) (?P<size>\d+)'
#print(logs)
#parsear las lineas usando expresiones regulares
log_data = []

for line in logs:
    match = re.match(log_pattern, line)
    if match:
        log_data.append(match.groupdict())

df_log = pd.DataFrame(log_data)

#Convertir columnas numericas y de fecha
df_log['status'] = df_log['status'].astype(int)
df_log['size'] = df_log['size'].astype(int)
df_log['timestamp'] = pd.to_datetime(df_log['timestamp'],format='%d/%b/%Y:%H:%M:%S %z')

#contar codigos de estado
status_code = df_log['status'].value_counts()
#print(status_code)

#contar solicitudes por metodos
print(df_log['method'].value_counts())

#Trafico total
print('Trafico total(bytes):')
print(df_log['size'].sum())

df_log['hour'] = df_log['timestamp'].dt.hour
traffic_by_hour = df_log.groupby('hour')['size'].sum()
print(traffic_by_hour)
#print()