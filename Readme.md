# 🇬🇧 LingoBot — Assistente Virtual Inteligente para Aprendizado de Inglês

> Projeto desenvolvido como parte do Lab **"Construa seu Assistente Virtual com Inteligência Artificial"** da [Digital Innovation One (DIO)](https://www.dio.me/).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![AI](https://img.shields.io/badge/Google--GenAI-Gemini%202.5--Flash-orange?style=flat)
![License](https://img.shields.io/badge/Licenca-MIT-green?style=flat)

---

## 📌 Visão Geral do Projeto

O **LingoBot** é um assistente virtual e tutor interativo voltado para pessoas que desejam aprender ou praticar a língua inglesa. Diferente de um tradutor comum ou dicionário estático, o LingoBot combina:

- **Análise Contextual de Vocabulário:** Tradução acompanhada de nível de proficiência (A1-C2), sinônimos e exemplos práticos.
- **Reforço Visual Mental:** Uso de descrições visuais e emojis para facilitar a associação e memorização de palavras.
- **Prática de Diálogo com Correção Ativa:** Permite conversação fluida em inglês com feedback gramatical e ortográfico em tempo real.
- **Geração de Exercícios Dinâmicos:** Atividades práticas de tradução e preenchimento de lacunas sob demanda.

---

## 🗂️ Estrutura do Repositório

```text
assistente-virtual-ia/
├── README.md             <- Apresentação do projeto, instruções e os 6 passos
├── data/
│   └── conhecimento.txt  <- Base de conhecimento pedagógica do assistente
├── docs/
│   └── documentacao.md   <- Detalhamento metodológico e de arquitetura
└── src/
    └── main.py           <- Aplicação principal em Python
```    
## 🚀 Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/kekeu0/LingoBot.git
```

## 2. Instalar Dependências

```bash
pip install google-genai python-dotenv
```

## 3. Configurar a Chave da API

Crie um arquivo `.env` na raiz do projeto com a sua chave do Google AI Studio:

```env
GEMINI_API_KEY=sua_chave_aqui
```

## 4. Rodar o LingoBot

```bash
python src/main.py
```

# 🎯 Exemplo de Uso

### Pergunta: `Resilience`

**LingoBot:**

> **Resilience** *(Substantivo)*
>
> * **Tradução:** Resiliência / Capacidade de recuperação.
> * 🖼️ **Dica Visual:** Imagine uma árvore curvando-se com um vento forte de tempestade, mas sem quebrar 🌳🌬️.
> * **Sinônimos:** Adaptability, Toughness.
> * **Exemplo:** *Her resilience helped her overcome the difficulty.*

---

### Entrada: `He go to school yesterday`

**LingoBot:**

> That is great! Going to school is very important. What subject did he study?
>
> 💡 **Correção Didática:**
>
> Como você mencionou uma ação do passado (*yesterday*), o correto é usar o verbo no passado:
>
> ❌ *He go to school yesterday*
>
> ✅ *He **went** to school yesterday*

# 📊 Métricas de Avaliação

| **Métrica**       | **Objetivo**                                                                          |
| ----------------- | ------------------------------------------------------------------------------------- |
| **Assertividade** | O agente responde corretamente ao padrão solicitado (palavra, conversa ou exercício)? |
| **Segurança**     | Evita inventar regras gramaticais ou palavras inexistentes (anti-alucinação)?         |
| **Didática**      | Mantém um tom encorajador e explica os erros de forma amigável e clara?               |
