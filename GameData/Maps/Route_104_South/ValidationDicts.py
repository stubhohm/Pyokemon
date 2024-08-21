blocked_spaces_dict = {(36, 29): True, (37, 29): True, (38, 29): True, (39, 29): True, (36, 30): True, (34, 31): True, (35, 31): True, (36, 31): True, (34, 32): True, (32, 33): True, (33, 33): True, (34, 33): True, (32, 34): True, (32, 35): True, (30, 35): True, (31, 35): True, (31, 36): True, (31, 37): True, (31, 38): True, (31, 39): True, (31, 40): True, (31, 41): True, (31, 42): True, (31, 43): True, (31, 44): True, (26, 35): True, (27, 35): True, (26, 31): True, (26, 32): True, (26, 33): True, (26, 34): True, (27, 31): True, (24, 31): True, (25, 31): True, (24, 29): True, (24, 30): True, (23, 29): True, (23, 27): True, (23, 28): True, (21, 27): True, (22, 27): True, (21, 25): True, (21, 26): True, (20, 25): True, (20, 23): True, (20, 24): True, (19, 23): True, (19, 19): True, (19, 20): True, (19, 21): True, (19, 22): True, (18, 19): True, (14, 19): True, (15, 19): True, (14, 12): True, (14, 13): True, (14, 14): True, (14, 15): True, (15, 12): True, (15, 13): True, (15, 14): True, (15, 15): True, (16, 12): True, (16, 13): True, (16, 14): True, (16, 15): True, (10, 12): True, (11, 12): True, (12, 12): True, (13, 12): True, (7, 11): True, (8, 11): True, (9, 11): True, (10, 11): True, (7, 9): True, (7, 10): True, (6, 6): True, (6, 7): True, (6, 8): True, (6, 9): True, (6, 5): True, (7, 5): True, (8, 5): True, (9, 5): True, (9, 2): True, (9, 3): True, (9, 4): True, (12, 2): True, (12, 3): True, (12, 4): True, (12, 5): True, (13, 5): True, (14, 5): True, (15, 5): True, (16, 5): True, (16, 6): True, (17, 6): True, (18, 6): True, (19, 6): True, (20, 5): True, (20, 6): True, (21, 5): True, (22, 5): True, (23, 5): True, (24, 5): True, (25, 5): True, (26, 5): True, (26, 6): True, (26, 7): True, (26, 8): True, (26, 9): True, (26, 10): True, (26, 11): True, (27, 11): True, (27, 12): True, (27, 13): True, (28, 13): True, (29, 13): True, (29, 11): True, (29, 12): True, (30, 11): True, (30, 7): True, (30, 8): True, (30, 9): True, (30, 10): True, (31, 8): True, (31, 5): True, (31, 6): True, (31, 7): True, (34, 5): True, (34, 6): True, (34, 7): True, (34, 8): True, (34, 9): True, (34, 10): True, (34, 11): True, (34, 12): True, (34, 13): True, (34, 14): True, (34, 15): True, (34, 16): True, (34, 17): True, (34, 18): True, (32, 18): True, (33, 18): True, (32, 19): True, (32, 20): True, (32, 21): True, (33, 21): True, (34, 21): True, (34, 22): True, (34, 23): True, (34, 24): True, (35, 24): True, (36, 24): True, (36, 25): True, (37, 25): True, (38, 25): True, (39, 25): True, (17, 12): True, (17, 13): True, (17, 14): True, (18, 12): True, (18, 13): True, (18, 14): True, (19, 12): True, (19, 13): True, (19, 14): True, (18, 15): True, (19, 15): True, (20, 15): True}


ref_dict = blocked_spaces_dict
empty_dict = {}
for key in ref_dict.keys():
    new_key = (key[0] + 1, key[1])
    value = ref_dict.get(key)
    empty_dict[new_key] = value
#print(empty_dict) 