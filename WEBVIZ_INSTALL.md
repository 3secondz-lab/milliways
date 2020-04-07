ROS-Webviz Tutorial
===================

# 1. Prerequisite

* Ubuntu 18.04 LTS

* ROS Melodic

본 Repository의 [ROS_INSTALL.md](ROS_INSTALL.md) instruction을 확인하여 설치 가능하다.



# 2. roslibjs 및 rosbridge 설치

ROS의 Javascript support와 관련된 패키지를 설치 한다.

[roslibjs Github](https://github.com/RobotWebTools/roslibjs)와 [rosbridge_suite Github](https://github.com/RobotWebTools/rosbridge_suite)를 catkin workspace 의 src 디렉토리 (ex. ~/catkin_ws/src)에 clone 한다.

두 패키지를 clone 한 뒤 catkin workspace에서 build를 실행하여 설치한다. 

```sh
catkin_make install
# 또는
catkin build
```



# 3. NodeJs 설치

Webviz를 PC에 설치하기 위해 node package manager (npm)이 필요하며, NodeJs를 설치하면 사용이 가능하다.

본 문서 작성 시점에는 NodeJs 12 이상의 버전을 이용할 경우 Webviz 설치에 문제가 있으므로, NodeJs 10.x 설치를 기준으로 한다.

차후 문제가 해결 되어 최신 버전을 설치하고 싶을 경우 [NodeJs Github](https://github.com/nodesource/distributions/blob/master/README.md) 에서 설치 방법 확인이 가능하다.

```sh
# Using Ubuntu
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs
```

정상적으로 설치 되었을 경우, 아래 커맨드로 버전 확인이 가능하다.

```sh
node -v
npm -v
```



# 4. Webviz 설치

[Webviz github](https://github.com/cruise-automation/webviz) 를 원하는 위치에 clone 한다.

Webviz 디렉토리 내부로 이동하여 아래 명령어를 이용하여 Webviz를 build 한다.

```sh
npm run bootstrap
npm run build
```



# 5. ROS Websocket 및 Webviz 실행

터미널 창을 4개 열어 아래 명령어를 터미널에서 순서대로 실행한다.

예제 데이터를 사용하기 위해 본 Repository에 준비된 [sample rosbag](data/sample.bag)을 원하는 디렉토리 (SAMPLE_ROSBAG_ROOT)에 다운로드 받아 준비한다.

Webviz 실행 명령어의 경우 Webviz를 설치한 디렉토리 (WEBVIZ_ROOT)에서 실행해야 한다.

```sh
# Terminal 1 : Rosmaster 실행
roscore
# Terminal 2 : ROS Websocket server 실행
roslaunch rosbridge_server rosbridge_websocket.launch
# Terminal 3 : Webviz 실행
cd WEBVIZ_ROOT
npm run docs
# Terminal 4 : Sample rosbag play
cd SAMPLE_ROSBAG_ROOT
rosbag play sample.bag -l
```

rosbag play의 -l 옵션을 통해 데이터를 반복하여 재생 할 수 있다.

Sample rosbag의 경우 아래 데이터들이 저장되어 있다.

* /test_msg1 : std_msgs/Float64MultiArray
* /test_msg2 : assetto_corsa/ACRaw (Custom message)
* /test_msg3 : sensor_msgs/Image

모든 과정이 끝난 후 웹 브라우저 (Chrome 또는 Firefox)의 http://localhost:8080/app 로 Webviz 접속이 가능하다.

접속 후 원하는 패널을 오른쪽 상단의 [+] 버튼을 이용해 추가 한 뒤, 원하는 topic을 선택하면 visualization이 가능하다.

사용 방법은 아래 동영상을 참고하면 된다.



<iframe width="560" height="315" src="https://www.youtube.com/embed/qd_d_f2fYuU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



# TODO

현재 ROS 기본 Message의 경우 이상 없이 확인 가능하나, Custom message의 경우 확인이 불가능하다.

따라서 Custom message support가 추가되어야 한다.
