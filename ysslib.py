import string, urllib2
from itertools import product

def fetch_symbols(candidates, request_size=200, verbose=False):
   candidates_len = len(candidates)
   symbols = []
   properties = 'sn'
   requests = xrange(0, candidates_len, request_size)
   requests_len = len(requests)
   i = 1
   for r in requests:
      group = candidates[ r : r + request_size ]
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
      if verbose:
         print 'Done (%d/%d, %f%%)' % ( i, requests_len,
               float( i ) / float( requests_len ) * float( 100 ) )
      i += 1
   return symbols

def get_candidate_symbols(length=8, verbose=False):
   candidates = []
   for n in range(1, length + 1):
      if verbose:
         print 'Computing candidates of length', n
      candidates += [''.join(c) for c in product(string.ascii_uppercase, repeat=n)]
   return candidates

def get_symbols(candidates=None, length=8, verbose=False):
   if not candidates:
      candidates = get_candidate_symbols( length=length, verbose=verbose )
   return fetch_symbols(candidates, verbose=verbose)
