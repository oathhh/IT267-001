from documentary import Documentaray
m = Documentaray()
m._add_movie('My Octoput Teacher',2020,'Documentary')
m.add_channel('NetFliex')
m._get_movie()

print(f'Title:{m._title}')