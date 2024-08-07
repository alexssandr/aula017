from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# conectando ao sqlite

engine = create_engine('sqlite:///meubanco.db', echo=True)

print('conexão com sqlite estabelecida')

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar a tabela do banco

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='alex',idade=40)
session.add(novo_usuario)
session.commit()

print('usuario inserido com sucesso')

usuario = session.query(Usuario).filter_by(nome='alex').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")