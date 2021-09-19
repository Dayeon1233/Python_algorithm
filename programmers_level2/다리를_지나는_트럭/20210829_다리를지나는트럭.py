from collections import deque
class Truck:
    def __init__(self, truck_weight, truck_time):
        self.truck_weight = truck_weight
        self.truck_time = truck_time


def solution(bridge_length, weight, truck_weights):
    truck = Truck(truck_weights[0],1)

    q = deque([truck])#차의 무게, 차가 다리위에 있던 시간, total무게
    idx = 1
    time = 1
    total_weight = truck_weights[0]

    while q:
        this_truck = q[0]

        if this_truck.truck_time >= bridge_length:#다리길이만큼 시간이 경과 되어 다리위에 있었다면 다리에서 빠져나오게 함
            q.popleft()
            total_weight -= this_truck.truck_weight


        if idx < len(truck_weights) and total_weight + truck_weights[idx] <= weight and len(q) < bridge_length: # 다리에 다음차가 올라올 수 있는 경우

                    for truck in q:
                        truck.truck_time += 1

                    next_truck = Truck(truck_weights[idx], 1)
                    q.append(next_truck)

                    total_weight += truck_weights[idx]
                    idx += 1
                    time += 1

        else:#다음차가 올라올 수 없는 경우
            for truck in q:
                truck.truck_time += 1

            time += 1
    return time

if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))