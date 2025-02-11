no_wires = int(input())
birds_per_wire = list(map(int, input().split()))
no_shots = int(input())

for _ in range(no_shots):
    wire_no, shot_bird = map(int, input().split())
    
    index = wire_no - 1
    
    if index > 0:  
        birds_per_wire[index - 1] += shot_bird - 1
    
    if index < len(birds_per_wire) - 1:  
        birds_per_wire[index + 1] += birds_per_wire[index] - shot_bird
    
    birds_per_wire[index] = 0

print("\n".join(map(str, birds_per_wire)))
