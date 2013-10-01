#! /usr/bin/python

import gdata.photos.service
import gdata.media
import gdata.geo
import urllib2
import os

class PicassoAlbumDownloader:
    
    def __init__(self,name,password,downloadfolder):
        self.username=name
        self.pwd=password
        self.dir=downloadfolder
        # self.gd_client=None
        # self.albums =None

    def login(self):
        self.gd_client = gdata.photos.service.PhotosService()
        self.gd_client.email =  self.username+"@gmail.com"
        print(self.gd_client.email)
        self.gd_client.password = self.pwd
        self.gd_client.source = 'exampleCo-exampleApp-1'
        self.gd_client.ProgrammaticLogin()

        self.albums = self.gd_client.GetUserFeed(user=self.username)
        for album in self.albums.entry: 
            print 'Album Name: %s, number of photos: %s, Ablum Id: %s' % (album.title.text,album.numphotos.text, album.gphoto_id.text)

    def downloadAlbum(self,albumid):
        photos = self.gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (self.username, albumid))                 
        for photo in photos.entry:
            print 'Photo title:', photo.content.src
            self.downloadFile(photo.content.src)

    def downloadFile(self,url):
        filename= url.split('/')[-1]
        print 'downloading file :', filename
        pic = urllib2.urlopen(url).read()
        #completeName = os.path.abspath(self.dir+filename)
        completeName=os.path.expanduser(self.dir+filename)
        #completeName = os.path.abspath(self.dir+filename)
        print completeName
        file=open(completeName,'w')  
        file.write(pic)
        file.close()
        print 'saving file :', filename


username = raw_input('Enter your username : ')
pwd = raw_input('Enter your password : ')
downloadpath = raw_input('Enter download folder: ')
t = PicassoAlbumDownloader(username,pwd,downloadpath)
t.login()
albumid = raw_input('Enter ablum id you want to download from above: ')
t.downloadAlbum(albumid)
print 'Download complete'


