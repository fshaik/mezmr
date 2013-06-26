import flickrapi
import urllib
import sys

api_key = 'f523daf2713c00c0d82ff776c66655c6'
flickr = flickrapi.FlickrAPI(api_key)


def getten(theme, picnum):
  if (theme == 'Landscape'):
    gid = '364847@N20'

  pool = flickr.groups_pools_getPhotos( api_key=api_key, group_id=gid, page='1', per_page=str(picnum))
  
  photoid = []
  secretid = []
  serverid = []
  farmid = []
  
  for photo in pool.iter('photo'):
    photoid.append(photo.attrib['id']) 
    secretid.append(photo.attrib['secret'])
    serverid.append(photo.attrib['server'])
    farmid.append(photo.attrib['farm'])
  
  photourl = []
  
  for i in range(len(farmid)):
    url = "http://farm%s.staticflickr.com/%s/%s_%s.jpg" % (farmid[i], serverid[i], photoid[i], secretid[i])
    save(url, 'Landscape', i)

def save(link, theme, num):
  #Save in folder
  image = urllib.urlretrieve(str(link), "images/" + str(num) + ".jpg")


def main(picload):
  getten('Landscape',picload)
  
if __name__ == '__main__':
  
  main(sys.argv[1])
