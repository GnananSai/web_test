from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2CKpNXaNba8Kkqc.root:vXvZuAtHltAJ9J1R@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/test?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    'ssl':{
      "ca": "isrgrootx1.pem",
    }
  }
)

def load_login_info():
  with engine.connect() as conn:
    result = conn.execute(text("select id, username, pw from login_info"))
    result_dict = []
    for row in result:
      result_dict.append(row._mapping)
  return(result_dict)

def get_pass(user):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT pw FROM login_info WHERE username = :u"),dict(u=user))
    dumb = []
    for row in result:
      dumb.append(row._mapping)
    return (dumb[0].get('pw'))
    
get_pass('admin')  