import wsyspath
from openload import OpenLoadResolver as Resolver
resolver=Resolver()
media_id='https://openload.co/f/EVpN8vjIKhI'
host='openload'
print resolver.get_media_url( host,'EVpN8vjIKhI')
