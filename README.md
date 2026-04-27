# ☢︎ SimuLock v1.0
### Educational Ransomware Simulation

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Security](https://img.shields.io/badge/focus-cybersecurity-red?style=for-the-badge)

## Sobre o Projeto

O **SimuLock** é uma simulação de ransomware desenvolvida para fins acadêmicos, com o objetivo de demonstrar conceitos de:

- Criptografia moderna
- Segurança da informação
- Controle de execução
- Simulação de ataques cibernéticos em ambiente seguro

> ⚠︎ Este projeto é estritamente educacional e não deve ser utilizado para fins maliciosos.

## Funcionalidades

- Criptografia de arquivos com AES-256 GCM
- Descriptografia mediante chave correta
- Controle de execução (evita reprocessamento)
- Sistema de logs
- Interface gráfica estilo ransomware
- Contador regressivo fake
- Alertas dinâmicos

## Estrutura do Projeto
```
ransomware_sim/
│
├── main.py
├── crypto.py
├── scanner.py
├── logger.py
├── control.py
├── ui.py
├── ui_gui.py
│
├── test_files/
└── logs/
```
## Como Executar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/simulock.git
cd simulock
```

### 2. Crie um ambiente virtual
```
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instale dependências
```
pip install cryptography
```

### 4. Execute
```
python main.py
```

### Como Testar

- Adicione arquivos na pasta `test_files/`
- Execute o sistema
- Observe:
  - arquivos sendo criptografados (`.locked`)
  - interface gráfica sendo exibida
- Insira a chave correta para recuperar

### Logs

Os logs são armazenados em:

`logs/log.txt`

Exemplo:
```
2026-xx-xx - Início da execução
2026-xx-xx - Criptografado: test_files/teste.txt
2026-xx-xx - Descriptografado: test_files/teste.txt
```

### Tecnologias

- Python 3
- Cryptography (AES-GCM)
- Tkinter (GUI)
- React + TypeScript (UI alternativa)

### Aviso Legal

⚠︎ Este projeto foi desenvolvido exclusivamente para fins educacionais.

⏺︎ Não utilize este código para atividades maliciosas  
⏺︎ Não execute em ambientes com dados reais  

### Autor

Desenvolvido por m4ntonio