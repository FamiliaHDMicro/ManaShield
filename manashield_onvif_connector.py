import asyncio
from onvif import ONVIFCamera

class ManaShieldONVIFConnector:
    def __init__(self, ip: str, port: int, user: str, password: str):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.camera = None

    async def conectar_camera(self):
        """
        Conecta na câmera IP usando o protocolo ONVIF.
        """
        try:
            print(f"[ONVIF] Conectando à câmera em {self.ip}:{self.port}...")
            # Inicializa a classe ONVIFCamera (caminho dos wsdl pode ser passado se necessário)
            self.camera = ONVIFCamera(self.ip, self.port, self.user, self.password)
            await self.camera.update_xaddrs()
            print(f"[ONVIF] Conexão estabelecida com sucesso com {self.ip}!")
            return True
        except Exception as e:
            print(f"[ERRO ONVIF] Falha ao conectar na câmera {self.ip}: {e}")
            return False

    async def obter_stream_rtsp(self) -> str:
        """
        Obtém o link RTSP oficial da câmera para alimentar a visão computacional da Alice e Sophia.
        """
        if not self.camera:
            print("[ERRO] Câmera não inicializada.")
            return ""

        try:
            # Cria o serviço de mídia
            media_service = self.camera.create_media_service()
            
            # Obtém os perfis de mídia disponíveis na câmera
            profiles = media_service.GetProfiles()
            if not profiles:
                print("[AVISO] Nenhum perfil de mídia encontrado.")
                return ""
            
            # Pega o primeiro perfil disponível (geralmente o stream principal HD)
            token = profiles[0].token
            
            # Requisita a URL do stream para o perfil
            stream_setup = {
                'Stream': 'RTP-Unicast',
                'Transport': {'Protocol': 'RTSP'}
            }
            uri_data = media_service.GetStreamUri({'StreamSetup': stream_setup, 'ProfileToken': token})
            
            rtsp_url = uri_data.Uri
            print(f"[ONVIF] Stream RTSP obtido com sucesso: {rtsp_url}")
            return rtsp_url
            
        except Exception as e:
            print(f"[ERRO ONVIF] Falha ao obter o URI do stream: {e}")
            return ""

# Exemplo de uso assíncrono para teste
async def main():
    # Substitua pelos dados reais da câmera IP do condomínio
    IP_CAMERA = "192.168.1.100"
    PORTA_ONVIF = 80
    USUARIO = "admin"
    SENHA = "password123"

    onvif_connector = ManaShieldONVIFConnector(IP_CAMERA, PORTA_ONVIF, USUARIO, SENHA)
    
    sucesso = await onvif_connector.conectar_camera()
    if sucesso:
        url_rtsp = await onvif_connector.obter_stream_rtsp()
        if url_rtsp:
            print(f"\n[ManaShield] Pronto para injetar o stream na análise de visão da Alice: {url_rtsp}")

if __name__ == "__main__":
    asyncio.run(main())