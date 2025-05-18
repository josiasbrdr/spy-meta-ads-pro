
import streamlit as st
import requests
import os
from urllib.parse import urlparse
from urllib.request import urlretrieve

st.set_page_config(page_title="Meta Ads Spy Pro", layout="wide")
st.title("🔍 Agente Spy PRO - Biblioteca de Anúncios Meta")

query = st.text_input("Digite a palavra-chave:", value="diabetes")
token = st.text_input("Cole seu Access Token da Meta aqui:", type="password")
limite = st.slider("Quantos anúncios buscar?", min_value=1, max_value=50, value=10)

def baixar_midia(url, nome_arquivo):
    try:
        caminho, _ = urlretrieve(url, nome_arquivo)
        return caminho
    except:
        return None

if st.button("Buscar Anúncios"):
    with st.spinner("Consultando a API..."):
        url = "https://graph.facebook.com/v19.0/ads_archive"
        params = {
            "access_token": token,
            "ad_reached_countries": ["US"],
            "search_terms": query,
            "ad_type": "ALL",
            "limit": limite
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "data" in data:
                for idx, ad in enumerate(data["data"], start=1):
                    st.markdown(f"### Anúncio #{idx}")
                    st.markdown("---")
                    st.markdown(f"**Data de Início:** `{ad.get('ad_delivery_start_time', 'Desconhecido')}`")
                    copy = ad.get('ad_creative_body', 'Sem texto')
                    titulo = ad.get('ad_creative_link_title', 'Sem título')
                    snapshot = ad.get('ad_snapshot_url', '#')

                    st.markdown(f"**Título:** `{titulo}`")
                    st.markdown(f"**Copy:**
                    st.code(copy, language="markdown")
                    st.markdown(f"[Ver Anúncio na Biblioteca]({snapshot})")

                    if "image_url" in ad:
                        img_url = ad["image_url"]
                        nome_arquivo = f"anuncio_{idx}.jpg"
                        caminho = baixar_midia(img_url, nome_arquivo)
                        if caminho:
                            with open(caminho, "rb") as file:
                                st.download_button(
                                    label="⬇️ Baixar Imagem",
                                    data=file,
                                    file_name=nome_arquivo,
                                    mime="image/jpeg"
                                )
                    st.markdown("---")
            else:
                st.warning("Nenhum anúncio encontrado com esse termo.")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")
