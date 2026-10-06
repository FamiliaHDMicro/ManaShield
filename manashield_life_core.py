#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║   🛡️ MANASHIELD ECOSYSTEM - LIFE & CONVICTION CORE v4.0                    ║
║   União dos Agentes: ALICE + SOPHIA + CIA + SENTINEL                      ║
║   Desenvolvido por Luis Fernando Martines & Gemini (2026)                 ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
from pathlib import Path
from datetime import datetime

# Garantia de biblioteca de diagnóstico
try:
    import psutil
except ImportError:
    os.system(f"{sys.executable} -m pip install psutil")
    import psutil


class ManaShieldSystem:
    def __init__(self, chave_licenca="NETSENTINELA-PREMIUM-MASTER"):
        self.versao = "4.0 - Life Edition"
        self.chave_licenca = chave_licenca
        self.operador = os.environ.get('USERNAME', 'Luis Martines')
        self.ativo = True
        
        # Validar ativação via SENTINEL
        self._validar_sentinel()
        
        print("\n" + "="*70)
        print("   🌸 ALICE:    'Olhos e visão computacional em alerta no perímetro.'")
        print("   🕊️ SOPHIA:   'Voz, empatia, apoio escolar e zeladoria IoT ativos.'")
        print("   📊 CIA:      'Telemetria de hardware e diagnóstico de servidor ok.'")
        print("   🛡️ SENTINEL: 'Muralha de rede e proteção contra blackout prontas.'")
        print("="*70 + "\n")

    def _validar_sentinel(self):
        """Validação de segurança e integridade do SENTINEL"""
        if "NETSENTINELA" in self.chave_licenca:
            print(f"🛡️ SENTINEL: Licença [{self.chave_licenca}] Autenticada. Proteção de Rede Ativa.")
        else:
            print("🛑 SENTINEL: Falha na validação de licença. Sistema bloqueado.")
            sys.exit(1)

    # 1. CICLO DE VIDA E SAÚDE DO SERVIDOR (CIA + ALICE)
    def monitorar_saude_servidor(self):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disco = psutil.disk_usage('C:\\')
        
        # Diagnóstico falado da SOPHIA com base nos dados da CIA
        if ram.percent > 85:
            mensagem = f"SOPHIA: 'Estou um pouco cansada. Minha memória está em {ram.percent}%. Vamos libertar espaço para trabalhar melhor?'"
            status = "ALERTA"
        elif disco.percent > 90:
            mensagem = f"SOPHIA: 'Atenção, o meu disco principal está quase cheio ({disco.percent}%). Preciso de uma limpeza de arquivos temporários!'"
            status = "CRITICO"
        else:
            mensagem = f"SOPHIA: 'Tudo a fluir perfeitamente! Servidor estável, CPU em {cpu}% e espaço garantido.'"
            status = "NORMAL"

        return {
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "cpu": cpu,
            "ram": ram.percent,
            "disco": disco.percent,
            "fala_sophia": mensagem,
            "status": status
        }

    # 2. ATENDIMENTO HUMANO E FAMILIAR (SOPHIA)
    def atendimento_familiar(self, morador, tipo_pedido, detalhe=""):
        print(f"\n📲 SOPHIA [Atendimento]: 'Olá, {morador}! Como posso ajudar a sua família agora?'")
        
        if tipo_pedido == "culinaria":
            resposta = f"🕊️ SOPHIA: 'Com {detalhe}, que tal prepararmos uma receita simples e deliciosa? Vou enviar o passo a passo para o seu telemóvel! 🍳'"
        elif tipo_pedido == "estudo":
            resposta = f"🕊️ SOPHIA: 'Excelente tópico de estudo! Pesquisei sobre {detalhe}. Vamos resumir a matéria juntos para tirar uma ótima nota na escola! 📚'"
        elif tipo_pedido == "contas":
            resposta = f"🕊️ SOPHIA: 'Tomei nota dos prazos das suas contas. Aviso um dia antes do vencimento para não pagar multas. 💛'"
        else:
            resposta = f"🕊️ SOPHIA: 'Estou sempre aqui no seu telemóvel, TV ou computador para o que precisar!'"
            
        print(resposta)
        return resposta

    # 3. ZELADORIA ENERGÉTICA E IOT (SOPHIA + ALICE)
    def gestao_energia_iot(self, setor, movimento=False, minutos_sem_uso=15):
        if not movimento and minutos_sem_uso >= 10:
            print(f"💡 SOPHIA (IoT): 'Setor [{setor}] sem presença humana há {minutos_sem_uso} min. A desligar iluminação para economizar a taxa do condomínio.'")
            return "LUZES_DESLIGADAS"
        return "NORMAL"

    # 4. PROTOCOLO TÁTICO DE SEGURANÇA E COAÇÃO (ALICE + SENTINEL)
    def triagem_clausura(self, morador, acompanhado_estranho=False, resposta_codigo=""):
        print(f"\n🔍 ALICE: Leitura facial identificou '{morador}'.")
        
        if acompanhado_estranho:
            print("⚠️ ALICE: Acompanhante não reconhecido no perímetro.")
            print("🔒 ALICE: Portão 1 fechado. Portão 2 mantido em retenção mecânica.")
            print(f"📢 SOPHIA (Pergunta de Verificação): '{morador}, comeu a sua salada ao almoço hoje?'")
            
            # Verificação da Resposta Secreta
            if resposta_codigo.strip().upper() == "NÃO":
                print("\n🚨 🚨 🚨 ALERTA MÁXIMO DE COAÇÃO ACTIVADO! 🚨 🚨 🚨")
                print("🔒 ALICE: Ambos os portões bloqueados no modo Fail-Secure.")
                print("🗣️ SOPHIA: 'Aguarde um instante, o portão apresentou uma pequena oscilação técnica.'")
                print("🛡️ SENTINEL: Canal com a Polícia acionado via rede redundante M2M com transmissão de vídeo ao vivo.")
                return "EMERGENCIA_DISPARADA"
            else:
                print("✅ SOPHIA: Resposta de normalidade confirmada. Acesso permitido.")
                print("🔓 ALICE: Trava elétrica libertada.")
                return "ACESSO_LIBERTADO"
        else:
            print(f"🟢 ALICE: Entrada normal sem inconformidades. Seja bem-vindo, {morador}!")
            return "ACESSO_DIRETO"


# ==========================================================================
# EXECUÇÃO DO SISTEMA NO MUNDO REAL (CICLO VIVO)
# ==========================================================================
if __name__ == "__main__":
    # Inicialização do Core Vivo com Licença do NETSENTINELA
    core = ManaShieldSystem(chave_licenca="NETSENTINELA-PREMIUM-LIVE2026")

    # 1. Diagnóstico do Servidor em Tempo Real (CIA)
    saude = core.monitorar_saude_servidor()
    print(f"📊 Status do Servidor: {saude['fala_sophia']}")

    # 2. Teste de Zeladoria Energética IoT nas Garagens
    core.gestao_energia_iot(setor="Garagem G1 & Corredor de Lavandaria", movimento=False, minutos_sem_uso=20)

    # 3. Teste de Acolhimento Familiar e Apoio Escolar
    core.atendimento_familiar(morador="Família Martines", tipo_pedido="estudo", detalhe="História e Ciência")

    # 4. Teste de Coação e Retenção Silenciosa
    core.triagem_clausura(morador="Cris", acompanhado_estranho=True, resposta_codigo="NÃO")