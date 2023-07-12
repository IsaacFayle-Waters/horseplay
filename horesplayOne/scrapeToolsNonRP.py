#for use in scraping odds from https://www.horseracing.net
def getBookieString(h_name,bookie):
  return '[data-runner="' + str(h_name) + '"]'+ ' [data-bookmaker="'+ bookie +'"] div::text'