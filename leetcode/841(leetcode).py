class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        arr = [False for _ in range(len(rooms))]
        arr[0] = True
        stack = [0]
        while True:
            if len(stack) == 0:
                break
            room = stack.pop()
            for i in rooms[room]:
                if arr[i] != True:
                    arr[i] = True
                    stack.append(i)

        print(arr)
        for i in arr:
            if i == False:
                return False
        return True
