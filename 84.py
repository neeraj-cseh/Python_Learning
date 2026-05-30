import time 
# current_time = time.time()
# print(current_time)

# print("Task started...")
# time.sleep(10)
# print("Task completed after 10 seconds.")

current_struct = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_struct)
print(formatted_time)