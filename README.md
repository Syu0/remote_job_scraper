# remote_job_scraper

결과물 URL + 캡쳐 이미지 2~3장
1. 화면소개 
<img width="1434" alt="search.html 검색화면" src="https://user-images.githubusercontent.com/3899544/150929085-0b520e30-068f-4d63-b31d-7e044732e28c.png">
<img width="1434" alt="report.html 결과화면" src="https://user-images.githubusercontent.com/3899544/150929100-a6d3656a-5820-44e7-8b59-6fe3d547d746.png">
2.서비스 및 기능소개
 검색어를 입력하여 3가지 구직사이트에서 JOB(채용공고)를 수집합니다. 
 결과화면에는 회사이름 / 근무지역 / 급여정보 가 포함됩니다. 
 
/search 화면에서 검색어를 입력합니다.
/report 화면에서 검색결과를 확인합니다. 
 + csv 파일로 다운로드 기능 
 
 검색대상은 https://stackoverflow.com/jobs / https://weworkremotely.com / https://remoteok.com 입니다.
3. python , flask , HTML, Beautifulsoup4, requests 이 사용되었습니다.
4. 앞으로의 계획
 리모트 job 을 대상으로 필터링 될 수 있도록 검색 결과에 대해 필터기능/페이징 기능을 추가할 예정입니다. 
 
5. last updated (2022.01.25)
6. 개발관련 문의 (meaningful.jy@gmail.com)
7. 사용방법
8. flask_main.py 파일을 실행하면 127.0.0.1:5000/search로 접속할 수 있습니다.
