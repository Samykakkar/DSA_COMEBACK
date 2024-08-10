class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        newpath=path.split("/")
        for dir in newpath:
            if dir =="..":
                if stack:
                    stack.pop()
            elif dir=="." or dir=="":
                continue
            else:
                stack.append(dir)
        return "/"+"/".join(stack)

        