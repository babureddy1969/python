def avg(marks):
    # assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)
def test_avg():
    mark2 = [55,88,78,90,79]
    assert avg(mark2) == 78.0
