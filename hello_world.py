#como criar um ambiente virtual
#como colocar uma versão do python especifica
#fazer um procedimento usar o deepseek
"""
No Zorin OS 17.03, você pode criar e gerenciar um ambiente virtual Python usando o terminal e, em seguida, configurá-lo no VS Code. O processo é direto e isola as dependências do seu projeto.

### 📝 Criar e Ativar o Ambiente Virtual pelo Terminal

Siga estes passos no terminal para criar e ativar seu ambiente virtual. É uma boa prática criar uma pasta para seu projeto primeiro.

| Passo | Comando / Ação | Descrição |
| :--- | :--- | :--- |
| **1. Criar Pasta** | `mkdir meu_projeto && cd meu_projeto` | Cria e navega para a pasta do projeto. |
| **2. Criar Ambiente** | `python3 -m venv venv` | Cria uma pasta `venv` com o ambiente virtual. |
| **3. Ativar** | `source venv/bin/activate` | Ativa o ambiente (o prompt mudará para `(venv)`). |

### ⚙️ Usar o Ambiente Virtual no VS Code

1.  **Abrir a Pasta no VS Code**: Na pasta do projeto (`meu_projeto`), execute `code .` ou abra manualmente.
2.  **Selecionar o Interpretador Python**:
    *   Abra o Command Palette com `Ctrl+Shift+P`.
    *   Digite e selecione **`Python: Select Interpreter`**.
    *   Escolha o interpretador que está no caminho `./venv/bin/python`.

### 🗃️ Gerenciar Dependências e Finalizar o Trabalho

Com o ambiente ativo (indicado no terminal como `(venv)`), use o `pip` para instalar pacotes. Essas bibliotecas ficarão isoladas no ambiente do projeto.

*   **Instalar Pacotes**: Por exemplo, `pip install requests`.
*   **Salvar Dependências**: Use `pip freeze > requirements.txt` para criar uma lista de pacotes. Compartilhe esse arquivo para que outros possam recriar o ambiente com `pip install -r requirements.txt`.
*   **Desativar o Ambiente**: Execute `deactivate` no terminal quando terminar.

Se encontrar problemas para criar o ambiente, verifique se o pacote `python3-venv` está instalado com `sudo apt install python3-venv`.

Espero que este guia ajude a configurar seu ambiente de desenvolvimento. Se tiver mais dúvidas, é só perguntar!

"""
#como excluir o ambiente virtual
#como instalar o pyenv com versão especifica do python
"""
Excluir um ambiente virtual Python é um processo simples: basta desativá-lo e depois apagar a pasta onde ele foi criado.

### 🗑️ Guia para Excluir um Ambiente Virtual

Siga estes dois passos no terminal do seu VSCode para remover o ambiente virtual com segurança.

| Passo | Comando / Ação | Observações |
| :--- | :--- | :--- |
| **1. Desativar o Ambiente** | `deactivate` | Execute no terminal. O prefixo `(venv)` some do _prompt_. |
| **2. Excluir a Pasta** | `rm -rf venv` | Remove a pasta "venv" e todo seu conteúdo. Confirme o nome da pasta antes. |

> **⚠️ Atenção:** Nunca tente desinstalar ou modificar a versão do Python que veio com o seu sistema operacional Zorin, pois isso pode danificar seu sistema.

No VS Code, lembre-se também de **selecionar um novo interpretador Python** (em `Ctrl+Shift+P` > "Python: Select Interpreter") se for continuar programando, para que o editor não tente usar o ambiente que já foi excluído.

Espero que estas instruções tenham ajudado. Se tiver mais alguma dúvida, é só perguntar!
"""
#como trabalhar com o git e github
#https://youtu.be/-VeVq64Fgw0?t=299

print("hello world")