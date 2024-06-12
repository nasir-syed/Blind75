def check(numCourses, prerequisites):
    preMap = {i: [] for i in range(numCourses)}

    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # VisitSet = all courses along the curr DFS path

    visitSet = set()

    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True

        visitSet.add(crs)

        for pre in preMap[crs]:
            if not dfs(pre): return False

        visitSet.remove(crs)
        preMap[crs] = []
        return True

    for crs in range(numCourses):
        if not dfs(crs): return False

    return True



numCourses = 5
prerequisites = ([0,1], [1,3], [3,4], [4,0]) # [course, prerequisite], for course 0 you need to complete course 1 first

print(check(numCourses, prerequisites))
