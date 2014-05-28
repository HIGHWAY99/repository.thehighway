### import splash_highway as splash
### splash.do_My_Splash('http://xbmchub.com/images/index-logo.png',10); 
### 
import xbmc,xbmcgui,time

class MyWindowCountDown(xbmcgui.WindowDialog):
	scr={}; #scr['L']=0; scr['T']=0; scr['W']=1280; scr['H']=720; 
	def __init__(self,bgArt='',L=0,T=0,W=1280,H=720):
		self.background=bgArt; self.scr['L']=L; self.scr['T']=T; self.scr['W']=W; self.scr['H']=H; 
		self.BG=xbmcgui.ControlImage(self.scr['L'],self.scr['T'],self.scr['W'],self.scr['H'],self.background,aspectRatio=0); 
		self.addControl(self.BG); 
		#t='0'; self.BG.setAnimations([('WindowOpen','effect=fade time='+t+' start=0 end=100'),('WindowClose','effect=fade time='+t+' end=0')])
		#self.close()
	def see(self): self.show(); 
	def updateBG(self,bgArt=''): self.background=bgArt; self.setImage(self.background); 
	def updateY(self,x,y): self.BG.setPosition(x,y); self.scr['L']=x; self.scr['T']=y; 
	def updateSize(self,w,h): self.BG.setWidth(w); self.BG.setHeight(h); self.scr['W']=w; self.scr['H']=h; 
	def updateW(self,w): self.BG.setWidth(w); self.scr['W']=w; 
	def updateH(self,h): self.BG.setHeight(h); self.scr['H']=h; 
	#def onInit(self): 
	#def onClick(self,control): 
	#def onControl(self,control): 
	#def onFocus(self,control): 
	#def onAction(self,action): 

def do_My_Splash(img='http://xbmchub.com/images/index-logo.png',HowLong=10,resize=False,L=0,T=0,W=1280,H=720): #HowLong in seconds.
	if resize==False: maxW=1280; maxH=720; W=maxW/2; H=maxH/2; L=maxW/4; T=maxH/4; 
	TempWindow2=MyWindowCountDown(bgArt=img,L=L,T=T,W=W,H=H); 
	StartTime=time.clock(); 
	while (time.clock()-StartTime) < HowLong:
		TempWindow2.show(); 
	try: del self.TempWindow2; 
	except: pass
	##
