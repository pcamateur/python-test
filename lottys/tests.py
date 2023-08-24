source_data = ["07", "08", "11", "14", "25", "31"]
input_data = ["07", "09", "11", "15", "25", "32"]
check_bingo = [ball for ball in input_data if ball in source_data]
print(check_bingo)