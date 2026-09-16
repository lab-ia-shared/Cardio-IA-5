# 💓 CardioIA - A Nova Era da Cardiologia Inteligente

## 📋 Descrição do Projeto

O **CardioIA** é um projeto acadêmico inovador focado na convergência entre tecnologia de ponta e saúde cardiovascular. O objetivo é desenvolver uma plataforma digital que simule um ecossistema cardiológico moderno, integrando dados clínicos, modelos de Machine Learning, Visão Computacional, IoT e, agora, Agentes Virtuais para triagem e orientação de pacientes.

Nesta **Fase 5 – Suporte Digital ao Paciente (Assistente Cardiológico Virtual)**, o projeto avança para a comunicação inteligente utilizando Processamento de Linguagem Natural (NLP). Assumimos o desafio de construir um chatbot conversacional simpático e eficiente, capaz de interagir com o usuário, interpretar sintomas relatados em linguagem natural e apresentar respostas contextualizadas, servindo como uma triagem primária e plataforma de orientação em saúde.

## 👨‍⚕️ Integrantes da Equipe
- <a href="https://www.linkedin.com/in/nicolas--araujo/">Nicolas Antonio Silva Araujo</a> (RM: 566307)
- <a href="https://www.linkedin.com/in/vitoria-bagatin-31ba88266/">Vitória Pereira Bagatin</a> (RM: 566519)

## 📂 Estrutura de Arquivos

A organização do repositório reflete a arquitetura de integração entre Inteligência Artificial, Backend e Interface do Usuário:

```text
Cardio-IA-5/
│
├── backend/
│   ├── app.py                           # Servidor Flask e integração com a API da IBM
│   ├── assistente_cardioia.json         # Backup das Intents/Entities do Watson Assistant
│
├── frontend/
│   └── index.html                       # Interface web interativa do chatbot (HTML/CSS/JS)
│
├── docs/
│   └── CardioIA-5_Relatorio_Fluxo.pdf   # Justificativas técnicas, arquitetura e fluxo conversacional
│
│
└── README.md                            # Documentação principal do projeto
```

## 🧠 1. Modelagem Conversacional (IBM Watson Assistant)
Para garantir que o assistente compreenda as variações da linguagem humana, modelamos a inteligência do chatbot utilizando a plataforma IBM Watson:

* **Intents (Intenções):** Mapeamento das motivações do usuário, treinadas com variações de frases para identificar saudações, relatos de sintomas cardíacos (como dor no peito e falta de ar), dúvidas sobre pressão arterial e situações de emergência.
* **Entities (Entidades):** Dicionários configurados para extrair dados específicos das frases, como tipos de sintomas e classificações de níveis de pressão.
* **Dialog Nodes (Árvore de Diálogo):** Fluxo lógico de respostas programadas para guiar a conversa, incluindo tratativas de exceção (Fallback) caso a inteligência não compreenda o relato do paciente.

## ⚙️ 2. Arquitetura de Backend (Python & Flask)
A comunicação entre o modelo de NLP na nuvem e a interface do usuário é orquestrada por um servidor robusto e leve:

* **API RESTful:** Implementação de rotas via Flask para receber as requisições HTTP (`POST`) vindas da interface.
* **Integração SDK:** Uso da biblioteca `ibm-watson` para autenticação via IAM (Identity and Access Management) e troca de mensagens bidirecional e segura com o Workspace do IBM Watson Assistant.
* **Tratamento de CORS:** Configuração de Cross-Origin Resource Sharing para permitir a fluidez de dados entre o frontend local e o backend de processamento.

## 🖥️ 3. Interface do Usuário (Frontend)
Para simular um ambiente de telessaúde realista e acessível, desenvolvemos uma interface conversacional customizada:

* **Design Responsivo:** Construída com HTML, CSS e JavaScript Vanilla, apresentando uma UI limpa e focada em acessibilidade (cores e contrastes voltados para o bem-estar).
* **Comunicação Assíncrona:** Utilização da `Fetch API` no JavaScript para enviar as dúvidas do paciente ao backend e renderizar as respostas do Watson na tela em tempo real, sem recarregamento da página.

## 🚀 4. Desafios Extras (Ir Além)
Para aprofundar as capacidades do ecossistema CardioIA, implementamos módulos avançados de automação e dados estruturados:

* **IA Generativa (LLMs):** Aplicação de técnicas de engenharia de prompt para extrair informações vitais de textos clínicos não estruturados, convertendo-os em saídas organizadas (JSON).
* **Automação RPA & Dados Híbridos:** Construção de um robô que realiza varreduras em bancos de dados relacionais (ex.: monitoramento de frequência cardíaca) e registra logs e anomalias em bancos não relacionais, emitindo alertas rastreáveis.

## 🎥 5. Demonstração Prática
Confira o assistente em funcionamento, desde a ingestão da dúvida pelo paciente até a resposta inteligente gerada pelo sistema:

🔗 **[Assista ao Vídeo de Demonstração (YouTube)](https://youtu.be/waaFQevwlEM)**

## 🛡️ Governança, Ética e Empatia no Atendimento Digital
Assim como o processamento de imagens exige responsabilidade, o uso de IA Conversacional na saúde lida com a sensibilidade humana e a privacidade:

* **Clareza de Identidade:** O assistente é programado para deixar claro, desde a saudação inicial, que é uma Inteligência Artificial, e não um médico humano.
* **Limites Diagnósticos:** O modelo foi treinado para orientar e realizar triagem básica. Sob nenhuma circunstância o bot prescreve medicações.
* **Gatilhos de Emergência:** Implementamos fluxos rígidos onde a detecção de palavras-chave críticas (como "infarto", "dor forte no braço") aciona imediatamente mensagens orientando o contato com o SAMU (192) ou busca por pronto-socorro.
* **Privacidade de Dados:** A arquitetura garante que as mensagens trafeguem apenas entre o cliente e o serviço cognitivo configurado, simulando o rigor exigido pela LGPD em sistemas reais de saúde digital.
