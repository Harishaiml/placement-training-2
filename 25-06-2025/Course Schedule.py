from collections import defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    visiting = set()

    def dfs(course):
        if course in visiting:
            return False
        if not graph[course]:
            return True

        visiting.add(course)
        for pre in graph[course]:
            if not dfs(pre):
                return False
        visiting.remove(course)
        graph[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False
    return True
