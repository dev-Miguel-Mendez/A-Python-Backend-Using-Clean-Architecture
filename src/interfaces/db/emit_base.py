from interfaces.db.engine import SyncEngine



from interfaces.db.declarative_base import Base
import interfaces.db.repositories.user_repository #! Load the models after the Base is loaded above







def emit_base ():
    Base.metadata.create_all(bind=SyncEngine)