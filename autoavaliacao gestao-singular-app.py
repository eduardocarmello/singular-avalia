import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Autoavaliação: Gestão da Singularidade",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS customizado para uma estética profissional e moderna
st.markdown("""
<style>
    .main {
        background-color: #f7f9fb;
    }
    h1, h2, h3 {
        color: #113f48 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .stProgress > div > div > div > div {
        background-color: #113f48;
    }
    .metric-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #113f48;
        margin-bottom: 20px;
    }
    .custom-title {
        text-align: center;
        padding: 10px;
        background: linear-gradient(135deg, #113f48 0%, #1c5e69 100%);
        color: white !important;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    .custom-title h1 {
        color: white !important;
    }
    .pilar-header {
        background-color: #eef4f6;
        padding: 10px 15px;
        border-radius: 5px;
        border-left: 4px solid #113f48;
        margin-top: 25px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho principal do App
st.markdown("""
<div class="custom-title">
    <h1>Autoavaliação de Maturidade: Você é um Gestor Singular?</h1>
    <p style="font-size: 1.1rem; margin-top: -5px;">Baseado na metodologia de Eduardo Carmello — Gestão da Singularidade</p>
</div>
""", unsafe_allow_html=True)

# Introdução
st.markdown("""
No dia a dia corporativo, tratar sua equipe como um bando ou estatística uniforme é o caminho mais rápido para desperdiçar talentos e gerar desengajamento. 
O **Gestor Singular** joga **Xadrez** em vez de **Damas**: ele reconhece que cada profissional possui uma história única de contribuição, disposição e proficiência.

Este mini-app interativo foi projetado para avaliar o seu nível de maturidade como líder diante das **9 práticas de gestão mais impactantes**.
Avalie sua atuação de forma honesta de **0 a 10** em cada prática.
""")

st.write("---")

# Sidebar com informações do Workshop e instruções de Deploy
st.sidebar.markdown("""
<div style='text-align: center; padding: 10px; background-color: #113f48; color: white; border-radius: 5px; margin-bottom: 20px;'>
    <h3 style='color: white !important; margin: 0;'>Workshop Singular</h3>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
### 🚀 Como usar no seu Workshop
Para que os participantes do seu workshop utilizem este aplicativo em tempo real no celular:

1. **Baixe este arquivo** (`gestao-singular-app.py`) do painel Studio.
2. **Crie um repositório gratuito** no GitHub e envie este arquivo para lá.
3. **Acesse [share.streamlit.io](https://share.streamlit.io)**, faça login com sua conta do GitHub e aponte para o arquivo.
4. **Pronto!** O Streamlit gerará um link público gratuito.
5. **Gere um QR Code** desse link e coloque no slide de apresentação para que seus participantes acessem instantaneamente pelo celular.
""")

st.sidebar.write("---")
st.sidebar.markdown("""
### 📊 Sobre as Notas:
* **9.0 a 10.0:** Excelência Singular (Mestre)
* **7.0 a 8.9:** Gestor em Evolução (Proficiente)
* **Abaixo de 7.0:** Gestor Tradicional (Aprendiz)
""")

# Formulário da Autoavaliação
with st.form("autoavaliacao_form"):
    
    # --- PILAR 1 ---
    st.markdown('<div class="pilar-header"><h3>📐 Pilar 1: Orientação Estratégica (O Norte)</h3></div>', unsafe_allow_html=True)
    st.markdown("*Garante que a equipe saiba exatamente para onde ir e o que é esperado dela, eliminando ambiguidades.*")
    
    p1 = st.slider(
        "1. Comunico e esclareço o Norte e os Objetivos Estratégicos.",
        min_value=0, max_value=10, value=5, step=1,
        help="Você traduz a estratégia macro da empresa em metas claras para o cotidiano de cada colaborador?"
    )
    
    p2 = st.slider(
        "2. Defino valores, expectativas de performance, regras, critérios e procedimentos específicos.",
        min_value=0, max_value=10, value=5, step=1,
        help="Suas regras de entrega são transparentes de modo que a equipe saiba o COMO e o QUE fazer?"
    )
    
    p3 = st.slider(
        "3. Elimino as ambiguidades de decisão, prioridades e/ou responsabilidades.",
        min_value=0, max_value=10, value=5, step=1,
        help="Você atua como um desatador de nós, esclarecendo papéis e impedindo conflitos de prioridade?"
    )

    # --- PILAR 2 ---
    st.markdown('<div class="pilar-header"><h3>🤝 Pilar 2: Incorporação de Valores & Engajamento</h3></div>', unsafe_allow_html=True)
    st.markdown("*Cria conexões éticas de valor, promovendo senso de justiça e mantendo a equipe mobilizada na turbulência.*")
    
    p4 = st.slider(
        "4. Envolvo-me e demonstro maior engajamento no papel de Gestor (administrando conflitos e gerando coerência).",
        min_value=0, max_value=10, value=5, step=1,
        help="Você é o guardião dos valores da marca, agindo com coerência entre o que é declarado e o que é praticado?"
    )
    
    p5 = st.slider(
        "5. Consigo promover o senso de equipe, gerenciando-a de forma singular e justa.",
        min_value=0, max_value=10, value=5, step=1,
        help="Você evita sermões coletivos e diferencia com justiça quem entrega acima da média daquele que entrega abaixo?"
    )
    
    p6 = st.slider(
        "6. Quando a equipe está sobrecarregada, transmito compreensão, apoio, confirmação e reconhecimento.",
        min_value=0, max_value=10, value=5, step=1,
        help="Você oferece suporte emocional e operacional real ou apenas exige 'comprometimento' sem dar apoio?"
    )

    # --- PILAR 3 ---
    st.markdown('<div class="pilar-header"><h3>🧠 Pilar 3: Capacitação de Talentos</h3></div>', unsafe_allow_html=True)
    st.markdown("*Desenvolve as pessoas no fluxo de trabalho com foco no desempenho prático e compartilhamento de conhecimento.*")
    
    p7 = st.slider(
        "7. Proporciono instrução, feedback e apoio para melhorar o desempenho.",
        min_value=0, max_value=10, value=5, step=1,
        help="Seus feedbacks são constantes e baseados em evidências/fatos em vez de opiniões pessoais?"
    )
    
    p8 = st.slider(
        "8. Construo espaços de conversação e compartilhamento de conhecimento (Conceito BA).",
        min_value=0, max_value=10, value=5, step=1,
        help="Você promove reuniões ágeis ou comunidades de prática para desatar restrições de processos operacionais?"
    )
    
    p9 = st.slider(
        "9. Verifico constantemente o curso de ação dos processos e atividades estratégicas.",
        min_value=0, max_value=10, value=5, step=1,
        help="Você acompanha o curso da ação de perto, ou apenas cobra no último dia quando o prazo já estourou?"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button("📊 Calcular Meu Nível de Maturidade")

# Ações pós-submissão do formulário
if submit_button:
    # Cálculo das médias por pilar e geral
    media_orientacao = (p1 + p2 + p3) / 3
    media_engajamento = (p4 + p5 + p6) / 3
    media_capacitacao = (p7 + p8 + p9) / 3
    media_geral = (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9) / 9
    
    # Layout de exibição dos resultados
    st.markdown("<h2>🎯 Seus Resultados</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <p style="color: gray; margin: 0; font-size: 0.9rem;">MÉDIA GERAL</p>
            <h2 style="margin: 0; color: #113f48;">{media_geral:.1f} / 10</h2>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-box" style="border-left-color: #1c5e69;">
            <p style="color: gray; margin: 0; font-size: 0.9rem;">ORIENTAÇÃO</p>
            <h2 style="margin: 0; color: #1c5e69;">{media_orientacao:.1f} / 10</h2>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-box" style="border-left-color: #3b8a95;">
            <p style="color: gray; margin: 0; font-size: 0.9rem;">ENGAJAMENTO</p>
            <h2 style="margin: 0; color: #3b8a95;">{media_engajamento:.1f} / 10</h2>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-box" style="border-left-color: #5bb3bf;">
            <p style="color: gray; margin: 0; font-size: 0.9rem;">CAPACITAÇÃO</p>
            <h2 style="margin: 0; color: #5bb3bf;">{media_capacitacao:.1f} / 10</h2>
        </div>
        """, unsafe_allow_html=True)

    # Classificação do Líder
    status = ""
    cor_status = ""
    descricao_status = ""
    
    if media_geral >= 8.5:
        status = "GESTOR SINGULAR (MESTRE)"
        cor_status = "#113f48"
        descricao_status = """
        **Parabéns! Sua maturidade é de nível excelente.** 
        Você já abandonou as práticas rasas do modelo de comando e controle tradicional. 
        Você enxerga e trata os membros de sua equipe como **sujeitos** corresponsáveis pelas entregas. 
        Sua gestão é baseada em processos justos, meritocracia autêntica e suporte no fluxo de trabalho (*just for you, just in time, just enough*). 
        Seu maior legado é desenvolver uma equipe tão autônoma e madura que você caminha para se tornar estrategicamente dispensável.
        """
    elif media_geral >= 6.0:
        status = "GESTOR EM TRANSIÇÃO (PROFICIENTE)"
        cor_status = "#e67e22"
        descricao_status = """
        **Você está no caminho certo, mas ainda mescla práticas singulares com hábitos tradicionais.**
        Muitas vezes, sob pressão ou turbulência, você pode escorregar de volta para o modelo de cobrança estéril (jogar Damas) ou aplicar sermões generalizados à equipe. 
        Seus talentos de alta performance (Grupo A) podem estar sentindo falta de um reconhecimento mais específico e de maior autonomia. 
        Foque em refinar a constância do acompanhamento, criando rituais estruturados de feedback baseados estritamente em evidências, eliminando notas e bônus artificiais e generalistas.
        """
    else:
        status = "GESTOR TRADICIONAL (APRENDIZ)"
        cor_status = "#c0392b"
        descricao_status = """
        **Atenção! Sua liderança está altamente concentrada no modelo tradicional de comando e controle.**
        Você provavelmente está 'jogando Damas', tratando todos na equipe de forma igualitária e pulverizada. 
        Soluções baseadas em broncas coletivas ou em buscar palestras motivacionais passageiras (como 'rafting na sexta-feira') não estão resolvendo as quedas de desempenho. 
        Sua equipe está saturada de informações genéricas, mas sedenta por conhecimento procedural claro (*como fazer*). 
        Comece imediatamente a segmentar a comunicação de forma justa para os grupos A, B e C, estabeleça promessas de metas claras e use o Mapa de Performance para direcionar o desenvolvimento.
        """

    st.markdown(f"""
    <div style="background-color: #fcfcfc; padding: 25px; border-radius: 8px; border: 1px solid #e1e8ed; margin-bottom: 30px;">
        <h3 style="margin-top: 0; color: {cor_status} !important;">🏆 Nível de Maturidade: {status}</h3>
        <p style="font-size: 1.05rem; line-height: 1.6;">{descricao_status}</p>
    </div>
    """, unsafe_allow_html=True)

    # Criação de Gráficos Comparativos com Plotly
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        st.markdown("### 📊 Gráfico de Desempenho por Pilar")
        df_pilares = pd.DataFrame({
            'Pilar': ['Orientação Estratégica', 'Valores & Engajamento', 'Capacitação de Talentos'],
            'Sua Média': [media_orientacao, media_engajamento, media_capacitacao]
        })
        fig = px.bar(
            df_pilares, x='Pilar', y='Sua Média',
            range_y=[0, 10], text='Sua Média',
            color='Pilar',
            color_discrete_sequence=['#113f48', '#3b8a95', '#5bb3bf']
        )
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig.update_layout(showlegend=False, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)

    with col_g2:
        st.markdown("### 🕸️ Mapa de Forças das 9 Práticas")
        
        categories = ['Norte Claro', 'Expectativas', 'Sem Ambiguidade', 
                      'Papel de Gestor', 'Senso de Equipe', 'Suporte Pressão',
                      'Instrução/Feedback', 'Espaços BA', 'Verificar Curso']
        values = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
        
        fig_radar = go.Figure(data=go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill='toself',
            fillcolor='rgba(17, 63, 72, 0.2)',
            line=dict(color='#113f48', width=2)
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=False,
            margin=dict(t=30, b=30, l=50, r=50)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    # Diretrizes de Ação para o Gestor de acordo com cada dimensão
    st.markdown("<h2>🛠️ Plano de Ação Personalizado</h2>", unsafe_allow_html=True)
    
    rec_orientacao = ""
    if media_orientacao >= 8.5:
        rec_orientacao = "Mantenha a transparência. Continue envolvendo sua equipe na cocriação de soluções estratégicas, mantendo o norte visível e banindo em definitivo qualquer ambiguidade de papéis."
    elif media_orientacao >= 6.0:
        rec_orientacao = "Esclareça as regras e as promessas de entrega. Reserve 15 minutos por semana para alinhar as prioridades individuais com seus colaboradores B e C, evitando que fiquem apagando incêndios desnecessários."
    else:
        rec_orientacao = "Pare de apenas cobrar metas genéricas por e-mail. Construa um Mapa de Performance (Matriz 3x3) definindo as 5 competências essenciais e as respectivas habilidades de desempenho que sua equipe realmente precisa manifestar."

    rec_engajamento = ""
    if media_engajamento >= 8.5:
        rec_engajamento = "Sua meritocracia é forte. Continue reconhecendo e recompensando quem realmente gera valor e mantendo consequências firmes para atitudes desalinhadas aos valores éticos da marca."
    elif media_engajamento >= 6.0:
        rec_engajamento = "Cuidado com o 'efeito bônus generalista' (onde todos tiram nota alta para receber bonificação, gerando injustiça). Agradeça de forma específica as contribuições do Grupo A e dê apoio próximo ao Grupo B."
    else:
        rec_engajamento = "Erradique broncas e sermões coletivos na equipe. Eles geram desânimo nos que performam bem e não resolvem a atitude de quem vai mal. Segmente sua comunicação imediatamente e aja com fatos, não com opiniões."

    rec_capacitacao = ""
    if media_capacitacao >= 8.5:
        rec_capacitacao = "Sua liderança como mentor/coach é evidente. Continue promovendo e sustentando os Espaços BA de aprendizagem e estimulando que seus Talentos A assumam o papel de ensinar os demais."
    elif media_capacitacao >= 6.0:
        rec_capacitacao = "Aumente a frequência dos feedbacks informais de desenvolvimento. Não espere a avaliação anual de desempenho. Ajude o Grupo B a focar em 1 ou 2 competências prioritárias para eles subirem de patamar."
    else:
        rec_capacitacao = "Não encaminhe profissionais para treinamentos genéricos (como cursos corporativos massificados) sem antes diagnosticar os Fatores Internos (FID) e Externos (FED) de Desempenho. Muitas vezes a queda de resultado ocorre por falta de ferramentas, processos disfuncionais ou desengajamento, e não por falta de conhecimento."

    col_rec1, col_rec2, col_rec3 = st.columns(3)
    with col_rec1:
        st.markdown(f"""
        <div style="background-color: #f7f9fb; padding: 20px; border-radius: 8px; border-top: 5px solid #1c5e69; height: 100%;">
            <h4 style="margin-top: 0; color: #1c5e69;">📐 Em Orientação Estratégica</h4>
            <p style="font-size: 0.95rem; line-height: 1.5; color: #333333;">{rec_orientacao}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_rec2:
        st.markdown(f"""
        <div style="background-color: #f7f9fb; padding: 20px; border-radius: 8px; border-top: 5px solid #3b8a95; height: 100%;">
            <h4 style="margin-top: 0; color: #3b8a95;">🤝 Em Valores & Engajamento</h4>
            <p style="font-size: 0.95rem; line-height: 1.5; color: #333333;">{rec_engajamento}</p>
        </div>
        """, unsafe_allow_html=True)
    with col_rec3:
        st.markdown(f"""
        <div style="background-color: #f7f9fb; padding: 20px; border-radius: 8px; border-top: 5px solid #5bb3bf; height: 100%;">
            <h4 style="margin-top: 0; color: #5bb3bf;">🧠 Em Capacitação de Talentos</h4>
            <p style="font-size: 0.95rem; line-height: 1.5; color: #333333;">{rec_capacitacao}</p>
        </div>
        """, unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.85rem;">
    Desenvolvido com carinho para apoiar a Liderança Estratégica na Gestão da Singularidade. © 2026.
</div>
""", unsafe_allow_html=True)
