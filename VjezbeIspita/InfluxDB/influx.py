from influxdb import InfluxDBClient

HOST = 'localhost'
PORT = 8086
USER = ''
PASSWORD = ''

DB_NAME = 'mydb'

client =  InfluxDBClient(host=HOST, port=PORT, username=USER, password=PASSWORD, database=DB_NAME)

client.create_database(DB_NAME)
client.switch_database(DB_NAME)

json_body = []

with open("sensor_data.txt", "r") as f:
    for linija in f:
        dio = linija.strip().split(",")
        if len(dio) < 5:
            continue
        kanal1 = float(dio[0])
        kanal2 = float(dio[1])
        kanal3 = float(dio[2])
        vijeme = dio[3]
        sensor_id = dio[4]

        točka = {
        "measurement": "mjerenja_senzora",
        "tags": {"sensorID": sensor_id},
        "time": vrijeme,
        "fields": {"kanal1": kanal1, "kanal2": kanal2, "kanal3": kanal3},
    }
    json_body.append(točka)

    client.write_points(json_body)
    print("Podatci su uspješno upisani u InfluxDB bazu podataka.")
    upit = (
    "SELECT kanal1 FROM mjerenja_senzora WHERE (sensorID = 'Sensor1' AND kanal1 >"
    " 0) OR (sensorID = 'Sensor3' AND kanal1 < 0)"
    )
    rezultat = client.query(upit)
    print("Rezultat upita:")
    for point in rezultat.get_points():
        print(point)
