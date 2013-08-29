### ############################################################################################################
###	#	
### # Project: 			#		teh_tools - by The Highway 2013.
### # Author: 			#		The Highway
### # Version:			#		(ever changing)
### # Description: 	#		My collection of common tools.
###	#	
### ############################################################################################################
### ############################################################################################################
from config 			import *
__plugin__	=	ps('__plugin__')
__authors__	=	ps('__authors__')
plugin_id		=	ps('_addon_id')
### ############################################################################################################
### ############################################################################################################
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
try: import requests ### <import addon="script.module.requests" version="1.1.0"/> ### 
except: t=''				 ### See https://github.com/kennethreitz/requests ### 
import urllib,urllib2,re,os,sys,htmllib,string,StringIO,logging,random,array,time,datetime
try: import urlresolver
except: t=''
import copy
try: import json
except ImportError: import simplejson as json
try: import StorageServer
except: import storageserverdummy as StorageServer
cache = StorageServer.StorageServer(plugin_id)
#import SimpleDownloader as downloader
from t0mm0.common.net import Net as net
from t0mm0.common.addon import Addon
#from config 			import *
### ############################################################################################################
### ############################################################################################################
### ### Common Imports ### 
### ######################
### import shutil, md5, base64, unicodedata, threading, string
### import resources.lib.common as common
### import xbmc, xbmcplugin, xbmcgui, xbmcaddon, xbmcvfs, common
### import os.path, sys, urllib, urllib2, cookielib, string, httplib, socket, random
### import os, re, math, binascii, datetime, HTMLParser
### from BeautifulSoup import BeautifulStoneSoup
### from BeautifulSoup import BeautifulSoup , Tag, NavigableString
### try: from xml.etree import ElementTree
### except: from elementtree import ElementTree
### from xbmcgui import Dialog
### import copy
### requests, httplib, urlparse
### from operator import itemgetter
### from metahandler import metahandlers
### from metahandler import metacontainers
### 
### 
### 
### 
### 
### 
### 
### 
### 
### ############################################################################################################
### ############################################################################################################
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param
### ############################################################################################################
### ############################################################################################################
cache						=	StorageServer.StorageServer(plugin_id)
addon						=	Addon(plugin_id, sys.argv)
local						=	xbmcaddon.Addon(id=plugin_id)
__settings__		=	xbmcaddon.Addon(id=plugin_id)
__home__				=	__settings__.getAddonInfo('path')
addonPath				=	__settings__.getAddonInfo('path')
artPath					=	addonPath+'/art/'	#special://home/addons/plugin.video.theanimehighway/art
if __settings__.getSetting("debug-enable") == "true":debugging=True				#if (debugging==True): 
else: debugging=False
if __settings__.getSetting("debug-show") == "true": shoDebugging=True			#if (showDebugging==True): 
else: shoDebugging=False
_debugging=debugging; _shoDebugging=shoDebugging
params=get_params()
ICON = os.path.join(__home__, 'icon.png')
fanart = os.path.join(__home__, 'fanart.jpg')

_addon=Addon(ps('_addon_id'), sys.argv);
def addst(r,s=''): return _addon.get_setting(r)   ## Get Settings
def addpr(r,s=''): return _addon.queries.get(r,s) ## Get Params
def cFL(t,c=ps('default_cFL_color')): ### For Coloring Text ###
	return '[COLOR '+c+']'+t+'[/COLOR]'
def cFL_(t,c=ps('default_cFL_color')): ### For Coloring Text ###
	return '[COLOR '+c+']'+t[0:1]+'[/COLOR]'+t[1:]
### ############################################################################################################
### ############################################################################################################
url=None; urlbac=None; name=None; name2=None; type2=None; favcmd=None; mode=None; scr=None; imgfan=None; show=None; category=None
try: category=urllib.unquote_plus(params["cat"])
except: pass
if category==None: category='Base'
try:
        url=urllib.unquote_plus(params["url"])
        urlbac=url
except: pass
try: scr=urllib.unquote_plus(params["scr"])
except: pass
try: imgfan=urllib.unquote_plus(params["fan"])
except: pass
try: favcmd=urllib.unquote_plus(params["fav"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: name2=urllib.unquote_plus(params["nm"])
except: pass
try: show=urllib.unquote_plus(params["show"])
except: pass
try: type2=int(params["tp"])
except: pass
try: mode=int(params["mode"])
except: pass
### ############################################################################################################
### ############################################################################################################
ICON8 = os.path.join(artPath, 'icon_watchdub.png');ICON7 = os.path.join(artPath, 'icon_dubhappy.png');ICON6 = os.path.join(artPath, 'iconDAOn2.png');ICON5 = os.path.join(artPath, 'iconA44couk.png');ICON4 = os.path.join(artPath, 'icongd.png');ICON3 = os.path.join(artPath, 'iconAPlus.png');ICON2 = os.path.join(artPath, 'iconA44.png');ICON1 = os.path.join(artPath, 'iconAG.png');ICON0 = os.path.join(__home__, 'icon.png')
fanart8 = os.path.join(artPath, 'fanart_watchdub.jpg');fanart7 = os.path.join(artPath, 'fanart_dubhappy.jpg');fanart6 = os.path.join(artPath, 'fanartDAOn2.jpg');fanart5 = os.path.join(artPath, 'fanartA44couk.jpg');fanart4 = os.path.join(artPath, 'fanartgd.jpg');fanart3 = os.path.join(artPath, 'fanartAPlus.jpg');fanart2 = os.path.join(artPath, 'fanartA44.jpg');fanart1 = os.path.join(artPath, 'fanartAG.jpg');fanart0 = os.path.join(__home__, 'fanart.jpg')
if type2==8:			#site 8
	fanart = os.path.join(artPath, 'fanart_watchdub.jpg');ICON = os.path.join(artPath, 'icon_watchdub.png');mainSite='http://www.watchdub.com/'
elif type2==7:			#site 7
	fanart = os.path.join(artPath, 'fanart_dubhappy.jpg');ICON = os.path.join(artPath, 'icon_dubhappy.png');mainSite='http://www.dubhappy.eu/'
elif type2==6:			#site 6
	fanart = os.path.join(artPath, 'fanartDAOn2.jpg');ICON = os.path.join(artPath, 'iconDAOn2.png');mainSite='http://dubbedanimeon.com/'
elif type2==5:			#site 5
	fanart = os.path.join(artPath, 'fanartA44couk.jpg');ICON = os.path.join(artPath, 'iconA44couk.png');mainSite='http://www.anime44.co.uk/'
	if ('-anime' in url) and ('http://' not in url): url = mainSite + 'subanime/' + url
	if ('-anime' in url) and ('http://' not in scr) and (artPath not in scr): scr = mainSite + 'subanime/' + scr
	if ('-anime' in url) and ('http://' not in imgfan) and (artPath not in imgfan): imgfan = mainSite + 'subanime/' + imgfan
	#if ('-anime' not in url) and ('http://' not in url): url = mainSite + 'english-dubbed/' + url
	#if ('-anime' not in url) and ('http://' not in scr) and (artPath not in scr): scr = mainSite + 'english-dubbed/' + scr
	#if ('-anime' not in url) and ('http://' not in imgfan) and (artPath not in imgfan): imgfan = mainSite + 'english-dubbed/' + imgfan
	#if ('alpha-anime' in url): url.replace('alpha-anime','subanime')
	#if ('alpha-movies' in url): url.replace('alpha-movies','subanime')
	#if ('alpha-anime' in show): show.replace('alpha-anime','subanime')
	#if ('alpha-movies' in show): show.replace('alpha-movies','subanime')
elif type2==4:			#site 4
	fanart = os.path.join(artPath, 'fanartgd.jpg');ICON = os.path.join(artPath, 'icongd.png');mainSite='http://www.gooddrama.net/'
elif type2==3:		#site 3
	fanart = os.path.join(artPath, 'fanartplus.jpg');ICON = os.path.join(artPath, 'iconplus.png');mainSite='http://www.animeplus.tv/'
elif type2==2:		#site 2
	fanart = os.path.join(artPath, 'fanartA44.jpg');ICON = os.path.join(artPath, 'iconA44.png');mainSite='http://www.anime44.com/'
else:							#site 1
	fanart = os.path.join(artPath, 'fanartAG.jpg');ICON = os.path.join(artPath, 'iconAG.png');mainSite='http://www.animeget.com/'
### ############################################################################################################
### ############################################################################################################
SiteBits=['nosite','animeget.com','anime44.com','animeplus.tv','gooddrama.net','anime44.co.uk','dubbedanimeon.com','dubhappy.eu','watchdub.com']
SiteNames=['nosite','[COLOR blue][COLOR white]Anime[/COLOR]Get[/COLOR]','[COLOR red][COLOR white]Anime[/COLOR]44[/COLOR]','[COLOR darkblue][COLOR white]Anime[/COLOR]Plus[/COLOR]','[COLOR grey]Good[COLOR white]Drama[/COLOR][/COLOR]','[COLOR maroon][COLOR white]Anime[/COLOR]Zone[/COLOR]','[COLOR teal]Dubbed[COLOR white]Anime[/COLOR]On [/COLOR]','[COLOR cornflowerblue][COLOR white]dub[/COLOR]happy[/COLOR]','[COLOR cornflowerblue]Watch[/COLOR][COLOR white]Dub[/COLOR]','','']
SitePrefixes=['nosite','','','','','subanime/','','','','','','','','','','','','']
SiteSufixes= ['nosite','','','','','.html','','','','','','','','','','','','','']
SiteSearchUrls= ['nosite','http://www.animeget.com/search','http://www.anime44.com/anime/search?search_submit=Go&key=','http://www.animeplus.tv/anime/search?search_submit=Go&key=','http://www.gooddrama.net/drama/search?stype=drama&search_submit=Go&key=','No Search Engine for VideoZone','http://dubbedanimeon.com/?s=','','','','','','','']
SiteSearchMethod= ['nosite','post','get','get','get','VideoZone','get','','','','','','','']
Sites=['animeget.com','anime44.com','animeplus.tv','gooddrama.net','anime44.co.uk','dubbedanimeon.com','dubhappy.eu','watchdub.com']
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyColors=['red','blue','darkblue','grey','maroon','teal','cornflowerblue','cornflowerblue','','','','']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
### ############################################################################################################
MyVideoLinkSrcMatches=['src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"'			,'src="(.+?)"'		,'src="(.+?)"',		'src="(.+?)"']
MyVideoLinkSrcMatchesB=['src="(.+?)"',			'<embed.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"',			'<iframe.+?src="(.+?)"'			,'src="(.+?)"'		,'src="(.+?)"',		'src="(.+?)"']
MyVideoLinkBrackets=['<iframe.+?src="(.+?)"', '<embed.+?src="(.+?)"', '<object.+?data="(.+?)"']
MyAlphabet=	['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=	['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
MySourcesV=		['videoweed.es',	'video44.net',	'novamov.com',	'dailymotion.com',	'videofun.me',	'yourupload.com',	'video.google.com',	'vidzur.com',	'upload2.com','putlocker.com','videoslasher.com','vidbull.com',		'uploadc.com',	'veevr.com',	'rutube.ru']
#MySourcesV=	['videoweed.es',	'video44.net',	'novamov.com',	'dailymotion.com',	'videofun.me',	'yourupload.com',	'video.google.com',	'vidzur.com',	'upload2.com','putlocker.com','videoslasher.com','vidbull.com',		'UploadC',	'veevr.com',	'rutube.ru',	'MP4UPLOAD'		,'AUENGINE']
MyIconsV=		[artPath + 'videoweed.jpg',	artPath + 'video44a.png',	artPath + 'novamov.jpg',	artPath + 'dailymotion.jpg',	artPath + 'videofun.png',	artPath + 'yourupload.jpg',	artPath + 'googlevideo.gif', artPath + 'vidzur.png', artPath + 'upload2.png', artPath + 'putlocker.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png', artPath + 'BLANK.png']#BLANK.png
MyNamesV=		['VideoWeed',			'Video44',			'NovaMov',			'DailyMotion',			'VideoFun',			'YourUpload',				'Google Video',			'VidZur',			'Upload2',		'PutLocker',		'VideoSlasher',		'VidBull',		'UploadC',	'Veevr',	'RuTube',			'MP4Upload'		,'AUEngine']
MyColorsV=	['lime',					'red',					'silver',				'green',						'cyan',					'grey',					'blue',					'orange',					'white',					'white',					'white',					'white',					'white',					'white', 			'white', 			'white', 			'white', 			'white', 			'white']
### ############################################################################################################
### ############################################################################################################
def getURLr(url,dReferer):
	try:
		req = urllib2.Request(url,dReferer)
		req.add_header(MyBrowser[0], MyBrowser[1]) 
		req.add_header('Referer', dReferer)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
	except:
		return('none')
def getURL(url):
	try:
		req = urllib2.Request(url)
		req.add_header(MyBrowser[0], MyBrowser[1]) 
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
	except:
		return('none')
def postURL(url,postStr):
		postData=urllib.urlencode(postStr)
		req = urllib2.Request(url,postData)
		req.add_header(MyBrowser[0], MyBrowser[1]) 
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
def notification(header="", message="", sleep=5000 ):
	xbmc.executebuiltin( "XBMC.Notification(%s,%s,%i)" % ( header, message, sleep ) )
	#notify(msg=message, title=header, delay=sleep, image=ICON)
	#notify(msg=message, title='[COLOR green][B]'+header+'[/B][/COLOR]', delay=sleep, image=ICON0)

### ############################################################################################################
##Example##VaddDir('[COLOR blue]' + text[0] + '[/COLOR]', '', 0, '', False)
def addFolder(name,name2,url,type2,mode,iconimage,categoryA='Blank'):
		###addDir(name,name2,url,type2,mode,iconimage,fanimage)
		if ('http://' in iconimage) or (artPath in iconimage): t=''
		else: iconimage = artPath + iconimage
		mainSite='http://'+SiteBits[type2]+'/'
		addDir(name,name2,mainSite + url,type2,mode,iconimage,fanart,categoryA)
		#addDirD(name,name2,mainSite + url,type2,mode,artPath + iconimage,fanart,'wow')
### from videolinks.py ###
#def addFolder(name,name2,url,type2,mode,iconimage):
#		##addDir(name,name2,url,type2,mode,iconimage,fanimage)
#		addDir(name,name2,mainSite + url,type2,mode,artPath + iconimage,fanart)
def addDirF(name,name2,url,favcmd,type2=0,mode=0,iconimage=ICON0,fanimage=fanart0,categoryA='Blank'):
        if (debugging==True): print 'Category: ',category,categoryA
        categoryA=category+' ::: '+categoryA
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&nm="+urllib.quote_plus(name2)+"&tp="+str(type2)+"&scr="+urllib.quote_plus(iconimage)+"&fan="+urllib.quote_plus(fanimage)+"&show="+urllib.quote_plus(name2)+"&cat="+categoryA+'&fav='+favcmd
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanimage )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir(name,name2,url,type2,mode,iconimage,fanimage,categoryA='Blank'):
        if (debugging==True): print 'Category: ',category,categoryA
        categoryA=category+' ::: '+categoryA
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&nm="+urllib.quote_plus(name2)+"&tp="+str(type2)+"&scr="+urllib.quote_plus(iconimage)+"&fan="+urllib.quote_plus(fanimage)+"&show="+urllib.quote_plus(name2)+"&cat="+categoryA
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanimage )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDirD(name,name2,url,type2,mode,iconimage,fanimage,doSorting=False,categoryA='Blank',Labels='none'):#,plot='Blank',genres='none listed',status='none',released='unknown',rating='none',others='none'):
        if Labels=='none': Labels={ "Title" : name }
        if categoryA=='Blank': categoryA=name
        #if (debugging==True): print 'Category: ',category,categoryA
        categoryA=category+' ::: '+categoryA
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&nm="+urllib.quote_plus(name2)+"&tp="+str(type2)+"&scr="+urllib.quote_plus(iconimage)+"&fan="+urllib.quote_plus(fanimage)+"&show="+urllib.quote_plus(name2)+"&cat="+urllib.quote_plus(categoryA)
        #
        if (debugging==True): print u
        vc_tag=visited_DoCheck(u)
        #if (name=='Maburaho'): visited_add(u)
        if (debugging==True): print vc_tag
        #
        ok=True
        liz=xbmcgui.ListItem(vc_tag+name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels= Labels ) #"Title": "'" + name + "'", "Plot" : plot, "Genres" : genres } )
        liz.setProperty( "Fanart_Image", fanimage )
        sysname = urllib.quote_plus(name)
        sysurl = urllib.quote_plus(url)
        sysscr = urllib.quote_plus(iconimage)
        sysfan = urllib.quote_plus(fanimage)
        #handle adding context menus
        contextMenuItems = []
        if (debugging==True): print getsetbool('enable-showurl')
        if __settings__.getSetting("enable-showurl") == "true":#doesn't work for some odd reason >> #if getsetbool('enable-showurl') == 'true':#
        	contextMenuItems.append(('[B][COLOR orange]Show[/COLOR][/B] ~  [B]URL[/B]',							'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(name2), type2, 'showurl', sysurl, sysscr, sysfan)))
        contextMenuItems.append(('[B][COLOR green]ADD[/COLOR][/B] ~  [B][COLOR tan]Favorite[/COLOR][/B]', 			'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s&show=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(name2), type2, 'add', sysurl, sysscr, sysfan,urllib.quote_plus(name2))))
        contextMenuItems.append(('[B][COLOR red]REMOVE[/COLOR][/B] ~  [B][COLOR tan]Favorite[/COLOR][/B]', 		'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s&show=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(name2), type2, 'rem', sysurl, sysscr, sysfan,urllib.quote_plus(name2))))
        contextMenuItems.append(('Show Information', 			'XBMC.Action(Info)'))
        #
        #contextMenuItems.append(('[B][COLOR orange]Test[/COLOR][/B] ~  [B]Test[/B]',"notification(%s,%s)" % (sysname,sysurl)))
        if (debugging==True): print getset('enable-clearfavorites')
        if __settings__.getSetting("enable-clearfavorites") == "true":#if getset('enable-clearfavorites')==True:
        	contextMenuItems.append(('[B][COLOR yellow]Clear[/COLOR][/B] ~  [B][COLOR tan]Favorites[/COLOR][/B]', 	'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(name2), type2, 'clr', sysurl, sysscr, sysfan)))
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)#True#liz.addContextMenuItems(contextMenuItems)
        if doSorting==True:
        	xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDirV(name,name2,url,type2,mode,iconimage,fanimage,categoryA=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&nm="+urllib.quote_plus(name2)+"&tp="+str(type2)+"&cat="+categoryA
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanimage )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
#def VaddDir(name, url, mode, iconimage, fanimage, is_folder=False,categoryA=''):#VANILLA ADDDIR (kept for reference)
#        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&cat="+categoryA
#        ok=True
#        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
#        liz.setInfo( type="Video", infoLabels={ "Title": name } )
#        liz.setProperty( "Fanart_Image", fanimage )
#        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=is_folder)
#        return ok
def VaddDir(name, url, mode, iconimage, fanimage, is_folder=False,categoryA=''):#VANILLA ADDDIR (kept for reference)
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&cat="+categoryA
        #if (debugging==True): print u
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanimage )
        contextMenuItems = []
        if __settings__.getSetting("enable-showurl") == "true":
        	contextMenuItems.append(('[B][COLOR orange]Show[/COLOR][/B] ~  [B]URL[/B]',							'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],mode , urllib.quote_plus(name), urllib.quote_plus(name), 877, 'showurl', urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanimage))))
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)#True#liz.addContextMenuItems(contextMenuItems)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=is_folder)
        return ok
### from theanimehighway.py ###
#def addLink(name,url,iconimage):
#        ok=True
#        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
#        liz.setInfo( type="Video", infoLabels={ "Title": name } )
#        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
#        return ok
def addLink(name,url,iconimage=ICON,fanimage=fanart,shoname='none',downloadable=True):
        ok=True
        if shoname=='none':
        	try: shoname=show
        	except:  shoname=name
        if fanimage==fanart:
        	try: fanimage=imgfan
        	except: pass
        if iconimage in MyIconsV:
        	try:
        		iconimage=scr
        	except: pass
        #
        #liz=xbmcgui.ListItem(name, iconImage=artPath+"blank.gif", thumbnailImage=iconimage)
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        ##if (debugging==True): print 'sitename name: '+SiteNames[type2] + name
        ##liz.setInfo( type="Video", infoLabels={ "Title": name } )
        Studio=name
        if (' - [COLOR grey]' 	in Studio): Studio = Studio.split(' - [COLOR grey]')[0]
        if (' [COLOR grey]- ' 	in Studio): Studio = Studio.split(' [COLOR grey]- ')[0]
        if ('[COLOR grey] - ' 	in Studio): Studio = Studio.split('[COLOR grey] - ')[0]
        if (' - [COLOR' 				in Studio): Studio = Studio.split(' - [COLOR')[0]
        showtitle=shoname
        if (' [COLOR lime](English Dubbed)[/COLOR]' in showtitle):
        	Studio += ' [COLOR lime](English Dubbed)[/COLOR]'
        	showtitle = showtitle.replace(' [COLOR lime](English Dubbed)[/COLOR]','')
        elif ('English Dubbed' 	in showtitle): Studio += ' [COLOR lime](English Dubbed)[/COLOR]'
        elif ('Eng Dubbed' 			in showtitle): Studio += ' [COLOR lime](English Dubbed)[/COLOR]'
        elif ('Dubbed' 					in showtitle): Studio += ' [COLOR lime](Dubbed)[/COLOR]'
        elif ('English Subbed' 	in showtitle): Studio += ' [COLOR lime](English Subbed)[/COLOR]'
        elif ('Eng Subbed' 			in showtitle): Studio += ' [COLOR lime](English Subbed)[/COLOR]'
        elif ('Subbed' 					in showtitle): Studio += ' [COLOR lime](Subbed)[/COLOR]'
        liz.setInfo( type="Video", infoLabels={ "Title": showtitle, "Studio": Studio } )
        #liz.setProperty( "Fanart_Image", fanimage )
        contextMenuItems = []
        if (debugging==True): print getset('enable-showurl')
        if __settings__.getSetting("enable-showurl") == "true":#if getset('enable-showurl')=='true':
        	contextMenuItems.append(('[B][COLOR orange]Show[/COLOR][/B] ~  [B]URL[/B]',							'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],0 , urllib.quote_plus(shoname), urllib.quote_plus(shoname), 0, 'showurl', urllib.quote_plus(url), iconimage, fanimage)))
        if (__settings__.getSetting("enable-downloading") == "true") and (downloadable == True):#if getset('enable-downloading',True)=='True':
        	#if ('videofun.me' not in url) and ('videoweed.es' not in url) and ('dailymotion.com' not in url):
        	if ('novamov.com' not in url) and ('videoweed.es' not in url) and ('dailymotion.com' not in url):
        		contextMenuItems.append(('[B][COLOR purple]Download[/COLOR][/B] ~  [B]File[/B]',				'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],0 , urllib.quote_plus(shoname), urllib.quote_plus(shoname), 0, 'download', urllib.quote_plus(url), iconimage, fanimage)))
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)#True#liz.addContextMenuItems(contextMenuItems)
        ##liz.addContextMenuItems([('[B][COLOR green]D[/COLOR][/B][B]ownload[/B]',"downloadfile(url,name)")])
        #liz.addContextMenuItems([('[B][COLOR green]D[/COLOR][/B][B]ownload[/B]',"XBMC.RunPlugin(%s?mode=%s&name=%s&url=%s)"%(sys.argv[0],999,name,url))])
        ##xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

### ############################################################################################################
def getset(idSetting):#,defaultValue=''):#Addon.getSetting('idNameOfSetting')
	return __settings__.getSetting(idSetting)#==defaultValue

def getsetbool(idSetting):#Addon.getSetting('idNameOfSetting') #Method seems to be an utter failure for BOOL(true/false)'s
	#if (debugging==True): print __settings__.getSetting(idSetting) == 'true'
	return __settings__.getSetting(idSetting) == 'true'
def getsetbool_(idSetting):#Addon.getSetting('idNameOfSetting') #Method seems to be an utter failure for BOOL(true/false)'s
	#if (debugging==True): print __settings__.getSetting(idSetting) == 'true'
	#try: tst=__settings__.getSetting(idSetting) == 'true'
	try: tst=__settings__.getSetting(idSetting)
	except: tst='False'
	if (tst=='true') or (tst=='True') or (tst=='TRUE'): return True
	else: return False
	#return __settings__.getSetting(idSetting) == 'true'
### ############################################################################################################
def download_it_now(url,name):## mode=1901 ##
	name=name.strip()
	if ('[/COLOR]' in name): name=name.replace('[/COLOR]','')
	if ('[COLOR lime]' in name): name=name.replace('[COLOR lime]','')
	if ('[/color]' in name): name=name.replace('[/color]','')
	if ('[color lime]' in name): name=name.replace('[color lime]','')
	#if ('' in name): name=name.replace('','')
	#if ('' in name): name=name.replace('','')
	#if ('' in name): name=name.replace('','')
	notification(name,'Attempting Download...')
	download_file_prep(url,name,name,name)
	## Example of how to connect to this addon's download feature from another plugin: ##
	#### xbmc.executebuiltin('XBMC.RunPlugin(%s?mode=1901&url=%s&name=%s)' % ('plugin://plugin.video.theanimehighway/', urllib.quote_plus(stream_url), urllib.quote_plus(title)))
	#### Simply make sure to include the quoted name and url for this function to work.
	#### File must be for a downloadable file or video stream, not for a page with a video on it.

def download_metapack(url, dest, displayname=False):
    print 'Downloading Metapack'
    print 'URL: %s' % url
    print 'Destination: %s' % dest
    if not displayname:
        displayname = url
    dlg = xbmcgui.DialogProgress()
    dlg.create('Downloading', '', displayname)
    start_time = time.time()
    if os.path.isfile(dest):
        print 'File to be downloaded already esists'
        return True
    try:
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dlg, start_time))
    except:
        #only handle StopDownloading (from cancel),
        #ContentTooShort (from urlretrieve), and OS (from the race condition);
        #let other exceptions bubble 
        if sys.exc_info()[0] in (urllib.ContentTooShortError, StopDownloading, OSError):
            return False
        else:
            raise
    return True

### 
### Dialog DialogBusy DialogButton Menu DialogContentSettings DialogContentMenu DialogExtendedProgressBar 
### DialogFavourites DialogKaiToast DialogKeyboard DialogOK DialogProgress DialogVolumeBar DialogVideoScan
### DialogVideoInfo DialogTextViewer DialogSlider DialogSelect DialogSeekBar DialogYesNo
### 

def download_file(url='',name='temp',localfilename='temp',localpath=artPath,filext='.flv'):
		t=''
		###url='https://github.com/HIGHWAY99/plugin.video.theanimehighway/archive/master.zip'
		###localfilename='plugin.video.theanimehighway.zip'
		###localpath=__home__
		#localfilewithpath=os.path.join(localpath,localfilename)
		#if (debugging==True): print 'Attempting to download "' + localfilename + '" to "' + localfilewithpath + '" from: ' + url
		###dialogbox('To: ' + localfilewithpath,'Download File: ' + localfilename,'From: ' + url,'[COLOR red]This is still being tested.[/COLOR]')
		#if os.path.isfile(localfilewithpath): 
		#	if (debugging==True): print 'File to be downloaded already esists.'
		#	notification('Download: '+localfilename,'File already exists.')#This function may never happen.
		#	return
		#dialog = xbmcgui.Dialog()
		#if dialog.yesno('Download File', 'Do you wish to download this file?','File: ' + localfilename,'To: ' + localpath):
		#	notification('Attempting to Download File',localfilename + '[CR] This function is still being tested.')#This function may never happen.
		#	try: dp = xbmcgui.DialogProgressBG() ## Only works on daily build of XBMC.
		#	except: dp = xbmcgui.DialogProgress()
		#	dp.create('Downloading', '', localfilename)
		#	####
		#	####urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhookb(nb, bs, fs, dlg, start_time))
		#	####
		#	urllib.urlretrieve(url, localfilewithpath, lambda nb, bs, fs: _pbhookb(nb, bs, fs, dlg, start_time))
		#	#urllib.urlretrieve(url, localfilewithpath)
		#	notification('Download File','Download Complete.[CR] ' + localfilename,15000)
		#	dialogbox_ok('File Size: ' + str(os.path.getsize(localfilewithpath)) + ' (bytes)','Download Complete','Note:','Make sure the size seems right.')
		#	###total_size += os.path.getsize(fp)
		###
		###
		###notification('Download File','Sorry this feature is not yet implimented.')#This function may never happen.

def _pbhookb(numblocks, blocksize, filesize, dlg, start_time):
    try:
        percent = min(numblocks * blocksize * 100 / filesize, 100)
        currently_downloaded = float(numblocks) * blocksize / (1024 * 1024)
        kbps_speed = numblocks * blocksize / (time.time() - start_time)
        if kbps_speed > 0:
            eta = (filesize - numblocks * blocksize) / kbps_speed
        else:
            eta = 0
        kbps_speed /= 1024
        total = float(filesize) / (1024 * 1024)
        mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total)
        est = 'Speed: %.02f Kb/s ' % kbps_speed
        est += 'ETA: %02d:%02d' % divmod(eta, 60)
        dlg.update(percent, mbs, est)
    except:
        percent = 100
        dlg.update(percent)
    #if dlg.iscanceled(): ## used for xbmcgui.DialogProgress() but causes an error with xbmcgui.DialogProgressBG()
    #    dlg.close()
    #    raise StopDownloading('Stopped Downloading')

def download_file_frodo(url='',name='temp',localfilename='temp',localpath=artPath,filext='.flv'):
		localfilewithpath=os.path.join(localpath,localfilename)
		if (debugging==True): print 'Attempting to download "' + localfilename + '" to "' + localfilewithpath + '" from: ' + url
		#dialogbox('To: ' + localfilewithpath,'Download File: ' + localfilename,'From: ' + url,'[COLOR red]This is still being tested.[/COLOR]')
		if os.path.isfile(localfilewithpath): 
			if (debugging==True): print 'File to be downloaded already esists.'
			notification('Download: '+localfilename,'File already exists.')#This function may never happen.
			return
		dialog = xbmcgui.Dialog()
		if dialog.yesno('Download File', 'Do you wish to download this file?','File: ' + localfilename,'To: ' + localpath):
			notification('Attempting to Download File',localfilename + '[CR] This function is still being tested.')#This function may never happen.
			dp = xbmcgui.DialogProgress()
			dp.create('Downloading', '', localfilename)
			start_time = time.time()
			urllib.urlretrieve(url, localfilewithpath, lambda nb, bs, fs: _pbhookb_frodo(nb, bs, fs, dp, start_time)) #urllib.urlretrieve(url, localfilewithpath)
			##urllib.urlretrieve(url, localfilewithpath, lambda nb, bs, fs: _pbhookb_frodo(nb, bs, fs, dlg, start_time)) #urllib.urlretrieve(url, localfilewithpath)
			notification('Download File','Download Complete.[CR] ' + localfilename,15000)
			dialogbox_ok('File Size: ' + str(os.path.getsize(localfilewithpath)) + ' (bytes)','Download Complete','Note:','Make sure the size seems right.')
			#total_size += os.path.getsize(fp)
		#notification('Download File','Sorry this feature is not yet implimented.')#This function may never happen.

def _pbhookb_frodo(numblocks, blocksize, filesize, dlg, start_time):
    try:
        percent = min(numblocks * blocksize * 100 / filesize, 100)
        currently_downloaded = float(numblocks) * blocksize / (1024 * 1024)
        kbps_speed = numblocks * blocksize / (time.time() - start_time)
        if kbps_speed > 0:
            eta = (filesize - numblocks * blocksize) / kbps_speed
        else:
            eta = 0
        kbps_speed /= 1024
        total = float(filesize) / (1024 * 1024)
        mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total)
        est = 'Speed: %.02f Kb/s ' % kbps_speed
        est += 'ETA: %02d:%02d' % divmod(eta, 60)
        dlg.update(percent, mbs, est)
    except:
        percent = 100
        dlg.update(percent)
    if dlg.iscanceled(): ## used for xbmcgui.DialogProgress() but causes an error with xbmcgui.DialogProgressBG()
        dlg.close()
        raise StopDownloading('Stopped Downloading')

def filename_filter_out_year(name=''):
	years=re.compile(' \((\d+)\)').findall('__'+name+'__')
	for year in years:
		name=name.replace(' ('+year+')','')
	name=name.strip()
	return name

def filename_filter_colorcodes(name=''):
	if ('[/color]' 				in name): name=name.replace('[/color]','')
	if ('[/COLOR]' 				in name): name=name.replace('[/COLOR]','')
	if ('[color lime]' 		in name): name=name.replace('[color lime]','')
	if ('[COLOR lime]' 		in name): name=name.replace('[COLOR lime]','')
	if ('[COLOR green]' 	in name): name=name.replace('[COLOR green]','')
	if ('[COLOR yellow]' 	in name): name=name.replace('[COLOR yellow]','')
	if ('[COLOR red]' 		in name): name=name.replace('[COLOR red]','')
	if ('[b]' 						in name): name=name.replace('[b]','')
	if ('[B]' 						in name): name=name.replace('[B]','')
	if ('[/b]' 						in name): name=name.replace('[/b]','')
	if ('[/B]' 						in name): name=name.replace('[/B]','')
	if ('[cr]' 						in name): name=name.replace('[cr]','')
	if ('[CR]' 						in name): name=name.replace('[CR]','')
	if ('[i]' 						in name): name=name.replace('[i]','')
	if ('[I]' 						in name): name=name.replace('[I]','')
	if ('[/i]' 						in name): name=name.replace('[/i]','')
	if ('[/I]' 						in name): name=name.replace('[/I]','')
	if ('[uppercase]' 		in name): name=name.replace('[uppercase]','')
	if ('[UPPERCASE]' 		in name): name=name.replace('[UPPERCASE]','')
	if ('[lowercase]' 		in name): name=name.replace('[lowercase]','')
	if ('[LOWERCASE]' 		in name): name=name.replace('[LOWERCASE]','')
	name=name.strip()
	#if ('' in name): name=name.replace('','')
	#if ('' in name): name=name.replace('','')
	#if ('' in name): name=name.replace('','')
	return name

def Download_PrepExt(url,ext='.flv'):
	if    '.zip' in url: ext='.zip' #Compressed Files
	elif  '.rar' in url: ext='.rar'
	elif   '.z7' in url: ext='.z7'
	elif  '.png' in url: ext='.png' #images
	elif  '.jpg' in url: ext='.jpg'
	elif  '.gif' in url: ext='.gif'
	elif  '.bmp' in url: ext='.bmp'
	elif '.jpeg' in url: ext='.jpeg'
	elif  '.mp4' in url: ext='.mp4' #Videos
	elif '.mpeg' in url: ext='.mpeg'
	elif  '.avi' in url: ext='.avi'
	elif  '.flv' in url: ext='.flv'
	elif  '.wmv' in url: ext='.wmv'
	elif  '.mp3' in url: ext='.mp3' #others
	elif  '.txt' in url: ext='.txt'
	#else: 							 ext='.flv' #Default File Extention ('.flv')
	return ext

def download_file_prep(url,name='none',name2='none',show='none',filext='none'):
	#
	if filext=='none':
		if   '.zip' in url: filext='.zip' #Compressed Files
		elif '.rar' in url: filext='.rar'
		elif '.z7' in url: filext='.z7'
		elif '.png' in url: filext='.png' #images
		elif '.jpg' in url: filext='.jpg'
		elif '.gif' in url: filext='.gif'
		elif '.mp4' in url: filext='.mp4' #Videos
		elif '.mpeg' in url: filext='.mpeg'
		elif '.avi' in url: filext='.avi'
		elif '.flv' in url: filext='.flv'
		elif '.wmv' in url: filext='.wmv'
		elif '.mp3' in url: filext='.mp3' #others
		elif '.txt' in url: filext='.txt'
		else: 							filext='.flv' #Default File Extention ('.flv')
	try: name=filename_filter_colorcodes(name)
	except: name=''
	try: name2=filename_filter_colorcodes(name2)
	except: name2=name
	try: show=filename_filter_colorcodes(show)
	except: show=name
	filname = name + filext
	dialog = xbmcgui.Dialog()
	if dialog.yesno('Local Path', 'Where would you like to download to?', '', filname, 'Shows', 'Movies'):
		localpath = getset('folder-movie')#__settings__.getSetting('folder-movie')
	else:
		localpath = getset('folder-show')#__settings__.getSetting('folder-show')
	if (debugging==True): print localpath
	#download_file(url,name,filname,localpath) ## For nightly builds 13.x+
	download_file_frodo(url,name,filname,localpath) ## For Frodo builds 12.x
	#

#def downloadfile(url,name):
#	import SimpleDownloader as downloader
#	downloader = downloader.SimpleDownloader()
#	url='http://www.xbmcswift.com/en/develop/api.html'
#	dlfold='/tmp'
#	#dlfold='F:\\xbmc\\theanimehighway\\'
#	params = { "url": url, "download_path": dlfold, "Title": name }
#	#params = { "url": url, "download_path": "F:\\xbmc\\theanimehighway\\", "Title": name, "live": "true", "duration": "20" }
#	filenm = name + ".txt"
#	#filenm = name + ".mp4"
#	notification('file download: ' + name, 'Downloading "' + url + '" to "' + filenm + '"')
#	downloader.download(filenm, params)

### ############################################################################################################
#def dialogboxyesno(txtMessage="",txtHeader="",txt3="",txt4=""):
#	dialog = xbmcgui.Dialog()
#	if dialog.yesno(txtHeader, txtMessage, txt3, txt4):

def dialogbox_ok(txtMessage="",txtHeader="",txt3="",txt4=""):
	dialog = xbmcgui.Dialog()
	ok = dialog.ok(txtHeader, txtMessage, txt3, txt4)
	#keyboard = xbmc.Keyboard(txtMessage, txtHeader, passwordField)#("text to show","header text", True="password field"/False="show text")

#import win64clipboard as wc
def copy_to_clipboard(msg):
		notification('Copy-to-Clipboard','Sorry this feature is not yet implimented.')
		#
		#
		#if sys.platform == 'win32':
		#	wc.OpenClipboard()
		#	wc.EmptyClipboard()
		#	wc.SetClipboardData(win32con.CF_TEXT, msg)
		#	wc.CloseClipboard()
		#
		#

def showkeyboard(txtMessage="",txtHeader="",passwordField=False):
	if txtMessage=='None': txtMessage=''
	keyboard = xbmc.Keyboard(txtMessage, txtHeader, passwordField)#("text to show","header text", True="password field"/False="show text")
	keyboard.doModal()
	if keyboard.isConfirmed():
		return keyboard.getText()
	else:
		return False # return ''

def dialogbox_number(Header="",n='',type=0):
	#Types:		#0 : ShowAndGetNumber		#1 : ShowAndGetDate		#2 : ShowAndGetTime		#3 : ShowAndGetIPAddress	dialog = xbmcgui.Dialog()
	dlg=xbmcgui.Dialog()
	if (n==''): r=dlg.numeric(1,Header)
	else: 			r=dlg.numeric(1,Header,n)
	return r


### ############################################################################################################
def checkForPartNo(url,partInfo=''):
	url=urllib.unquote_plus(url)
	if '_part_' in urllib.unquote_plus(url):
		try:
			matchaptn=re.compile('_part_(.+?).').findall(url)
			partInfo=' - Part # ' + matchaptn[0]
		except:
			partInfo=' - Part # ' + 'Unknown'
	elif '-part-' in urllib.unquote_plus(url):
		try:
			matchaptn=re.compile('-part-(.+?).').findall(url)
			partInfo=' - Part # ' + matchaptn[0]
		except:
			partInfo=' - Part # ' + 'Unknown'
	elif 'part' in urllib.unquote_plus(url):
		try:
			matchaptn=re.compile('part(.+?).').findall(url)
			partInfo=' - Part # ' + matchaptn[0]
		except:
			temp=''
	return partInfo

### ############################################################################################################
def aSortMeth(sM,h=int(sys.argv[1])):
	xbmcplugin.addSortMethod(handle=h, sortMethod=sM)

def set_view(content='none',view_mode=50,do_sort=False):
	if (debugging==True): print 'content type: ',content
	if (debugging==True): print 'view mode: ',view_mode
	h=int(sys.argv[1])
	#try:		h=int(sys.argv[1])
	#except:	h=_addon.handle
	if (content is not 'none'): xbmcplugin.setContent(h, content)
	#types:									# set_view()
	# 50		CommonRootView
	# 51		FullWidthList
	# 500		ThumbnailView
	# 501		PosterWrapView
	# 508		PosterWrapView2_Fanart
	# 505		WideIconView
	# 
	# 
	# set content type so library shows more views and info
	if (tfalse(addst("auto-view"))==True):
		xbmc.executebuiltin("Container.SetViewMode(%s)" % view_mode)
	# set sort methods - probably we don't need all of them
	#aSortMeth(xbmcplugin.SORT_METHOD_NONE)
	aSortMeth(xbmcplugin.SORT_METHOD_UNSORTED)
	aSortMeth(xbmcplugin.SORT_METHOD_TITLE)
	aSortMeth(xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE)
	aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_TITLE)
	aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_SORT_TITLE_IGNORE_THE)
	aSortMeth(xbmcplugin.SORT_METHOD_LABEL)
	aSortMeth(xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
	aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_RATING)
	aSortMeth(xbmcplugin.SORT_METHOD_DATE)
	aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_YEAR)
	#aSortMeth(xbmcplugin.SORT_METHOD_PROGRAM_COUNT)
	aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_RUNTIME)
	aSortMeth(xbmcplugin.SORT_METHOD_GENRE)
	#
	aSortMeth(xbmcplugin.SORT_METHOD_FILE)
	#aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_RUNTIME)
	#aSortMeth(xbmcplugin.SORT_METHOD_VIDEO_RATING)
	#aSortMeth(xbmcplugin.SORT_METHOD_STUDIO)
	#aSortMeth(xbmcplugin.SORT_METHOD_STUDIO_IGNORE_THE)
	#aSortMeth(xbmcplugin.SORT_METHOD_PLAYLIST_ORDER)
	aSortMeth(xbmcplugin.SORT_METHOD_EPISODE)
	aSortMeth(xbmcplugin.SORT_METHOD_DURATION)
	#aSortMeth(xbmcplugin.SORT_METHOD_BITRATE)
	#
	if (do_sort == True):
		#aSortMeth(h, xbmcplugin.SORT_METHOD_TITLE)#xbmcplugin.SORT_METHOD_LABEL
		xbmcplugin.addSortMethod(h, xbmcplugin.SORT_METHOD_TITLE)#xbmcplugin.SORT_METHOD_LABEL
	#
	####xbmcplugin.addSortMethod(handle=h, sortMethod=xbmcplugin.SORT_METHOD_TRACKNUM)
#	#SORT_METHOD_NONE, SORT_METHOD_UNSORTED, SORT_METHOD_VIDEO_TITLE,
#	#                        SORT_METHOD_TRACKNUM, SORT_METHOD_FILE, SORT_METHOD_TITLE
#	#                        SORT_METHOD_TITLE_IGNORE_THE, SORT_METHOD_LABEL
#	#                        SORT_METHOD_LABEL_IGNORE_THE, SORT_METHOD_VIDEO_SORT_TITLE,
#	#                        SORT_METHOD_VIDEO_SORT_TITLE_IGNORE_THE

### ############################################################################################################
### from theanimehighway.py ###
#def showurl(name,url,scr=ICON0,imgfan=fanart0,type2=0,mode=0):
#	copy_to_clipboard(url)
#	if (debugging==True): print url, name, scr, imgfan
#	kmsg=showkeyboard(url, name)
def showurl(name,url,scr=ICON,imgfan=fanart,type2=0,mode=0):
	copy_to_clipboard(url)
	if (debugging==True): print url, name, scr, imgfan
	kmsg=showkeyboard(url, name)

### ############################################################################################################
def metaArt_empty():
  saved_fans = cache.get('MetaArt_')
  fans = []
  cache.set('MetaArt_', str(fans))
  notification('[B][COLOR orange]Fanart[/COLOR][/B]','[B] Your Cached Fanart(s) Have Been Wiped Clean. Bye Bye.[/B]')
def emptyFavorites():
  saved_favs = cache.get('favourites_')
  favs = []
  cache.set('favourites_', str(favs))
  notification('[B][COLOR orange]Favorites[/COLOR][/B]','[B] Your Favorites Have Been Wiped Clean. Bye Bye.[/B]')
def addfavorite(name,url,scr=ICON0,imgfan=fanart0,tp2=0,mode=0):
    if (debugging==True): print name,url,scr,imgfan,tp2,mode
    saved_favs = cache.get('favourites_')
    favs = []
    if saved_favs:
        favs = eval(saved_favs)
        if favs:
            if (name,url,scr,imgfan,tp2,mode) in favs:
                notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] Already in your Favorites[/B]')
                #xbmc.executebuiltin("XBMC.Notification([B][COLOR orange]"+name.upper()+"[/COLOR][/B],[B] Already in your Favourites[/B],5000,"")")
                return
    favs.append((name,url,scr,imgfan,tp2,mode))
    cache.set('favourites_', str(favs))
    notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] Added to Favorites[/B]')
    #xbmc.executebuiltin("XBMC.Notification([B][COLOR orange]"+name.upper()+"[/COLOR][/B],[B] Added to Favourites[/B],5000,"")")
def removefavorite(name,url,scr=ICON0,imgfan=fanart0,tp2=0,mode=0):#,scr,imgfan
  if (debugging==True): print name,url,scr,imgfan,tp2,mode
  saved_favs = cache.get('favourites_')
  if saved_favs:
    favs = eval(saved_favs)
    if (name,url,scr,imgfan,tp2,mode) in favs:
    	favs.remove((name,url,scr,imgfan,tp2,mode))
    	cache.set('favourites_', str(favs))
    	notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] Removed from Favorites[/B]')
    	if (debugging==True): print name+' Removed from Favorites.'
    	#set_view('tvshows',int(getset('viewmode-favs')),True)
    	#VaddDir('[COLOR maroon] Visit with [COLOR tan]Highway[/COLOR] and others @ [COLOR white]#XBMCHUB[/COLOR] on [COLOR white]irc.freenode.net[/COLOR]:6667 [/COLOR]', '', 0, ICON, fanart, False)
    	#LastPage=page_last_update()
    	#xbmc.executebuiltin("XBMC.Container.Update(%s)" % (LastPage))
    	xbmc.executebuiltin("XBMC.Container.Refresh")
    	#VaddDir('[COLOR maroon] Visit with [COLOR tan]Highway[/COLOR] and others @ [COLOR white]#XBMCHUB[/COLOR] on [COLOR white]irc.freenode.net[/COLOR]:6667 [/COLOR]', '', 0, ICON, fanart, False)
    	##xbmc.Container.Refresh
    	#xbmc.sleep(4000)
    elif ((name) in favs):
    	favs.remove((name))
    	cache.set('favourites_', str(favs))
    	notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] Removed from Favorites[/B]')
    	if (debugging==True): print name+' Removed from Favorites. (Hopefully)'
    	xbmc.executebuiltin("XBMC.Container.Refresh")
    elif favs:
    	tf=False
    	for (_name,_url,_scr,_imgfan,_tp2,_mode) in favs:
    		if (name==_name):
    			favs.remove((name,_url,_scr,_imgfan,_tp2,_mode))
    			cache.set('favourites_', str(favs))
    			notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] Removed from Favorites[/B]')
    			if (debugging==True): print name+' Removed from Favorites. (Hopefully)'
    			tf=True
    			xbmc.executebuiltin("XBMC.Container.Refresh")
    			return
    	if (tf==False): notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] not found in your Favorites[/B]')
    else:
    	notification('[B][COLOR orange]'+name.upper()+'[/COLOR][/B]','[B] not found in your Favorites[/B]')
    #xbmc.executebuiltin("XBMC.Notification([B][COLOR orange]"+name.upper()+"[/COLOR][/B],[B] Removed from Favourites[/B],5000,"")")
def metaArt_add(show_name,show_title_thetvdb,show_id,url_thetvdb,show_fanart,show_poster,show_bannner,show_desc,show_genres,show_status,show_language,show_network,show_rating):#metaArt_add(match_showname,match_showid,match_thetvdb_url,match_fanart,match_poster,match_banner)
	##if (debugging==True): print name,url,scr,imgfan,tp2,mode
	saved_fans = cache.get('MetaArt_')
	fans = []
	if saved_fans:
		fans = eval(saved_fans)
		if fans:
			if (show_name,show_id,url_thetvdb,show_fanart,show_poster,show_bannner,show_desc) in fans:
				#notification('[B][COLOR orange]'+show_name.upper()+'[/COLOR][/B]','[B] Already in your Cached Fanart(s).[/B]')
				return
	fans.append((show_name,show_title_thetvdb,show_id,url_thetvdb,show_fanart,show_poster,show_bannner,show_desc,show_genres,show_status,show_language,show_network,show_rating))
	cache.set('MetaArt_', str(fans))
	#notification('[B][COLOR orange]'+show_name.upper()+'[/COLOR][/B]','[B] Added to MetaArt[/B]')
	##xbmc.executebuiltin("XBMC.Notification([B][COLOR orange]"+name.upper()+"[/COLOR][/B],[B] Added to Favourites[/B],5000,"")")
### ############################################################################################################
def getAlphaFolder(alphaTxt='',typeTxt='',slashTxt=''):
	if type2==5: return 'subanime/'
	#elif mode==211: return 'alpha-anime/'
	#elif mode==311: return 'alpha-movies/'
	else: return alphaTxt+typeTxt+slashTxt
def getAlphaEnd(typeTxt='',alphaTxt=''):
	if   (type2==5) and (typeTxt=='anime'):  return '-2'
	elif (type2==5) and (typeTxt=='movies'): return '-3'
	else: return alphaTxt
def showlistdir(vLetterA,vLetterB,vImageC):#SitePrefixes#SiteSufixes
	addFolder('[COLOR ' + MyColors[1] + ']' + vLetterB + '[/COLOR]','shows',getAlphaFolder('alpha-','anime','/') + vLetterA + getAlphaEnd('anime') + SiteSufixes[type2],type2,6,'Glossy_Black\\' + vImageC + '.png')
def movielistdir(vLetterA,vLetterB,vImageC):
	addFolder('[COLOR ' + MyColors[1] + ']' + vLetterB + '[/COLOR]','movies',getAlphaFolder('alpha-','movies','/') + vLetterA + getAlphaEnd('movies') + SiteSufixes[type2],type2,6,'Glossy_Black\\' + vImageC + '.png')

### ############################################################################################################
def clean_filename(filename):
    # filename = _1CH.unescape(filename)
    return re.sub('[/:"*?<>|]+', ' ', filename)

def ParseDescription(plot): ## Cleans up the dumb number stuff thats ugly.
	if ('&#' in plot) and (';' in plot):
		if ("&amp;"  in plot):  plot=plot.replace('&amp;'  ,'&')#&amp;#x27;
		if ("&#8211;" in plot): plot=plot.replace("&#8211;",";") #unknown
		if ("&#8216;" in plot): plot=plot.replace("&#8216;","'")
		if ("&#8217;" in plot): plot=plot.replace("&#8217;","'")
		if ("&#8220;" in plot): plot=plot.replace('&#8220;','"')
		if ("&#8221;" in plot): plot=plot.replace('&#8221;','"')
		if ("&#215;"  in plot): plot=plot.replace('&#215;' ,'x')
		if ("&#x27;"  in plot): plot=plot.replace('&#x27;' ,"'")
		if ("&#xF4;"  in plot): plot=plot.replace('&#xF4;' ,"o")
		if ("&#xb7;"  in plot): plot=plot.replace('&#xb7;' ,"-")
		if ("&#xFB;"  in plot): plot=plot.replace('&#xFB;' ,"u")
		if ("&#xE0;"  in plot): plot=plot.replace('&#xE0;' ,"a")
		if ("&#0421;" in plot): plot=plot.replace('&#0421;',"")
		if ("&#xE9;" in plot):  plot=plot.replace('&#xE9;' ,"e")
		if ("&#xE2;" in plot):  plot=plot.replace('&#xE2;' ,"a")
		if ('&#' in plot) and (';' in plot):
			try:		matches=re.compile('&#(.+?);').findall(plot)
			except:	matches=''
			if (matches is not ''):
				for match in matches:
					if (match is not '') and (match is not ' ') and ("&#"+match+";" in plot):  plot=plot.replace("&#"+match+";" ,"")
		#if ("\xb7"  in plot):  plot=plot.replace('\xb7'   ,"-")
		#if ('&#' in plot) and (';' in plot): plot=unescape_(plot)
	return plot
def unescape_(s):
	p = htmllib.HTMLParser(None)
	p.save_bgn()
	p.feed(s)
	return p.save_end()

def check_ifUrl_isHTML(pathUrl): ## Doesn't work yet. Needs Fixed.
	######## 'http://s12.trollvid.net/videos/'+testString+'/'+vid_id1+'.mp4'
	##timeout=10
	##socket.setdefaulttimeout(timeout) # timeout in seconds
	if (debugging==True): print 'TestingUrl: '+pathUrl
	try:
		req=urllib2.Request(pathUrl)#,timeout=6)
		tUrl=urllib2.urlopen(req)
		return True
	except:
		return False

### ############################################################################################################
def visited_DoCheck(urlToCheck,s='[B][COLOR yellowgreen]@[/COLOR][/B] ',e='[COLOR black]@[/COLOR] '):
	#visited_empty()
	#return ''
	vc=visited_check(urlToCheck)
	if (vc==True): return s
	else: 
		##visited_add(urlToCheck)
		return e

def visited_check(urlToCheck):
  try: saved_visits = cache.get('visited_')
  except: return False
  erNoFavs='XBMC.Notification([B][COLOR orange]Favorites[/COLOR][/B],[B]You have no favorites saved.[/B],5000,"")'
  if not saved_visits: return False #xbmc.executebuiltin(erNoFavs)
  if saved_visits == '[]': return False #xbmc.executebuiltin(erNoFavs)
  if saved_visits:
  	visits = eval(saved_visits)
  	if (urlToCheck in visits): return True
  return False

def visited_empty():
  saved_favs = cache.get('visited_')
  favs = []
  cache.set('visited_', str(favs))
  notification('[B][COLOR orange]Visited[/COLOR][/B]','[B] Your Visited Data has been wiped clean. Bye Bye.[/B]')

def visited_add(urlToAdd):
	if (urlToAdd==''): return ''
	elif (urlToAdd==None): return ''
	if (debugging==True): print 'checking rather url has been visited: ' + urlToAdd
	saved_visits = cache.get('visited_')
	visits = []
	if saved_visits:
		#if (debugging==True): print 'saved visits: ',saved_visits
		visits = eval(saved_visits)
		if visits:
			if (urlToAdd) in visits: return
	visits.append((urlToAdd))
	cache.set('visited_', str(visits))

def qp_get(n): ## Deals with errors in using None type within a urllib.quote_plus().
	#print n
	if (n==''): return ''
	elif (n==None): return ''
	else: return urllib.quote_plus(n)
def st_get(n): ## Deals with errors in using None type within a str().
	#print n
	if (n==None): return ''
	else: return str(n)

def page_last_get(defaultLastPage=sys.argv[0]+'?mode=0'):
  try: last_visited = cache.get('lastpage')
  except: return defaultLastPage
  erNoFavs='XBMC.Notification([B][COLOR orange]Favorites[/COLOR][/B],[B]You have no favorites saved.[/B],5000,"")'
  if not last_visited: return defaultLastPage
  if last_visited == '[]': return defaultLastPage
  if last_visited == '': return defaultLastPage
  if last_visited:
  	return eval(last_visited)
  return defaultLastPage

def page_last_update(defaultLastPage=sys.argv[0]+sys.argv[2]):
	cache.set('lastpage', defaultLastPage)

def format_eta(seconds):
    minutes, seconds = divmod(seconds, 60)
    if minutes > 60:
        hours, minutes = divmod(minutes, 60)
        return "ETA: %02d:%02d:%02d " % (hours, minutes, seconds)
    else:
        return "ETA: %02d:%02d " % (minutes, seconds)

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    if minutes > 60:
        hours, minutes = divmod(minutes, 60)
        return "%02d:%02d:%02d" % (hours, minutes, seconds)
    else:
        return "%02d:%02d" % (minutes, seconds)

### ############################################################################################################
### ############################################################################################################
class TextBox_FromFile:
	# constants
	WINDOW = 10147
	CONTROL_LABEL = 1
	CONTROL_TEXTBOX = 5
	def __init__(self, *args, **kwargs):
		xbmc.executebuiltin("ActivateWindow(%d)" % ( self.WINDOW, ))				# activate the text viewer window
		self.win = xbmcgui.Window(self.WINDOW)															# get window
		xbmc.sleep(1000)																										# give window time to initialize
		self.setControls()
	def setControls(self,txtFilepath=__home__,txtFilename='changelog.txt'):
		HeaderMsg = "%s - ( v%s )" % (__plugin__,addon.get_version())										# set heading
		self.win.getControl(self.CONTROL_LABEL).setLabel(HeaderMsg)
		#root = addon.get_path()																							# set text
		txt_path = os.path.join(txtFilepath,txtFilename)
		#txt_path = os.path.join(__home__, 'news.txt')
		f = open(txt_path)
		text = f.read()
		self.win.getControl(self.CONTROL_TEXTBOX).setText(text)
### ############################################################################################################
class TextBox_FromUrl: ## Usage Example: TextBox_FromUrl().load('https://raw.github.com/HIGHWAY99/plugin.video.theanimehighway/master/README.md')
	WINDOW 						=	10147
	CONTROL_LABEL 		=	1
	CONTROL_TEXTBOX 	=	5
	HEADER_MESSAGE		=	"%s - ( v%s )" % (__plugin__,addon.get_version())										# set heading
	def load(self, URL_PATH, HEADER_MESSAGE2=''):
		if (HEADER_MESSAGE2==''): HEADER_MESSAGE2=self.HEADER_MESSAGE
		print 'text window from url: ',URL_PATH #self.URL_PATH
		try: 			text=getURL(URL_PATH)#(self.URL_PATH)
		except: 	text=''
		xbmc.executebuiltin("ActivateWindow(%d)" % ( self.WINDOW, ))				# activate the text viewer window
		self.win = xbmcgui.Window(self.WINDOW)															# get window
		xbmc.sleep(500)																											# give window time to initialize
		self.win.getControl(self.CONTROL_LABEL).setLabel(HEADER_MESSAGE2)
		self.win.getControl(self.CONTROL_TEXTBOX).setText(text)
### ############################################################################################################
class TextBox2: ## Usage Example: TextBox_FromUrl().load('https://raw.github.com/HIGHWAY99/plugin.video.theanimehighway/master/README.md')
	WINDOW 						=	10147
	CONTROL_LABEL 		=	1
	CONTROL_TEXTBOX 	=	5
	HEADER_MESSAGE		=	"%s - ( v%s )" % (__plugin__,addon.get_version())										# set heading
	def load_url(self, URL_PATH, HEADER_MESSAGE2=''):
		if (debugging==True): print 'text window from url: ',URL_PATH #self.URL_PATH
		try: 			text=getURL(URL_PATH)#(self.URL_PATH)
		except: 	text=''
		self.load_window()
		self.set_header(HEADER_MESSAGE2)
		self.set_text(text)
	def load_file(self, FILE_NAME='changelog.txt', HEADER_MESSAGE2='', FILE_PATH=__home__):
		txt_path = os.path.join(FILE_PATH,FILE_NAME)
		if (debugging==True): print 'text window from file: ',txt_path
		f = open(txt_path)
		text = f.read()
		self.load_window()
		self.set_header(HEADER_MESSAGE2)
		self.set_text(text)
	def load_string(self, text_string='', HEADER_MESSAGE2=''):
		self.load_window()
		self.set_header(HEADER_MESSAGE2)
		self.set_text(text_string)
	def load_window(self, sleeptime=500):
		xbmc.executebuiltin("ActivateWindow(%d)" % ( self.WINDOW, ))				# activate the text viewer window
		self.win = xbmcgui.Window(self.WINDOW)															# get window
		xbmc.sleep(sleeptime)																											# give window time to initialize
	def set_header(self, HEADER_MESSAGE2=''):
		if (HEADER_MESSAGE2==''): HEADER_MESSAGE2=self.HEADER_MESSAGE
		self.win.getControl(self.CONTROL_LABEL).setLabel(HEADER_MESSAGE2)
	def set_text(self, text=''):
		self.win.getControl(self.CONTROL_TEXTBOX).setText(text)
### ############################################################################################################
### ############################################################################################################
class class_itmOBJ(object): ## Thx to those of plugin.video.SportsDevil.
	def __init__(self):
		self.infos_names = []
		self.infos_values = []
	def __getitem__(self, key, type1=1):
		#return self.getInfo_str(key)
		if (type1==1): return self.getInfo_str(key)
		if (type1==2): return self.getInfo_int(key)
		if (type1==3): return self.getInfo_b(key)
		else: return self.getInfo(key)
	def __setitem__(self, key, value):
		self.setInfo(key, value)
	def reset(self):
		self.infos_names = []
		self.infos_values = []
	def setInfo(self, key, value):
		if key in self.infos_names:
			self.infos_values[self.infos_names.index(key)] = value
		else:
			self.infos_names.append(key)
			self.infos_values.append(value)
			#if (debugging==True): print 'value: ',value
			#if (debugging==True): print 'key: '+key
			#if (debugging==True): print 'value set: ',self.infos_values[self.infos_names.index(key)]
			##if (debugging==True): notification('value',value)
	def getInfo(self, key):
		if (debugging==True): print self.infos_names
		if (debugging==True): print self.infos_values
		if self.infos_names.__contains__(key):
			return self.infos_values[self.infos_names.index(key)]
		return None
	def getInfo_str(self, key):
		if self.infos_names.__contains__(key):
			return self.infos_values[self.infos_names.index(key)]
		return ''
	def getInfo_int(self, key):
		if self.infos_names.__contains__(key):
			return self.infos_values[self.infos_names.index(key)]
		return 0
	def getInfo_b(self, key):
		if self.infos_names.__contains__(key):
			return self.infos_values[self.infos_names.index(key)]
		return False
	def merge(self, item):
		for info_name in item.infos_names:
			if not self[info_name]:
				self[info_name] = item[info_name]
	def __str__(self):
		txt = ''
		for info_name in self.infos_names:
			txt += string.ljust(info_name,15) +':\t' + self[info_name] + '\n'
		return txt
### ############################################################################################################
class class_MyMenu(object):
	def eod(self): ## 
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
	def refresh(self): ## To Refresh the Menu.
		xbmc.executebuiltin("XBMC.Container.Refresh")
	def get_u(self,iOBJ): ## To make  the plugin URL.
		u=sys.argv[0]
		u+="?url="+urllib.quote_plus(iOBJ['url'])
		u+="&mode="+str(iOBJ['mode'])
		u+="&name="+urllib.quote_plus(iOBJ['name'])
		u+="&nm="+urllib.quote_plus(iOBJ['name2'])
		u+="&tp="+str(iOBJ['type2'])
		u+="&scr="+urllib.quote_plus(iOBJ['image_thumbnail'])
		u+="&fan="+urllib.quote_plus(iOBJ['image_fanart'])
		u+="&show="+urllib.quote_plus(iOBJ['show'])
		u+="&cat="+urllib.quote_plus(iOBJ['category'])
		return u
	def addDir_MI(self,iOBJ): ## For Folders - Menu Items
		#if (debugging==True): print iOBJ
		if (debugging==True): print 'addDir_MI -- label_title: '+iOBJ['label_title']
		ok=True; u=self.get_u(iOBJ)
		if (debugging==True): print 'addDir_MI -- u: '+u
		liz=xbmcgui.ListItem(iOBJ['name'], iconImage="DefaultFolder.png", thumbnailImage=iOBJ['image_thumbnail'])
		liz.setInfo( type="Video", infoLabels={ "Title": iOBJ['label_title'] } )
		liz.setProperty( "Fanart_Image", iOBJ['image_fanart'] )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=iOBJ['isFolder'])
		return ok
	def addDir_FC(self,iOBJ): ## For Folders - Menu Items with %Fav= for special over-ride commands.
		ok=True; u=self.get_u(iOBJ)
		u+='&fav='+iOBJ['favcmd']
		if (debugging==True): print 'addDir_FC -- u: '+u
		liz=xbmcgui.ListItem(iOBJ['name'], iconImage="DefaultFolder.png", thumbnailImage=iOBJ['image_thumbnail'])
		liz.setInfo( type="Video", infoLabels={ "Title": iOBJ['label_title'] } )
		liz.setProperty( "Fanart_Image", iOBJ['image_fanart'] )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=iOBJ['isFolder'])
		return ok
	def addDir_LA(self,iOBJ): ## Label Text
		ok=True; u=self.get_u(iOBJ)
		if (debugging==True): print 'addDir_LA -- u: '+u
		liz=xbmcgui.ListItem(iOBJ['name'], iconImage="DefaultFolder.png", thumbnailImage=iOBJ['image_thumbnail'])
		liz.setInfo( type="Video", infoLabels={ "Title": iOBJ['label_title'] } )
		liz.setProperty( "Fanart_Image", iOBJ['image_fanart'] )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=iOBJ['isFolder'])
		return ok
	def addDir_CM1(self,iOBJ): ## For ??
		ok=True; u=self.get_u(iOBJ)
		if (debugging==True): print 'addDir_CM1 -- u: '+u
		liz=xbmcgui.ListItem(iOBJ['name'], iconImage="DefaultFolder.png", thumbnailImage=iOBJ['image_thumbnail'])
		liz.setInfo( type="Video", infoLabels={ "Title": iOBJ['label_title'] } )
		liz.setProperty( "Fanart_Image", iOBJ['image_fanart'] )
		contextMenuItems = []
		if __settings__.getSetting("enable-showurl") == "true":
			contextMenuItems.append(('[B][COLOR orange]Show[/COLOR][/B] ~  [B]URL[/B]',							'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],iOBJ['mode'] , urllib.quote_plus(iOBJ['name']), urllib.quote_plus(iOBJ['name']), 877, 'showurl', urllib.quote_plus(iOBJ['url']), urllib.quote_plus(iOBJ['image_thumbnail']), urllib.quote_plus(iOBJ['image_fanart']))))
		liz.addContextMenuItems(contextMenuItems, replaceItems=True)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=iOBJ['isFolder']) ## is_folder=False
		return ok
	def addDir_CM2(self,iOBJ,Labels='none'): ## For Folder - Used for show listings.
		if Labels=='none': Labels={ "Title" : iOBJ['label_title'] }
		#Labels=self.get_L(iOBJ,Labels)
		ok=True; u=self.get_u(iOBJ)
		if (debugging==True): print 'addDir_CM2 -- u: '+u
		vc_tag=visited_DoCheck(u)
		if (debugging==True): print vc_tag
		liz=xbmcgui.ListItem(vc_tag+iOBJ['name'], iconImage="DefaultFolder.png", thumbnailImage=iOBJ['image_thumbnail'])
		liz.setInfo( type="Video", infoLabels=Labels )
		liz.setProperty( "Fanart_Image", iOBJ['image_fanart'] )
		contextMenuItems = []
		sysname = urllib.quote_plus(iOBJ['name'])
		sysurl = urllib.quote_plus(iOBJ['url'])
		sysscr = urllib.quote_plus(iOBJ['image_thumbnail'])
		sysfan = urllib.quote_plus(iOBJ['image_fanart'])
		if (debugging==True): print getsetbool('enable-showurl')
		if __settings__.getSetting("enable-showurl") == "true":#doesn't work for some odd reason >> #if getsetbool('enable-showurl') == 'true':#
			contextMenuItems.append(('[B][COLOR orange]Show[/COLOR][/B] ~  [B]URL[/B]',														'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(iOBJ['name2']), type2, 'showurl', sysurl, sysscr, sysfan)))
		contextMenuItems.append(('[B][COLOR green]ADD[/COLOR][/B] ~  [B][COLOR tan]Favorite[/COLOR][/B]', 			'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s&show=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(iOBJ['name2']), type2, 'add', sysurl, sysscr, sysfan,urllib.quote_plus(iOBJ['name2']))))
		contextMenuItems.append(('[B][COLOR red]REMOVE[/COLOR][/B] ~  [B][COLOR tan]Favorite[/COLOR][/B]', 			'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s&show=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(iOBJ['name2']), type2, 'rem', sysurl, sysscr, sysfan,urllib.quote_plus(iOBJ['name2']))))
		contextMenuItems.append(('Show Information', 			'XBMC.Action(Info)'))
		contextMenuItems.append(('[B][COLOR orange]Metadata[/COLOR][/B] ~ Show Name',												'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(iOBJ['name2']), type2, 'metachangeshowname', sysurl, sysscr, sysfan)))
		#contextMenuItems.append(('[B][COLOR orange]Test[/COLOR][/B] ~  [B]Test[/B]',"notification(%s,%s)" % (sysname,sysurl)))
		if (debugging==True): print getset('enable-clearfavorites')
		if __settings__.getSetting("enable-clearfavorites") == "true":#if getset('enable-clearfavorites')==True:
			contextMenuItems.append(('[B][COLOR yellow]Clear[/COLOR][/B] ~  [B][COLOR tan]Favorites[/COLOR][/B]', 	'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],mode , sysname, urllib.quote_plus(iOBJ['name2']), type2, 'clr', sysurl, sysscr, sysfan)))
		liz.addContextMenuItems(contextMenuItems, replaceItems=True)
		if iOBJ['doSorting']==True: ## doSorting=False by default
			xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=iOBJ['isFolder']) ## is_folder=True
		return ok
	def addLink_(self, iOBJ, downloadable=True): ## For Video Links.
		ok=True; u=self.get_u(iOBJ)
		if (debugging==True): print u
		liz=xbmcgui.ListItem(iOBJ['name'], iconImage="DefaultFolder.png", thumbnailImage=iOBJ['image_thumbnail'])
		if (' - [COLOR grey]' 	in iOBJ['label_studio']): iOBJ['label_studio']=iOBJ['label_studio'].split(' - [COLOR grey]')[0]
		if (' [COLOR grey]- ' 	in iOBJ['label_studio']): iOBJ['label_studio']=iOBJ['label_studio'].split(' [COLOR grey]- ')[0]
		if ('[COLOR grey] - ' 	in iOBJ['label_studio']): iOBJ['label_studio']=iOBJ['label_studio'].split('[COLOR grey] - ')[0]
		if (' - [COLOR' 				in iOBJ['label_studio']): iOBJ['label_studio']=iOBJ['label_studio'].split(' - [COLOR')[0]
		if (' [COLOR lime](English Dubbed)[/COLOR]' in iOBJ['label_title']):
			iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](English Dubbed)[/COLOR]'
			iOBJ['label_title'] =iOBJ['label_title'].replace(' [COLOR lime](English Dubbed)[/COLOR]','')
		elif ('English Dubbed' 	in iOBJ['label_title']): iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](English Dubbed)[/COLOR]'
		elif ('Eng Dubbed' 			in iOBJ['label_title']): iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](English Dubbed)[/COLOR]'
		elif ('Dubbed' 					in iOBJ['label_title']): iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](Dubbed)[/COLOR]'
		elif ('English Subbed' 	in iOBJ['label_title']): iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](English Subbed)[/COLOR]'
		elif ('Eng Subbed' 			in iOBJ['label_title']): iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](English Subbed)[/COLOR]'
		elif ('Subbed' 					in iOBJ['label_title']): iOBJ['label_studio']=iOBJ['label_studio']+' [COLOR lime](Subbed)[/COLOR]'
		liz.setInfo( type="Video", infoLabels={ "Title": iOBJ['label_title'], "Studio": iOBJ['label_studio'] } )
		liz.setProperty( "Fanart_Image", iOBJ['image_fanart'] )
		if (debugging==True): print getset('enable-showurl')
		if (getsetbool_('enable-showurl')==True):
			contextMenuItems.append(('[B][COLOR orange]Show[/COLOR][/B] ~  [B]URL[/B]',							'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],0 , urllib.quote_plus(iOBJ['show']), urllib.quote_plus(iOBJ['show']), 0, 'showurl', urllib.quote_plus(iOBJ['url']), iOBJ['image_thumbnail'], iOBJ['image_fanart'])))
		if (getsetbool_('enable-downloading') == True) and (downloadable==True):
			if ('novamov.com' not in iOBJ['url']) and ('videoweed.es' not in iOBJ['url']) and ('dailymotion.com' not in iOBJ['url']):
				contextMenuItems.append(('[B][COLOR purple]Download[/COLOR][/B] ~  [B]File[/B]',				'XBMC.RunPlugin(%s?mode=%s&name=%s&nm=%s&tp=%s&fav=%s&url=%s&scr=%s&fan=%s)' % (sys.argv[0],0 , urllib.quote_plus(iOBJ['show']), urllib.quote_plus(iOBJ['show']), 0, 'download', urllib.quote_plus(iOBJ['url']), iOBJ['image_thumbnail'], iOBJ['image_fanart'])))
		liz.addContextMenuItems(contextMenuItems, replaceItems=True)
		if iOBJ['doSorting']==True:
			xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz) ## is_folder=True
		return ok

### ############################################################################################################
### ############################################################################################################
def getparambool_(idSetting):
	try: o=params[idSetting]
	except: o=None
	if (o==True) or (o=='True') or (o=='true') or (o=='TRUE'): return True
	else: return False

def getparamstr_(idSetting):
	try: o=params[idSetting]
	except: o=None
	if (o==None): return ''
	else: return o

def getparamint_(idSetting):
	try: o=params[idSetting]
	except: o=None
	if (o==None): return 0
	else: return o
### ############################################################################################################

def make_item_fill_it( _name='', _isFolder=False, _mode=0, _type2=0, _category='Unknown', _image_thumbnail=ICON0, _image_fanart=fanart0, _url='', _name2='', _label_title='' ):
	if (_name2==''): _name2=_name
	if (_label_title==''): _label_title=_name
	cio=class_itmOBJ()
	if (_name==''): return cio
	cio['url']=_url
	cio['category']=getparamstr_('cat')+' ::: '+_category
	cio['type2']=_type2
	cio['mode']=_mode
	cio['name']=_name
	cio['name2']=_name2
	cio['label_title']=_label_title
	cio['image_thumbnail']=_image_thumbnail
	cio['image_fanart']=_image_fanart
	cio['isFolder']=_isFolder
	return cio

def make_item( _name='', _isFolder=False, _mode=0, _type2=0, _category='Unknown', _image_thumbnail=ICON0, _image_fanart=fanart0, _url='', _name2='', _label_title='' ):
	cio=make_item_fill_it( _name, _isFolder, _mode, _type2, _category, _image_thumbnail, _image_fanart, _url, _name2, _label_title )
	MyMenu.addDir_MI(cio)
	return cio

def make_item_cmd( _favcmd='', _name='', _isFolder=False, _mode=0, _type2=0, _category='Unknown', _image_thumbnail=ICON0, _image_fanart=fanart0, _url='', _name2='', _label_title='' ):
	cio=make_item_fill_it( _name, _isFolder, _mode, _type2, _category, _image_thumbnail, _image_fanart, _url, _name2, _label_title )
	cio['favcmd']=_favcmd
	MyMenu.addDir_FC(cio)
	return cio

def make_item_show( cio ): # _name='', _isFolder=False, _mode=0, _type2=0, _category='Unknown', _image_thumbnail=ICON0, _image_fanart=fanart0, _url='', _name2='', _label_title='' ):
	#cio=make_item_fill_it( _name, _isFolder, _mode, _type2, _category, _image_thumbnail, _image_fanart, _url, _name2, _label_title )
	#cio['Plot']=_
	#cio['Rating']=_
	#cio['Date_Added']=_
	#cio['Date_Released']=_
	#cio['Genres']=_
	#cio['Themes']=_
	#cio['_image_banner']=_
	#cio['Date_Aired']=_
	#cio['']=_
	#cio['']=_
	#cio['']=_
	#cio['']=_
	#cio['']=_
	cio['isFolder']=True
	Labels={ 'Title':cio['label_title'],'Plot':cio['Plot'],'Year':cio['Year'],'Status':cio['Status'],'Rating':cio['Rating'], 'ShowID':cio['id_show'],'Votes':cio['Votes'],'Type':cio['Type'], 'Fanart':cio['image_fanart'], 'Poster':cio['image_thumbnail'], 'Banner':cio['image_banner'], 'Language':cio['Language'], 'Network':cio['Network'], 'Genre':cio['Genres'] } 
	#
	#
	#
	MyMenu.addDir_CM2(cio,Labels)
	return cio


### ############################################################################################################
### ############################################################################################################

def get_xbmc_os():
	try: xbmc_os = os.environ.get('OS')
	except: xbmc_os = "unknown"
	return xbmc_os
def get_xbmc_version():
	rev_re = re.compile('r(\d+)')
	try: xbmc_version = xbmc.getInfoLabel('System.BuildVersion')
	except: xbmc_version = 'Unknown'
	return xbmc_version
def get_xbmc_revision():
	rev_re = re.compile('r(\d+)')
	try: xbmc_version = xbmc.getInfoLabel('System.BuildVersion')
	except: xbmc_version = 'Unknown'
	try:
		xbmc_rev = int(rev_re.search(xbmc_version).group(1))
		print "addoncompat.py: XBMC Revision: %s" % xbmc_rev
	except:
		print "addoncompat.py: XBMC Revision not available - Version String: %s" % xbmc_version
		xbmc_rev = 0
	return xbmc_rev

def _SaveFile(path, data):
	file = open(path,'w')
	file.write(data)
	file.close()
def _OpenFile(path):
	if os.path.isfile(path): ## File found.
		file = open(path, 'r')
		contents=file.read()
		file.close()
		return contents
	else: return '' ## File not found.
def _CreateDirectory(dir_path):
	dir_path = dir_path.strip()
	if not os.path.exists(dir_path): os.makedirs(dir_path)
def _get_dir(mypath, dirname): #...creates sub-directories if they are not found.
	subpath = os.path.join(mypath, dirname)
	if not os.path.exists(subpath): os.makedirs(subpath)
	return subpath
#def _cleanfilename(name):
#	valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
#	return ''.join(c for c in name if c in valid_chars)
#def _cleanFilename(name):
#	valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
#	return ''.join(c for c in name if c in valid_chars)

def _time2ms(time):
	hour,minute,seconds = time.split(';')[0].split(':')
	frame = int((float(time.split(';')[1])/24)*1000)
	milliseconds = (((int(hour)*60*60)+(int(minute)*60)+int(seconds))*1000)+frame
	return milliseconds
def _convert_time(milliseconds):
	seconds = int(float(milliseconds)/1000)
	milliseconds -= (seconds*1000)
	hours = seconds / 3600
	seconds -= 3600*hours
	minutes = seconds / 60
	seconds -= 60*minutes
	return "%02d:%02d:%02d,%3d" % (hours, minutes, seconds, milliseconds)

def check_url_v(_url):
	rs=0
	try:
		r = requests.head(_url)
		#if (debugging==True): print str(r.status_code)
		rs=r.status_code
	except: t=''
	if (rs==404) or (rs=='') or (rs==None): return False
	elif (rs==200) or (rs==302): return True
	else: return False
### >>> url = 'http://hup.hu'
### >>> r = requests.head(url)
### >>> r.status_code
### 200    # requests.codes.OK
### >>> url = 'http://www.google.com'
### >>> r = requests.head(url)
### >>> r.status_code
### 302    # requests.codes.FOUND
### >>> url = 'http://simile.mit.edu/crowbar/nothing_here.html'
### >>> r = requests.head(url)
### >>> r.status_code
### 404    # requests.codes.NOT_FOUND

def thetvdb_com_episodes3(show_id,season):
	if (debugging==True): print 'thetvdb.com show ID: '+show_id
	link=getURL('http://www.thetvdb.com/?tab=seasonall&id='+show_id)
	print 'thetvdb_com_episodes:  '+'http://www.thetvdb.com/?tab=seasonall&id='+show_id
	itable=(link.split('<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center" id="listtable">')[1]).split('</table>')[0]
	if (season=='') or (season.lower()=='all'):	iresults=re.compile('<tr><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)-(.+?)-(.+?)</td>(.+?)</tr>').findall(itable)
	else:																				iresults=re.compile('<tr><td class=".+?"><a href="(.+?)">(['+season+'][\s][x][\s]\d+)</a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)-(.+?)-(.+?)</td>(.+?)</tr>').findall(itable)
	### <tr><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">1 x 2</a></td><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">The Kidnapping of a Company President's Daughter Case</a></td><td class="even">1996-01-15</td><td class="even"><img src="/images/checkmark.png" width=10 height=10> &nbsp;</td></tr>
	#return iresults
	return sorted(iresults, key=lambda item: item[1], reverse=True)

def thetvdb_com_episodes2(show_id):
	if (debugging==True): print 'thetvdb.com show ID: '+show_id
	link=getURL('http://www.thetvdb.com/?tab=seasonall&id='+show_id)
	print 'thetvdb_com_episodes:  '+'http://www.thetvdb.com/?tab=seasonall&id='+show_id
	itable=(link.split('<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center" id="listtable">')[1]).split('</table>')[0]
	iresults=re.compile('<tr><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)-(.+?)-(.+?)</td>(.+?)</tr>').findall(itable)
	### <tr><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">1 x 2</a></td><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">The Kidnapping of a Company President's Daughter Case</a></td><td class="even">1996-01-15</td><td class="even"><img src="/images/checkmark.png" width=10 height=10> &nbsp;</td></tr>
	return iresults

def thetvdb_com_episodes(show_id):
	if (debugging==True): print 'thetvdb.com show ID: '+show_id
	link=getURL('http://www.thetvdb.com/?tab=seasonall&id='+show_id)
	itable=(link.split('<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center" id="listtable">')[1]).split('</table>')[0]
	iresults=re.compile('<tr><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)-(.+?)-(.+?)</td><td class=".+?">(<img src=".+?" width=10 height=10>)* &nbsp;</td></tr>', re.IGNORECASE | re.DOTALL).findall(itable)
	#iresults=re.compile('<tr><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)-(.+?)-(.+?)</td><td class=".+?"><img src="(.+?)" width=.+? height=.+?>.+?</td></tr>', re.IGNORECASE | re.DOTALL).findall(itable)
	### <tr><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">1 x 2</a></td><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">The Kidnapping of a Company President's Daughter Case</a></td><td class="even">1996-01-15</td><td class="even"><img src="/images/checkmark.png" width=10 height=10> &nbsp;</td></tr>
	#print iresults
	return iresults
	#
	#
	#

def thetvdb_com_episodes1(show_id):
	if (debugging==True): print 'thetvdb.com show ID: '+show_id
	link=getURL('http://www.thetvdb.com/?tab=seasonall&id='+show_id)
	print 'thetvdb_com_episodes:  '+'http://www.thetvdb.com/?tab=seasonall&id='+show_id
	itable=(link.split('<table width="100%" border="0" cellspacing="0" cellpadding="2" align="center" id="listtable">')[1]).split('</table>')[0]
	iresults=re.compile('<tr><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)-(.+?)-(.+?)</td><td class=".+?"><img src="(.+?)" width=.+? height=.+?>.+?</td></tr>').findall(itable)
	### <tr><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">1 x 2</a></td><td class="even"><a href="/?tab=episode&seriesid=72454&seasonid=4166&id=86048&amp;lid=7">The Kidnapping of a Company President's Daughter Case</a></td><td class="even">1996-01-15</td><td class="even"><img src="/images/checkmark.png" width=10 height=10> &nbsp;</td></tr>
	return iresults
	#
	#
	#

def Episode__get_S_Ep_No(episode_title):
	season_number=''; episode_number=''
	if (' Season ' in episode_title): season_number=(re.compile(' Season (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' season ' in episode_title): season_number=(re.compile(' season (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' s ' in episode_title): season_number=(re.compile(' s (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' S ' in episode_title): season_number=(re.compile(' S (\d+) ').findall(episode_title+' ')[0]).strip()
	else: season_number='1'
	if (' Episode ' in episode_title): episode_number=(re.compile(' Episode (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' episode ' in episode_title): episode_number=(re.compile(' episode (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' ep ' in episode_title): episode_number=(re.compile(' ep (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' Ep ' in episode_title): episode_number=(re.compile(' Ep (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' EP ' in episode_title): episode_number=(re.compile(' EP (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' e ' in episode_title): episode_number=(re.compile(' e (\d+) ').findall(episode_title+' ')[0]).strip()
	elif (' E ' in episode_title): episode_number=(re.compile(' E (\d+) ').findall(episode_title+' ')[0]).strip()
	else: episode_number=''
	return (season_number,episode_number)

def Episode__get_thumb(the_url,show_img):
	deb('the_url',the_url)
	if ('/?tab=episode&' in the_url) and ('&seriesid=' in the_url) and ('&id=' in the_url):
		id_series=(re.compile('&seriesid=(\d+)&').findall(the_url+'&')[0]).strip()
		id_episode=(re.compile('&id=(\d+)&').findall(the_url+'&')[0]).strip()
		episode_thumbnail='http://www.thetvdb.com/banners/episodes/'+id_series+'/'+id_episode+'.jpg'
		deb('Episode__get_thumb','| '+id_series+' | '+id_episode+' | '+episode_thumbnail+' |')
	else: 
		episode_thumbnail=show_img; id_series=''; id_episode=''
	return (episode_thumbnail,id_series,id_episode)

def Episode__get_date(thetvdb_episode):
	return (thetvdb_episode[4].strip()+'-'+thetvdb_episode[5].strip()+'-'+thetvdb_episode[6].strip(),thetvdb_episode[4].strip(),thetvdb_episode[5].strip(),thetvdb_episode[6].strip())

def thetvdb_com__show_search(show_name,show_id='none'):
	default_return= None
	#if (show_id=='none'):
	if (debugging==True): print 'thetvdb.com show name: '+show_name
	url_search='http://thetvdb.com/index.php?fieldlocation=2&language=7&genre=&year=&network=&zap2it_id=&tvcom_id=&imdb_id=&order=translation&addedBy=&searching=Search&tab=advancedsearch&seriesname='+urllib.quote_plus(show_name)
	#else:
	#	if (debugging==True): print 'thetvdb.com show id: '+show_id
	#	url_search='http://thetvdb.com/index.php?fieldlocation=2&language=7&genre=&year=&network=&zap2it_id=&tvcom_id=&imdb_id=&order=translation&addedBy=&searching=Search&tab=advancedsearch&seriesname='+urllib.quote_plus(show_name)
	if (debugging==True): print 'thetvdb.com search: '+url_search
	link=getURL(url_search)
	if (link=='none') or (link==''): return default_return
	elif 'No Series found.' in link: return default_return
	else:
		try:
			match=re.compile('<tr><td class=".+?">.+?</td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)</a></td><td class=".+?">(.+?)</td><td class=".+?">(.+?)</td><td class=".+?">.+?</td><td class=".+?">(.+?)</td><td class=".+?">.+?</td></tr>').findall(link)
			return match
		except:
			try:
				match=re.compile('<tr><td class=".+?">.+?</td><td class=".+?"><a href="(.+?)">(.+?)</a></td><td class=".+?">(.+?)</a></td><td class=".+?">(.+?)</td><td class=".+?">(.+?)</td><td class=".+?"></td><td class=".+?">(.+?)</td><td class=".+?">.+?</td></tr>').findall(link)
				return match
			except: return default_return

def thetvdb_com__show_select(show_name,show_id='none',getFirst=False):
	default_return= None
	rMatches=thetvdb_com__show_search(show_name) ### match_showurl,match_name,match_genres,match_status,match_language,match_network,match_rating
	if (rMatches==None): 
		if (debugging==True): print 'thetvdb_com__show_select() >> thetvdb_com__show_search() >> [no resullts found.]'
		if (shoDebugging==True): notification('Searching Shows for MetaData',show_name+': No Shows were found.')
		return default_return
	if (getFirst==True):
		if (option_list==[]):
			if (shoDebugging==True): notification('Searching Shows for MetaData',show_name+': No Results were found.')
			return default_return
		else: return rMatches[0]
	else:
		dialogSelect = xbmcgui.Dialog()
		option_list = []
		for rMatch in rMatches:
			option_list.append(rMatch[1])
		if (option_list==[]):
			if (shoDebugging==True): notification('Searching Shows for MetaData',show_name+': No Results were found.')
			return default_return
		index=dialogSelect.select('Choose', option_list)
		if (debugging==True): print 'choice selected: '+str(index)+'.)  '+option_list[index]
		if (shoDebugging==True): notification('choice selected: ',str(index)+'.)  '+option_list[index])
		return rMatches[index]

def metachange__Show_Name(show_name,show_id='none',getFirst=False):
	rSelected=thetvdb_com__show_select(show_name,show_id,getFirst)
	if (rSelected==None): return
	
def episode__AirDates(show_name,show_id='none',getFirst=False):
	if (show_id=='none'):
		rSelected=thetvdb_com__show_select(show_name,show_id,getFirst)
		if (rSelected==None): 
			if (debugging==True): print 'AirDates >> rSelect==None'
			return
		if ('&id=' in rSelected[0]): 
			show_id=(re.compile('&id=(\d+)&').findall(rSelected[0]+'&')[0]).strip()
			show_name=(rSelected[1]).strip()
		elif (';id=' in rSelected[0]): 
			show_id=(re.compile(';id=(\d+)&').findall(rSelected[0]+'&')[0]).strip()
			show_name=(rSelected[1]).strip()
		else: 
			if (debugging==True): print 'AirDates >> no "&id=" found'
			if (debugging==True): print rSelected[0]
			return
	rEpisodes=thetvdb_com_episodes(show_id) ## 'http://www.thetvdb.com/?tab=seasonall&id='+show_id ##
	if (rEpisodes==[]): 
		if (debugging==True): print 'AirDates >> rEpisodes is empty'
		return
	rEpisodes=sorted(rEpisodes, key=lambda item: item[4]+item[5]+item[6], reverse=True)
	dialogSelect = xbmcgui.Dialog(); option_list = []
	for rMatch in rEpisodes:
		dateColor='tan'
		if (int(rMatch[4].strip()) > int(datetime.date.today().strftime("%Y"))) or (int(rMatch[4].strip())==int(datetime.date.today().strftime("%Y"))):
			if (int(rMatch[5].strip()) > int(datetime.date.today().strftime("%m"))): dateColor='cornflowerblue'
			elif (int(rMatch[5].strip()) > int(datetime.date.today().strftime("%m"))) or (int(rMatch[5].strip())==int(datetime.date.today().strftime("%m"))):
				if (int(rMatch[6].strip())==int(datetime.date.today().strftime("%d"))) and (int(rMatch[5].strip())==int(datetime.date.today().strftime("%m"))) and (int(rMatch[4].strip())==int(datetime.date.today().strftime("%Y"))): dateColor='orange'
				elif (int(rMatch[6].strip())==int(datetime.date.today().strftime("%d"))) or (int(rMatch[6].strip()) > int(datetime.date.today().strftime("%d"))): dateColor='cornflowerblue'
		#datetime.date.today().strftime("%B %d, %Y")
		option_list.append('[COLOR red][B]'+rMatch[1]+'[/B][/COLOR]  [COLOR purple]([COLOR '+dateColor+']'+rMatch[4]+'[/COLOR]-[COLOR '+dateColor+']'+rMatch[5]+'[/COLOR]-[COLOR '+dateColor+']'+rMatch[6]+'[/COLOR])[/COLOR]  [COLOR green][I]'+rMatch[3]+'[/I][/COLOR]')
	if (option_list==[]): 
		if (debugging==True): print 'AirDates >> option_list is empty'
		return ##if (shoDebugging==True): notification('Searching Shows for MetaData',show_name+': No Results were found.')
	index=dialogSelect.select('Episodes:  '+show_name, option_list)
	#
	#

def search_for_airdates(r=''):
	if (r==None) or (r=='') or (r=='none') or (r==False): r=showkeyboard('','Search for Show:')
	else: r=filename_filter_out_year(filename_filter_colorcodes(r))
	if (r==False) or (r==None) or (r==''): return
	rr=episode__AirDates(r)

def askSelection(option_list=[],txtHeader=''):
	if (option_list==[]): 
		if (debugging==True): print 'askSelection() >> option_list is empty'
		return None
	dialogSelect = xbmcgui.Dialog();
	index=dialogSelect.select(txtHeader, option_list)
	#if (index== -1): 
	#	return None
	#if (index==False) or (index==None) or (index=='') or (index== -1): 
	#	if (debugging==True): print 'askSelection() >> problem retreiving selected item'
	#	if (debugging==True): print index
	#	if (debugging==True): print str(index)
	#	return None
	#else: return index
	return index

def tfalse(r,d=False): ## Get True / False
	if   (r.lower()=='true' ): return True
	elif (r.lower()=='false'): return False
	else: return d

## ### This is already in default.py for the plugin.video.solarmovie.so addon / plugin.
##def cFL(t,c='white'): ### For Coloring Text ###
##	return '[COLOR '+c+']'+t+'[/COLOR]'

def iFL(t): ### For Italic Text ###
	return '[I]'+t+'[/I]'
def bFL(t): ### For Bold Text ###
	return '[B]'+t+'[/B]'
def _FL(t,c,e=''): ### For Custom Text Tags ###
	if (e==''): d=''
	else: d=' '+e
	return '['+c.upper()+d+']'+t+'[/'+c.upper()+']'

def WhereAmI(t): ### for Writing Location Data to log file ###
	if (_debugging==True): print 'Where am I:  '+t
def deb(s,t): ### for Writing Debug Data to log file ###
	if (_debugging==True): print s+':  '+t
def debob(t): ### for Writing Debug Object to log file ###
	if (_debugging==True): print t

def nolines(t):
	it=t.splitlines()
	t=''
	for L in it:
		t=t+L
	t=((t.replace("\r","")).replace("\n",""))
	return t

def checkImgUrl(img):
	img=xbmc.translatePath(img)#; deb('Local Image',img)
	if (check_ifUrl_isHTML(img)==True): return img
	else: return ''
def checkImgLocal(img):
	img=xbmc.translatePath(img)#; deb('Local Image',img)
	if (os.path.isfile(img)): return img
	else: return ''

### ############################################################################################################
### ############################################################################################################


def Library_SaveTo_Movies(url,iconimage,name,year):
  library=xbmc.translatePath(_addon.get_profile())
  foldername=xbmc.translatePath(os.path.join(library, 'Movies'))
  if os.path.exists(foldername)==False: os.mkdir(os.path.join(library, 'Movies'))
  strm='%s?mode=%s&section=%s&url=%s&iconimage=%s&title=%s&showtitle=%s&year=%s&showyear=%s'% (sys.argv[0],'PlayLibrary',ps('section.movie'),urllib.quote_plus(url),urllib.quote_plus(iconimage),urllib.quote_plus(name),urllib.quote_plus(name),year,year)
  filename=name+'  ('+year+')'
  filename=clean_filename(filename+'.strm')
  file    =xbmc.translatePath(os.path.join(foldername,filename))
  ##print file
  a=open(file, "w"); a.write(strm); a.close()
  myNote('Library Movie:',filename)

def Library_SaveTo_Episode(url,iconimage,name,year,country,season_number,episode_number,episode_title):
  library=xbmc.translatePath(_addon.get_profile())
  foldermain=xbmc.translatePath(os.path.join(library, 'TV'))
  if os.path.exists(foldermain)==False: os.mkdir(foldermain)
  foldername=xbmc.translatePath(os.path.join(foldermain,name+'  ('+year+')'))
  if os.path.exists(foldername)==False: os.mkdir(foldername)
  folderseason=xbmc.translatePath(os.path.join(foldername, 'Season '+season_number))
  if os.path.exists(folderseason)==False: os.mkdir(folderseason)
  strm='%s?mode=%s&section=%s&url=%s&iconimage=%s&title=%s&showtitle=%s&year=%s&showyear=%s&country=%s&season=%s&episode=%s&episodetitle=%s'% (sys.argv[0],'PlayLibrary',ps('section.tv'),urllib.quote_plus(url),urllib.quote_plus(iconimage),urllib.quote_plus(name),urllib.quote_plus(name),year,year,country,season_number,episode_number,episode_title)
  #
  #
  filename=name+'  ('+year+')  S'+season_number+'E'+episode_number
  filename=clean_filename(filename+'.strm')
  file    =xbmc.translatePath(os.path.join(folderseason,filename))
  ##print file
  a=open(file, "w"); a.write(strm); a.close()
  myNote('Library TV:',filename)


def myNote( header='',msg='',delay=5000,image='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/US_99_%281961%29.svg/40px-US_99_%281961%29.svg.png'):
	header=cFL(header,ps('cFL_color')); msg=cFL(msg,ps('cFL_color2'))
	_addon.show_small_popup(title=header,msg=msg,delay=delay,image=image)

### ############################################################################################################
### ############################################################################################################

def twitter_timeline(person):
	HTML=getURL('http://mobile.twitter.com/'+person) ### HTML=getURL('http://twitter.com/'+person)
	#
	#





### ############################################################################################################
### ############################################################################################################






### ############################################################################################################
### ############################################################################################################



### ############################################################################################################
### ############################################################################################################



### ############################################################################################################
### ############################################################################################################



### ############################################################################################################
### ############################################################################################################
### ############################################################################################################



### ############################################################################################################



### ############################################################################################################



### ############################################################################################################









### ############################################################################################################
### ############################################################################################################

MyMenu=class_MyMenu()
#notification('Current Site',mainSite)
### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
