from database.model import session,User


def create_user(db_session,login,password):
    new_user = User(login=login,password=password)
    db_session.add(new_user)#добавляем нового пользователя
    try:
        db_session.commit()
    except:
        db_session.rollback()
    db_session.refresh(new_user)#чтобы получить id обновляем
    return new_user

def get_all(db_session):
    return db_session.query(User).all()

def get_name(db_session,name):
    return db_session.query(User.id).filter(User.name == name).first()

def del_all(db_session):
    user = db_session.query(User).delete()
    db_session.commit()

db = session


db.close()