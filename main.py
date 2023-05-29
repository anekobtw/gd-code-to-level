import gd
import csv
import asyncio

client = gd.Client()
editor = gd.api.Editor()
level = asyncio.run(client.get_level(91110088))
asyncio.run(client.login(user=input('Enter your GD username: '), password=input('Enter your password: ')))

with open(input('Enter file name: '), 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    for row in reader:
        block_id = int(row[0])
        x_position = int(row[1])
        y_position = int(row[2])
        
        obj = gd.api.Object(id=block_id)
        obj.set_pos(x=x_position, y=y_position)
        editor.add_objects(obj)

level.data = editor.dump()
asyncio.run(level.upload(name=input('Enter level name: '), id=0, version=1, copyable=True))