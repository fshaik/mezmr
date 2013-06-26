#!/bin/bash


#run get ten

#start slideshow
##launch fbi for pic 1
##launch fbi
###lanch fbi
#runget during slideshow
interval=2
picload=5
echo "Downloading $picload pictures please wait"

#python flickr.py $picload 

for((i = 0; i< $picload; i++)) 
do
  fbi images/$i.jpg
  sleep $interval
  echo '6' > /proc/pid/fd/0

  #if[ i >= picload/2]
  #then
    # launch subshell and download 4 more
  #fi

done

