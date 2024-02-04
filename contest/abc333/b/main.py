S=input()
T=input()

def are_segments_equal(s1, s2, t1, t2):
    vertices = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    def are_adjacent(v1, v2):
        return abs(vertices[v1] - vertices[v2]) == 1 or abs(vertices[v1] - vertices[v2]) == 4

    return are_adjacent(s1, s2) == are_adjacent(t1, t2)

print("Yes" if are_segments_equal(S[0], S[1], T[0], T[1]) else "No")
