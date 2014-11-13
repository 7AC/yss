#!/usr/bin/env python

import ysslib
import getopt, sys, time

# pylint: disable=W0312,C0301,W0311,W0622

def help():
	print 'to retrieve all 1-character symbols:'
	print '\tpython get_yahoo_stock_symbols.py -v -c 1'
	print '\tyahoo_stock_symbols_1.txt = symbols, yahoo_stock_symbols_1.csv = symbols w/names'
	print 'to retrieve all 1 and 2-character symbols:'
	print '\tpython get_yahoo_stock_symbols.py -v -c 2'
	print '\tyahoo_stock_symbols_2.txt = symbols, yahoo_stock_symbols_2.csv = symbols w/names'
	print
	print '(likewise for 3 and 4)'
	print
	print 'to retrieve all 1, 2, 3, 4, and 5-character symbols (takes 2 hours w/broadband):'
	print '\tpython get_yahoo_stock_symbols.py -v -c 5'
	print '\tyahoo_stock_symbols_5.txt = symbols, yahoo_stock_symbols_5.csv = symbols w/names'
	print

def usage():
	print 'usage: python get_yahoo_stock_symbols.py "vhc:", ["help", "characters="]'

def main():
	try:
		opts, _ = getopt.getopt(sys.argv[1:], "vhc:", ["help", "characters="])
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit(2)
	verbose = False
	characters = None
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-h", "--help"):
			help()
			sys.exit()
		elif o in ("-c", "--characters"):
			characters = a
		else:
			assert False, "unhandled option"
	if verbose:
		print time.strftime("%m/%d/%Y %I:%M"),
		sys.stdout.flush()
	if characters == None:
		help()
		sys.exit()
        atotal = ysslib.get_symbols(length=int(characters), verbose=verbose,
                                    get_names=True)
	csv = 'yahoo_stock_symbols_%s.csv' % characters
	txt = 'yahoo_stock_symbols_%s.txt' % characters
	fcsv = open(csv, 'w')
	ftxt = open(txt, 'w')
	for s in atotal:
		fcsv.write(','.join(s)+'\n')
		sym = s[0]
		ftxt.write(sym+'\n')
	fcsv.close()
	ftxt.close()
	if verbose:
		print time.strftime("%m/%d/%Y %I:%M")
		sys.stdout.flush()

if __name__ == "__main__":
	main()

