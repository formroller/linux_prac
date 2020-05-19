# =============================================================================
# 6장 파일접근 권한관리
# =============================================================================

# 권한 chmod
 - ls -l 결과로 권한여부 확인 가능
 - 총 9개의 문자로 구성
 - r(read) w(write) x(excute)의 권한으로 구성
 - 각 권한을 부여하는 방식에는 기호/숫자 모드가 있음
 - rwx(소유자권한) rwx(소유자가 속한 그룹 권한) rwx(기타사용자 권한)
 - 디렉터리 권한 변경시 하위 목록에 영향을 미치지 않음
 -R, 하위 모든 권한도 함께 변경


1) 기호모드 : 현재권한에서 특정 권한의 추가(+)와 삭제(-)를 기호로 전달
u : 사용자에게 권한 추가 및 삭제
g : 같은 그룹 사용자에게 권한 추가 및 삭제
o : 기타 사용자에게 권한 추가 및 삭제
a : 전체 그룹에 권한 추가 및 삭제

ex)
chmod g+rw test.sh 
chmod a+r test.sh
* 디렉터리 실행(excute) -> 이동 여부 의미


2) 숫자모드 : 각 권한을 나타내는 숫자의 합으로 권한 부여

rwx
421
chmod 644 test.sh -> rw--r--r- *권한 변경

연습문제)  access.sh
디렉터리명과 권한을 입력받고
해당 디렉터리의 권한(소유자)을 갖는 일반파일 목록을 출력하는 쉘 작성
rw

#!/bin/sh

echo "디렉터리명 : \c"
read dname

echo "찾을 권한 입력 (rwx) : \c"
read pname 

for fname in $(find $dname -maxdepth 1 -type f)
do
if [ $? -eq 0 ]
 then
  echo "$fname 권한에 $pname 포함"
 else
  echo "$fname 권한에 $pname 포함"   
 fi
done


디렉터리 명 : /home/jun/linux_ex/ch8
찾을 권한 입력(rwx) : x

# =============================================================================
# sed ***
# =============================================================================
 - 비대화형 편집기 : 건별로 리턴해 편집(명령어 개녕)
 (<-> 대화형 편집기(vi) : 편집내용을 하나씩 확인하며 편집)

sed [옵션] '명령어' 파일명

[명령어]
-s : 치환
sed 's/sh/SH/g' test.sh

-! : 제외
sed '1!s/sh/sh' test.sh

-d : 삭제
sed '1d' test.sh    # 첫번째 라인 삭제
sed '3,$d' test.sh  # 3 ~ 끝까지 삭제
sed '/sh/d' test.sh # 'sh' 패턴이 포함된 라인 삭제

-a : append (현재커서에)
sed '1a\abcd' test.sh    # 첫번째 라인 다음(두번째)라인에 abcd 입력
sed '/sh/i\bdc' test.sh  # sh가 포함된 라인 다음 라인에 bcd 입력

-i : insert (현재커서 다음)
sed '1i\bcd' test.sh     # 첫번째 라인에 bcd 입력
sed '/sh/i\bdc' test.sh  # sh가 포함된 라인에 bcd 입력

-p : 출력
sed '1p' test.sh       # 기존 내용에 첫번째 라인 추가 출력
sed -n '1p' test.sh    # 첫번째 라인만 출력 (-n옵션) 
sed -n '/sh/p' test.sh # sh가 포함된 라인만 출력 (-n옵션)

#[sed의 활용]
(주석)
sed '1,5s/^/#' read.sh  # 1~5라인 주석 처리
sed '/^#/d' read.sh     # 시작이 #(주석)인 라인 삭제
(들여쓰기)
sed '1,5s/^/ /' read.sh  # 1줄 들여쓰기
(빈 줄 삭제)
sed ' /^$/d' read.sh  # ^$ (빈줄, enter) 제거
sed ' /^$/d' while.sh
(빈 줄 삽입)
sed 'a\' while.sh
sed 'a\\' while.sh
(패턴 삭제)
sed '/^#/d' read.sh  # 검색된 패턴 삭제
sed '/^#/!d' read.sh # 검색된 패턴 제외하고 삭제

echo abcde > set_test
sed 's/ab/AB/' sed_test

sed 's/ab/AB/' sed_test > sed_test * 불가

sed'1!s/ab/AB/' sed_test  -> 1s : 첫번째 열 / 1!s : 첫번째 열 제외(제외 - !)


# sed 옵션
# -n 실행 명령어의 조건만 출력
sed '1p' read1.sh   -> 첫번째 라인이 두번 출력
sed '1,3p' read1.sh -> 1,3번째 라인 반복

sed -n '1,3p' read1.sh -> -n 1,3번째 라인만 출력

sed '/sh/p' read1.sh -> sh포함된 라인 추가해 출력
sed -n '/sh/p' read1.sh -> sh포함된 라인만 출력

# d 제거 옵션
sed '1d' aaa1 -> 1번째 라인 제거
sed '3,$d' aaa1 ->  3~마지막 라인 제거
sed '^,3d' aaa1 ->  처음부터 3번째 라인 제거


ex)
sed 's/sh/SH/g' test.sh



#==============================================================================
cp /etc/services . -> services를 현재 경로에 복사

[vi 편집기]
(치환)
:s/tcp/TCP -> 현재 커서가 위치한 라인에서 소문자 -> 대문자로 변경
s 현재커서가 위치한 라인에서 변경
:s 편집커서

(g, global)
:s/tcp/TCP/g 
g (global), 현재 라인에 모든 단어 치환

(라인넘버 치환)
:14s/tcp/TCP
:숫자s -> 라인의 범위 s앞에 설정

(20~25, 연속된 범위 치환 / 라인범위 ',')
:20,25s/tcp/TCP

(%s ,전체범위 치환)
:%s/tcp/TCP/g 

(주석처리-전체범위 %s)
:%s/^/# -> ^, 첫 공간부터 

:%s/^#//  * 첫 # 치환



#[연습문제] edit.sh
편집 프로그램 작성
파일명, 찾을 문자열, 바꿀 문자열 입력받은 후
해당파일에서 바뀌기 전, 바뀐 후 화면에 출력한 뒤
'저장할까요' 라는 질문을 전달받아 저장 여부에 따른 실행


#!/bin/sh

echo "파일명 : \c"
read fname

echo "찾을문자열 : \c"
read fword

echo "바꿀문자열 : \c"
read sword

for fname in $(sed 's/$fword/$sword/' $fname)
 do






[실습 10번]
*.sh로 되어있는 파일들에 대해 #으로 주석처리가 되어있는 라인을 모두 삭제하는 
쉘 프로그램 작성(단, 첫 라인의 쉘 표시 된 부분까지 삭제하지 않도록 유의!)

#!/bin/sh

for flist $(find -name "*.sh")








