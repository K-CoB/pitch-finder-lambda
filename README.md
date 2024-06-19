# Pitch Finder 
부를 노래 추천을 위한 음역대 측정 기반 노래 필터링 서비스

> ‘들을’ 노래가 아닌 ‘부를’ 노래를 찾기 위해 <br/>
> 개인 음역대를 측정하고 측정된 음역대를 기반으로 <br/>
> 노래를 필터링하는 서비스, 피치파인더

<br/>

## 🧑‍🤝‍🧑 Team
|<img src="https://avatars.githubusercontent.com/u/79985974?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/75469131?v=4" width="150" height="150"/>|<img src="https://avatars.githubusercontent.com/u/89910703?v=4" width="150" height="150"/>|
|:-:|:-:|:-:|
|[@chaeri93](https://github.com/chaeri93)|[@seondal](https://github.com/seondal)|[@CSE-pebble](https://github.com/CSE-pebble)|
|데이터 수집 & 백엔드 개발|프론트엔드 개발|팀장 & 프론트엔드 개발|

<br/>


##  🛠️ How to install
- 본 레포 clone `git clone https://github.com/K-CoB/pitch-finder-frontend`
- 클론한 프로젝트 폴더를 연다
- [[AWS] API Gateway + Lambda + RDS(Mysql)로 서버리스 서버 구축하기](https://velog.io/@chaeri93/AWS-API-Gateway-Lambda-RDSMysql%EB%A1%9C-%EC%84%9C%EB%B2%84-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0#api-gateway-%EC%84%A4%EC%A0%95) : aws 클라우드 구축
- AWS Lambda 함수에 폴더 업로드

  
<br/>

## 📚 Stack
| **Section**       | Tech        |
| ---------------- | ---------------------------- |
| **인프라**       | AWS Lambda, API Gateway, CloudWatch      |
| **언어**         | Python                       |
| **데이터베이스** | MySQL, AWS RDS               |
| **데이터** | BeautifulSoup, Youtube API        |

<br/>

## 🔐 System Architecture
<img width="816" alt="image" src="https://github.com/K-CoB/pitch-finder-lambda/assets/79985974/c119c65a-5870-445e-8410-5032825995df">

<br/>

## 🗂️ Folder Structure
```python
pitch-finder-lambda
├── PyMySQL-1.1.0.dist-info # 데이터베이스에 접근하기 위한 pymysql 라이브러리
│   ├── INSTALLER
│   ├── LICENSE
│   ├── METADATA
│   ├── RECORD
│   ├── REQUESTED
│   ├── WHEEL
│   └── top_level.txt
├── lambda_function.py # 이 파일 통해 람다 호출하여 이벤트(api)를 처리
└── pymysql # 데이터베이스에 접근하기 위한 pymysql 라이브러리
```
