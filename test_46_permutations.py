import code_46_permutations as c

def test_example_1():
    s = c.Solution()
    assert sorted(s.permute([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])