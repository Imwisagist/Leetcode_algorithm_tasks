# https://leetcode.com/problems/flatten-nested-list-iterator/


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._res = []
        self._index = 0

        def dfs(li, nums):
            for el in li:
                if el.isInteger(): nums.append(el.getInteger())
                else: dfs(el.getList(), nums)

        dfs(nestedList, self._res)

    def next(self):
        val = self._res[self._index]; self._index += 1

        return val

    def hasNext(self):
        return self._index < len(self._res)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())