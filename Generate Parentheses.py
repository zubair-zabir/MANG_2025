"""BFS solution"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        result = []

        queue = deque([(0, 0, "")])

        while queue:
            open_count, close_count, cur_str = queue.popleft()

            if len(cur_str) == n*2:
                result.append(cur_str)

            if open_count < n:
                queue.append((open_count+1, close_count, cur_str +"("))

            if close_count < open_count:
                queue.append((open_count, close_count+1, cur_str + ")"))

        return result


"""DFS Solution"""

result = []
        def dfs(left_count, right_count, cur_str):
            if len(cur_str) == n*2:
                result.append(cur_str)
                return

            if left_count < n:
                dfs(left_count+1, right_count, cur_str+"(")
            if right_count < left_count:
                dfs(left_count, right_count + 1, cur_str+")")
        dfs(0,0,"")
        return result
