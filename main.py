from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import builder
from kivymd.uix.textfield import MDTextFieldRect
from kivy.uix.textinput import TextInput
import math
from kivymd.toast import toast
from kivy.factory import Factory


class mycalc(FloatLayout):
	
	def squ(self):
		value = int(self.textfield.text)
		
		print(pow(value, 1/2))
		sol = str(pow(value, 1/2))
		
		def clean(self):
			self.textfield.text = ''
		
		clean(self)
	
	
		self.textfield.insert_text(sol)
	
	def c(self):
		self.textfield.text = ''
		

	def delete(self):
		self.textfield.do_backspace(from_undo=False, mode='bkspc')
		
	
	def evaluate(self):
		val = str(self.textfield.text)
		
		solution = str(eval(val))
		
		def cln(self):
			self.textfield.text = ''
			
		cln(self)
		
		self.textfield.insert_text(solution)
		
	
	
	
	
	def toast1(self):
		toast("1")
	
	def toast2(self):
		toast("2")
	
	def toast3(self):
		toast("3")
	
	def toast4(self):
		toast("4")
	
	def toast5(self):
		toast("5")
	
	def toast6(self):
		toast("6")
	
	def toast7(self):
		toast("7")
	
	def toast8(self):
		toast("8")
	
	def toast9(self):
		toast("9")
	
	def toast0(self):
		toast("0")
	
	def toast_bkspce(self):
		toast("<<<<<<")
	
	def toast_dot(self):
		toast(".")
	
	def toast_c(self):
		toast("Clear")
	
	def toast_eval(self):
		toast("Evaluate")
	
#	def new(self):
	#	self.ids['1'].background_color = 0, 0, 1, 1
		
class my(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Blue"
#		self.toast1 = Factory.toast(duration=0.5)

		
		return mycalc()
		

if __name__=="__main__":
	my().run()
