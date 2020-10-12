import link_extractor
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
link_extractor.all_links_extractor('https://infallible-varahamihira-e94f86.netlify.app', 10)
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())