# 工业机器人安全检查示例
# 这个程序用 if 语句来演示机器人在工作前如何判断是否可以继续运行。

battery_level = 85         # 电量百分比
joint_temperature = 48    # 关节温度
obstacle_detected = False  # 是否检测到障碍物

if battery_level >= 20 and joint_temperature <= 60 and not obstacle_detected:
    print("机器人状态正常，准备开始执行任务。")
    print("机械臂正在平稳移动。")
else:
    print("机器人已停止运行，原因如下：")
    if battery_level < 20:
        print("- 电量不足")
    if joint_temperature > 60:
        print("- 关节温度过高")
    if obstacle_detected:
        print("- 检测到障碍物")

print("\n这个例子说明了：")
print("1. if 可以用来判断机器人的安全状态")
print("2. and 可以同时满足多个条件")
print("3. else 可以处理异常情况")