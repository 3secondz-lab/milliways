# Ubuntu 18.04.4에 ROS Melodic 설치 (2020. 4.)

ROS 설치는 매뉴얼이 굉장히 잘 되어 있는 편이며 특히 Ubuntu에 설치하는 건 기본적으로 ROS Wiki ( [https://wiki.ros.org/melodic/Installation/Ubuntu](https://wiki.ros.org/melodic/Installation/Ubuntu) ) 를 따라가면 된다.
이 문서는 2020년 4월 1일 기준 위키 매뉴얼에 대한 약간의 부연 및 우리를 위한 팁을 기록한다.

Updated 4/7

## 0\. Pre\-installation
<br>
Ubuntu 18.04.4 에 Anaconda3 을 설치하고, 기본 디렉토리는 기본값으로 둔다.
그러면 파이썬은 /home/[사용자명]/anaconda3에 설치될 것.
<br>
## 1\. Installation

### 1.1. 우분투 리퐈쥐토뤼(repository) 설정

restricted, universe 및 multiverse를 허용하라고 하는데 기본값이 허용되어 있으니 패스.

### 1.2\~1.3. 소스 목록 및 키 등록

package.ros.org 에서 소프트웨어를 받을 수 있게 해 준다.
curl -sSL .... 이 부분은 넘어간다

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

### 1.4. 설치

apt update 후 desktop-full install 로 설치한다.
<br>
```
sudo apt update
sudo apt install ros-melodic-desktop-full
```

### 1.5. 환경 설정

이것만 실행.

```
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

source /opt/ros..../setup.bash 라는 명령을 홈의 .bashrc 파일 제일 밑에 기록하라는 의미이다.
그리고 기록된 bashrc 를 실행하라는 게 아래의 source 명령.
.bashrc 파일은 저 옛날 DOS의 autoexec.bat 나 윈도우의 시작프로그램 비슷한 거라 생각하면 편리하다.
이제 터미널을 켤 때마다 방금 설치한 ROS 환경이 로드된다.
source \~/.bashrc 의 의미는, 방금 수정한 .bashrc 를 현재 실행 중인 터미널 세션에 다시 로드하라는 의미이며 이 과정이 귀찮으면 세션 창을 닫았다가 새 세션 창을 열면 된다. (ctrl + alt + T)
<br>
### 1.6. 패키지 빌드를 위한 의존성 패키지 설치

아무튼 (sudo) apt는 마법의 주문이다. 아무 생각 없이 실행해 주자. 뭐하는건지는 며느리도 모름.

```
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

이제 ros dependency 를 초기화하고 업데이트한다.
**두 번째 줄에는 sudo가 없는 것에 주의!** sudo rosdep update 할 경우 심각한 경고를 내뱉는다.

```
sudo rosdep init
rosdep update
```
<br>
다음으로 튜토리얼로 넘어가자.
<br>
## 2\. 환경 관리
<br>
Managing your environment 라고 했지만 우리는 단일 환경만 쓸 것이고 그나마도 자동 활성화를 켰으므로(1.5), 무시해도 된다. 이미 1장에서 다 했다.

## 3\. ROS 작업 공간 생성

catkin 이라는 편리한 도구를 이용하는, ROS의 워크스페이스 생성. catkin에 대해 알고 싶으면 구글링을 활용하자. 물론 필자도 잘 모릅니다.
<br>
```
$ mkdir -p ~/catkin_ws/src        // catkin_ws와 그 하위 src 디렉토리까지 만들어라
$ cd ~/catkin_ws/                //  catkin_ws 로 이동
```
<br>
눈치빠른 독자는 catkin\_make를 하지 않았다는 것을 알 수 있다.
그렇다. 여기서 catkin\_make를 하기 전에 python 버전을 맞춰 주어야 한다.
ROS는 현재 ROS2 버전을 준비하고 있지만 ROS1은 굉장히 오래전에 만들어졌고 Python 2 기반이다.
다행히 높으신(?) 분들이 각성해서 이제 Python3도 지원을 슬슬 시작하고 있으니, 우리 workspace 상에서 python3.7을 쓰도록 해 주자.

**여기가 공식 튜토리얼과 다른 부분이다.**

먼저 catkin\_pkg를 설치하여 catkin\_make가 동작할 수 있도록 한다.

<br>
```
$ pip install catkin_pkg
```
<br>
****우리는 아나콘다에 딸려온 파이썬3을 쓸 것이므로 경로를 아래와 같이 해 준다(ys는 필자의 홈 디렉토리이므로 바꿔준다).****
<br>
```
$ catkin_make -DPYTHON_EXECUTABLE=/home/ys/anaconda3/bin/python3
```
<br>
확실히 하기 위하여, 우리가 어떤 파이썬을 사용하고 있는지 확인하는 방법은 아래와 같다.
<br>
```
$ which python3
/home/ys/anaconda3/bin/python3
```
<br>
이제, catkin\_ws 디렉토리는 워크스페이스가 되었다. 앞으로는 catkin\_make 만 해도 src 아래에 생성된 우리의 프로젝트들이 빌드될 것이다.

우리의 프로젝트 디펜던시들도 터미널을 켤 때마다 자동 로드되게 하려면 다음 명령을 입력하여 .bashrc 에 추가해 주고 현재 터미널 세션에 로드하자.
<br>
```
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
<br>
지금까지 과정이 제대로 되었다면 아래 명령을 입력하여 확인해 볼 수 있다.
<br>
```
$ echo $ROS_PACKAGE_PATH
/home/ys/catkin_ws/src:/opt/ros/melodic/share
```
<br>
이상의 과정 (2장, 3장) 은 [https://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment](https://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment) 의 내용을 우리의 실정에 맞게 기록한 내용이다.

이제 해당 링크 맨 아래의 "ROS file system tutorial" 로 가서 심화 학습을 해 보아도 좋겠으나, 랩탑에서 간단히 해 볼 수 있는 예제를 돌려서 ROS가 제대로 설치 및 구동되고 있는지 확인해 보자.
<br>
## 4\. Simple ROS node: usb\_cam

usb\_cam은 ROS에서 usb webcam (정확히는 V4L 장비 전체)들을 구동해 볼 수 있는 패키지이다.
노트북에 달려 있는 웹캠, 화상회의용 로지텍 웹캠 뿐 아니라 땡프리카TV용 HDMI-USB 그래버도 돌릴 수 있는 혜자 패키지이며 우리도 게임 시뮬레이터 영상의 획득을 위하여 이 패키지를 활용할 것이다.

패키지 설명은 wiki ([https://wiki.ros.org/usb\_cam](https://wiki.ros.org/usb_cam))를 참고하고,
패키지를 받기 위해 github([https://github.com/ros-drivers/usb\_cam](https://github.com/ros-drivers/usb_cam)) 주소로 이동하여 develop 브랜치를 받는다.
<br>
```
$ cd ~/catkin_ws/src
$ git clone -b develop https://github.com/ros-drivers/usb_cam.git
```
<br>
\~/catkin\_ws/src/usb\_cam은 include, launch, nodes, src 디렉토리 및 xml, cmakelist 등으로 이루어져 있다.

우선 아무 생각 없이 빌드해 보자. 빌드는 catkin\_ws 디렉토리에서 이루어진다.
<br>
```
$ cd ..   (혹은 cd ~/catkin_ws)
$ catkin_make
```
<br>
별 일이 없다면 빌드가 성공할 것이다. 오래된 패키지라 warning 이 난무하는 건 무시하자.

이제 첫 번째 ros 패키지를 실행해 볼 차례이다.

터미널을 하나 더 열어서, roscore 를 실행하자. roscore는 저그 오버마인드 같은 존재이다.

<br>
```
$ roscore
```
<br>
이제, 기존 창에서 roslaunch를 이용하여 실행해 보자. 일단은 따라 써 보자.
<br>
```
$ roslaunch usb_cam usb_cam-test.launch
```
<br>
새 창으로 웹캠 이미지가 보인다면 성공이다.

끄는 방법은 간단하다. roslaunch를 실행한 창에서 ^C. 일단 꺼 주자.
<br>
## 5\. rostopic 명령: 발행중인 topic 확인

roscore 가 돌고 있는 상태에서, ros가 발행하고 있는 주제들을 조회하기 위해 다음 명령을 활용해 보자.
<br>
```
$ rostopic list
/rosout
/rosout_agg
```
<br>
이제, 다른 터미널을 켜서 usb\_cam 을 실행시키고 위 명령을 다시 입력해 보자.

Terminal #1

```
$ roslaunch usb_cam usb_cam-test.launch
```
<br>
#Terminal 2

```
$ rostopic list
/rosout
/rosout_agg
/usb_cam/camera_info
/usb_cam/image_raw
/usb_cam/image_raw/compressed
/usb_cam/image_raw/compressed/parameter_descriptions
/usb_cam/image_raw/compressed/parameter_updates
/usb_cam/image_raw/compressedDepth
/usb_cam/image_raw/compressedDepth/parameter_descriptions
/usb_cam/image_raw/compressedDepth/parameter_updates
/usb_cam/image_raw/theora
/usb_cam/image_raw/theora/parameter_descriptions
/usb_cam/image_raw/theora/parameter_updates
```
<br>
뭐가 잔뜩 생겼다.
팀원들이 만든(그리고 만들) 패키지들은 당연히 다수의 topic들을 publish 하게 되어 있다.

해당 topic이 무엇을 담고 있는지 보려면 다음 명령을 활용하자.
<br>
```
$ rostopic echo /usb_cam/camera_info
```
<br>
아마 타임스탬프, 시퀀스 넘버, 해상도와 카메라 모델, (0으로 가득한) roi 등을 방출할 것이다.
<br>
```
$ rostopic echo /usb_cam/image_raw
```

이러면 현재 수신된 이미지 픽셀 정보를 화면에 난사할 텐데 당연히 이걸 해석 가능한 휴먼은 없을 것이다.
이를 보기 위해(사실 이미 별도 창에 보이고 있지만) ros 기본 제공 도구인 image\_view 를 써 보려면 다음과 같이 하면 된다.
<br>
```
$ rosrun image_view image_view image:=/usb_cam/image_raw
```

아마 기존 이미지 창이 꺼지고 새 이미지 창이 똑같이 뜰 텐데, 이런 식으로 image\_raw topic들을 확인할 수 있다.

그 외에, 현재 발행 중인 topic의 속도를 보려면 다음과 같이 하자.
<br>
```
$ rostopic hz /usb_cam/image_raw
subscribed to [/usb_cam/image_raw]
average rate: 29.904
min: 0.032s max: 0.036s std dev: 0.00196s window: 28
average rate: 29.944
min: 0.031s max: 0.037s std dev: 0.00198s window: 58
average rate: 29.930
min: 0.031s max: 0.040s std dev: 0.00206s window: 88
```
<br>
## 6\. rosbag: topic의 기록 및 재생

아마 뷰를 개발하기 위해서 모든 센서를 다 켜고 차(혹은 시뮬레이터)를 직접 타고 데이터를 수집해야 한다면 그것만한 고역이 없을 것이다.
이를 막기 위해 우리 연구진 및 세계 유수의 연구원들은 rosbag 이라는 편리한 도구를 이용하여, 발행된 rostopic들을 bag으로 저장하여 제공할 것이다.

저장 방법은 차차 논의하고, 여기서는 재생 방법을 확인하자.
rosbag 파일은 \*.bag 이라는 확장자로 제공된다.
<br>
### 6.1. CUI

```
$ rosbag play [filename]
```
<br>
이 상태에서 다른 터미널을 띄워 rostopic list 를 해 보면, play 되는 동안 기록된 topic 목록이 나열되는 것을 확인할 수 있다.
<br>
### 6.2 GUI

터미널 창에서 아래 명령을 실행하자.

```
$ rqt_bag
```
<br>
그러면 GUI 가 열리는데, 여기서 "열기" 버튼을 이용하여 bag 파일을 열면 bag 파일의 재생, loop 등이 가능하다.

<br>
<br>
To be continued...