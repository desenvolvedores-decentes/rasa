# Rasa X

Rasa and Rasa X

# Passo 1
Instalar docker compose do rasax
- https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose/

# Passo 2
Copiar/sobrescrever arquivos:
- `docker.compose.override.yml`
- `docker.compose.yml`

# Passo 3
Subir docker compose com o comando
```bash
$ docker-compose up -d
```
> Caso queira ver as logs tire a flag -d

# Passo 4
Subir este código em um git e dar acesso a chave ssh fornecida nas logs do compose

# Passo 5
Subir frontend

## Required exposed ports
- 8080 `ou uma de sua escolher`
- 443 `nao e obrigatoria`
- 5005

### requirements
 - pip install python-dotenv
 
 ### Resetar senha
 ```bash
    sudo python3 rasa_x_commands.py create --update admin me <PASSWORD>
 ```
