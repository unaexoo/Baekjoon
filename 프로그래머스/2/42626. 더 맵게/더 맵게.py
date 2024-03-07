import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        if len(scoville) < 2:
            return -1
        
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        new = one + (two * 2)
        heapq.heappush(scoville,new)
        answer += 1
    
    return answer