linux - putty

ip 고정

(다른곳에 이식할 때) pc가상 네트워크 주소(vmnet8) 확인, 영역대 변경

# =============================================================================
# ls 명령어 (현재 디렉터리의 하위 디렉터리 표시)
# =============================================================================
ls : 현재 디렉터리, 하위 디렉터리 표시

ls  -(옵션) (인자)
ls anaconda(인자) : 해당 디렉터리 하위 디렉터리 내용 표시
ls -l anaconda3 : -l 상세정보 리스트 형식으로 출력
출력=> 권한/ user/ 해당파일소유자/ 소유자그룹/ 파일사이즈 / 마지막 수정일 / 디렉터리 명

ls -l ~ : home디렉터리 하위 목록 상세 출력
ls -la ~ : 숨겨진 디렉터리까지 상세히 출력
mas ls : man, 설명

[이동]
enter, 줄단위 이동 / space bar, 페이지 단위 이동
 
/ : 링크 디렉토리
@ :  다른 링크에 연결된 디렉토리

. 현재 디렉터리
.. 상위 디렉터리
../ 상위 경로로 이동

절대경로 : 디렉터리 구조에 기반한 경로
상대경로 : 현재 커서가 위치한 디렉터리 기반 경로


현재 디렉터리가 user1일 때 
user1의 절대 경로명: /home/user1 
user1 아래 ‘다운로드’의 절대 경로명: /home/user1/다운로드 
‘다운로드’의 상대 경로명: 다운로드 또는 ./다운로드 
 hosts 파일의 상대 경로명: ../../etc/hosts 
 
 디렉터리/파일명    절대 경로              상대 경로 
/                    cd ../../             cd .. cd ..
home                 cd ../                cd .. 
tmp                  cd ../../tmp          cd .. 
lib                  cd ../ ../usr/lib
ls                   cd ../../bin/ls

# =============================================================================
# [명령어]
# =============================================================================
ls [옵션][파일, 디렉토리명]
(옵션) - [R, l, a, d]


ls -la (숨김파일 포함 모든 파일 목록 출력)
ls -ld /home/jun   jun 디렉터리 정보를 리스트로 출력
ls -R /home | more  # | 앞의 명령어 결과를 뒤의 인자로 전달. more : 페이지 단위로 출력


ls -R 하위디렉터리 목록까지 출력

cat etc/serivec
* more etc/serivec

cat : 파일 내용 확인 명령어
#[.bashrc / .profile - 환경설정 파일]

#[디렉터리 파일 상세 정보]
ls -l 파일/디렉터리 권한 확인 가능 (- : 파일 / d: 디렉터리)
ex) drwxr-x-rx (d, 디렉터리) / -rwxr-x-rx (-, 파일)

drwxr-xr-x 2  user1 user1 4096 2월 20 21:28 공개 
drwxr-xr-x (3, 소유자 권한 / 3, 그룹 권한 / 3, 그 외 유저)
2 : 하드링크 갯수
user1 파일 소유자
user1 파일이 속한 그룹
4096 파일 크기


# * 유닉스 / 리눅스 /쉘 바이블 (추천서)

# =============================================================================
# 1. grep 명령어 **중요
# =============================================================================
 grep : 패턴 찾는 함수 (라인단위)

[사용법]
grep 옵션 패턴 대상
 -w : 정확한 패턴 검색 시 사용
grep -w ^root /etc/passwd

#예제) jun(본인유저) 생성여부 확인
cat /etc/passwd : 현 서버에 생성된 정보를 자동으로 기록하는 파일
gerp jun /etc/passwd  
grep ^bin /etc/passwd (^bin , bin으로 시작하는 명령여)

#[참고, in oracle]
#select *
#  from dba_users
# where username = 'jun';
#--

#useradd : 유저생성 명령어
# - 관리자 권한 없을경우  Permission denied. 출력된다
# => sudo useradd rooto

#예제) home 디렉터리 하위에 있는 일반 파일만 출력 (파일의 상세 정보가 출력되도록)
ls -l | grep ^-


# =============================================================================
# 2. mkdir 디렉터리 생성
# =============================================================================
mkdir 옵션 디렉터리명
** 디렉터리명은 상대/절대 경로로 전달 가능, 여러개 전달 가능

-p : 인자에 디렉터리 경로 전달 시 중간경로 디렉터리도 동시에 생성

mkdir -p test2/a2
(확인) ls test2  => a2

# =============================================================================
# rmdir 디렉터리 삭제
# =============================================================================
rmdir 옵션 디렉터리명
#(옵션)
-p : 인자에 디렉터리 경로 전달 시 중간경로 디렉터리도 동시에 삭제
(단, 하위디렉터리 삭제 후 중간 경로 디렉터리가 빈 디렉터리일 경우만 함께 삭제 가능)

-r : 빈디렉터리 아닌경우에도 삭제 가능
rm -r test2

#(하위 삭제 후 중간 디렉터리가 빈디렉터리인 경우)
rmdir test2/a2 => a2만 지워짐
rmdir -p test/a1 => 중간 디렉터리까지 같이 삭제

#(하위 디렉터리 삭제, 빈디렉터리 아닌경우)
mkdir test2/a1
mkdir test2/a2
rmdir -p test2/a1  * 빈 디렉터리 아니므로 중간경로 삭제 불가(a1 디렉터리만 삭제)


#[연습문제]
#① 현재 위치를 확인한다. 홈 디렉터리가 아니면 홈 디렉터리로 이동한다.
pwd
cd /home
#② 실습을 위한 기본 디렉터리를 만든다. 
#먼저 홈 디렉터리에 linux_ex 디렉터리를 만들고 그 디렉터리로 이동한다. 
#앞으로 모든 실습은 이 디렉터리 아래에서 한다. 
sudo mkdir linux_ex
#③ ch2 디렉터리를 만들고 그 디렉터리로 이동하여 현재 위치를 확인한다. 
mkdir ch2
cd ch2
pwd
#④ one, two, three 디렉터리를 동시에 만든다.
mkdir one two three
#⑤ one 디렉터리 아래에 tmp/test 디렉터리를 만든다. 
#중간 경로인 tmp 디렉터리가 자동 생성되도록 한다. 
mkdir -p ch2/one/tmp/test

#⑥ two, three 디렉터리를 동시에 삭제한다.
cd ch2
rmdir two three
#⑦ 실습을 마치고 홈 디렉터리로 이동한다.
cd /home 

# =============================================================================
# cp 복사 수행
# =============================================================================
linux_ex$ cp /etc/services .

#[방향키]
h 위 
j 아래
k 왼쪽
l 오른쪽

vi services
vi 편집기 : 문서 편집기능
vi : [입력 / 명령]모드
# - 입력모드
 1) a : 다음커서에 입력
 2) i : insert, 현재커서에 입력
 3) o : 다음라인에 입력
=> 입력 -> 명령모드 전환 ESC 

# 삭제) 
1) x  : 뒷 내용(글자) 삭제
2) dd : 라인 삭제 (3dd / 4dd ->ndd, n줄 삭제)
3) u  : 한 단계 실행취소
4) U  : 현재 라인의 모든 실행 취소

# 수정)
1) r  : 한글자 수정
2) cw : 단어의 치환
3) yy : 라인 복사
3) p  : 다음에 라인에 붙여넣기

# 이동 / 단어찾기
1) ^ : 라인 맨 앞으로 이동
^ /(단어) -> ^/udp

2) $ :  라인 맨 뒤로 이동
^ /(단어) -> ^/udp 


- 명령모드 : 치환, 삭제, 커서이동, 복사,붙여넣기 
 
 - 마지막 행 모드 : 종료
 1) :q   * 종료 (수정 내용 있을 경우 종료 불가)
 2) :q!  * 강제종료, 저장하지않고 나옴
 3) :wq  * 저장 후 종료
 4) :set nu *행 번호 같이 출력 

# [연습문제]
services 파일에서 
#1) 두번째 라인에 test 단어 삽입
a test (esc)
#2) 13번째 끝라인으로 이동
$
#3) 18번째 라인의 users 삭제
x 삭제
#4) 20번째 라인의 daytime date로 수정
a, date
#5) 30번째 라인 복사 후 39번째 라인 뒤 붙여넣기
30번째 yy -> 39번째 r
#4) 45번째 라인으로 부터 5번째 라인 삭제
5dd
#7) 저장 후 종료
:wq1

# =============================================================================
# wc : 워드카운트
# =============================================================================
[사용법]
wc 옵션 파일명

 -l  라인 수
 -w  단어 수
 -c  글자 수

예제)
wc /etc/passwd
[출력결과]
# 45      73      2588    /etc/passwd
 라인수  단어수   글자수      파일명

# 파일명 같이 출력
wc -l /etc/passwd   * 라인 수 / 파일명 출력
# 45 /etc/passwd

#파일명 없이 출력)
cat /etc/passwd | wc -l

#[연습문제]
#1. 홈디렉토리 하위 모든 파일 및 디렉토리를 체크해 파일 갯수 출력
ls -Rl ~ | grep ^- | wc -l

#sh로 끝나는 파일 갯수(셸 스크립트)
ls -Rl ~ | grep $sh | wc -l 

#2. bin디렉터리를 홈 디렉터리로 갖는 유저 갯수 출력
grep -w /bin: /etc/passwd | wc -l


# =============================================================================
# find 파일, 디렉터리 찾는 명령어
# =============================================================================
cat read1.sh | wc -l * 라인수만 출력



