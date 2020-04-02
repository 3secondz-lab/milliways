# Ubuntu 18.04.4에 ROS Melodic 설치 (2020. 4.)

ROS 설치는 매뉴얼이 굉장히 잘 되어 있는 편이며 특히 Ubuntu에 설치하는 건 기본적으로 ROS Wiki ( [https://wiki.ros.org/melodic/Installation/Ubuntu](https://wiki.ros.org/melodic/Installation/Ubuntu) ) 를 따라가면 된다.
이 문서는 2020년 4월 1일 기준 위키 매뉴얼에 대한 약간의 부연 및 우리를 위한 팁을 기록한다.
<br>
## 0\. Pre\-installation

공식 documentation에는 없는 내용이다.
Ubuntu 18.04.4 에 Anaconda3 을 설치하고, 기본 디렉토리는 기본값으로 둔다.
그러면 /home/[사용자명]/anaconda3에 설치될 것.

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

**여기가 공식 튜토리얼과 다른 부분이다. 우리는 아나콘다에 딸려온 파이썬3을 쓸 것이므로 경로를 아래와 같이 해 준다.**
**ys는 필자의 홈 디렉토리이므로 바꿔준다.**
<br>
```
$ catkin_make -DPYTHON_EXECUTABLE=/home/ys/anaconda3/bin/python3
```