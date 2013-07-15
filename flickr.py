import flickrapi
import urllib 
import sys
import subprocess
import time

slideshowtimeinsecs = 3

class Downloader:

  def __init__(self):
    self.api_key = 'f523daf2713c00c0d82ff776c66655c6'
    self.flickr = flickrapi.FlickrAPI(self.api_key)
    self.imagefilename = 0

  def getten(self, theme, picnum,resultpagenumber):
    if (theme == 'Landscape'):
      gid = '364847@N20'

    pool = self.flickr.groups_pools_getPhotos( api_key=self.api_key, group_id=gid, page=str(resultpagenumber), per_page=str(picnum))
  
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
      url = "http://farm%s.staticflickr.com/%s/%s_%s_b.jpg" % (farmid[i], serverid[i], photoid[i], secretid[i])
      print url
      self.save(url, 'Landscape', self.imagefilename)
      self.imagefilename+=1

  def save(self, link, theme, num):
    #Save in folder
    image = urllib.urlretrieve(str(link), "images/" + str(num) + ".jpg")


def main( numofpicstoload):
  initial = Downloader()
  resultpagenumber = 1
  
  initial.getten('Landscape',numofpicstoload, resultpagenumber)
  resultpagenumber = 2
  fbihandler = subprocess.Popen('fbi -noverbose -a -t 3 ./images/*.jpg', shell=True)


  while fbihandler.poll() == None: #return code could be negative
    time.sleep(int(numofpicstoload)/2 * slideshowtimeinsecs) #chillout
    print "Downloading More Images"
    initial.getten('Landscape', numofpicstoload, resultpagenumber)
    resultpagenumber += 1
    if resultpagenumber % 3:
      inital.imagefilename = 0


  fbihandler.wait()

 #getten and name them differently
#clean up every three times

  


  #resultpagenumber = resultpagenumber + 1
  #initial.getten('Landscape',picload, resultpagenumber)
    #pause
    #getten for next page
  
if __name__ == '__main__':
  assert(sys.argv[1])

  main(sys.argv[1])
