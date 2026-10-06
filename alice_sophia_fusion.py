#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║   🌸 FUSÃO ALICE & SOPHIA v3.0 - MANASHIELD                               ║
║   Visão Computacional + Empatia de Voz + Protocolos de Coação             ║
║   Integrado com NETSENTINELA & Diagnóstico do Servidor                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

try:
    import psutil
except ImportError:
    os.system(f"{sys.executable} -m pip install psutil")
    import psutil


class SentinelLicenca:
    """Validador de Chaves de Licença do MANASHIELD"""
    @staticmethod
    def verificar(chave):
        if chave.startswith("NETSENTINELA-PREMIUM-") or chave.startswith("NETSENTINELA-ANUAL-"):
            return True, "LICENÇA OPERACIONAL COMPLETA"
        elif chave.startswith("NETSENTINELA-PRO-FREE-"):
            return True, "LICENÇA DEMO ATIVA"
        return False, "LICENÇA INVÁLIDA"


class FusionAliceSophia:
    def __init__(self, licenca_key="NETSENTINELA-PREMIUM-MASTER"):
        # Validação do SENTINEL
        valido, msg = SentinelLicenca.verificar(licenca_key)
        if not valido:
            print(f"🛑 SENTINEL: Acesso negado. {msg}")
            sys.exit(1)

        self.nome_operador = os.environ.get('USERNAME', 'Gestor')
        self.drive_path = self._encontrar_drive()
        
        print("="*70)
        print("🌸 ALICE (Visão & Borda): 'Câmeras prontas, reconhecimento facial ativo.'")
        print("🕊️ SOPHIA (Empatia & Voz): 'Interface de áudio e protocolos de coação prontos.'")
        print("="*70)

    def _encontrar_drive(self):
        user_home = Path.home()
        possiveis_nomes = ["Google Drive", "Meu Drive", "Google Drive (Meu Drive)"]
        for nome in possiveis_nomes:
            caminho = user_home / nome
            if caminho.exists():
                pasta = caminho / "Projetos" / "ManaShield_Fusion"
                pasta.mkdir(parents=True, exist_ok=True)
                return pasta
        return Path.cwd() / "ManaShield_Backup"

    # ----------------------------------------------------------------------
    # 1. SAÚDE DO SERVIDOR COM EMPATIA (ALICE CORE + CIA)
    # ----------------------------------------------------------------------
    def monitorar_servidor(self):
        """Coleta métricas e traduz em linguagem de cuidado humano"""
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disco = psutil.disk_usage('C:\\')

        # Fala empática da SOPHIA com base nos dados da ALICE
        if ram.percent > 85:
            fala = f"SOPHIA: 'Estou me sentindo um pouco carregada. Minha memória RAM está em {ram.percent}%. Seria bom fechar tarefas secundárias.'"
            severidade = "ALERTA"
        elif disco.percent > 90:
            fala = f"SOPHIA: 'Atenção! Meu armazenamento principal está quase cheio ({disco.percent}% usado). Preciso de uma limpeza de arquivos temporários.'"
            severidade = "CRITICO"
        else:
            fala = f"SOPHIA: 'Tudo está fluindo em perfeita harmonia! Processador em {cpu}% e servidor em excelente estado.'"
            severidade = "NORMAL"

        return {
            "cpu": cpu,
            "ram": ram.percent,
            "disco": disco.percent,
            "fala": fala,
            "severidade": severidade,
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

    # ----------------------------------------------------------------------
    # 2. PROTOCOLO DE ANOMALIA E COAÇÃO CONTEXTUAL ("SALADA")
    # ----------------------------------------------------------------------
    def triagem_clausura(self, morador, acompanhado_desconhecido=True):
        print(f"\n🔍 ALICE: Leitura facial confirma morador '{morador}'.")
        
        if acompanhado_desconhecido:
            print("⚠️ ALICE: Acompanhante não cadastrado identificado na clausura.")
            print("🔒 ALICE: Portão 1 (Rua) fechado. Portão 2 (Condomínio) mantido travado.")
            
            # Pergunta de Segurança da SOPHIA
            pergunta_seguranca = f"SOPHIA (Voz Interna): 'Oi, {morador}! Você comeu sua salada no almoço hoje?'"
            print(f"\n📢 {pergunta_seguranca}")
            return True # Requer validação
        else:
            print(f"🟢 ALICE: Entrada normal sem desvios de padrão. Portão 2 liberado.")
            print(f"🕊️ SOPHIA: 'Seja bem-vindo de volta, {morador}!'")
            return False

    def processar_resposta_morador(self, morador, resposta):
        """
        Gatilho do Código Secreto:
        'NÃO' = Código de Coação Ativado (Perigo)
        'SIM' = Situação de Normalidade
        """
        if resposta.strip().upper() == "NÃO":
            print("\n🚨 🚨 🚨 ALERTA MÁXIMO DE COAÇÃO CONFIRMADO! 🚨 🚨 🚨")
            print("🔒 ALICE: Retenção física ativada. Ambos os portões trancados em modo Fail-Secure.")
            print("🗣️ SOPHIA (Soberana & Tranquila): 'Cris, o portão apresentou uma inconsistência mecânica. Aguarde apenas um minuto, por favor.'")
            print("🛡️ SENTINEL: Canal direto com a Polícia Civil/SSP acionado com vídeo ao vivo, foto do acompanhante e localização exata.")
            return "SOCORRO_ACIONADO"
        else:
            print("\n✅ SOPHIA: Resposta de normalidade confirmada. Liberando Portão 2...")
            print("🔓 ALICE: Trava elétrica acionada. Acesso permitido.")
            return "ACESSO_CONCEDIDO"

    # ----------------------------------------------------------------------
    # 3. INTERVENÇÃO TÁTICA EM BRIGAS (SATURAÇÃO SENSORIAL)
    # ----------------------------------------------------------------------
    def intervir_conflito(self, local="Hall do Bloco B"):
        print(f"\n⚡ SOPHIA: Nível de decibéis anormal e palavras de agressão detectadas em '{local}'.")
        print("🚔 SENTINEL: Viaturas da PM e Guarda Municipal chamadas silenciosamente com rota livre de portões.")
        print("📢 SOPHIA + ALICE: Disparando alarme simulado de evacuação de incêndio no setor...")
        print("🔊 SOM: 'ATENÇÃO! Detecção de fumaça no setor. Por favor, evacuem o local com calma.'")
        print("💡 ALICE: Iluminação do corredor alternada para modo de emergência tática (Interrupção de padrão).")


# ==========================================================================
# TESTE DE BANCADA (LIVE DEMO DE LABORATÓRIO)
# ==========================================================================
if __name__ == "__main__":
    # Inicializa com chave do gerador NETSENTINELA[cite: 10]
    sistema = FusionAliceSophia(licenca_key="NETSENTINELA-PREMIUM-99B2A71F")

    # 1. Teste de Diagnóstico de Borda
    status = sistema.monitorar_servidor()
    print(f"\n📊 Diagnóstico do Servidor: {status['fala']}")

    # 2. Teste do Protocolo Secreto "Salada"
    precisa_validar = sistema.triagem_clausura(morador="Cris", acompanhado_desconhecido=True)
    
    if precisa_validar:
        # Simula resposta do morador (Simula o uso da senha secreta 'NÃO')
        resultado = sistema.processar_resposta_morador(morador="Cris", resposta="NÃO")

    # 3. Teste de Interrupção de Conflito em Área Comum
    sistema.intervir_conflito(local="Garagem G1")