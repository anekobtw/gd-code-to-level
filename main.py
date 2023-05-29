import asyncio
import csv
import gd

client = gd.Client()
editor = gd.api.Editor()
level = asyncio.run(client.get_level(91110088))

username = input('Enter your GD username: ')
password = input('Enter your account password: ')
asyncio.run(client.login(user=username, password=password))

with open(input('Enter file name: '), 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    for row in reader:
        obj = gd.api.Object(id=int(row[0]))
        obj.set_pos(x=int(row[1]), y=int(row[2]))
        editor.add_objects(obj)

level.data = editor.dump()
asyncio.run(level.upload(name=input('Enter level name: '), id=0, version=1, copyable=True))
