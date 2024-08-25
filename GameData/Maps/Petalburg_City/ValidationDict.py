# spaces that cannot be walked, to trim down on uneeded data, only map the boarder that cannot be entered
blocked_spaces_dict = {(26, 19): True, (27, 19): True, (28, 19): True, (29, 19): True, (26, 20): True, (18, 20): True, (19, 20): True, (20, 20): True, (21, 20): True, (22, 20): True, (23, 20): True, (24, 20): True, (25, 20): True, (18, 21): True, (18,22): True, (19, 23): True, (19, 22): True, (20, 22): True, (21, 22): True, (22, 22): True, (22, 21): True, (22, 23): True, (21, 23): True, (25, 21): True, (25, 22): True, (25, 23): True, (25, 24): True, (25, 25): True, (26, 25): True, (26, 26): True, (26, 27): True, (13, 27): True, (14, 27): True, (15, 27): True, (16, 27): True, (17, 27): True, (18, 27): True, (19, 27): True, (20, 27): True, (21, 27): True, (22, 27): True, (23, 27): True, (24, 27): True, (25, 27): True, (13, 23): True, (13, 24): True, (13, 25): True, (13, 26): True, (12, 23): True, (12, 24): True, (12, 25): True, (12, 26): True, (12, 27): True, (12, 28): True, (12, 29): True, (10, 29): True, (11, 29): True, (10, 27): True, (10, 28): True, (5, 27): True, (6, 27): True, (7, 27): True, (8, 27): True, (9, 27): True, (5, 28): True, (5, 29): True, (1, 29): True, (2, 29): True, (3, 29): True, (4, 29): True, (1, 13): True, (1, 14): True, (1, 15): True, (1, 16): True, (1, 17): True, (1, 18): True, (1, 19): True, (1, 20): True, (1, 21): True, (1, 22): True, (1, 23): True, (1, 24): True, (1, 25): True, (1, 26): True, (1, 27): True, (1, 28): True, (0, 13): True, (0, 10): True, (1, 10): True, (1, 8): True, (1, 9): True, (3, 3): True, (3, 4): True, (3, 5): True, (3, 6): True, (3, 7): True, (3, 8): True, (4, 3): True, (5, 3): True, (5, 4): True, (6, 4): True, (6, 3): True, (7, 3): True, (8, 3): True, (8, 4): True, (9, 4): True, (10, 4): True, (10, 5): True, (10, 6): True, (10, 7): True, (10, 8): True, (11, 7): True, (12, 7): True, (13, 7): True, (14, 7): True, (11, 8): True, (16, 7): True, (17, 7): True, (18, 7): True, (18, 8): True, (17, 9): True, (12, 6): True, (13, 6): True, (14, 6): True, (15, 6): True, (16, 6): True, (17, 6): True, (18, 1): True, (18, 2): True, (18, 3): True, (18, 4): True, (18, 5): True, (18, 6): True, (18, 0): True, (19, 0): True, (20, 0): True, (21, 0): True, (22, 0): True, (23, 0): True, (24, 0): True, (25, 0): True, (26, 0): True, (26, 1): True, (26, 2): True, (26, 3): True, (26, 4): True, (26, 5): True, (26, 6): True, (26, 7): True, (26, 8): True, (24, 8): True, (24, 9): True, (24, 10): True, (24, 11): True, (25, 10): True, (26, 10): True, (27, 10): True, (26, 11): True, (27, 11): True, (28, 11): True, (28, 12): True, (28, 13): True, (28, 14): True, (29, 14): True, (19, 12): True, (19, 13): True, (19, 14): True, (20, 12): True, (20, 13): True, (20, 14): True, (21, 12): True, (21, 13): True, (21, 14): True, (22, 12): True, (22, 13): True, (22, 14): True, (21, 15): True, (22, 15): True, (19, 15): True, (17, 15): True, (9, 15): True, (9, 16): True, (9, 17): True, (9, 18): True, (10, 15): True, (10, 16): True, (10, 17): True, (11, 15): True, (11, 16): True, (11, 17): True, (12, 15): True, (12, 16): True, (12, 17): True, (11, 18): True, (12, 18): True, (7, 13): True, (7, 14): True, (7, 15): True, (7, 16): True, (7, 17): True, (7, 18): True, (8, 13): True, (8, 14): True, (8, 15): True, (8, 16): True, (8, 17): True, (8, 18): True}

house_1_block_spaces_dict = {}

house_2_block_spaces_dict = {}

house_3_block_spaces_dict = {}
