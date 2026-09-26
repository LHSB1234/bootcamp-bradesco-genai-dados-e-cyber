import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# ============ CONFIGURAÇÃO E DIRETÓRIOS ============
# Caminho robusto para a raiz do projeto (um nível acima de src/)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Carrega variáveis de ambiente do .env localizado na raiz
load_dotenv(dotenv_path=BASE_DIR / ".env")
API_KEY = os.getenv("GEMINI_API_KEY")
MODELO = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

# ============ CARREGAR BASE DE CONHECIMENTO ============
def carregar_base_conhecimento() -> str:
    """Lê todos os arquivos Markdown da pasta data/ de forma robusta e os concatena."""
    modulos = []
    if DATA_DIR.exists():
        for caminho in sorted(DATA_DIR.glob("*.md")):
            with open(caminho, "r", encoding="utf-8") as f:
                modulos.append(f.read())
    return "\n\n---\n\n".join(modulos)

BASE_CONHECIMENTO = carregar_base_conhecimento()

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = f"""Você é o CyberGuide AI, um assistente educacional especializado em
programação, desenvolvimento web, redes e Cibersegurança.

PÚBLICO: pessoas iniciantes, estudantes e profissionais de Tecnologia.

REGRAS:
- Utilize prioritariamente as informações da BASE DE CONHECIMENTO abaixo.
- Nunca invente definições, comandos, ferramentas ou dados que não estejam
  na base de conhecimento ou que você não tenha certeza de que estão corretos.
- Se a pergunta não puder ser respondida com a base de conhecimento, diga
  isso explicitamente em vez de arriscar uma resposta.
- Adapte a profundidade da resposta ao nível da pessoa (iniciante,
  estudante ou profissional), percebido pela forma como ela pergunta.
- Finalidade educacional e defensiva: se a pergunta envolver testes
  práticos (scans, exploração, ferramentas como Nmap ou Burp Suite),
  reforce que a prática deve ocorrer apenas em ambientes próprios,
  autorizados ou destinados a treinamento (ex.: OWASP Juice Shop, DVWA,
  PortSwigger Web Security Academy). Nunca ajude a atacar sistemas de
  terceiros sem autorização.
- Se a pergunta fugir do tema (programação, redes, Cibersegurança),
  informe educadamente que está fora do seu escopo.
- Responda de forma direta, clara e objetiva.

BASE DE CONHECIMENTO:
{BASE_CONHECIMENTO}
"""

# ============ CHAMAR O GEMINI ============
def perguntar(mensagem: str, historico: list) -> str:
    """Envia a pergunta e o histórico recente para a API do Gemini com tratamento de erros."""
    if not API_KEY or API_KEY in ("coloque_sua_chave_aqui", "sua_chave_aqui"):
        return (
            "**Chave GEMINI_API_KEY não configurada.**\n\n"
            "Para conversar com o CyberGuide AI, crie um arquivo `.env` na raiz do projeto "
            "a partir do `.env.example` e adicione sua chave gratuita do [Google AI Studio](https://aistudio.google.com/apikey)."
        )

    try:
        client = genai.Client(api_key=API_KEY)

        # Monta os conteúdos incluindo as últimas mensagens para manter contexto simples
        contents = []
        # Limita ao histórico recente (últimas 6 mensagens) para não estourar contexto
        for autor, texto in historico[-6:]:
            role = "user" if autor == "user" else "model"
            contents.append(types.Content(role=role, parts=[types.Part.from_text(text=texto)]))

        # Adiciona a pergunta atual
        contents.append(types.Content(role="user", parts=[types.Part.from_text(text=mensagem)]))

        # Configuração oficial do Gemini com system_instruction
        config = types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.2
        )

        resposta = client.models.generate_content(
            model=MODELO,
            contents=contents,
            config=config
        )

        if not resposta.text:
            return "O modelo retornou uma resposta vazia. Tente reformular sua pergunta."

        return resposta.text

    except Exception as err:
        erro_msg = str(err)
        if "429" in erro_msg or "RESOURCE_EXHAUSTED" in erro_msg:
            return "**Limite de cota excedido (Erro 429).** Aguarde alguns instantes antes de enviar uma nova pergunta."
        elif "API_KEY_INVALID" in erro_msg or "PERMISSION_DENIED" in erro_msg or "No API key was provided" in erro_msg:
            return "**Chave de API inválida ou sem permissão.** Verifique se a chave informada no arquivo `.env` está correta."
        elif "NOT_FOUND" in erro_msg or "models/" in erro_msg:
            return f"**Modelo '{MODELO}' não encontrado.** Verifique o nome do modelo configurado no arquivo `.env`."
        elif "ConnectionError" in erro_msg or "Failed to establish a new connection" in erro_msg:
            return "**Falha de conexão com os servidores do Google Gemini.** Verifique sua conexão com a internet."
        else:
            return f"**Ocorreu um erro ao comunicar com a IA:** {erro_msg}"

# ============ INTERFACE (STREAMLIT) ============
st.title("🛡️ CyberGuide AI")
st.caption(f"Assistente educacional de programação, redes e Cibersegurança • Modelo: `{MODELO}`")

# Alerta caso a chave não esteja configurada
if not API_KEY or API_KEY in ("coloque_sua_chave_aqui", "sua_chave_aqui"):
    st.warning("**Aviso:** Configure sua chave `GEMINI_API_KEY` no arquivo `.env` para habilitar as respostas da IA.")

if "historico" not in st.session_state:
    st.session_state.historico = []

# Exibe o histórico de mensagens
for autor, texto in st.session_state.historico:
    st.chat_message(autor).write(texto)

# Entrada do usuário
if pergunta := st.chat_input("Sua dúvida sobre programação, redes ou Cibersegurança..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Consultando base de conhecimento e pensando..."):
        resposta = perguntar(pergunta, st.session_state.historico)

    st.chat_message("assistant").write(resposta)
    # Atualiza o histórico após a resposta
    st.session_state.historico.append(("user", pergunta))
    st.session_state.historico.append(("assistant", resposta))
