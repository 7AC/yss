import string, urllib2
from itertools import product

def fetch_symbols(candidates, request_size=200, verbose=False):
   groups = [candidates[x:x+request_size] for x in xrange(0, len(candidates),
                                                          request_size)]
   symbols = []
   properties = 'sn'
   for group in groups:
      url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % ( '+'.join(group),
                                                                  properties )
      if verbose:
         print 'Fetching:', url
      data = urllib2.urlopen(url).read()
      results = data.strip().split('\r\n')
      for line in results:
         line = line.replace('"', '').split(',', 1)
         if len(line) == 2 and line[1] and line[0] != line[1]:
            if verbose:
               print line
            symbols.append(line)
   return symbols

def get_symbols(length=8, verbose=False):
   candidates = []
   for n in range(1, length + 1):
      candidates += [''.join(c) for c in product(string.ascii_uppercase, repeat=n)]
   return fetch_symbols(candidates, verbose=verbose)
