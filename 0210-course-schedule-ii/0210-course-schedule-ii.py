class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
            # Create adjacency list
        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        # Define DFS function
        output = []
        visited = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            
            visited.add(course)
            output.append(course)
            return True
        
        # Perform DFS for each course
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output