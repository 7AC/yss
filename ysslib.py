import string, sys, urllib2
from itertools import product

def get_data(url):
   try:
      v = urllib2.urlopen(url).read()
   except Exception: # pylint: disable=W0703
      return ''
   try:
      v = v.strip()
   except Exception: # pylint: disable=W0703
      return ''
   return v

def get_group(a200):
   s = '+'.join(a200)
   f = 'sn'
   url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (s, f)
   v = get_data(url)
   a = v.split("\r\n")
   group = []
   for s in a:
      if s.find('N/A') == -1:
         aa = s.replace('"', '').split(',', 1)
         try:
            if aa[1] and aa[0] != aa[1]:
               group.append(aa)
         except Exception: # pylint: disable=W0703
            continue
   return group

def _get_symbols(a1, verbose):
   i = 0
   j = 0
   a200 = []
   symbols = []
   for e in a1:
      try:
         a200.append(e)
      except Exception: # pylint: disable=W0703
         break
      i += 1
      if i == 200:
         j += 1
         if verbose:
            print j,
            sys.stdout.flush()
         symbols += get_group(a200)
         a200 = []
         i = 0
   symbols += get_group(a200)
   if verbose:
      print "\n%d" % len(symbols)
      sys.stdout.flush()
   return symbols

uppercase_a = ord('A')
ascii_uppercase_len = len(string.ascii_uppercase)
def get_symbols(length=5, verbose=False, get_names=False):
   a1 = []
   for n in range(1, length + 1):
      for chars in product(range(uppercase_a, uppercase_a + ascii_uppercase_len),
                           repeat=n):
         a1.append( ''.join(chr(c) for c in chars))
   return _get_symbols(a1, verbose)
