-- Geração de Modelo físico
-- Sql

CREATE TABLE faz (
id_usuario int,
id_sugestao int
)

CREATE TABLE contem (
id_atividade int,
id_aula int
)

CREATE TABLE Login (
id_login int PRIMARY KEY,
data_login date
)

CREATE TABLE entra (
id_aula int,
id_usuario int
)

CREATE TABLE Sugestao_usuario (
id_sugestao int PRIMARY KEY,
comentario_sugestao varchar(240)
)

CREATE TABLE Cadastro_usuario (
id_usuario int PRIMARY KEY,
email varchar(50),
p_nome varchar(30),
s_nome varchar(30),
senha_usuario char(64),
tipo_conta int,
id_ranking int,
id_login int,
FOREIGN KEY(id_login) REFERENCES Login (id_login)
)

CREATE TABLE Aula (
id_aula int PRIMARY KEY,
nome_aula varchar(30),
descricao_aula varchar(240),
data_up_aula date,
video_aula varchar
)

CREATE TABLE Atividade (
id_atividade int PRIMARY KEY,
nome_atividade varchar(30),
descricao_atividade varchar(240),
id_ranking int
)

CREATE TABLE Ranking (
id_ranking int PRIMARY KEY,
tipo_ranking varchar(30),
classificacao_aluno int,
pontuacao_aluno decimal(7,2)
)

ALTER TABLE faz ADD FOREIGN KEY(id_usuario) REFERENCES Cadastro_usuario (id_usuario)
ALTER TABLE faz ADD FOREIGN KEY(id_sugestao) REFERENCES Sugestao_usuario (id_sugestao)
ALTER TABLE contem ADD FOREIGN KEY(id_atividade) REFERENCES Atividade (id_atividade)
ALTER TABLE contem ADD FOREIGN KEY(id_aula) REFERENCES Aula (id_aula)
ALTER TABLE entra ADD FOREIGN KEY(id_aula) REFERENCES Aula (id_aula)
ALTER TABLE entra ADD FOREIGN KEY(id_usuario) REFERENCES Cadastro_usuario (id_usuario)
ALTER TABLE Cadastro_usuario ADD FOREIGN KEY(id_ranking) REFERENCES Ranking (id_ranking)
ALTER TABLE Atividade ADD FOREIGN KEY(id_ranking) REFERENCES Ranking (id_ranking)
