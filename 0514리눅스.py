#cp /etc/services : /etc/services 파일을 현재 디렉터리에 복사

#alias 별칭

ll
which 인자 : 인자 위치 
which ll
which ipython

#alias 만들기
alias grep ='grep' --color
.bashrc .profile (환경설정 파일에)
cd
vi  .bashrc

(85) o alias c='clear'

. .bashrc 실행

# ls 옵션
ls -ldRa

# touch
 - 빈파일 생성 명령어
 touch a1 a2 a3 a4
 vi a5 : 새로운 파일 작성 및 수정
 
 # rm
#**옵션
 -r 디렉터리 삭제
 -i 대화식 옵션(정말 삭제할 것인지 확인)
 -f 강제 삭제
 
rm a1 : 일반 파일 삭제

mkdir test : 일반 파일 삭제
rm -r test : 디렉터리 삭제

alias rm ='rm -i' 해당 세션에서만 유효한 alias (재접속시 없어짐)
 -i : 확인하기 위한 옵션(대화식 옵션)

rm -f a3 
 -f : 강제적으로 수행

# tail : 뒷 부분 출력
 -f : 모니터링 옵션 (새로운 세션 생성 후 아래 echo 명령어로 확인 가능)
 
tail -10 services : services 뒤에서 열 줄 출력
tail -5 /etc/passwd

tail +10 services : services 10번째 라인부터 끝까지 출력
tail +5 /etc/passws

tail -f a4 : a4에 누적되는 데이터 출력
tail -f /etc/passwd : 입력되는 행의 연속 출력 (모니터링)
 
# head
head -5 services : services 앞에서 다섯 줄 출력

#echo 
# - print와 비슷(화면에 즉시 출력)
echo aaaa : aaaa출력
echo aaaa > a4  : aaaa를 a4파일에 전달 (두 번 쓸 경우 덮어쓰기 수행)
echo bbbb >> a4 : >> 이어쓴다


#os에서 쓴 명령어를 프로그램(R/python/sql)에 전달! 
redirection
 - >
 - <
 - >>
 
#ctrl + c , 인터럽션

#파일 출력 (화면단위)
 cat services | more
 more services
 less services

ctrl + b 이전화면
 <-> space bar (ctrl + f)다음화면

# cp 복사명령어
cp 파일명1 파일명2
cp 파일명1 디렉터리명
cp 파일명1 디렉터리명/파일명2 (다른이름으로 디렉터리에 저장)
cp 파일명1 파일명2...디렉터리명

** 옵션
 -i, 대화식 옵션(덮어쓰기 방지)
 -r, 디렉터리 복사
 
cp a4 a5 : a4를 a5로 복사

mkdir test
cp a4 test : 파일 디렉터리 -> 디렉터리 하위에 파일을 복사

cp 인자1,인자2,인자3,디렉터리 : 앞 인자들을 맨 뒤 디렉터리로 복사해라
cp a1 a2 a3 a4 test

- 존재하는 파일에 다시 cp할 경우 덮어쓴다.

cp -i a1 a2 a3 a4 test
 -i , 대화식 옵션
 
cp -r test test2 : 디렉터리 복사

# move 파일명 변경
mv

mv a1 A1 : a1->A1
mv A1 test : A1잘라내서 test에 붙여넣기

# find 파일찾기
find . : 현재 디렉터리에서 찾는다
find 위치 -maxdepth n -name 파일명 -type 파일타입 -exec 명령어 {}\;

 -name : 파일 및 디렉터리 이름(패턴 가능)
 -type : 일반파일(f), 디렉터리(d)만 찾고자 할 경우
 -maxdepth : 검색 범위 설정
 -exec : find명령의 결과(파일, 디렉터리 등)를 특정 명령어의 인자로 전달할 필요가 있을 경우 사용

* ~ : 홈 디렉터리

find . -name a1 : . 상대경로
find / -name a1 : / 절대경로
find ~/linux_ex/ch2 -name a1
find . -name "a*" : a가 포함된 파일/디렉터리명 찾는다
"" -> 특수기호 변환 (파일/디렉터리 둘 다 찾는다)

find ~/linux_ex/ch2 -name a1 -type f : 파일 찾음
find ~/linux_ex/ch2 -name a1 -type d : 디렉터리 찾는다

find ~/linux_ex/ch2 -maxdepth 1 -name "a*"
- maxdepth n(출력범위) <-> mindepth


find . -name "a*" -type d -exec
find . -name adir -type d : adir 이름을 갖는 디렉터리 출력

find . -name adir -type d -exec ls -l {} \; : find 결과를 -exec의 뒤에 나오는 {}위치에 넣어 실행
total 0 (출력결과) - 빈 디렉터리이기 때문.

find . -name adir -type d -exec ls -ld {} \; :
drwxrwxr-x 2 jun jun 4096  5월 14 11:07 ./adir (출력결과)

#find 결과를 수행하기 위해서는 -exec 옵션 {} \; 사용해야한다.

#[연습문제]
~/linux_ex/ch2/test2 디렉터리 생성
~/linux_ex/ch2에 있는 a로 시작하는 모든 파일을 찾아  test2 디렉터리로 복사
(반드시 find 명령어 한 번만 사용)

find ~/linux_ex/ch2 -name "a*" -type f -exec {} ~/linux_ex/ch2/test2 \;

find . -name "a*" -type f -exec cp{} test2 \;

* redirection *
A1> B 정상출력, 1은 생략 가능 / A내용을 B에 출력
A2> B 비정상 출력 * 화면에 출력은 안된다.

1)
find . -name "a*" -type f -exec cp{} test2 \; 2> error.log
: 왼쪽 수행 결과가 비정상이면 error.log file 에 넣어라
2)
find . -name "a*" -type f -exec cp{} test2 \; 2> /dev/null
: 왼쪽 수행 결과 비정상이면 날린다.
dev.null (출력 내용 버리는 장치 = drop시킨다.)

echo aaa 2> /dev/null
3)
echo aaaa > /dev/null >&2
정상출력은 놔두고 비정상 출력(>&2) 날린다. 
4)
echo aaa > a1 2>a2
정상 출력은 a1에 비정상 출력은 a2로
5)
echo aaa > a1 2>&1
정상/ 비정상 입력 위치 동일

 A < B


#[연습문제]
# 루트 디렉터리 전체를 검색해 .sh로 끝나는 파일을 찾아라
# 파일명, 파일 사이즈 등의 정보 출력, shell_list.txt파일에 저장
# 검색과정에 불필요한 에러는 shell_list.error파일에 저장

find / -name "*.sh" -type f -exec ls -l {} \; > shell_list.txt 2> shell_list.error

 find ./ -name "*.sh" -type f

# =============================================================================
# 4장. 셸 사용하기
# =============================================================================
grep jun(유저명) /etc/passwd

# 셸 확인 
which ksh
which sh (본셸) ** 현업에서 사용

vi.db_adim.sh (셸 작성)
#!/bin/sh 본셸로 사용하시오 (맨 윗줄에 표시)

find / -name "*.sh" -type f > ~linux_ex/ch2/list.txt

for i in  ...:
    
cat ...

#!/bin/sh 본셸로 사용하시오 (맨 윗줄에 표시)
find / -name "*.sh" -type f > ~linux_ex/ch2/list.txt 2> /dev/null # 에러메세지 null처리
. db_admin.sh (실행)

# ls 색인
ls *.txt
ls t*t
ls a[0-9]

ls [ab]* a,b 포함하는 파일 출력
ls [a-z][0-9]

touch A1
ls [a-Z][0-9]  출력 가능

# 특수기호 정리
1. *  (모든) 
2. [] (글자묶음)
3. ~ (home 디렉토리 -> 유저 default 디렉터리)
4. . (. :현재 디렉터리, .파일명 : 실행)
5. - (cd - , 이전 디렉터리)
6. A | B (A의 결과를 B의 인자로 전달)

7. ; (명령어 연속 실행) [ex in R] v1 <- 1;v2<-2, \;(특수문자 \붙여야함)
    /$ date ; pwd ; ls

8. $ (변수 호출)*****
    v1=1, $v1 =>출력불가 (실행 기본이기 때문)
    echo $변수, echo $v1 (간단한 출력 - echo)
    $v1 + 1, 연산 불가

9. \ (escape문자)
10. ''  **** 문자열 묶음, 모든 특수기호 무시(일반기호화)
11. ""  **** 문자열 묶음, 일부 기호 제외 대부분 특수기호 무시
12. ``  **** 명령어 결과 묶어 변수 전달 시 사용

''  **** 모든 특수문자를 일반 문자로 간주
""  **** $ `` \ * 제외한 모든 특수문자를 일반 문자로 간주

date , 날짜
v2=date
echo $ve 불가
 
[변수에 명령어 할당]
v2=`date`
v3=$(date)

echo '$v1'  ''따옴표로 묶을 경우 변수 의미 사라짐.
echo '$v2 is v1 varialble' $v1 변수 의미 사라짐
echo "Sv2 is v1 varialble" $v1 변수로 사용 가능

(예)
v1 = 1

echo $v1
1

echo '$v1 is v1 variable'
$v1 is v1 variable

echo "$v1 is v1 variable"
1 is v1 variable


for i in list:
do
 rm $i
 echo "$i 파일을 지웠습니다." >>a.log


# =============================================================================
# 9장 셸 프로그래밍
# =============================================================================
v1=100
v2=200

$v1 + $v2 : 연산 불가
expr 명령어 사용 (정수만 표현 가능)
더하기. expr $v1+v2 : 연산 가능
나누기. expr \( $v1 + $v2 \) / 2

나누기. expr \( $v1 + $v2 \) / 11         * 출력 불가 (셸 호환 불가)
나누기. echo \( $v1 + $v2 \) / 11 | bc -l * 출력 가능

곱하기 expr \( $v1 + $v2 \) \* 1.1 | bc -l


bc 계산기 - quit 

#[연습문제]
#~/linux_ex/ch4 디렉토리 생성
#아래 이름의 빈 파일 생성 a1 b1 ab1 abc1 aba1 cba
mkdir  linux_ex/ch4
cd linux_ex/ch4

touch a1 b1 ab1 abc1 aba1 cba

#1. ~/linux_ex/ch4 디렉터리에서 세개의 영문 이름 갖는 파일 이름 출력
ls [a-z][a-z][a-z]*

#2. 숫자로 끝나는 파일명 출력
ls *[0-9]
find ~linux_ex/ch4 grep "[$0-9]"

#3. a or b로 시작하는 파일 삭제
find . -name "[ab]*" -exec rm {} \;

#4. 홈디렉터리 하위 2 레벨에서 a를 포함하는 파일명을 갖는 파일을 찾아 alist에 저장
find . -maxdepth 2 "*a*" > alist
. alit  (실행)

#5. 루트디렉터리에서 .sh파일의 갯수와 .log 파일 갯수를 더해 v_total 변수에 저장
sh=ls -R ~ | grep "\.sh$" | wc -w
log=ls -R ~ | grep "\.log$" | wc -w

#6. /etc/services 파일의 5-10번째 라인을 services2에 저장






























