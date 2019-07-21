#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate

tst_xml = r'''<?xml version="1.0"?>
<ol>
    <li>
		<a href="/python">Python</a>
	</li>
	<li>
		<a href="/ruby">Ruby</a>
	</li>
	<S>
		<J>Java</J>
	</S>
</ol>
'''

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)));
	
	def end_element(self, name):
		print('sax:end_element: %s' % name);

	def char_data(self, text):
		print('sax:char_data: %s' % text);


def main():
	handler = DefaultSaxHandler();
	parser = ParserCreate();
	parser.StartElementHandler = handler.start_element;
	parser.EndElementHandler = handler.end_element;
	parser.CharacterDataHandler = handler.char_data;
	parser.Parse(tst_xml);

if __name__ == '__main__':
	main();
