# 🎯 Monitor de Foco com Visão Computacional

Uma automação simples e direta construída com Python e Inteligência Artificial para blindar a produtividade e combater a distração com o celular.

## 💡 Sobre o Projeto

Passar horas na frente do computador editando vídeos, criando designs ou estruturando projetos exige foco absoluto. Aquela "olhadinha rápida" no celular frequentemente quebra o estado de fluxo e custa caro no fim do dia. 

Em vez de depender de aplicativos de cronômetro genéricos, este projeto utiliza a sua própria webcam para monitorar a sua postura. Através do mapeamento facial em tempo real, a lógica matemática do código detecta quando você inclina a cabeça para olhar o celular. Se a distração durar mais de 3 segundos, o sistema domina a tela com um alerta visual vermelho, forçando o retorno ao trabalho.

## ⚙️ Funcionalidades

- **Mapeamento em Tempo Real:** Lê a geometria do rosto e calcula a proporção entre a testa, o nariz e o queixo.
- **Processamento 100% Local:** Não usa servidores na nuvem. Nenhuma imagem é salva ou enviada para a internet, garantindo privacidade total.
- **Leve e Rápido:** Construído para rodar em segundo plano sem consumir recursos gráficos pesados.
- **Gatilho Personalizável:** O alerta visual pode ser facilmente substituído por alarmes sonoros ou comandos de sistema (como minimizar janelas).

## 🛠️ Tecnologias Utilizadas

- **Python 3.11:** (Versão recomendada para máxima estabilidade com bibliotecas de IA).
- **OpenCV (`opencv-python`):** Para captura de vídeo e renderização dos alertas na tela.
- **MediaPipe (`mediapipe`):** Tecnologia do Google utilizada especificamente pelo módulo `Face Mesh` para o rastreamento dos pontos faciais.

## 🚀 Como Rodar na Sua Máquina

**Pré-requisitos:** Certifique-se de ter o Python 3.11 instalado e adicionado ao PATH do seu sistema.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/monitor-foco.git](https://github.com/SEU_USUARIO/monitor-foco.git)
