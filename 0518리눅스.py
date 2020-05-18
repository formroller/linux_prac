# [연습문제] vi test4.sh
 디렉터리와 파일 패턴을 입력받고
 파일사이즈가 100이상인 파일의 이름과 번호 함께 출력
 복사할 파일번호 사용자에게 입력 받은 뒤 
 해당 파일을 임의의 디렉터리에 복사하는 셀 작성

#!/bin/sh

#사용자에게 디렉토리, 파일명 입력받고 사이즈 100 이상인 파일 복사

echo "파일 찾을 디렉터리 위치 :\c"
read dname

echo "찾을 패턴 :\c "
read fname

funm=1

for flist in $(find $dname -maxdepth 1 -name "*$fname*" -type f)
do
 fsize=`ls -l $flist | cut -d" " -f5`
 if [ $fsize -ge 100 ]
 then
   echo $funm : $flist
   echo $fnum : $flist >> imsi.txt
   fnum=`expr $fnum + 1 `
 fi
done

echo "복사할 파일 번호를 입력하세요 : \c"
read vnum

cp_file=`grep -w ^$vnum imsi.txt | cut -d" " -f3`

#실제 파일 복사 수행
mkdir -p ~/test 2> /dev/null
cp $cp_file ~/test



# =============================================================================
# # while문

while [ 조건 ]
do
 반복할 문장
done
# =============================================================================

# [while문 예제 : 패스워드 일치할 때까지 묻기]

echo "패스워드 입력 : \c"
read passwd

while [ $passwd != "1234" ]
do
 echo "패스워드 틀림 , 재입력 : \c"
 read passwd
done

echo "옳바른 패스워드"

# =============================================================================


#[연습문제]  while_sum.sh
1부터 100까지 총 합을 아와 같이 출력
1+2+3+...+100 = 5050
    
#!/bin/sh

i=1
while [ $i -le 100 ]
do
 hap=`expr $hap + $i`
 i=`expr $i + 1`
done

echo " 1+2+3...+100 = $hap"

# =============================================================================
#[연습문제]  while2.sh
파일명 : /home/jun/ ../abc.sh

1. 파일 위치출력
2. 파일 사이즈 출력
3. 파일 내용 보기

만약 사용자가 메뉴를 잘못입력하면 다시 원래 매뉴 출력되도록

# [tr 명령어]
 - translaste
 - 선택한 문자들에 대해 치환이나 삭제 수행. (표준 입력을 표준 출력으로 내보낼 때.)
 - (특징) 파일명을 인자로 받지 않음
tr 옵션 찾을문자열 바꿀문자열 < 파일명

# [옵션]
 -d : 글자삭제시 필요

echo abcd | tr 'ab' 'AB'
echo abcda | tr '[a-z]' '[A-Z]'

(삭제)
echo abcda | tr -d 'a'  => bcd

tr '[a-z]' '[A-Z]' test.sh (불가)
tr '[a-z]' '[A-Z]' < test.sh     * 리다이렉션을 통해 한 줄씩 전달 가능
cat test.sh |tr '[a-z]' '[A-Z]'  * 가능

cat a1.sh | tr '[a-z]' '[A-Z]' > a1.sh  * 날아간다.
=> 똑같은 파일의 입출력을 허용하지 않기때문

#[연습문제] tr.sh (l5_tr.sh)
.sh에 대해 문서의 내용을 모두 대문자로 바꾸는 쉘을 작성.
(현재 실행 쉘은 제외)
(단, 입출력이 같은 파일일 경우 파일 손상될 수 있으니 주의)

절대경로로 작성하는게 좋다 (~/linux_ex/ch8/)
cat $fname | tr '[a-z]' '[A-Z]' > $fname_imsi  => 불가, 변수내용에 텍스트 붙이는 방법은 ${fname}_imsi 변수명에 중괄호 사용
cat $fname | tr '[a-z]' '[A-Z]' > ${fname}_imsi

#[1_test.sh]
# $? : 이전 수행한 명령어의 참거짓 여부를 갖는 임시 변수.
# echo $? -> 0 참 / 1 거짓

echo $0 # 실행되는 파일명
echo $1 # 실행되는 파일명 뒤에 붙는 첫번째 인자
echo $2 # 실행되는 파일명 뒤에 붙는 두번째 인자
echo $3 # 실행되는 파일명 뒤에 붙는 세번째 인자
echo $0 # 직전에 실행된 명령어의 참 거짓 여부 (0, 참 / 1, 거짓)

# [cut 명령어]
 - 문자열 추출
 - split, substr 기능 수행
# [옵션]
 -d : 구분자
 -c : 글자위치 전달
 -b : 바이트수 전달
 
-c 단어 
echo abcde | cut -c1    1첫번째 단어 추출
echo abcde | cut -c1,4  1,4 단어 추출
echo abcde | cut -c1-3
echo abdce | cut -c3
echo abcde | cut -c3-   뒤가 생략된 경우 끝까지

-b byte
echo abcde | cut -b3-

# [tee명령어]  
화면 상 출력과 파일에 기록 동시 수행
명령어 | tee 옵션

# [옵션]
 -a : 파일에 연속 쓰기

echo 1234 | tee a1234
echo 5678 | tee a1234 (덮어쓴다.)
echo 8901 | tee -a a1234 (쌓는다.)



# eval 명령어 : 실행 명령어 
 - 입력된 문자를 실행하는 명령어

# [awk 명령어]
 - 자료처리 명령어
 
awk 옵션 '( 실행문장 )' 파일명

#1) 산술연산
awk '{print 1 + 2 }'       * 인자없이 명령어 종료되지 않음
echo | awk '{print 1 +2}'  * echo -> sql의 from dual과 같은 기능

#2) 검색 (=grep)
awk /파일명/ /패턴
grep jun /etc/passwd = cat /etc/passwd | awk /jun
awk /jun/ /etc/passwd

(위치값 기반 cutting)
ls -l test1.sh | cut -d" " -f9
ls -l test1.sh | awk '{print $1}' * 공백은 따로 분리구분기호 사용하지 않음.
ls -l test1.sh | awk '{print $1,$2}'
ls -l test1.sh | awk '{print $1,$NF}' * NF, 마지막 문자열 가져온다.

(문자열 결합)
ls -l test1.sh | awk '{print $1,"is ...",$NF}' * ""기호 사용해 문자열 결합

#3) cut 
(분리구분기호 기반 cutting)
awk -F: '{print $1,"is ...",$NF}' /etc/passwd  * -F, 필드구분자
awk -F: '/jun/ {print $1,"is ...",$NF}' /etc/passwd *jun에 포함된 라인만 실행 검색후 실행

#[연습문제] vi awk.sh
#파일명을 입력받고 파일명과 파일사이즈를 아래와 같이 출력 (단, awk사용)
파일명 : test 사이즈 :110

ls -l | awk '{print "파일명 : ", $NF, "\t","크기 :", $5}