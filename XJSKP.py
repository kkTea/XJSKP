import pyautogui
import time


def find(image_path, timeout=3):
    """
    寻找并点击指定图片
    :param image_path: 图片路径
    :param timeout: 超时时间（秒）
    :return: 是否找到并点击成功
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if location:
                return True
        except pyautogui.ImageNotFoundException as e:
            break
    return False


def find_and_click(image_path, timeout=3):
    """
    寻找并点击指定图片
    :param image_path: 图片路径
    :param timeout: 超时时间（秒）
    :return: 是否找到并点击成功
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
            if location:
                pyautogui.click(location)
                return True
        except pyautogui.ImageNotFoundException as e:
            break
    return False


def select_jineng(game_num):
    if find_and_click('images/qiangxie.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘枪械’")
        return
    if find_and_click('images/dianjizhu.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘电极柱’")
        return
    if find_and_click('images/wenyadan.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘温压弹’")
        return
    if find_and_click('images/zhidaojiguang.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘制导激光’")
        return
    if find_and_click('images/xuanfengjianong.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘旋风加农’")
        return
    if find_and_click('images/ganbingdan.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘干冰弹’")
        return
    if find_and_click('images/ranyoudan.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘燃油弹’")
        return
    if find_and_click('images/bingbaofashengqi.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘冰暴发生器’")
        return
    if find_and_click('images/wurenjichongji.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘无人机冲击’")
        return
    if find_and_click('images/zhuangjiache.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘装甲车’")
        return
    if find_and_click('images/diancichuanci.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘电磁穿刺’")
        return
    if find_and_click('images/gaonengshexian.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘高能射线’")
        return
    if find_and_click('images/yasuoqiren.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘压缩气刃’")
        return
    if find_and_click('images/kongtouhongzha.png'):
        print(f"第【{game_num}】局 - 当前执行 - ‘空投轰炸’")
        return


def start_games(wait_time):
    game_num = 1
    while True:
        time.sleep(3)
        # 开始单局游戏
        if find_and_click('images/xunluoche.png'):
            print(f"巡逻车奖励 - 领取")
            time.sleep(1)
            find_and_click('images/lingqu.png')
            time.sleep(1)
            find_and_click('images/dianjikongbaichuguanbi2.png')
            time.sleep(0.5)
            find_and_click('images/dianjikongbaichuguanbi1.png')
        elif find_and_click('images/kaishiyouxi.png'):
            print(f"第【{game_num}】局 - 当前执行 - ‘开始游戏’")
        else:
            # 中途开始脚本
            while True:
                if find('images/xuanzejineng.png'):
                    print(f"第【{game_num}】局 - 当前执行 - ‘选择技能’")
                    select_jineng(game_num)
                    time.sleep(wait_time)
                elif find('images/jingyingdiaoluo.png'):
                    print(f"第【{game_num}】局 - 当前执行 - '精英掉落'")
                    time.sleep(1)
                    find_and_click('images/dianjikongbaichuguanbi.png')
                    print(f"第【{game_num}】局 - 当前执行 - '点击空白处跳过'")
                    time.sleep(wait_time)
                elif find('images/fanhui.png'):
                    if find('images/gongxihuode.png'):
                        # 挑战成功
                        print(f"第【{game_num}】局 - 当前执行 - '挑战成功✌️✌️✌️'")
                    else:
                        # 挑战失败
                        print(f"第【{game_num}】局 - 当前执行 - '挑战失败😭😭😭'")

                    if find_and_click('images/shuangbeijiangli.png'):
                        print(f"第【{game_num}】局 - 当前执行 - '双倍奖励'")
                        time.sleep(35)

                    # 游戏结束返回
                    find_and_click('images/fanhui.png')
                    print(f"第【{game_num}】局 - 当前执行 - '返回' - 游戏结束")
                    game_num = game_num + 1
                    break
                elif find('images/guanggaoyihuodejiangli.png'):
                    print(f"第【{game_num}】局 - 当前执行 - '广告-已获得奖励'")
                    if find_and_click('images/guanbi.png'):
                        print(f"第【{game_num}】局 - 当前执行 - '广告-关闭'")
                time.sleep(3)


def main():
    # 难易程度
    wait_time = 5

    # 定位到小程序的“开始游戏”按钮并点击
    start_games(wait_time=wait_time)


if __name__ == "__main__":
    main()
