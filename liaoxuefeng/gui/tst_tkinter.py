#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master);
		self.pack();
		self.createWidgets();

	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello Python Tkinter');
		self.helloLabel.pack();
		self.guitButton = Button(self, text='Quit', command=self.quit);
		self.guitButton.pack();

class Application2(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master);
		self.pack();
		self.createWidgets();

	def createWidgets(self):
		self.nameInput = Entry(self);
		self.nameInput.pack();
		self.alterButton = Button(self, text='Hello', command=self.hello);
		self.alterButton.pack();
	
	def hello(self):
		name = self.nameInput.get() or 'World';
		messagebox.showinfo('Message', 'Hello, %s' %name);

def main():
	#app = Application();
	app = Application2();
	app.master.title('Hello');
	app.mainloop();

if __name__ == '__main__':
	main();
