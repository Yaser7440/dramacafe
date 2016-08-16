parts=''' 116,"origin":"gcs","url":"https://s.vimeocdn.com/vimeo-prod-skyfire-std-us
/01/2182/5/135911377/402464149.mp4?token=55d5e36a_0xd0864983b3114adf77df3004b777
212aebe0f840","cdn":"fastly","height":202,"width":480,"id":402464149,"bitrate":4
00,"availability":112},"hd":{'''
url=parts.split(",")[2].replace('"url":','').replace('"','')
quality='low'
print url
