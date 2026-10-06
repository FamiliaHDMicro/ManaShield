#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔════════════════════════════════════════════════════════════╗
║      🌸 ALICE MANASHIELD CORE v2.0 - Tática & Borda        ║
║      Visão Computacional + Saúde do Servidor + Licença     ║
║      Adaptado para Ecossistema MANASHIELD - 2026           ║
╚════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import hashlib
from pathlib import Path
from datetime import datetime

try:
    import psutil
except ImportError:
    os.system(f"{sys.executable} -m pip install psutil")
    import psutil

class ManaShieldLicenca:
    """Módulo de validação de licenças do SENTINEL baseada no gerador NETSENTINELA"""
    @staticmethod
    def validar_chave(chave):
        if chave.startswith("NETSENTINELA-PREMIUM-") or chave.startswith("NETSENTINELA-ANUAL-"):
            return True, "LICENÇA VÁLIDA - MODO TÁTICO COMPLETO"
        elif chave.startswith("NETSENTINELA-PRO-FREE-"):
            return True, "LICENÇA DEMO (7 DIAS)"
        return False, "LICENÇA INVÁLIDA OU EXPIRADA"

class AliceTacticalCore:
    def __init__(self, licenca_key="NETSENTINELA-PREMIUM-MASTER"):
        self.nome_usuario = os.environ.get('USERNAME', 'Operador')
        self.drive_path = self._encontrar_drive()
        
        # Validação do SENTINEL
        valido, msg = ManaShieldLicenca.validar_chave(licenca_key)
        print(f"\n🛡️ SENTINEL: {msg}")
        if not valido:
            sys.exit(1)
            
        print(f"🌸 ALICE: \"Oi, {self.nome_usuario}! Sistema MANASHIELD ativo. Câmeras e servidor sob minha vigilância.\" 💚\n")

    def _encontrar_drive(self):
        user_home = Path.home()
        possiveis_nomes = ["Google Drive", "Meu Drive", "Google Drive (Meu Drive)"]
        for nome in possiveis_nomes:
            caminho = user_home / nome
            if caminho.exists():
                pasta_alice = caminho / "Projetos" / "Alice_ManaShield"
                pasta_alice.mkdir(parents=True, exist_ok=True)
                return pasta_alice
        return Path.cwd() / "Alice_Backup"

    def analisar_saude_servidor(self):
        """Coleta dados do hardware do servidor local (Integração com a CIA)"""
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disco = psutil.disk_usage('C:\\')
        
        return {
            "cpu": cpu,
            "ram_percent": ram.percent,
            "ram_gb": f"{ram.used / (1024**3):.1f} / {ram.total / (1024**3):.1f} GB",
            "disco_percent": disco.percent,
            "disco_livre_gb": f"{disco.free / (1024**3):.1f} GB",
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

    def disparar_protocolo_coacao(self, morador_nome, palavra_chave):
        """Protocolo Tático de Retenção e Alerta em Caso de Coação (Ex: 'Salada')"""
        if palavra_chave.upper() == "NÃO":
            print("\n🚨 ALICE TÁTICA: PALAVRA DE SEGURANÇA DETECTADA!")
            print(f"🔒 Ação: Portão 1 e Portão 2 Trancados em Modo Retenção.")
            print(f"📢 SOPHIA: '{morador_nome}, o portão deu um probleminha, aguarde um minuto.'")
            print("📲 SENTINEL: Transmitindo vídeo ao vivo e coordenadas para Delegacia / SSP via M2M...\n")
            return "RETENCAO_ATIVADA"
        else:
            print(f"\n✅ ALICE: Acesso liberado normalmente para {morador_nome}.")
            return "ACESSO_LIBERADO"

    def gerar_relatorio_diario(self, dados):
        nome_arquivo = f"Diario_ManaShield_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
        caminho_arquivo = self.drive_path / nome_arquivo

        conteudo = f"""
==================================================
🌸 DIÁRIO DE OPERAÇÃO MANASHIELD - {dados['timestamp']}
==================================================
Servidor Local: {self.nome_usuario}
Status: OPERACIONAL

📊 SAÚDE DO SERVIDOR (CIA):
• CPU: {dados['cpu']}%
• RAM: {dados['ram_percent']}% ({dados['ram_gb']})
• Disco C:: {dados['disco_percent']}% usado ({dados['disco_livre_gb']} livres)

🛡️ ALICE & SENTINEL: Perímetro blindado e câmeras ativas.
==================================================
"""
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"💾 Relatório salvo em: {caminho_arquivo}")

if __name__ == "__main__":
    alice = AliceTacticalCore(licenca_key="NETSENTINELA-PREMIUM-88A1F92B")
    dados_pc = alice.analisar_saude_servidor()
    
    # Simulação da verificação do Protocolo "Salada"
    alice.disparar_protocolo_coacao(morador_nome="Cris", palavra_chave="NÃO")
    alice.gerar_relatorio_diario(dados_pc)