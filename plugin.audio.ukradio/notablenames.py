### ############################################################################################################
###	#	
### # Project: 			#		Notable Names - by The Highway 2013.
### # Author: 			#		The Highway
### # Version:			#		v0.0.1
### # Description: 	#		For a quick and easy file that can be traded out when updates are needed.
###	#	Import:				#		from notablenames import *
###	#	
### ############################################################################################################
### ############################################################################################################
##### Imports #####
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import urllib,urllib2,re,os,sys,htmllib,string,StringIO,logging,random,array,time,datetime
##### /\ ##### Imports #####
##### Functions #####
sc='*'
sp=' '
def SC_(s,n,c=False,t=True):
	if (c==t): return c
	if (n[0:len(s)]==s): c=True
	return c

def StarCheck(n,c=False,t=True):
	if (n=='') or (n==None): return n
	n=StarCheck_parse(n,c,t)
	n=StarCheck_rtmp(n,c,t)
	return n

def StarCheck_parse(n,c=False,t=True):		### unhandled links that havent had parsing setup for them.
	c=SC_('BBC ',n,c)
	if (c==t): n=sc+sp+n
	return n

def StarCheck_rtmp(n,c=False,t=True):			### unhandled links that use rtmp audio streams that don't seem to be handled by xbmc player(s).
	if (SC_('*',n,c)==t): return n
	c=SC_('Viking ',n,c)
	c=SC_('West Sound',n,c)
	c=SC_('Kiss 100',n,c)
	c=SC_('Magic ',n,c)
	if (c==t): n=sc+sc+sp+n
	return n


##### /\ ##### Functions #####
### ############################################################################################################
### ############################################################################################################
