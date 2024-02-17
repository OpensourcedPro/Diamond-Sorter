import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinterpages.photomanagement import photomanage
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from threading import Thread
from time import sleep

class LabeledEntry(tk.LabelFrame):
	def __init__(self,parent, lbltext,imglocation='', *args, **kwargs):
		tk.LabelFrame.__init__(self,parent, *args, **kwargs)
		self.config(text=lbltext,bd=0)
		self.font=('verdana',12)
		self.entryVar=tk.StringVar()
		self.entry = tk.Entry(self,textvariable=self.entryVar,borderwidth=1,font=self.font,highlightthickness=1,relief='flat',width=18)
		self.entry.pack(fill='both',side='right')


class LabeledEntryInt(tk.LabelFrame):
	def __init__(self,parent, lbltext):
		tk.LabelFrame.__init__(self,parent)
		self.configure(bd=0,text=lbltext)
		self.font=('Arial',11)
		self.entryVar=tk.IntVar()
		self.entryVar.set(self.place)
		self.entry = tk.Entry(self,borderwidth=2,font=self.font,highlightthickness=1,relief='flat',width=18,fg='#666')
		self.entry.pack(fill='both',side='right',padx=3)
		self.entry.configure(textvariable=self.entryVar)


class ImageLabel(tk.LabelFrame):
	def __init__(self,parent,lbltxt, *args,**kwargs):
		tk.LabelFrame.__init__(self, parent, *args,**kwargs)
		self['text']=lbltxt
		#icons
		self.pth=r'media/icons/du_swipe_dragger_monkey.png'
		self.cam = tk.PhotoImage(file=r'media/icons/capture .png')
		self.fle = tk.PhotoImage(file=r'media/icons/folder.png')
		self.ph=tk.PhotoImage(file=self.pth)
		#labels
		self.imglbl=tk.Label(self,image=self.ph,height=143,width=146)
		self.imglbl.pack()
		self.btnbl=tk.Label(self)
		self.btnbl.pack(side='bottom',fill='x')
		kw={"relief":'flat','overrelief':'raised','compound':'left','justify':'left'}
		tk.Button(self.btnbl,image=self.cam,text='Camera',command=lambda c=0:self.a(c,self.imglbl),**kw).pack(side='left')
		tk.Button(self.btnbl,image=self.fle,text='   Files   ',command=lambda c=1:self.a(c,self.imglbl),**kw).pack()
	def a(self,c,lbl):
		if c==0: newfp=photomanage.PhotoManage.TakePhoto(lbl)
		else:
			newfp=photomanage.PhotoManage.choosePhoto(lbl)
			if newfp=='': newfp=self.pth
		self.pth=newfp
		return newfp


def WindowAlert(message,details,mtype='info',title='info'):
	if mtype=="yesno": return messagebox.askyesno(title=title, message=message, detail=details)
	if mtype=='info':  return messagebox.showinfo(title=title, message=message, detail=details)


class cbb(tk.LabelFrame):
	"""  dropdown button """
	def __init__(self,parent, lbltext,vllist,errmsg=False, *args,**kwargs):
		tk.LabelFrame.__init__(self,parent, *args,**kwargs)
		self.configure(bd=0,text=lbltext)
		self.font=('Arial',11)
		self.entryVar=tk.StringVar()
		self.entry = Combobox(self,width=15,textvariable=self.entryVar,values=vllist,state='readonly',font=self.font)
		self.entry.pack(fill='both',side='top',padx=3)
		if not errmsg==False:
			self.errormessage=tk.Label(self,fg='red',font=('',8))
			self.errormessage.pack(side='bottom',fill='x',expand=1)
	

class LabeledCheck(tk.LabelFrame):
	def __init__(self,parent, lbltext,command=None,*args, **kwargs):
		tk.LabelFrame.__init__(self,parent,*args, **kwargs)
		self['text']=lbltext
		self['bd']=0
		self.font=('Arial',11)
		self.entryVar=tk.IntVar()
		self.entryVar.set(0)
		self.entry = tk.Checkbutton(self,text='No  ',variable=self.entryVar,font=self.font,*args, **kwargs)
		self.entry.pack(fill='both',side='right',padx=3)
		
		if command==None:self.entry['command']=self.check
		else:self.entry['command']=command
	def check(self):
		if self.entryVar.get()==0:self.entry['text']='No  '
		else:self.entry['text']='Yes'


class Dateentry(tk.LabelFrame):
	""" Calendar to choose date """
	def __init__(self,parent, lbltext, *args, **kwargs):
		tk.LabelFrame.__init__(self,parent, *args, **kwargs)
		self['text']=lbltext
		self['bd']=0
		self.font=('Arial',11)
		self.entryVar=tk.StringVar()
		self.entry = DateEntry(self,width=15,textvariable=self.entryVar,font=self.font)
		self.entry.pack(fill='both',side='right',padx=3)


class LabeledEntryErrorDisplay(tk.LabelFrame):
	""" just like labeledEntry but having a bottom label to display any alert or messages """
	def __init__(self,parent, lbltext,imglocation='',*args, **kwargs):
		tk.LabelFrame.__init__(self,parent,*args, **kwargs)
		self.configure(text=lbltext,bd=0)
		
		self.entryVar=tk.StringVar()
		self.imglbl=tk.Label(self, **kwargs)

		self.entry = tk.Entry(self,textvariable=self.entryVar,borderwidth=1,font=('Arial',11),highlightthickness=0,relief='flat',width=18,**kwargs)
		self.errormessage=tk.Label(self,fg='red',bd=0,font=('',8), anchor='nw',**kwargs)
		
		self.lining = tk.Frame(self,bg='red',relief='raised')
		#packing
		if imglocation!='':
			self.im=tk.PhotoImage(file=imglocation)
			self.imglbl['image']=self.im
			self.imglbl.image=self.im

		self.errormessage.pack(side='bottom',fill='x')
		self.lining.pack(side='bottom',fill='x')
		self.imglbl.pack(anchor='nw',side='left',fill='y')
		self.entry.pack(anchor='nw',fill='both',expand=1)
		self.entry.bind('<FocusIn>',self.Focusin)
	def Focusin(self,event):self.errormessage['text']=''

class ToggledFrame(tk.Frame):
	"""  param : parent , text(top display on button), side='bottom'(bydefault)
	 	side can be top  or bottom to set the poso=ition of subframe
	  """
	def __init__(self, parent,text,*args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.p=parent
		self.show=0
		self.arup= tk.PhotoImage(file=r'media/icons/arrow_up.png')
		self.ardown= tk.PhotoImage(file=r'media/icons/arrow_down.png')
		self.showbtn=tk.Button(self,text=text+'\t',anchor='nw',command=self.set_sub_frame,
						relief='flat',bd=0,bg='#777',fg='white',image=self.ardown,font=('verdana',12),compound='right')
		#hiiden Frame
		self.sub_frame = tk.Frame(self, bd=2,relief='ridge')
		ok_btn = tk.Button(self.sub_frame,anchor='e',relief='flat',bd=0,
			bg='#fffcccbbb',justify='center',text='Close',command=self.set_sub_frame)
		#packings
		self.showbtn.pack(side='top',anchor='nw',fill='both')
		ok_btn.pack(side='bottom',fill='x')
		# self.sub_frame.bind('<Leave>',self.set_sub_frame)
	def set_sub_frame(self,event=None):
		if self.show==0:
			self.sub_frame.pack(side='bottom',anchor='nw')
			self.showbtn['image']=self.arup
			self.show=1
		elif self.show==1:
			self.sub_frame.pack_forget()
			self.showbtn['image']=self.ardown
			self.show=0


class alert_CloseLabel(tk.Frame):
	""" display alert with close button """
	def __init__(self,parent,text ,*args,**kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		tk.Label(self,text=text,fg='red',relief='flat',justify="left",bd=0,
			anchor="center", font=("",10) ,**kwargs).pack(anchor='nw',side='left',fill='both')
		
		tk.Button(self,text='x',fg='white',bg='red',activebackground='#1ff',relief='flat',justify="left",bd=0,
			anchor="center", font=("",10) ,command=self.destroy).pack()



class PopUpMidContaierFrame(tk.Frame):
	"""  param : parent , text(top display on button), side='bottom'(bydefault)
	 	side can be top  or bottom to set the poso=ition of subframe"""

	def __init__(self, parent,text,pos,*args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.p=parent
		self.show=0
		self.pos=pos
		self.prevColor = "white"

		self.close= tk.PhotoImage(file=r'media/icons/c1.png')
		self.nxt= tk.PhotoImage(file=r'media/icons/next.png')

		self.showbtn=tk.Button(self,text=text+'\t',anchor='nw',command=self.set_sub_frame,
						relief='flat',bd=0,bg='#5ff',image=self.nxt,font=('verdana',12),compound='right')
		#hiiden Frame
		self.sub_frame = tk.Frame(self.p.master, bd=0)
		ok_btn = tk.Button(self.sub_frame,relief='flat',bd=0,bg='#fffcccbbb',image=self.close,
			command=self.set_sub_frame,height=20,width=20)
		#packings
		self.showbtn.pack(side='top',anchor='nw',fill='both')
		ok_btn.pack(side='top',anchor='e')
		# self.sub_frame.bind('<Leave>',self.set_sub_frame)
	def set_sub_frame(self,event=None):
		if self.show==0:	
			self.sub_frame.place(x=self.pos[0],y=self.pos[1])
			self.prevColor = self.showbtn['bg']
			self.showbtn['bg']='#8ff'
			self.show=1
		elif self.show==1:
			self.showbtn['bg']=self.prevColor
			self.sub_frame.place_forget()
			self.show=0


class ExtendedButtonFrame(tk.Frame):
	""" Button having icon being displayed and
	   shows text as mouse goest on it   """
	def __init__(self, parent,text,command,imglcn,*args, **kwargs):
		tk.Button.__init__(self, parent,*args, **kwargs)
		self.imglcn=imglcn

		self.configure(bd=0,overrelief='raised')
		self.btn = tk.Button(self,command=command,bd=0,text=text,*args, **kwargs)
		self.btn.pack(side='left',fill='y')
		self.set_image(self.imglcn)
		self.btn.bind("<Enter>",self.change_image_on_hover)
		self.btn.bind("<Leave>",self.return_to_prev_image)
	def set_image(self,lcn):
		self.img=tk.PhotoImage(file=lcn)
		self.btn['image']=self.img
	def change_image_on_hover(self,event):
		self.btn['bg']='#555'
	def return_to_prev_image(self,image):
		self.btn['bg']='#777'


class LabeledTexrArea(tk.LabelFrame):
	def __init__(self,parent,lbltext, *args, **kwargs):
		tk.LabelFrame.__init__(self,parent, *args, **kwargs)
		self.config(bd=0,text=lbltext)

		sb=tk.Scrollbar(self,orient='vertical',bg='red')
		text_area=tk.Text(self,height=3,width=20,yscrollcommand=sb.set)
		text_area.pack(side='left',fill='both',anchor='nw')
		sb.pack(side='right',fill='y',anchor='nw')
		sb['command']=text_area.yview


class PopUpMidContaierFrameWithImage(tk.Frame):
	"""  param : parent , text(top display on button), side='bottom'(bydefault)
	 	side can be top  or bottom to set the poso=ition of subframe
	  """
	def __init__(self, parent,text,pos,imglcn,*args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.p=parent
		self.show=0
		self.pos=pos
		self.usr= tk.PhotoImage(file=imglcn)
		self.close= tk.PhotoImage(file=r'media/icons/c1.png')

		#default bg
		self.button_bg=None

		self.showbtn=tk.Button(self,text=text,command=self.set_sub_frame,
						relief='flat',bd=0,image=self.usr,font=('verdana',12),compound='top',**kwargs)
		#hiiden Frame
		self.sub_frame = tk.Frame(self.p.master, bd=0)
		
		ok_btn = tk.Button(self.sub_frame,relief='flat',bd=0,bg='#fffcccbbb',image=self.close,
			command=self.set_sub_frame,height=20,width=20)
		#packings
		self.showbtn.pack(side='top',anchor='nw',fill='both')
		ok_btn.pack(side='top',anchor='e')
		# self.sub_frame.bind('<Leave>',self.set_sub_frame)
	def set_sub_frame(self,event=None):
		if self.show==0:	
			self.sub_frame.place(x=self.pos[0],y=self.pos[1])
			self.bg=self.showbtn['bg']
			self.showbtn['bg']='light green'
			self.show=1
		elif self.show==1:
			self.sub_frame.place_forget()
			self.showbtn['bg']=self.bg
			self.show=0


class DBLabeledEntry(LabeledEntry):
	def __init__(self,parent, lbltext,dbinfo,imglcn='',*args, **kwargs):
		LabeledEntry.__init__(self,parent,lbltext,imglcn,*args, **kwargs)

		self.dbinfo=dbinfo
		self.entryVar.trace("w",lambda a,b,c:self.set_buttons())
		self.btnF=tk.Frame(parent.master)
		#images
		self.tick = tk.PhotoImage(file="media/icons/tick.png")
		self.ccl = tk.PhotoImage(file="media/icons/cancel.png")

		tk.Button(self.btnF,image=self.tick,command=self.update).pack(side='left')
		self.cnclbtn = tk.Button(self.btnF,image=self.ccl,command=lambda :self.btnF.place_forget())
		self.cnclbtn.pack()
	def set_buttons(self):
		self.btnF.place(x=self.winfo_x()+185,y=self.winfo_y()+17)
	def update(self):
		from databases.my_sql import dbsys
		# {dbname:'',tablename:'',fieldname:'',uid:''}
		qry = """ UPDATE %s SET %s = ? WHERE St_RegistrationId = ? """%( self.dbinfo['tablename'], self.dbinfo['fieldname'])
		db  = dbsys.DBrowser(self.dbinfo['dbname'])
		db.action(qry,(self.entryVar.get().strip(), self.dbinfo['uid'] ),'updt')
		self.btnF.place_forget()



class DBDateentry(Dateentry):
	def __init__(self,parent, lbltext,dbinfo,*args, **kwargs):
		Dateentry.__init__(self,parent,lbltext,*args, **kwargs)

		self.dbinfo=dbinfo
		self.entryVar.trace("w",lambda a,b,c:self.set_buttons())
		self.btnF=tk.Frame(parent.master)
		#images
		self.tick = tk.PhotoImage(file="media/icons/tick.png")
		self.ccl = tk.PhotoImage(file="media/icons/cancel.png")
		tk.Button(self.btnF,image=self.tick,command=self.update).pack(side='left')
		self.cnclbtn = tk.Button(self.btnF,image=self.ccl,command=lambda :self.btnF.place_forget())
		self.cnclbtn.pack()
	def set_buttons(self):
		self.btnF.place(x=self.winfo_x()+185,y=self.winfo_y()+17)
	def update(self):
		from databases.my_sql import dbsys
		# {dbname:'',tablename:'',fieldname:'',uid:''}
		qry = """ UPDATE %s SET %s = ? WHERE St_RegistrationId = ? """%( self.dbinfo['tablename'], self.dbinfo['fieldname'])
		db  = dbsys.DBrowser(self.dbinfo['dbname'])
		db.action(qry,(self.entryVar.get().strip(), self.dbinfo['uid'] ),'updt')
		self.btnF.place_forget()


class ElskerButton( tk.Frame ):
	""" 
	A Button class created by Button and Frame widget.
	
	parent   >>  root, 
	label    >>  text (to be displayed on the button),
	file     >>  gif (A gif file path),
	command  >>  command (command for button default None)
	duration >>  ( default=0.0299 ,sleep time in changing a simple frame), *args, **kwargs.
	"""

	def __init__(self,parent, text, gif ,command=None,infinite=True, duration=0,*args,**kwargs):
		tk.Frame.__init__(self, parent)
		self.gif_fp = gif
		self.duration = duration
		self.infinite = infinite
		
		self.new_frame = Image.open(self.gif_fp)
		self.no_of_frames = self.new_frame.n_frames

		self.ll = tk.Button(self,text=text,compound='left', command=command, *args, **kwargs)
		self.ll.pack(anchor='nw', fill='both')

		self.bind("<Enter>", self.__hover_in)
		self.bind("<Leave>", self.__hover_out)
		self.__default_image()
		
	def __hover_in(self, event):
		self.animate_thread =  Thread(target=self.__animate)
		self.animate_thread.start()

	def __default_image(self):
		self.img = ImageTk.PhotoImage(file=self.gif_fp)
		self.ll['image']=self.img
		self.ll.image = self.img

	def __animate(self):
		#lets display the gif !
		j = 0
		while j <= self.no_of_frames:

			if j >= self.no_of_frames:
				if self.infinite:
					j = 0 #run infinitly
				else:
					break
			elif not self.animate_thread.isAlive(): break  #closes as button loses focus!
			else:
				try:
					self.i = ImageTk.PhotoImage(self.new_frame)
					self.new_frame.seek(j)
					
					self.ll['image']= self.i
					self.ll.image = self.i
					# #UPDATE IDLE TASKS TO overcome not responding and update window each moment
					self.update()
					self.update_idletasks()
					# wait for a few secs to make it look good!
					sleep(self.duration)
					j += 1
				except:
					self.__hover_out(None)
		self.__default_image()

	def __hover_out(self, e):
		print("hover out")
		if self.animate_thread.isAlive():
			self.animate_thread._tstate_lock.release()
			self.animate_thread._stop()
