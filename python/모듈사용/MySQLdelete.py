import date05.SQL모듈.MySQL연결모듈 as db

id = input('아이디를 입력하세요. ')

db.delete(id)