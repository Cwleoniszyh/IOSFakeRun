# IOSFakeRun
声明：本项目仅用于学习，不得用于盈利或其他任何非法活动

本项目基于 [iOSRealRun-cli-17](https://github.com/iOSRealRun/iOSRealRun-cli-17) 修改而来，并更新了依赖的 [pymobiledevice3](https://github.com/doronz88/pymobiledevice3)。

如果使用时出现了无法解决的报错可以考虑使用[这个仓库手动启动](https://github.com/BiancoChiu/iOSEasyRun)。

测试环境：
- 操作系统：MacOS，Windows11，Linux
- Python版本：3.12
- iOS版本：18.3.2

## 用法简介

### 前置条件

1. 系统是 `Windows` 或 `MacOS`（Linux请参考[此issue](https://github.com/BiancoChiu/iOSRealRun-cli-18/issues/4)）
2. iPhone 或 iPad 系统版本大于等于 18（也许17的一些后期版本也可以用，未经测试）
3. Windows 需要安装 iTunes
4. 已安装 `Python3` 和 `pip3`
5. **重要**: 只能有一台 iPhone 或 iPad 连接到电脑，否则会出问题

### 步骤

1. 克隆本项目到本地并进入项目目录
2. 安装依赖（建议使用虚拟环境）  
    ```shell
    pip3 install -r requirements.txt
    ```
    VScode终端
    ```
    pip install -r requirements.txt
    ```
    如果 `pip3` 无法安装，请使用 `pip` 替代  
    如果提示没有需要的版本，请尝试不适用国内源  
3. 修改配置和路线文件 （见 [这里](https://github.com/iOSRealRun/iOSRealRun-cli/blob/main/README.md#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95) 的 4、5、7 步）
4. 将设备连接到电脑，解锁，如果请求信任的提示框，请点击信任
5. ~~打开终端（cmd 或 PowerShell），执行以下命令获取DDI~~（经测试此步骤可跳过）
    ```shell
    pymobiledevice3 mounter auto-mount
    ```
6. Windows **以管理员身份** 打开终端（cmd 或 PowerShell）或者以管理员权限打开VScode，先进入项目目录，然后执行以下命令 
    ```shell
    python main.py
    ```
    ```VScode 以管理员权限打开VScode，点击运行main.py即可
    如果运行报错可以试试文件名改成对应文件的路径
    ```
    MacOS 打开终端，先进入项目目录，然后执行以下命令  
    ```shell
    sudo python3 main.py
    ```
    > 需要 管理员 或 root 权限是因为需要创建 tun 设备  

7. 按照提示操作，如果一直说没有设备连接，Windows请确保 iTunes 已安装（可能需要打开），重新运行程序，在第3步时请确保设备已连接，解锁并信任
8. 结束请务必使用 `Ctrl + C` 终止程序，否则无法恢复定位
9. 如果定位未恢复，可以重启手机解决
