가상머신 복사방법
1. 리눅스 서버 power off

2. 리눅스 디렉터리 복사
(vmware 홈 디렉터리 하위 리눅스 이름으로 생성 됨.)
=> C:\user\kictcoop\Documenst\Virtual Machines 밑에 ubuntu 디렉터리

3. 이식할 pc에 vmware설치

4. 이식할 pc에 vmware 홈 디렉터리 위 복사본 붙여넣기
(vmware) 홈디렉터리는 기본값이 c:\User\KITCOOP\Documents\Virtual Machines

5. 복사한 디렉터리로 들어가서 Ububtu.vmx 파일 더블 클릭
=> copy or move여부 물어봄 (어떤 것이든 상관 없다.)

6.ipconfig로 VMware Network Adapter vMnet8의 네트워크 영역대 확인

7. 이식한 리눅스 서버의 아이피를 위 영역대로 변경

### 쉘 프로그래밍
 # read 
 read 변수명 : 사용자가 입력한 값을 변수에 저장

###########
*변수의 삽입
v1=1

*생성된 변수 호출시 $기호 사용
v1=1
v2=2
touch a1234
fname=a1234
rm $fname시 a1234도 제거된다.

#명령어 담기 위해 ``기호 사용

*연산
bc -l : 소숫점 표현

echo v1 + 1 | bc (echo-출력 | bc-전달)형식
expr v1 + 1

* vi 편집기
 - which sh로 sh경로 확인후 아래와 같이 작성
 - sh   : 본쉘
 - xsh  : 콘쉘
 - csh  : C쉘
 - bsah : 배쉬쉘 (리눅스용)


cd linux_ex/ch8 vi a.sh * 셀 작성
#!/bin/sh  본쉘로 사용

echo $1
echo $2
echo $3


sh a.sh 1 2 3
sh a.sh aa bb cc dd => cc까지만 출력됨.

cd linux_ex/ch8 vi read.sh
#!/bin/sh

echo "사용자명을 입력하세요 : \c"
read username
echo $username


echo -e :\c 기호 해석

#[if문] 2_read.sh
#!/bin/sh

echo "사용자명을 입력하세요 : \c"
read username

if grep -w ^$username /etc/passwd: > /dev/null (사용자가 있을경우 모니터 출력 날림)
then
 echo "$username 사용자가 있습니다."
esle
 echo "$username 사용자가 없습니다."
fi


[파일 찾기] 3_read.sh
#!/bin/sh

echo "파일명을 입력하시오 : \c"
read fname

if [ -f $fname ]
then 
 echo "$fname 파일이 있습니다."
else
 echo "$fname 파일이 없습니다."
fi

:w (저장)


#[연습문제] 4_read.sh
#사용자로부터 파일명을 입력받고
#해당 파일의 라인수가 50라인 이상이면 큰 파일입니다.
#50라인 이하면 작은 파일입니다. 출력


#!/bin/sh

echo "파일명을 입력하시오 : \c"
read filename

if [ -f $filename ]
then
 echo "$filename은 작은  파일입니다"
 fsize=`cat $filename |wc -l`
 if [ $fsize -ge 50]
 then
  echo "$filename 파일은 큰 파일이다."
 else
echo "$filename은 작은 파일입니다."
 fi
else
 echo "$filename은존재하지 않습니다."
fi

#[case문]

echo "파일명을 입력하시오 : \c"
read filename

if [ -f $filename ]
then
 echo "$filename은 작은  파일입니다"
 fsize=`cat $filename |wc -l`
 if [ $fsize -ge 50]
 then
  echo "$filename 파일은 큰 파일이다."
  echo :$filename 파일을 지울까요? (y|n) : \c"
  read ans
   case $ans in
    Y|y|YES|yes|Yes)
     rm $filename;;
    N|n|NO|no|No)
     echo "$filename 파일을 지우지 않겠습니다." ;;
   *)
    echo "잘못된 입력입니다.";;
  esac
 else
  echo "$filename은 작은 파일입니다."
 fi

#[연습문제] 6_find.sh
#파일을 특정 디렉터리로부터 찾아 출력하는 쉘 프로그램 작성
#사용자로부터 찾을 디렉터리명 입력(1 depth로만 찾기)
#사용자로부터 찾을 파일의 패턴 입력(abc입력시 abc를 포함하는 파일 찾기)

#찾은 파일명을 모두 출력하는 프로그램 작성

find -name "*$fname"

#/bin/sh

clear
echo"파일찾기프로그램"

echo

find #dname -maxdepth 1 -type f -name "*fname*" > flist

clear
echo "파일 목록"

fnum=1
for fname in `cat flist`
do
 echo "$fnum : $fname"
 fnum=`expr $fnum + 1`
done 

echo
echo

#[for] 
1)
for i in a b c d   *리눅스는 인자의 나열
do
 echo $i
done


2) 7_for.sh
j=1
for i in a b c d
do 
 echo "$j : $i"
 j=`expr $j + 1`
done

3) 8_for2.sh
#!/bin/sh

#현 디렉터리에서 *.sh파일 목록을 for문으로 출력
echo "for문 없이 출력"

flist=`ls *.sh`
echo $flist

echo "for문으로 출력"
for i in $flist
do
 echo $i
done

#[연습문제] 9_for3.sh
#현재 디렉터리의 .sh파일에 대해 다음과 같은 형식으로 출력

#파일명 : a.sh  파일라인수 : 7
#파일명 : b.sh  파일라인수 : 10

#!/bin/sh

for fname in $(ls *.sh)
do 
 lcnt=`cat $fname | wc -l`
#lcnt=$(cat $fname | wc -l)
 echo "파일이름 : $fname \t 파일라인수 : $lcnt"
done

sh -x for3.sh
 * 쉘 실행시 -x옵션시 디버깅
  '+'기호는 정상 수행.

#[* winscp : os간 파일 전송]
host - ip 주소

# profile1 이동시 plt 주석처리 (그래픽연결 에러)
  
# =============================================================================
# 문자열 분리 cut
# =============================================================================
cut -d: -f6 /etc/passwd

grep jun /etc/passwd | cut -d: -f6
  cut -d: -f6
  -d 분리구분기호
  -f6 분리된 구분기호중 몇번째 필드 가져올 것인지


ls -l *.sh
ls -l. *sh | cut -d" " -f1
 - 공백일 경우 -d" "
 - 모든 라인의 공백 다를 경우 cut 출력시 조건에 맞지 않는 값은 공백출력
 
#[연습문제] 10_for4.sh
# 현재 디렉토리에서 .sh파일에 대해 아래와 같이 출력 (test3)

#파일명 : a.sh  파일라인수 : 7    파일크기 : 10
#파일명 : b.sh  파일라인수 : 10   파일크기 : 300

#!/bin/sh
 
for fname in $(ls *.sh)
 do 
 lcnt=`cat $frame | wc -l`
 fsize=`ls -l $fname | cut -d" " -f5`
 echo "파일명 : $fname \t 파일라인수 : $lcnt \t 파일크기 : $fsize"
done
 
 
# [연습문제] 11_ex.sh
 디렉터리와 파일 패턴을 입력받고
 파일사이즈가 100이상인 파일의 이름과 번호 함께 출력
 복사할 파일번호 사용자에게 입력 받은 뒤 
 해당 파일을 임의의 디렉터리에 복사하는 셀 작성
 

#파일명 : a.sh  파일라인수 : 7
#파일명 : b.sh  파일라인수 : 10

#!/bin/sh

# 사용자에게 디렉터리, 파일명 입력받고 사이즈 100 이상인 파일 복사
 
echo "파일 찾을 디렉터리 위치 :\c"
read dname

echo "찾을 패턴 :\c"
read fname

fnum=1
for flist in $(find $dname -maxdepth 1 -name "*$fname*" -type f):
do 
 fsize=`ls -l $flist | cut -d" " -f5`
 if [ $fsize -ge 100 ]:
 then 
   echo $fnum : $flist
   fnum=`expr $fnum + 1`
  fi
done

echo "복사할 파일번호 입력 :\c "
read vnum




for fname in $(ls *.sh)
do 
 lcnt=`cat $fname | wc -l`
 echo "파일이름 : $fname \t 파일라인수 : $lcnt"
done

sh -x for3.sh
 * 쉘 실행시 -x옵션시 디버깅
  '+'기호는 정상 수행.
