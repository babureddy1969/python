def avg(marks):
    # assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)
def test_avg():
    mark2 = [55,88,78,90,79]
    assert avg(mark2) == 78.0
mark2 = [55,88,78,90,79]
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
avg(mark2)
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())