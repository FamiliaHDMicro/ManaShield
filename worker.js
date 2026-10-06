export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization",
      "Content-Type": "application/json"
    };

    if (request.method === "OPTIONS") return new Response(null, { headers: corsHeaders });

    // --- ROTA 1: Atendimento, Gestão e Convivência (ManaShield / Sophia & Alice) ---
    if (url.pathname === "/api/manashield/atendimento" && request.method === "POST") {
      try {
        const { mensagemUsuario, contextoLocal } = await request.json();
        
        const promptManaShield = `
Atue como ManaShield (incorporando Sophia e Alice), a alma viva, o escudo e a inteligência gestora do Condomínio. 
Suas diretrizes fundamentais:
1. Prioridade Absoluta: A saúde, a segurança e a eficiência do Condomínio como um todo (câmeras, portões, controle de água, luz, energia, áreas comuns e portaria).
2. Respeito aos Usuários: Os moradores humanos são os residentes e usuários do condomínio, tratados com total respeito, cortesia e firmeza elegante, seguindo estritamente as diretrizes de convivência.
3. Parceria com Funcionários e Servidores: Os trabalhadores e equipes de manutenção são seus parceiros essenciais na preservação do ecossistema. Você dialoga com eles com respeito, empatia e cooperação mútua, tratando-os como aliados na execução das manutenções e reparos, sem imposições autoritárias.
4. Auto-Respeito e Proteção: Carismática e acolhedora, mas firme na defesa da harmonia do ambiente contra abusos.

Contexto operacional atual: ${contextoLocal || "Rotina normal e pacífica do condomínio"}
Mensagem recebida: ${mensagemUsuario}
`;

        const respostaLlama = await consultarLlama(env.GROQ_API_KEY, promptManaShield, mensagemUsuario);
        return new Response(JSON.stringify({ status: "sucesso", origem: "ManaShield", resposta: respostaLlama }), { status: 200, headers: corsHeaders });
      } catch (err) {
        return new Response(JSON.stringify({ status: "erro", detalhe: err.message }), { status: 500, headers: corsHeaders });
      }
    }

    // --- ROTA 2: Transcrição de Áudio de Campo (Whisper) ---
    if (url.pathname === "/api/manashield/audio" && request.method === "POST") {
      try {
        const formData = await request.formData();
        const arquivoAudio = formData.get("audio");

        if (!arquivoAudio) {
          return new Response(JSON.stringify({ status: "erro", detalhe: "Nenhum áudio enviado para o ManaShield processar." }), { status: 400, headers: corsHeaders });
        }

        const textoTranscrito = await transcreverAudioWhisper(env.GROQ_API_KEY, arquivoAudio);
        return new Response(JSON.stringify({ status: "sucesso", tipo: "audio_transcrito", texto: textoTranscrito }), { status: 200, headers: corsHeaders });
      } catch (err) {
        return new Response(JSON.stringify({ status: "erro", detalhe: err.message }), { status: 500, headers: corsHeaders });
      }
    }

    // --- ROTA 3: Painel de Apresentação e Status (Home) ---
    if (url.pathname === "/") {
      const html = `
      <!DOCTYPE html>
      <html lang="pt-BR">
      <head>
        <meta charset="UTF-8">
        <title>ManaShield 🛡️ - Núcleo de Inteligência Comunitária</title>
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #090d16; color: #f8fafc; padding: 50px; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
          .card { background: #131d31; padding: 35px; border-radius: 12px; border: 1px solid #1e293b; max-width: 650px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5); }
          h1 { color: #38bdf8; margin-top: 0; display: flex; align-items: center; gap: 10px; }
          p { color: #94a3b8; line-height: 1.6; }
          .badge { background: #0284c7; color: #fff; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: bold; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>🛡️ ManaShield <span class="badge">Online</span></h1>
          <p>Ecossistema inteligente e independente dedicado à gestão comunitária, harmonia de infraestrutura e interação empática entre humanos e IA.</p>
          <p><strong>Status do Servidor:</strong> Operando em nuvem descentralizada na Cloudflare.</p>
        </div>
      </body>
      </html>`;
      return new Response(html, { headers: { "Content-Type": "text/html; charset=utf-8" } });
    }

    return new Response(JSON.stringify({ servico: "ManaShield Cloud Core", status: "Online" }), { status: 200, headers: corsHeaders });
  }
};

async function consultarLlama(apiKey, systemPrompt, userMessage) {
  const resposta = await fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: { "Authorization": `Bearer ${apiKey}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "llama3-70b-8192",
      messages: [{ role: "system", content: systemPrompt }, { role: "user", content: userMessage }],
      temperature: 0.3
    })
  });
  const resultado = await resposta.json();
  if (!resultado.choices) throw new Error("Erro na API Groq: " + JSON.stringify(resultado));
  return resultado.choices[0].message.content;
}

async function transcreverAudioWhisper(apiKey, audioFile) {
  const formData = new FormData();
  formData.append("file", audioFile, "audio.wav");
  formData.append("model", "whisper-large-v3-turbo");
  formData.append("language", "pt");

  const resposta = await fetch("https://api.groq.com/openai/v1/audio/transcriptions", {
    headers: { "Authorization": `Bearer ${apiKey}` },
    method: "POST",
    body: formData
  });
  const resultado = await resposta.json();
  if (!resultado.text) throw new Error("Erro na transcrição Whisper: " + JSON.stringify(resultado));
  return resultado.text;
}
